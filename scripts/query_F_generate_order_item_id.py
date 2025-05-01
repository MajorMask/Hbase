import time

print("\n✅ F. Generate Auto-Increment Order Item ID\n")

def generate_order_item_id():
    return str(int(time.time() * 1000))

print(f"Generated order_item_id: {generate_order_item_id()}")