import json
from typing import TypedDict, List
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
from database import get_price, get_all_product_names

class RFQState(TypedDict):
    email_data: str
    found_items: List[str]
    missing_items: List[str]
    final_response: str

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", google_api_key="")

def extraction_node(state: RFQState):

    valid_list = get_all_product_names()
    content = state['email_data']['snippet']

    prompt = f"""
        Extract products from: "{content}"
        Match them ONLY to this list: {valid_list}
        Return JSON: {{"found": [], "unavailable": []}}
        """
    res = llm.invoke(prompt)
    clean_json = res.content.replace("```json", "").replace("```", "").strip()
    data = json.loads(clean_json)

    return {"found_items": data['found'], "missing_items": data['unavailable']}

def pricing_node(state: RFQState):
    response = "Quotation Summary:\n"
    for item in state['found_items']:
        price = get_price(item)
        response += f"- {item}: ${price}\n"
    
    if state['missing_items']:
        response += f"\nNote: The following items are currently unavailable: {', '.join(state['missing_items'])}"
    
    return {"final_response": response}

workflow = StateGraph(RFQState)
workflow.add_node("extract", extraction_node)
workflow.add_node("price", pricing_node)
workflow.set_entry_point("extract")
workflow.add_edge("extract", "price")
workflow.add_edge("price", END)
rfq_agent = workflow.compile()