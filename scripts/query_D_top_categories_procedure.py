import happybase
from collections import defaultdict

conn = happybase.Connection('hbase', port=9090)

products = conn.table('products')
items = conn.table('order_items')
top_table = conn.table('top_categories')

print("\n✅ D. Top Categories → HBase Table Insert (top_categories)\n")

sales_count = defaultdict(int)

for _, item in items.scan():
    pid = item[b'details:product_id'].decode()
    product = products.row(pid)
    category = product.get(b'info:category', b'Unknown').decode()
    sales_count[category] += 1

for cat, count in sales_count.items():
    if count > 100:
        top_table.put(cat.encode(), {b'summary:orders': str(count).encode()})
with open('top_categories.csv', 'w') as f:
    f.write('Category,Orders\n')
    for cat, count in sales_count.items():
        if count > 100:
            f.write(f'{cat},{count}\n')

print("Top categories saved to top_categories.csv.")