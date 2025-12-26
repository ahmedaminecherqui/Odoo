
import xmlrpc.client
import socket
socket.setdefaulttimeout(30)

url = 'http://localhost:8070'
db = 'atlas_maison_db'
username = 'admin'
password = 'admin'

try:
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

    module = models.execute_kw(db, uid, password, 'ir.module.module', 'search_read', [[['name', '=', 'atlas_warehouse_management']]], {'fields': ['state']})
    print(f"Module State: {module}")

    field_info = models.execute_kw(db, uid, password, 'stock.location', 'fields_get', [['abc_category']], {'attributes': ['string']})
    print(f"Field Info: {field_info}")

    warehouses = models.execute_kw(db, uid, password, 'stock.warehouse', 'search_read', [[]], {'fields': ['name', 'code']})
    print(f"Warehouses: {warehouses}")
except Exception as e:
    print(f"Error: {e}")
