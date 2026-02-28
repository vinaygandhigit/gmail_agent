import time
import schedule
from gmail_service import authenticate_gmail, send_reply
from email_agent import rfq_agent

def process_rfqs():
    print("Checking for new RFQ emails...")
    service = authenticate_gmail()
    
    # Search for unread emails with the specific subject
    query = 'subject:"Request for Quotation" is:unread'
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])

    for m in messages:
        # Get full email
        msg = service.users().messages().get(userId='me', id=m['id']).execute()
        
        # Run AI Agent
        result = rfq_agent.invoke({"email_data": msg})
        
        # Extract sender from headers
        headers = msg['payload']['headers']
        sender = next(h['value'] for h in headers if h['name'] == 'From')
        subject = next(h['value'] for h in headers if h['name'] == 'Subject')

        # Send Reply
        send_reply(service, sender, msg['threadId'], subject, result['final_response'])
        
        # Mark as read
        service.users().messages().batchModify(
            userId='me', 
            body={'ids': [m['id']], 'removeLabelIds': ['UNREAD']}
        ).execute()
        print(f"Replied to {sender}")

# Schedule the loop
schedule.every(3).minutes.do(process_rfqs)

if __name__ == "__main__":
    print("QuoteFlow AI is running...")
    # Run once immediately on start
    process_rfqs()
    while True:
        schedule.run_pending()
        time.sleep(1)