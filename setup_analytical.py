
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

print("Creating analytical accounts...")
centers = ['Commercial', 'Logistique', 'Administration']
for center in centers:
    models.execute_kw(db, uid, password, 'account.analytic.account', 'create', [{'name': center}])
    print(f"Analytical account '{center}' created.")
