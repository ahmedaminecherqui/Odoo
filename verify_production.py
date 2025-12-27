
import xmlrpc.client
import socket
socket.setdefaulttimeout(30)

url = 'http://localhost:8070'
db = 'atlas_maison_db'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

print("Verifying Production Cycle...")

# 1. Find the Sofa Product
sofa_ids = models.execute_kw(db, uid, password, 'product.product', 'search', [[['name', '=', 'Canapé Sur-Mesure "Atlas v2"']]])
if not sofa_ids:
    print("Error: Sofa product not found.")
    exit(1)
sofa_id = sofa_ids[0]

# 2. Create Production Order
prod_id = models.execute_kw(db, uid, password, 'mrp.production', 'create', [{
    'product_id': sofa_id,
    'product_qty': 1.0,
}])
print(f"Production Order {prod_id} created.")

# 3. Confirm the order (action_confirm)
models.execute_kw(db, uid, password, 'mrp.production', 'action_confirm', [[prod_id]])
print("Production Order confirmed.")

# 4. Check atlas_real_cost
prod_data = models.execute_kw(db, uid, password, 'mrp.production', 'read', [[prod_id], ['atlas_real_cost', 'state']])
print(f"Production Order State: {prod_data[0]['state']}")
print(f"Atlas Real Cost: {prod_data[0]['atlas_real_cost']} MAD")

print("Validation completed.")
