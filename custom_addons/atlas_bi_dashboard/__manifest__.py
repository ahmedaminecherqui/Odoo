{
    'name': 'Atlas BI Dashboard',
    'version': '1.0',
    'summary': 'Tableaux de bord et Reporting pour Atlas Maison',
    'description': """
        Module centralisant les tableaux de bord et rapports BI :
        - Direction Générale
        - Commercial
        - Logistique
        - Finance
    """,
    'author': 'Atlas Maison',
    'category': 'Reporting',
    'depends': ['base', 'sale', 'stock', 'account', 'board'],
    'data': [
        'views/bi_menus.xml',
        'views/executive_dashboard.xml',
        'views/sales_dashboard.xml',
        'views/logistics_dashboard.xml',
        'views/finance_dashboard.xml',
        'reports/sales_custom_report.xml',
    ],
    'installable': True,
    'application': True,
    'sequence': 1,
}
