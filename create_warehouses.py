
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

print("Creating regional warehouses...")

# 1. Marrakech
wh_mrk = models.execute_kw(db, uid, password, 'stock.warehouse', 'create', [{
    'name': 'Marrakech',
    'code': 'MRK',
}])
print(f"Warehouse Marrakech created with ID: {wh_mrk}")

# 2. Tanger
wh_tng = models.execute_kw(db, uid, password, 'stock.warehouse', 'create', [{
    'name': 'Tanger',
    'code': 'TNG',
}])
print(f"Warehouse Tanger created with ID: {wh_tng}")

print("Regional warehouses setup completed.")
