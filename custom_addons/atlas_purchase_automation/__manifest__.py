# -*- coding: utf-8 -*-
{
    'name': 'Atlas Maison : Automatisation des Achats',
    'version': '1.0',
    'category': 'Inventory/Purchase',
    'summary': 'Seuils d alerte et automatisation des achats pour Atlas Maison',
    'description': """
Automatisation des Achats Atlas Maison
======================================
* Ajout d'un seuil d'alerte d'achat sur les articles.
* Intégration avec les règles de réapprovisionnement.
    """,
    'author': 'Atlas Maison',
    'depends': ['purchase', 'stock'],
    'data': [
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
