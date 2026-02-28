DB_INVENTORY = {
    "macbook pro 14-inch (m3)": 1999.00,
    "dell xps 13 laptop": 1099.00,
    "samsung galaxy s24 ultra": 1299.00,
    "iphone 15 pro max": 1199.00,
    "logitech mx master 3s mouse": 99.00,
    "keychron k2 mechanical keyboard": 79.00,
    "lg 27-inch 4k monitor": 449.00,
    "sony wh-1000xm5 headphones": 399.00,
    "bose quietcomfort earbuds ii": 299.00,
    "hp laserjet pro printer": 249.00,
    "herman miller aeron chair": 1600.00,
    "steelcase gesture desk chair": 1200.00,
    "fully jarvis standing desk": 599.00,
    "ikea kallax shelving unit": 120.00,
    "flexispot e7 pro standing desk": 499.00,
    "led desk lamp with usb port": 35.00,
    "ergonomic footrest": 45.00,
    "privacy screen filter (24-inch)": 55.00,
    "dual monitor mount arm": 85.00,
    "under-desk cable tray": 25.00,
    "post-it notes (bulk pack)": 15.00,
    "pilot g2 retractable pens (black)": 12.00,
    "a4 printing paper (5 reams)": 40.00,
    "heavy duty stapler": 20.00,
    "whiteboard markers (set of 8)": 18.00,
    "scotch magic tape (6 pack)": 10.00,
    "laptop stand (aluminum)": 45.00,
    "usb-c hub multiport adapter": 65.00,
    "external 2tb ssd drive": 180.00,
    "webcam (1080p hd)": 75.00
}

def get_price(product_name):
    return DB_INVENTORY.get(product_name.lower().strip())

def get_all_product_names():
    return list(DB_INVENTORY.keys())