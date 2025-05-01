print("\n✅ E. Delete Policy Simulation (Prevent Order Delete)\n")

def delete_order_safe(order_id):
    raise Exception("❌ Deletion of orders is not allowed by policy.")

# Example usage:
# delete_order_safe("ORDER123")