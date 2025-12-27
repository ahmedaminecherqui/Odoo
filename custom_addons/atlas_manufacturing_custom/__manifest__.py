
{
    'name': 'Atlas Manufacturing Custom',
    'version': '1.0',
    'category': 'Manufacturing/Manufacturing',
    'summary': 'Custom manufacturing features for Atlas Maison',
    'description': """
        Enhancements for Atlas Maison Manufacturing:
        - Real cost calculation on Production Orders
        - Custom production indicators
        - Better visibility on component consumption
    """,
    'author': 'Antigravity',
    'depends': ['mrp'],
    'data': [
        'views/mrp_production_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
