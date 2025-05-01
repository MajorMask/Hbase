import happybase

conn = happybase.Connection('hbase', port=9090)

items = conn.table('order_items')

print("\n✅ C. Total Freight for a Seller (seller_id = 'SELLER123')\n")

total = 0.0
for _, item in items.scan():
    if item[b'details:seller_id'].decode() == 'SELLER123':
        total += float(item[b'details:freight_value'])
print(f"Total freight for SELLER123: {total}")