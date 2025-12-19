# -*- coding: utf-8 -*-
{
    'name': 'Atlas Maison : Ventes',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Personnalisation du processus de vente pour Atlas Maison',
    'description': """
Gestion Commerciale Atlas Maison
================================
* Configuration des workflows de vente
* Approbation des devis > 50 000 MAD
    """,
    'author': 'Atlas Maison',
    'depends': ['sale'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
}
