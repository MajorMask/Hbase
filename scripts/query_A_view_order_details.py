import happybase

conn = happybase.Connection('hbase', port=9090)

orders = conn.table('orders')
items = conn.table('order_items')
products = conn.table('products')
customers = conn.table('customers')

print("\\n✅ A. Simulated View: Order Details (JOIN 4 tables)\\n")

for order_key, order_data in orders.scan():
    cust_id = order_data[b'meta:customer_id'].decode()
    customer = customers.row(cust_id)
    customer_state = customer.get(b'info:state', b'N/A').decode()

    for item_key, item_data in items.scan():
        if item_data[b'details:order_id'] == order_key:
            prod_id = item_data[b'details:product_id'].decode()
            price = item_data[b'details:price'].decode()

            product = products.row(prod_id)
            category = product.get(b'info:category', b'Unknown').decode()

            print(f"Order: {order_key.decode()} | State: {customer_state} | Category: {category} | Price: {price}")
