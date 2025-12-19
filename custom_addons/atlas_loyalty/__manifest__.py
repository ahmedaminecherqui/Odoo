# -*- coding: utf-8 -*-
{
    'name': 'Atlas Maison : Fidélité',
    'version': '1.0',
    'category': 'CRM',
    'summary': 'Programme de fidélité pour Atlas Maison (1 MAD = 1 point)',
    'description': """
Programme de Fidélité Atlas Maison
==================================
* Ajout de points de fidélité sur les fiches clients.
* Calcul automatique : 1 MAD dépensé = 1 point gagné.
* Historique des points sur les commandes.
    """,
    'author': 'Atlas Maison',
    'depends': ['sale', 'crm'],
    'data': [
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
