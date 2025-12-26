
{
    'name': 'Atlas Accounting Morocco',
    'version': '1.0',
    'category': 'Accounting/Localizations',
    'summary': 'Custom accounting features for Atlas Maison (Morocco)',
    'description': """
        Accounting enhancements for Atlas Maison:
        - Specific financial reports (Bilan, CPC)
        - Analytical tracking enforcement
        - Custom finance dashboard
    """,
    'author': 'Antigravity',
    'depends': ['account', 'l10n_ma'],
    'data': [
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
