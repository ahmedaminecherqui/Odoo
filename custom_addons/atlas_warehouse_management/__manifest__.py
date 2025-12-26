
{
    'name': 'Atlas Warehouse Management',
    'version': '1.0',
    'category': 'Inventory/Inventory',
    'summary': 'Advanced warehouse and logistics management for Atlas Maison',
    'description': """
        Advanced Logistics for Atlas Maison:
        - Multi-warehouse configuration (Casablanca, Marrakech, Tanger)
        - ABC classification for storage locations
        - Logistics dashboard
    """,
    'author': 'Antigravity',
    'depends': ['stock'],
    'data': [
        'views/stock_location_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
