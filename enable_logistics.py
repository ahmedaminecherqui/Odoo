
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

print("Activating logistics features...")

# Create a settings record
settings_id = models.execute_kw(db, uid, password, 'res.config.settings', 'create', [{
    'group_stock_multi_locations': True,
    'group_stock_multi_warehouses': True,
    'group_stock_adv_location': True,
    'group_stock_lot_print_gs1': True, # In Odoo 17+, lots are often linked to GS1 or other settings
    'group_production_lot': True,
}])

# Execute the settings (this applies the changes)
models.execute_kw(db, uid, password, 'res.config.settings', 'execute', [[settings_id]])

print("Logistics features activated successfully.")
