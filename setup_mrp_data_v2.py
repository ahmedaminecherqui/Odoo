
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

def get_or_create_wc(name, code):
    existing = models.execute_kw(db, uid, password, 'mrp.workcenter', 'search', [[['code', '=', code]]])
    if existing:
        print(f"Work Center '{name}' already exists.")
        return existing[0]
    wc_id = models.execute_kw(db, uid, password, 'mrp.workcenter', 'create', [{
        'name': name,
        'code': code,
    }])
    print(f"Work Center '{name}' created.")
    return wc_id

# 1. Create Work Centers
get_or_create_wc('Atelier Menuiserie', 'WC_WOOD')
get_or_create_wc('Atelier Tapisserie', 'WC_FABRIC')
get_or_create_wc('Atelier Assemblage', 'WC_ASS')

# 2. Create Components
def get_or_create_product(name, ptype='consu'):
    existing = models.execute_kw(db, uid, password, 'product.product', 'search_read', [[['name', '=', name]]], {'fields': ['id']})
    if existing:
        print(f"Product '{name}' already exists.")
        return existing[0]['id']
    
    tmpl_id = models.execute_kw(db, uid, password, 'product.template', 'create', [{
        'name': name,
        'type': ptype,
    }])
    prod_id = models.execute_kw(db, uid, password, 'product.product', 'search', [[['product_tmpl_id', '=', tmpl_id]]])[0]
    print(f"Product '{name}' created.")
    return prod_id

wood_id = get_or_create_product('Structure Bois (Chêne)')
foam_id = get_or_create_product('Mousse Haute Densité')
fabric_id = get_or_create_product('Tissu Velours (Mètre)')

# 3. Create Final Product
sofa_tmpl_id = models.execute_kw(db, uid, password, 'product.template', 'create', [{
    'name': 'Canapé Sur-Mesure "Atlas v2"',
    'type': 'consu',
}])
sofa_id = models.execute_kw(db, uid, password, 'product.product', 'search', [[['product_tmpl_id', '=', sofa_tmpl_id]]])[0]

# 4. Create BOM
models.execute_kw(db, uid, password, 'mrp.bom', 'create', [{
    'product_tmpl_id': sofa_tmpl_id,
    'product_qty': 1.0,
    'type': 'normal',
    'bom_line_ids': [
        (0, 0, {'product_id': wood_id, 'product_qty': 1}),
        (0, 0, {'product_id': foam_id, 'product_qty': 2}),
        (0, 0, {'product_id': fabric_id, 'product_qty': 5}),
    ]
}])
print(f"BOM created for 'Canapé Sur-Mesure Atlas v2'.")

print("Manufacturing configuration completed.")
