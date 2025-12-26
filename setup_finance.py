
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

print("Configuring Jalon 5 Finance...")

# 1. Create Analytical Plan
try:
    plan_id = models.execute_kw(db, uid, password, 'account.analytic.plan', 'create', [{
        'name': 'Plan Atlas Maison',
    }])
    print(f"Analytical Plan created with ID: {plan_id}")

    # 2. Create Analytical Accounts
    centers = ['Commercial', 'Logistique', 'Administration']
    for center in centers:
        models.execute_kw(db, uid, password, 'account.analytic.account', 'create', [{
            'name': center,
            'plan_id': plan_id,
        }])
        print(f"Analytical Account '{center}' created.")
except Exception as e:
    print(f"Error during analytical setup: {e}")

# 3. Verify Taxes (Moroccan VAT)
try:
    taxes = models.execute_kw(db, uid, password, 'account.tax', 'search_read', [[['amount', '>', 0]]], {'fields': ['name', 'amount']})
    print("Moroccan Taxes found:")
    for tax in taxes:
        print(f"- {tax['name']}: {tax['amount']}%")
except Exception as e:
    print(f"Error verifying taxes: {e}")

print("Jalon 5 Finance setup completed.")
