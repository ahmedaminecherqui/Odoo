
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

print("Configuring Manufacturing Infrastructure...")

# 1. Create Work Centers
work_centers = [
    {'name': 'Atelier Menuiserie', 'code': 'WC_WOOD', 'time_efficiency': 100, 'capacity': 1, 'time_start': 10, 'time_stop': 10},
    {'name': 'Atelier Tapisserie', 'code': 'WC_FABRIC', 'time_efficiency': 100, 'capacity': 1, 'time_start': 15, 'time_stop': 15},
    {'name': 'Atelier Assemblage', 'code': 'WC_ASS', 'time_efficiency': 100, 'capacity': 1, 'time_start': 5, 'time_stop': 5},
]

for wc in work_centers:
    models.execute_kw(db, uid, password, 'mrp.workcenter', 'create', [wc])
    print(f"Work Center '{wc['name']}' created.")

# 2. Create Components
components = [
    {'name': 'Structure Bois (Chêne)', 'type': 'product', 'uom_id': 1},
    {'name': 'Mousse Haute Densité', 'type': 'product', 'uom_id': 1},
    {'name': 'Tissu Velours (Mètre)', 'type': 'product', 'uom_id': 1}, # Assuming 1 is unit, better check UoM
]

comp_ids = {}
for comp in components:
    comp_id = models.execute_kw(db, uid, password, 'product.template', 'create', [comp])
    comp_ids[comp['name']] = models.execute_kw(db, uid, password, 'product.product', 'search', [[['product_tmpl_id', '=', comp_id]]])[0]
    print(f"Component '{comp['name']}' created.")

# 3. Create Final Product
sofa_tmpl_id = models.execute_kw(db, uid, password, 'product.template', 'create', [{
    'name': 'Canapé Sur-Mesure "Atlas"',
    'type': 'product',
    'produce_delay': 7,
}])
sofa_id = models.execute_kw(db, uid, password, 'product.product', 'search', [[['product_tmpl_id', '=', sofa_tmpl_id]]])[0]
print(f"Final Product 'Canapé Sur-Mesure Atlas' created.")

# 4. Create Bill of Materials (BOM)
bom_id = models.execute_kw(db, uid, password, 'mrp.bom', 'create', [{
    'product_tmpl_id': sofa_tmpl_id,
    'product_qty': 1.0,
    'type': 'normal',
    'bom_line_ids': [
        (0, 0, {'product_id': comp_ids['Structure Bois (Chêne)'], 'product_qty': 1}),
        (0, 0, {'product_id': comp_ids['Mousse Haute Densité'], 'product_qty': 2}),
        (0, 0, {'product_id': comp_ids['Tissu Velours (Mètre)'], 'product_qty': 5}),
    ]
}])
print(f"BOM created for the custom sofa.")

print("Manufacturing configuration completed.")
