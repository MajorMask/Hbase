import happybase
from collections import defaultdict

conn = happybase.Connection('hbase', port=9090)

products = conn.table('products')
items = conn.table('order_items')

print("\\n✅ B. Product Sales by Category (>100 sales)\\n")

sales_count = defaultdict(int)

for _, item in items.scan():
    pid = item[b'details:product_id'].decode()
    product = products.row(pid)
    category = product.get(b'info:category', b'Unknown').decode()
    sales_count[category] += 1

for cat, count in sales_count.items():
    if count > 100:
        print(f"{cat}: {count}")
