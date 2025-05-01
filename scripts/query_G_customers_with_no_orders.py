import happybase

conn = happybase.Connection('hbase', port=9090)

customers = conn.table('customers')
orders = conn.table('orders')

print("\n✅ G. Customers with No Orders (Anti-Join)\n")

cust_ids = set(key.decode() for key, _ in customers.scan())
ordered_custs = set()

for _, o in orders.scan():
    ordered_custs.add(o[b'meta:customer_id'].decode())

no_orders = cust_ids - ordered_custs
print("Customers with no orders:")
for cid in no_orders:
    print(f"  - {cid}")