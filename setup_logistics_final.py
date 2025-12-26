
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

groups = [
    'stock.group_stock_multi_locations',
    'stock.group_stock_multi_warehouses',
    'stock.group_adv_location',
    'stock.group_production_lot'
]

group_ids = []
for g in groups:
    try:
        gid = models.execute_kw(db, uid, password, 'ir.model.data', 'xmlid_to_res_id', [g])
        if gid:
            group_ids.append(gid)
            print(f"Group {g} ID: {gid}")
    except Exception as e:
        print(f"Error finding group {g}: {e}")

if group_ids:
    print(f"Adding user {uid} to groups: {group_ids}")
    models.execute_kw(db, uid, password, 'res.users', 'write', [[uid], {
        'groups_id': [(4, gid) for gid in group_ids]
    }])
    print("User groups updated successfully.")

# Also configure some locations for ABC
print("Configuring Casablanca locations as ABC...")
wh_stock = models.execute_kw(db, uid, password, 'stock.location', 'search', [[['name', '=', 'Stock'], ['location_id.name', '=', 'WH']]])
if wh_stock:
    # Create sub-locations for A, B, C
    models.execute_kw(db, uid, password, 'stock.location', 'create', [{
        'name': 'Zone A (Fast)',
        'location_id': wh_stock[0],
        'abc_category': 'a',
    }])
    models.execute_kw(db, uid, password, 'stock.location', 'create', [{
        'name': 'Zone B (Medium)',
        'location_id': wh_stock[0],
        'abc_category': 'b',
    }])
    models.execute_kw(db, uid, password, 'stock.location', 'create', [{
        'name': 'Zone C (Slow)',
        'location_id': wh_stock[0],
        'abc_category': 'c',
    }])
    print("ABC sub-locations created in Casablanca.")
