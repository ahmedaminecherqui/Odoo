# 🎯 Formation Odoo 19 - Premier Module

**Module 2 : Créer votre premier module Odoo complet**

---

## 📋 Table des matières

1. [Planification du module](#planification)
2. [Structure du module](#structure)
3. [Le fichier __manifest__.py](#manifest)
4. [Créer le premier modèle](#modele)
5. [Créer les vues](#vues)
6. [Configurer la sécurité](#securite)
7. [Ajouter des données](#donnees)
8. [Installer et tester](#installation)
9. [Exercices pratiques](#exercices)

---

## <a id="planification"></a>📝 1. Planification du module

### 1.1 Définir le besoin

Nous allons créer un module complet : **Gestion de Bibliothèque**

**Objectif** : Gérer les livres d'une bibliothèque et leurs emprunts

**Fonctionnalités** :
- 📚 Cataloguer des livres (titre, auteur, ISBN, pages, prix)
- 👥 Gérer des membres de bibliothèque
- 📖 Suivre les emprunts et retours
- 📊 Visualiser les statistiques
- 🔍 Rechercher et filtrer les livres

### 1.2 Modélisation des données

```
┌─────────────────────────────────────┐
│         LIBRARY.BOOK                │
│  (Livre)                            │
├─────────────────────────────────────┤
│ • id                                │
│ • name (titre)                      │
│ • isbn                              │
│ • author_id → res.partner           │
│ • publisher_id → res.partner        │
│ • pages                             │
│ • price                             │
│ • date_publication                  │
│ • category_id → library.category    │
│ • tag_ids ↔ library.tag             │
│ • state (draft/available/borrowed)  │
│ • description                       │
└─────────────────────────────────────┘
          │
          │ One2many
          ↓
┌─────────────────────────────────────┐
│      LIBRARY.BOOK.BORROW            │
│  (Emprunt)                          │
├─────────────────────────────────────┤
│ • id                                │
│ • book_id → library.book            │
│ • member_id → library.member        │
│ • borrow_date                       │
│ • return_date                       │
│ • state (ongoing/returned/late)     │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│       LIBRARY.MEMBER                │
│  (Membre)                           │
├─────────────────────────────────────┤
│ • id                                │
│ • partner_id → res.partner          │
│ • member_number                     │
│ • date_start                        │
│ • date_end                          │
│ • state (active/suspended)          │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│      LIBRARY.CATEGORY               │
│  (Catégorie)                        │
├─────────────────────────────────────┤
│ • id                                │
│ • name                              │
│ • parent_id → library.category      │
└─────────────────────────────────────┘
```

---

## <a id="structure"></a>🏗️ 2. Structure du module

### 2.1 Créer la structure

```bash
# Aller dans custom_addons
cd ~/odoo19/custom_addons  # ou C:\odoo19\custom_addons sur Windows

# Créer le module library_app
mkdir library_app
cd library_app

# Créer l'arborescence
mkdir models views security data static
mkdir static/description
touch __init__.py __manifest__.py
touch models/__init__.py
touch security/ir.model.access.csv
```

Résultat :
```
library_app/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── library_book.py
│   ├── library_member.py
│   ├── library_category.py
│   └── library_borrow.py
├── views/
│   ├── library_book_views.xml
│   ├── library_member_views.xml
│   └── library_menu.xml
├── security/
│   └── ir.model.access.csv
├── data/
│   └── library_data.xml
└── static/
    └── description/
        ├── icon.png
        └── index.html
```

### 2.2 Créer une icône

L'icône du module (256x256 pixels) :
- Créer ou télécharger une icône
- La placer dans `static/description/icon.png`
- Format : PNG, 256x256 pixels

---

## <a id="manifest"></a>📦 3. Le fichier __manifest__.py

### 3.1 Contenu complet

```python
# -*- coding: utf-8 -*-

{
    # ==================== INFORMATIONS DE BASE ====================
    
    # Nom du module affiché dans l'interface
    'name': 'Gestion de Bibliothèque',
    
    # Version du module (format: odoo_version.major.minor.patch)
    # Odoo 19 = 19.0.x.y.z
    'version': '19.0.1.0.0',
    
    # Catégorie du module dans la liste des apps
    # Catégories disponibles :
    # - Accounting, Sales, Website, Inventory, Manufacturing,
    # - Human Resources, Marketing, Services, Productivity, Tools
    'category': 'Services',
    
    # Résumé court (une ligne)
    'summary': 'Gérer une bibliothèque de livres et les emprunts',
    
    # Description longue (supporte le format ReStructuredText)
    'description': """
Gestion de Bibliothèque
=======================

Application complète pour gérer une bibliothèque.

Fonctionnalités principales :
-----------------------------
* **Catalogue de livres** : Gérer les livres avec toutes leurs informations
  (titre, auteur, ISBN, nombre de pages, prix, etc.)
* **Catégories** : Organiser les livres par catégories hiérarchiques
* **Tags** : Étiqueter les livres pour une meilleure organisation
* **Membres** : Gérer les membres de la bibliothèque
* **Emprunts** : Suivre les emprunts et les retours
* **Alertes** : Notifications pour les retards
* **Statistiques** : Rapports sur les livres les plus empruntés
* **Recherche avancée** : Filtres et recherches puissants

Vues disponibles :
------------------
* Vue liste (tableau)
* Vue formulaire (détail)
* Vue Kanban (cartes)
* Vue calendrier (pour les emprunts)
* Graphiques et statistiques

Configuration :
---------------
1. Installer le module
2. Créer des catégories de livres
3. Ajouter des livres au catalogue
4. Enregistrer des membres
5. Gérer les emprunts

Support :
---------
Pour toute question, contactez support@example.com
    """,
    
    # ==================== AUTEUR ET LICENCE ====================
    
    # Auteur du module
    'author': 'Votre Nom',
    
    # Site web de l'auteur
    'website': 'https://www.example.com',
    
    # Mainteneur (optionnel, si différent de l'auteur)
    # 'maintainer': 'Autre Nom',
    
    # Licence du module
    # LGPL-3 : Pour Community Edition (open source)
    # OPL-1 : Pour Enterprise Edition (propriétaire)
    'license': 'LGPL-3',
    
    # Email de support
    'support': 'support@example.com',
    
    # ==================== DÉPENDANCES ====================
    
    # Modules qui doivent être installés AVANT ce module
    # Ces modules seront installés automatiquement si nécessaire
    'depends': [
        'base',           # Module de base (obligatoire pour tous les modules)
        'mail',           # Module de messagerie (pour le chatter)
        'web',            # Module web (pour l'interface)
    ],
    
    # Dépendances externes Python (facultatif)
    # Ces packages doivent être installés via pip
    # 'external_dependencies': {
    #     'python': ['requests', 'pandas'],
    #     'bin': ['wkhtmltopdf'],
    # },
    
    # ==================== FICHIERS DE DONNÉES ====================
    
    # Fichiers de données à charger (ORDRE IMPORTANT!)
    'data': [
        # 1. SÉCURITÉ (toujours en premier)
        'security/library_security.xml',      # Groupes de sécurité
        'security/ir.model.access.csv',       # Droits d'accès CRUD
        
        # 2. DONNÉES DE BASE (séquences, catégories par défaut, etc.)
        'data/library_data.xml',
        
        # 3. VUES (dans l'ordre logique)
        'views/library_menu.xml',             # Menus
        'views/library_category_views.xml',   # Catégories
        'views/library_book_views.xml',       # Livres
        'views/library_member_views.xml',     # Membres
        'views/library_borrow_views.xml',     # Emprunts
        
        # 4. RAPPORTS (si applicable)
        # 'report/library_report_templates.xml',
        
        # 5. WIZARDS (si applicable)
        # 'wizard/library_wizard_views.xml',
    ],
    
    # Données de démonstration (chargées uniquement si case cochée)
    'demo': [
        'data/library_demo.xml',
    ],
    
    # ==================== ASSETS (JavaScript/CSS) ====================
    
    # Fichiers JavaScript et CSS à charger
    'assets': {
        # Assets pour le backend (interface admin)
        'web.assets_backend': [
            'library_app/static/src/js/*.js',
            'library_app/static/src/css/*.css',
        ],
        # Assets pour le frontend (site web public)
        # 'web.assets_frontend': [
        #     'library_app/static/src/js/frontend.js',
        # ],
    },
    
    # ==================== CONFIGURATION DU MODULE ====================
    
    # Le module peut être installé
    'installable': True,
    
    # C'est une application (apparaît dans le menu Apps)
    # True = Application standalone
    # False = Module technique/extension
    'application': True,
    
    # Installation automatique si dépendances installées
    # True = S'installe automatiquement
    # False = Installation manuelle requise
    'auto_install': False,
    
    # ==================== ODOO APP STORE ====================
    
    # Séquence d'affichage (ordre dans la liste)
    # Plus petit = plus haut dans la liste
    'sequence': 10,
    
    # Prix du module (pour l'App Store)
    # 0.00 = Gratuit
    'price': 0.00,
    
    # Devise du prix
    'currency': 'EUR',
    
    # Images du module (captures d'écran pour l'App Store)
    'images': [
        'static/description/banner.png',
        'static/description/screenshot_books.png',
        'static/description/screenshot_kanban.png',
    ],
    
    # ==================== AUTRES ====================
    
    # Liste des contributeurs
    # 'contributors': [
    #     'Contributeur 1 <email1@example.com>',
    #     'Contributeur 2 <email2@example.com>',
    # ],
    
    # Version minimale d'Odoo requise
    # 'min_version': '19.0',
    
    # Version maximale d'Odoo supportée
    # 'max_version': '19.0.99',
    
    # Modules en conflit (ne peuvent être installés ensemble)
    # 'excludes': ['other_library_module'],
    
    # URL du dépôt Git
    # 'repository': 'https://github.com/username/library_app',
    
    # Branche Git
    # 'branch': 'main',
    
    # Post-installation : URL à ouvrir après installation
    # 'post_init_hook': '_post_install_hook',
    
    # Pre-uninstall : fonction à appeler avant désinstallation
    # 'pre_uninstall_hook': '_pre_uninstall_hook',
    
    # Clé de développement (non utilisé en production)
    # 'development_status': 'Beta',  # Alpha, Beta, Production/Stable, Mature
    
    # Est-ce un module payé
    # 'paid': False,
    
    # Lien vers la documentation
    # 'doc_url': 'https://docs.example.com/library_app',
}
```

### 3.2 Explications détaillées

#### Version du module

Format : `ODOO_VERSION.MAJOR.MINOR.PATCH`

```
19.0.1.0.0
│  │ │ │ └─ Patch : Corrections de bugs
│  │ │ └─── Minor : Petites fonctionnalités
│  │ └───── Major : Changements importants
│  └─────── Sous-version Odoo
└────────── Version Odoo
```

Exemples :
- `19.0.1.0.0` : Première version pour Odoo 19
- `19.0.1.1.0` : Ajout de fonctionnalités mineures
- `19.0.1.1.1` : Correction de bug
- `19.0.2.0.0` : Refonte majeure

#### Dépendances

```python
'depends': ['base', 'mail', 'sale']
```

**Règles** :
- `base` est toujours requis
- Ordre important si modules interdépendants
- Si module A dépend de B, installer B d'abord

#### Ordre des fichiers data

```python
'data': [
    '1. security/*.xml',      # Groupes et règles
    '2. security/*.csv',      # Droits d'accès
    '3. data/*.xml',          # Données de base
    '4. views/menu.xml',      # Menus
    '5. views/*_views.xml',   # Vues
    '6. report/*.xml',        # Rapports
    '7. wizard/*.xml',        # Wizards
]
```

---

## <a id="modele"></a>🔵 4. Créer le premier modèle

### 4.1 Fichier __init__.py (racine)

```python
# -*- coding: utf-8 -*-

"""
Point d'entrée du module library_app.
Importe tous les sous-packages.
"""

# Importer le package models
from . import models

# Si vous avez des contrôleurs (plus tard)
# from . import controllers

# Si vous avez des wizards (plus tard)
# from . import wizard
```

### 4.2 Fichier models/__init__.py

```python
# -*- coding: utf-8 -*-

"""
Package models : contient tous les modèles du module.
"""

# Importer tous les fichiers de modèles
from . import library_book
from . import library_category
from . import library_member
from . import library_borrow
```

### 4.3 Modèle : library_book.py

```python
# -*- coding: utf-8 -*-

"""
Modèle principal pour gérer les livres de la bibliothèque.
"""

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import date

class LibraryBook(models.Model):
    """
    Modèle représentant un livre dans la bibliothèque.
    
    Hérite de models.Model pour devenir une table PostgreSQL persistante.
    Chaque enregistrement = une ligne dans la table 'library_book'.
    """
    
    # ==================== MÉTADONNÉES DU MODÈLE ====================
    
    # Nom technique unique du modèle (OBLIGATOIRE)
    # Devient la table PostgreSQL 'library_book' (remplace . par _)
    _name = 'library.book'
    
    # Description lisible du modèle
    # Utilisée dans les logs, exports CSV, etc.
    _description = 'Livre de bibliothèque'
    
    # Héritage de fonctionnalités existantes
    # mail.thread : Ajoute le chatter (messages, followers)
    # mail.activity.mixin : Ajoute les activités planifiées
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    # Ordre par défaut des enregistrements (SQL ORDER BY)
    # Utilisé dans les recherches sans order explicite
    _order = 'name, date_publication desc'
    
    # Champ utilisé pour le nom d'affichage (par défaut: 'name')
    # C'est le champ affiché dans les Many2one et breadcrumbs
    _rec_name = 'name'
    
    # Créer automatiquement une séquence pour ce modèle
    # Génère des IDs séquentiels (LIB001, LIB002, etc.)
    # _sql_sequence = 'library_book_id_seq'
    
    # ==================== CHAMPS DE BASE ====================
    
    # Champ Char : Chaîne de caractères courte (VARCHAR en SQL)
    name = fields.Char(
        string='Titre',              # Label affiché dans l'interface
        required=True,                # Champ obligatoire (NOT NULL en SQL)
        index=True,                   # Créer un index BDD pour recherches rapides
        tracking=True,                # Suivre les modifications dans le chatter
        help='Titre complet du livre',  # Texte d'aide (tooltip)
        translate=True,               # Permettre traduction du contenu
    )
    
    # Champ Text : Texte long multi-lignes (TEXT en SQL)
    description = fields.Text(
        string='Résumé',
        help='Description détaillée et résumé du livre'
    )
    
    # Champ Char avec taille maximale
    isbn = fields.Char(
        string='ISBN',
        size=13,                      # Maximum 13 caractères
        copy=False,                   # Ne pas copier lors d'un duplicate()
        index=True,
        help='Code ISBN à 10 ou 13 chiffres'
    )
    
    # ==================== CHAMPS NUMÉRIQUES ====================
    
    # Champ Integer : Nombre entier (INTEGER en SQL)
    pages = fields.Integer(
        string='Nombre de pages',
        default=0,                    # Valeur par défaut
        help='Nombre total de pages du livre'
    )
    
    # Champ Float : Nombre décimal (NUMERIC en SQL)
    price = fields.Float(
        string='Prix',
        digits=(10, 2),               # (total chiffres, décimales) = 99999999.99
        default=0.0,
        help='Prix de vente du livre'
    )
    
    # Champ Monetary : Prix avec devise (utilise Float en interne)
    # Nécessite un champ currency_id
    price_currency = fields.Monetary(
        string='Prix TTC',
        currency_field='currency_id',
        help='Prix dans la devise de l\'entreprise'
    )
    
    # Champ Many2one pour la devise
    currency_id = fields.Many2one(
        'res.currency',
        string='Devise',
        default=lambda self: self.env.company.currency_id,
        help='Devise utilisée pour le prix'
    )
    
    # ==================== CHAMPS DATE/HEURE ====================
    
    # Champ Date : Date sans heure (DATE en SQL)
    date_publication = fields.Date(
        string='Date de publication',
        default=fields.Date.today,    # Date du jour par défaut
        help='Date de première publication du livre'
    )
    
    # Champ Datetime : Date avec heure (TIMESTAMP en SQL)
    date_added = fields.Datetime(
        string='Ajouté le',
        default=fields.Datetime.now,  # Date et heure actuelles
        readonly=True,                # Lecture seule (pas éditable)
        help='Date et heure d\'ajout à la bibliothèque'
    )
    
    # ==================== CHAMPS BOOLÉENS ET SÉLECTION ====================
    
    # Champ Boolean : Vrai/Faux (BOOLEAN en SQL)
    available = fields.Boolean(
        string='Disponible',
        default=True,
        tracking=True,
        help='Indique si le livre est disponible à l\'emprunt'
    )
    
    # Champ active : Spécial, permet d'archiver les enregistrements
    # Si active=False, l'enregistrement est caché par défaut
    active = fields.Boolean(
        string='Actif',
        default=True,
        help='Décocher pour archiver le livre sans le supprimer'
    )
    
    # Champ Selection : Liste de choix prédéfinis
    # Stocké comme VARCHAR avec contrainte CHECK en SQL
    state = fields.Selection(
        selection=[                   # Liste de tuples (valeur_technique, label_affiché)
            ('draft', 'Brouillon'),
            ('available', 'Disponible'),
            ('borrowed', 'Emprunté'),
            ('maintenance', 'En maintenance'),
            ('lost', 'Perdu'),
        ],
        string='État',
        default='draft',              # Valeur par défaut
        required=True,
        tracking=True,
        help='État actuel du livre dans la bibliothèque'
    )
    
    # ==================== CHAMPS RELATIONNELS ====================
    
    # Many2one : Relation N→1 (plusieurs livres → un auteur)
    # Crée une colonne 'author_id' (INTEGER) avec FK vers res_partner.id
    author_id = fields.Many2one(
        'res.partner',                # Modèle cible
        string='Auteur',
        ondelete='restrict',          # Action si l'auteur est supprimé:
                                      # - 'restrict': Empêcher suppression
                                      # - 'cascade': Supprimer les livres aussi
                                      # - 'set null': Mettre à NULL
        domain=[('is_company', '=', False)],  # Filtre: seulement personnes
        index=True,                   # Index sur la FK
        tracking=True,
        help='Auteur principal du livre'
    )
    
    # Many2one vers un autre contact (éditeur)
    publisher_id = fields.Many2one(
        'res.partner',
        string='Éditeur',
        ondelete='set null',
        domain=[('is_company', '=', True)],  # Seulement entreprises
        help='Maison d\'édition du livre'
    )
    
    # Many2one vers un modèle personnalisé
    category_id = fields.Many2one(
        'library.category',           # Notre propre modèle
        string='Catégorie',
        ondelete='restrict',
        index=True,
        help='Catégorie principale du livre'
    )
    
    # One2many : Relation 1→N (un livre → plusieurs emprunts)
    # Champ virtuel (pas de colonne en BDD)
    # Définit l'inverse d'un Many2one
    borrow_ids = fields.One2many(
        'library.book.borrow',        # Modèle cible
        'book_id',                    # Champ Many2one dans library.book.borrow
        string='Historique d\'emprunts',
        help='Liste de tous les emprunts de ce livre'
    )
    
    # Many2many : Relation N↔N (plusieurs livres ↔ plusieurs tags)
    # Crée une table intermédiaire : library_book_library_tag_rel
    # Avec colonnes : book_id, tag_id
    tag_ids = fields.Many2many(
        'library.tag',                # Modèle cible
        'library_book_tag_rel',       # Nom table intermédiaire (optionnel)
        'book_id',                    # Colonne pour ce modèle (optionnel)
        'tag_id',                     # Colonne pour le modèle cible (optionnel)
        string='Tags',
        help='Étiquettes associées au livre'
    )
    
    # ==================== CHAMPS CALCULÉS ====================
    
    # Champ calculé : Valeur calculée automatiquement
    page_category = fields.Selection(
        selection=[
            ('short', 'Court (< 200 pages)'),
            ('medium', 'Moyen (200-400 pages)'),
            ('long', 'Long (> 400 pages)'),
        ],
        string='Catégorie de taille',
        compute='_compute_page_category',  # Méthode de calcul
        store=True,                         # Stocker en BDD (optionnel)
                                             # store=True → calculé puis stocké
                                             # store=False → calculé à chaque lecture
        help='Catégorie automatique basée sur le nombre de pages'
    )
    
    @api.depends('pages')             # Dépendances: recalculer si 'pages' change
    def _compute_page_category(self):
        """
        Calcule la catégorie de taille basée sur le nombre de pages.
        
        Décorateur @api.depends() :
        - Indique à Odoo quels champs déclenchent le recalcul
        - Si 'pages' change, cette méthode est appelée automatiquement
        - Peut suivre des relations : @api.depends('author_id.country_id.name')
        """
        for book in self:  # TOUJOURS itérer sur self (recordset)
            if book.pages < 200:
                book.page_category = 'short'
            elif book.pages < 400:
                book.page_category = 'medium'
            else:
                book.page_category = 'long'
    
    # Champ calculé plus complexe
    total_borrows = fields.Integer(
        string='Nombre total d\'emprunts',
        compute='_compute_total_borrows',
        store=False,                  # Ne pas stocker (calculé à la volée)
        help='Nombre de fois que ce livre a été emprunté'
    )
    
    @api.depends('borrow_ids')
    def _compute_total_borrows(self):
        """Compte le nombre d'emprunts."""
        for book in self:
            book.total_borrows = len(book.borrow_ids)
    
    # Champ calculé INVERSABLE (peut être édité)
    # Utile pour créer des raccourcis éditables
    author_email = fields.Char(
        string='Email de l\'auteur',
        compute='_compute_author_email',
        inverse='_inverse_author_email',  # Méthode appelée lors de l'édition
        store=False,
        help='Email de l\'auteur (éditable)'
    )
    
    @api.depends('author_id.email')
    def _compute_author_email(self):
        """Récupère l'email de l'auteur."""
        for book in self:
            book.author_email = book.author_id.email if book.author_id else False
    
    def _inverse_author_email(self):
        """Met à jour l'email de l'auteur quand on modifie ce champ."""
        for book in self:
            if book.author_id:
                book.author_id.email = book.author_email
    
    # ==================== CHAMPS LIÉS (RELATED) ====================
    
    # Champ lié : Raccourci vers un champ d'un objet lié
    # Crée automatiquement un champ calculé en lecture seule (ou éditable)
    author_country_id = fields.Many2one(
        'res.country',
        string='Pays de l\'auteur',
        related='author_id.country_id',  # Chemin vers le champ cible
        readonly=False,                   # Permet l'édition (modifie l'auteur)
        store=True,                       # Optionnel: stocker en BDD
        help='Pays de résidence de l\'auteur'
    )
    
    # Related sur plusieurs niveaux
    author_country_code = fields.Char(
        string='Code pays de l\'auteur',
        related='author_id.country_id.code',
        readonly=True
    )
    
    # ==================== CONTRAINTES ====================
    
    # Contraintes SQL : Validées au niveau de la base de données
    # Très performantes, toujours respectées même hors Odoo
    _sql_constraints = [
        # Format: (nom_contrainte, définition_sql, message_erreur)
        
        (
            'isbn_unique',              # Nom technique de la contrainte
            'UNIQUE(isbn)',             # SQL: ISBN doit être unique
            'Ce code ISBN existe déjà dans la bibliothèque!'
        ),
        (
            'pages_positive',
            'CHECK(pages >= 0)',        # Pages ne peut pas être négatif
            'Le nombre de pages doit être positif!'
        ),
        (
            'price_positive',
            'CHECK(price >= 0)',
            'Le prix ne peut pas être négatif!'
        ),
    ]
    
    # Contraintes Python : Validations métier complexes
    # Plus flexibles mais moins performantes que SQL
    @api.constrains('pages')
    def _check_pages(self):
        """
        Valide que le nombre de pages est dans une plage raisonnable.
        
        Décorateur @api.constrains() :
        - Indique quels champs déclenchent la validation
        - Appelé automatiquement à la création/modification
        - Peut valider plusieurs champs simultanément
        
        Raises:
            ValidationError: Si la validation échoue
        """
        for book in self:
            if book.pages < 0:
                raise ValidationError(
                    'Le nombre de pages ne peut pas être négatif!'
                )
            
            if book.pages > 10000:
                raise ValidationError(
                    'Le nombre de pages semble irréaliste (> 10000). '
                    'Veuillez vérifier.'
                )
    
    @api.constrains('isbn')
    def _check_isbn_format(self):
        """
        Valide le format de l'ISBN (10 ou 13 chiffres).
        """
        for book in self:
            if book.isbn:
                # Nettoyer l'ISBN (retirer tirets et espaces)
                isbn_clean = book.isbn.replace('-', '').replace(' ', '')
                
                # Vérifier la longueur
                if len(isbn_clean) not in [10, 13]:
                    raise ValidationError(
                        f'L\'ISBN doit contenir 10 ou 13 chiffres. '
                        f'Actuellement: {len(isbn_clean)} caractères.'
                    )
                
                # Vérifier que ce sont bien des chiffres
                if not isbn_clean.isdigit():
                    raise ValidationError(
                        'L\'ISBN ne doit contenir que des chiffres '
                        '(espaces et tirets acceptés).'
                    )
    
    @api.constrains('date_publication')
    def _check_date_publication(self):
        """
        Valide que la date de publication n'est pas dans le futur.
        """
        today = fields.Date.today()
        for book in self:
            if book.date_publication and book.date_publication > today:
                raise ValidationError(
                    f'La date de publication ({book.date_publication}) '
                    f'ne peut pas être dans le futur!'
                )
    
    # ==================== MÉTHODES ONCHANGE ====================
    
    @api.onchange('pages')
    def _onchange_pages(self):
        """
        Méthode onchange : Réagit aux changements AVANT sauvegarde.
        
        Décorateur @api.onchange() :
        - Exécuté côté serveur mais AVANT la sauvegarde
        - Peut modifier d'autres champs
        - Peut afficher des warnings
        - Ne persiste rien en BDD tant que l'utilisateur ne sauvegarde pas
        
        Différences avec @api.depends :
        - onchange : Interface, avant save, peut afficher warnings
        - depends : Calculs, après save, modifie la BDD
        """
        if self.pages and self.pages > 1000:
            # Afficher un warning (bulle d'avertissement)
            return {
                'warning': {
                    'title': 'Attention',
                    'message': (
                        f'Ce livre a {self.pages} pages. '
                        f'Vérifiez que cette valeur est correcte.'
                    )
                }
            }
    
    @api.onchange('author_id')
    def _onchange_author(self):
        """
        Quand l'auteur change, remplir automatiquement l'éditeur.
        """
        if self.author_id and not self.publisher_id:
            # Chercher l'éditeur habituel de cet auteur
            last_book = self.search([
                ('author_id', '=', self.author_id.id),
                ('publisher_id', '!=', False)
            ], limit=1, order='date_publication desc')
            
            if last_book:
                self.publisher_id = last_book.publisher_id
    
    # ==================== MÉTHODES CRUD SURCHARGÉES ====================
    
    @api.model
    def create(self, vals):
        """
        Surcharge de create() pour ajouter de la logique à la création.
        
        Args:
            vals (dict): Dictionnaire des valeurs à créer
            
        Returns:
            recordset: L'enregistrement créé
            
        Note:
            @api.model signifie que cette méthode ne nécessite pas
            un recordset existant (méthode de classe)
        """
        # ===== AVANT CRÉATION =====
        
        # Normaliser l'ISBN
        if vals.get('isbn'):
            vals['isbn'] = vals['isbn'].replace('-', '').replace(' ', '')
        
        # Validation personnalisée
        if vals.get('pages', 0) > 5000:
            raise ValidationError(
                'Un livre ne peut pas avoir plus de 5000 pages!'
            )
        
        # Mettre en majuscules le titre
        if vals.get('name'):
            vals['name'] = vals['name'].title()
        
        # ===== CRÉATION RÉELLE =====
        book = super(LibraryBook, self).create(vals)
        
        # ===== APRÈS CRÉATION =====
        
        # Logger la création dans le chatter
        book.message_post(
            body=f"Nouveau livre ajouté : {book.name}",
            subject="Création"
        )
        
        # Notifier les abonnés
        # book._notify_followers()
        
        return book
    
    def write(self, vals):
        """
        Surcharge de write() pour ajouter de la logique à la modification.
        
        Args:
            vals (dict): Dictionnaire des valeurs à modifier
            
        Returns:
            bool: True si succès
        """
        # ===== AVANT MODIFICATION =====
        
        # Logger les changements importants
        if 'state' in vals:
            for book in self:
                old_state = book.state
                new_state = vals['state']
                
                if old_state != new_state:
                    book.message_post(
                        body=f"État changé : {dict(self._fields['state'].selection)[old_state]} → "
                             f"{dict(self._fields['state'].selection)[new_state]}"
                    )
        
        # Empêcher la modification de l'ISBN si le livre a des emprunts
        if 'isbn' in vals:
            for book in self:
                if book.borrow_ids:
                    raise UserError(
                        f'Impossible de modifier l\'ISBN du livre "{book.name}" '
                        f'car il a un historique d\'emprunts.'
                    )
        
        # ===== MODIFICATION RÉELLE =====
        result = super(LibraryBook, self).write(vals)
        
        # ===== APRÈS MODIFICATION =====
        
        # Si le livre devient disponible, notifier les intéressés
        if vals.get('available') == True:
            for book in self:
                book.message_post(
                    body=f'Le livre "{book.name}" est maintenant disponible!'
                )
        
        return result
    
    def unlink(self):
        """
        Surcharge de unlink() pour ajouter de la logique à la suppression.
        
        Returns:
            bool: True si succès
        """
        # ===== AVANT SUPPRESSION =====
        
        # Empêcher la suppression si le livre est emprunté
        for book in self:
            if book.state == 'borrowed':
                raise UserError(
                    f'Impossible de supprimer le livre "{book.name}" '
                    f'car il est actuellement emprunté!'
                )
            
            # Supprimer les emprunts associés
            book.borrow_ids.unlink()
        
        # Logger la suppression
        for book in self:
            # Créer un log avant suppression
            self.env['library.log'].sudo().create({
                'message': f'Livre supprimé : {book.name} (ISBN: {book.isbn})',
                'date': fields.Datetime.now(),
                'user_id': self.env.user.id,
            })
        
        # ===== SUPPRESSION RÉELLE =====
        return super(LibraryBook, self).unlink()
    
    def copy(self, default=None):
        """
        Surcharge de copy() pour personnaliser la duplication.
        
        Args:
            default (dict): Valeurs à écraser dans la copie
            
        Returns:
            recordset: La copie créée
        """
        self.ensure_one()  # S'assurer qu'il n'y a qu'un seul enregistrement
        
        default = dict(default or {})
        
        # Personnaliser les valeurs de la copie
        default.update({
            'name': f"{self.name} (Copie)",
            'isbn': False,  # Ne pas copier l'ISBN (unique)
            'state': 'draft',  # Remettre en brouillon
            'date_added': fields.Datetime.now(),
            'borrow_ids': False,  # Ne pas copier les emprunts
        })
        
        return super(LibraryBook, self).copy(default)
    
    # ==================== MÉTHODES MÉTIER ====================
    
    def action_make_available(self):
        """
        Bouton d'action : Rendre le livre disponible.
        
        Cette méthode peut être appelée depuis un bouton dans la vue XML.
        Elle met le livre en état "disponible".
        
        Returns:
            bool: True si succès
        """
        for book in self:
            # Vérifier les conditions
            if book.state == 'lost':
                raise UserError(
                    'Un livre perdu ne peut pas être rendu disponible. '
                    'Veuillez d\'abord le marquer comme retrouvé.'
                )
            
            # Changer l'état
            book.write({
                'state': 'available',
                'available': True
            })
            
            # Logger l'action
            book.message_post(
                body="Livre rendu disponible",
                subject="Changement d'état"
            )
        
        return True
    
    def action_borrow(self):
        """
        Action pour emprunter un livre.
        
        Ouvre un wizard pour sélectionner le membre emprunteur.
        
        Returns:
            dict: Action Odoo pour ouvrir le wizard
        """
        self.ensure_one()
        
        # Validation
        if not self.available:
            raise UserError(
                f'Le livre "{self.name}" n\'est pas disponible!'
            )
        
        # Retourner une action pour ouvrir le wizard d'emprunt
        return {
            'type': 'ir.actions.act_window',
            'name': 'Emprunter un livre',
            'res_model': 'library.book.borrow.wizard',
            'view_mode': 'form',
            'target': 'new',  # Ouvrir en popup
            'context': {
                'default_book_id': self.id,
                'default_borrow_date': fields.Date.today(),
            }
        }
    
    def action_view_borrows(self):
        """
        Action pour voir tous les emprunts de ce livre.
        
        Returns:
            dict: Action Odoo pour ouvrir la liste des emprunts
        """
        self.ensure_one()
        
        return {
            'type': 'ir.actions.act_window',
            'name': f'Emprunts de "{self.name}"',
            'res_model': 'library.book.borrow',
            'view_mode': 'tree,form',
            'domain': [('book_id', '=', self.id)],
            'context': {'default_book_id': self.id}
        }
    
    @api.model
    def get_available_books(self, category_id=None):
        """
        Méthode pour récupérer tous les livres disponibles.
        
        Args:
            category_id (int, optional): Filtrer par catégorie
            
        Returns:
            recordset: Livres disponibles
            
        Note:
            @api.model car ne nécessite pas de recordset existant
        """
        domain = [
            ('available', '=', True),
            ('state', '=', 'available')
        ]
        
        if category_id:
            domain.append(('category_id', '=', category_id))
        
        return self.search(domain)
    
    def compute_statistics(self):
        """
        Calculer des statistiques sur ce livre.
        
        Returns:
            dict: Dictionnaire de statistiques
        """
        self.ensure_one()
        
        # Compter les emprunts
        total_borrows = len(self.borrow_ids)
        ongoing_borrows = len(self.borrow_ids.filtered(
            lambda b: not b.return_date
        ))
        late_borrows = len(self.borrow_ids.filtered(
            lambda b: b.state == 'late'
        ))
        
        return {
            'total_borrows': total_borrows,
            'ongoing_borrows': ongoing_borrows,
            'late_borrows': late_borrows,
            'popularity': 'High' if total_borrows > 10 else 
                         'Medium' if total_borrows > 5 else 'Low'
        }
```

Ce modèle est extrêmement complet et commenté. Continuons avec les autres modèles dans le prochain message !

