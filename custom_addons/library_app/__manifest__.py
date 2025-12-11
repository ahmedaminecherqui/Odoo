# -*- coding: utf-8 -*-
{
    'name': 'Gestion de Bibliothèque',
    'version': '19.0.1.0.0',
    'category': 'Services',
    'summary': 'Gérer une bibliothèque de livres et les emprunts',
    'description': """
Gestion de Bibliothèque
=======================

Application complète pour gérer une bibliothèque.

Fonctionnalités principales :
* Catalogue de livres
* Catégories
* Tags
* Membres
* Emprunts
    """,
    'author': 'Votre Nom',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'data/library_data.xml',
        'views/library_menu.xml',
        'views/library_category_views.xml',
        'views/library_book_views.xml',
        'views/library_member_views.xml',
        'views/library_borrow_views.xml',
    ],
    'application': True,
    'installable': True,
}
