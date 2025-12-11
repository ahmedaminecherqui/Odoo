# 🚀 Formation Odoo 19 - Introduction et Architecture

**Module 0 : Fondations**

---

## 📋 Table des matières

1. [Introduction à Odoo](#introduction)
2. [Architecture logicielle complète](#architecture)
3. [Concepts fondamentaux](#concepts)
4. [Écosystème Odoo](#ecosysteme)

---

## <a id="introduction"></a>📚 1. Introduction à Odoo

### 1.1 Qu'est-ce qu'Odoo ?

**Odoo** est un ERP (Enterprise Resource Planning) open source qui permet de gérer l'intégralité des processus d'une entreprise. C'est l'une des solutions ERP les plus populaires au monde avec :

- 🌍 **7+ millions d'utilisateurs** dans 120+ pays
- 🏢 **30+ applications** métiers intégrées
- 👥 **100 000+ entreprises** utilisatrices
- 📈 **Croissance rapide** avec une nouvelle version majeure chaque année

### 1.2 Histoire et évolution

```
2005 : TinyERP (Belgique)
   ↓
2008 : Renommé OpenERP
   ↓
2014 : Renommé Odoo
   ↓
2024 : Odoo 18 (Enterprise)
   ↓
2025 : Odoo 19 (Community + Enterprise)
```

### 1.3 Versions d'Odoo

**Community Edition (CE)** :
- ✅ **Gratuite** et open source
- ✅ Licence **LGPL-3**
- ✅ Code source disponible sur GitHub
- ✅ Modules de base complets
- ❌ Pas de support officiel
- ❌ Fonctionnalités avancées limitées

**Enterprise Edition (EE)** :
- 💰 **Payante** (licence par utilisateur)
- ✅ Licence **OPL-1** (Odoo Proprietary License)
- ✅ **Support officiel** d'Odoo S.A.
- ✅ **Fonctionnalités avancées** (Studio, Documents, Signature, etc.)
- ✅ **Design amélioré**
- ✅ **Applications mobiles** natives
- ✅ **Hébergement cloud** (Odoo.sh)

**Odoo.sh** :
- ☁️ Plateforme **cloud managée**
- ✅ Hébergement, backups, mises à jour automatiques
- ✅ Environnements de développement, staging, production
- ✅ Intégration GitHub
- 💰 Abonnement mensuel

### 1.4 Applications Odoo

**Ventes & CRM** :
- 📊 CRM : Gestion des opportunités
- 💼 Ventes : Devis, commandes
- 🤝 Point de vente (POS)
- 🌐 E-commerce

**Opérations** :
- 📦 Inventaire : Gestion des stocks
- 🏭 Fabrication (MRP)
- 🛒 Achats
- 📍 Code-barres

**Finance** :
- 💰 Comptabilité
- 💳 Facturation
- 📈 Frais
- 🏦 Paiements

**RH** :
- 👥 Employés
- 📅 Congés
- ⏰ Feuilles de temps
- 📊 Recrutement
- 💸 Paie (EE)

**Marketing** :
- 📧 Email Marketing
- 📱 Marketing Automation
- 🎯 Événements
- 📞 Marketing téléphonique

**Services** :
- 🔧 Projet : Gestion de projets
- 🎫 Assistance : Helpdesk
- 📋 Feuilles de service
- 🏗️ Chantiers

**Productivité** :
- 📝 Documents
- ✍️ Signature électronique
- 📞 VoIP
- 💬 Discuss (Chat)

**Site Web** :
- 🌐 Constructeur de site web
- 📝 Blog
- 📚 Forum
- 📊 Live Chat

### 1.5 Pourquoi apprendre Odoo ?

**Opportunités professionnelles** :

```
Développeur Odoo Junior
   Salaire : 30K-45K € / an
   ↓
Développeur Odoo Confirmé
   Salaire : 45K-60K € / an
   ↓
Développeur Odoo Senior
   Salaire : 60K-80K € / an
   ↓
Architecte Odoo
   Salaire : 80K-100K+ € / an
```

**Compétences transférables** :
- 🐍 **Python** : Langage de programmation moderne
- 🗄️ **PostgreSQL** : Base de données relationnelle
- 💻 **JavaScript** : Développement frontend
- 🏗️ **Architecture MVC** : Conception logicielle
- 🔐 **Sécurité** : Gestion des droits et permissions
- 📊 **Modélisation de données** : Conception de bases de données

**Marché en croissance** :
- 📈 **Demande forte** de développeurs Odoo
- 🌍 **Marché international** (Europe, Afrique, Moyen-Orient, Amérique)
- 🏢 **Tous secteurs** : PME, grandes entreprises, startups
- 💼 **Freelancing** : Nombreuses missions disponibles

### 1.6 Prérequis pour cette formation

**Connaissances essentielles** :
- ✅ **Python** : Variables, fonctions, classes, héritage
- ✅ **SQL** : SELECT, INSERT, UPDATE, DELETE, JOIN
- ✅ **HTML/CSS** : Bases de la structure web
- ✅ **Programmation orientée objet** : Classes, objets, héritage

**Connaissances recommandées** :
- 📘 **JavaScript** : Syntaxe de base, DOM
- 📘 **Git** : Gestion de versions
- 📘 **Linux** : Commandes de base
- 📘 **Framework web** : Django, Flask (similaire à Odoo)

**Outils nécessaires** :
- 💻 **Ordinateur** : Windows, macOS ou Linux
- 🔧 **IDE** : VS Code, PyCharm, ou Sublime Text
- 🌐 **Navigateur** : Chrome, Firefox (avec DevTools)
- 📝 **Terminal** : PowerShell (Windows), Terminal (macOS/Linux)

> 💡 **Astuce** : Même si vous êtes débutant, cette formation vous guidera pas à pas. Tous les concepts sont expliqués en détail.

---

## <a id="architecture"></a>🏗️ 2. Architecture logicielle d'Odoo

### 2.1 Vue d'ensemble : Architecture Trois Tiers

Odoo utilise une **architecture trois tiers** (three-tier architecture) qui sépare clairement les responsabilités :

```
┌──────────────────────────────────────────────────────────┐
│                   TIER 1 : PRÉSENTATION                  │
│                   (Client - Frontend)                     │
│                                                           │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐        │
│  │ Navigateur │  │   Mobile   │  │    API     │        │
│  │    Web     │  │    App     │  │  Externe   │        │
│  └────────────┘  └────────────┘  └────────────┘        │
│                                                           │
│       HTML/CSS          JavaScript (OWL)                 │
│       QWeb Templates    Bootstrap                        │
└──────────────────────────────────────────────────────────┘
                           ↕
                  HTTP / HTTPS (Port 8069)
                  JSON-RPC / XML-RPC
                           ↕
┌──────────────────────────────────────────────────────────┐
│                   TIER 2 : APPLICATION                    │
│                   (Serveur - Backend)                     │
│                                                           │
│  ┌────────────────────────────────────────────────────┐ │
│  │           ODOO FRAMEWORK (Python 3.10+)            │ │
│  │                                                     │ │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐        │ │
│  │  │  Models  │  │  Views   │  │Controllers│        │ │
│  │  │ (Python) │  │  (XML)   │  │ (Python)  │        │ │
│  │  └──────────┘  └──────────┘  └──────────┘        │ │
│  │                                                     │ │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐        │ │
│  │  │   ORM    │  │ Security │  │ Workflow  │        │ │
│  │  │ (Active  │  │  (ACL)   │  │  Engine   │        │ │
│  │  │  Record) │  └──────────┘  └──────────┘        │ │
│  │  └──────────┘                                      │ │
│  │                                                     │ │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐        │ │
│  │  │  Cache   │  │   Queue  │  │  Report   │        │ │
│  │  │ (Redis)  │  │   Jobs   │  │  Engine   │        │ │
│  │  └──────────┘  └──────────┘  └──────────┘        │ │
│  └────────────────────────────────────────────────────┘ │
│                                                           │
│              Werkzeug (WSGI Server)                      │
│              Gevent (Async I/O)                          │
└──────────────────────────────────────────────────────────┘
                           ↕
                      SQL Queries
                    (psycopg2 driver)
                           ↕
┌──────────────────────────────────────────────────────────┐
│                   TIER 3 : DONNÉES                       │
│                (Base de données PostgreSQL)               │
│                                                           │
│         ┌──────────────────────────────┐                │
│         │      PostgreSQL 12+          │                │
│         │      (Port 5432)             │                │
│         │                              │                │
│         │  ┌────────────────────────┐ │                │
│         │  │  Tables                │ │                │
│         │  │  - res_partner         │ │                │
│         │  │  - sale_order          │ │                │
│         │  │  - product_product     │ │                │
│         │  │  - account_move        │ │                │
│         │  │  - ...                 │ │                │
│         │  └────────────────────────┘ │                │
│         │                              │                │
│         │  ┌────────────────────────┐ │                │
│         │  │  Indexes & Constraints │ │                │
│         │  │  Views & Functions     │ │                │
│         │  │  Sequences             │ │                │
│         │  └────────────────────────┘ │                │
│         └──────────────────────────────┘                │
└──────────────────────────────────────────────────────────┘
```

**Explications détaillées** :

#### 🔵 Tier 1 : Présentation (Frontend)

**Rôle** : Interface utilisateur et expérience utilisateur

**Technologies** :
- **HTML5** : Structure des pages
- **CSS3 / Bootstrap** : Styles et mise en page responsive
- **JavaScript** : Interactivité côté client
- **OWL (Odoo Web Library)** : Framework JavaScript propriétaire (similaire à Vue.js)
- **QWeb** : Moteur de templates XML pour le rendu

**Composants** :
```
Interface Web
├── Views (Vues)
│   ├── Form View (Formulaires)
│   ├── List View (Tableaux)
│   ├── Kanban View (Cartes)
│   ├── Calendar View (Calendrier)
│   ├── Graph View (Graphiques)
│   └── Pivot View (Tableaux croisés)
├── Widgets (Composants UI)
│   ├── Date Picker
│   ├── Many2one Select
│   ├── Image Upload
│   └── Rich Text Editor
└── Actions
    ├── Buttons
    ├── Menus
    └── Wizards
```

**Communication** :
- **JSON-RPC** : Appels de méthodes à distance en JSON
- **Websocket** : Pour le chat et les notifications en temps réel
- **Long Polling** : Pour les mises à jour asynchrones

#### 🟢 Tier 2 : Application (Backend)

**Rôle** : Logique métier, traitement des données, sécurité

**Technologies** :
- **Python 3.10+** : Langage principal
- **Werkzeug** : Serveur WSGI (Web Server Gateway Interface)
- **Gevent** : Bibliothèque pour l'asynchrone (coroutines)
- **Babel** : Internationalisation (i18n)
- **Pillow** : Traitement d'images
- **reportlab / wkhtmltopdf** : Génération de PDF
- **lxml** : Parsing et manipulation XML

**Framework Odoo** :

```python
odoo/
├── addons/              # Modules officiels
│   ├── base/           # Module de base (obligatoire)
│   ├── sale/           # Module des ventes
│   ├── account/        # Module de comptabilité
│   └── ...
├── odoo/               # Core du framework
│   ├── __init__.py
│   ├── api.py          # Décorateurs @api
│   ├── models.py       # Classe Model de base
│   ├── fields.py       # Types de champs
│   ├── orm.py          # ORM (Active Record)
│   ├── sql_db.py       # Connexion PostgreSQL
│   ├── http.py         # Contrôleurs HTTP
│   ├── service/        # Services (cron, mail, etc.)
│   └── tools/          # Utilitaires
└── odoo-bin            # Point d'entrée (serveur)
```

**ORM (Object-Relational Mapping)** :

Odoo utilise le pattern **Active Record** :

```python
# Un objet Python = Une ligne en base de données
book = env['library.book'].browse(1)
book.name = "Nouveau titre"
book.write({'price': 29.99})  # UPDATE en SQL

# Une collection d'objets = Plusieurs lignes
books = env['library.book'].search([('author', '=', 'Hugo')])
for book in books:
    print(book.name)  # SELECT en SQL
```

**Sécurité** :

```
Requête HTTP
    ↓
1. Authentification (Session / Token)
    ↓
2. Vérification des droits d'accès (ACL)
    ↓
3. Application des règles d'enregistrement (Record Rules)
    ↓
4. Exécution de la méthode
    ↓
5. Filtrage des champs visibles
    ↓
Réponse
```

#### 🟣 Tier 3 : Données (Database)

**Rôle** : Persistance des données

**PostgreSQL** :
- **Version minimale** : 12 (recommandé : 14 ou 15)
- **Port par défaut** : 5432
- **Encodage** : UTF-8
- **Locale** : en_US.UTF-8 ou fr_FR.UTF-8

**Structure de la base de données** :

```sql
-- Tables principales
res_partner          -- Contacts (clients, fournisseurs)
res_users            -- Utilisateurs
res_company          -- Entreprises
ir_model             -- Métadonnées des modèles
ir_model_fields      -- Métadonnées des champs
ir_ui_view           -- Définitions des vues
ir_actions           -- Actions (menus, boutons)
ir_cron              -- Tâches planifiées
ir_attachment        -- Fichiers joints

-- Tables métier (exemples)
sale_order           -- Commandes de vente
sale_order_line      -- Lignes de commande
product_product      -- Produits
product_template     -- Modèles de produits
account_move         -- Écritures comptables
stock_picking        -- Bons de livraison
```

**Conventions de nommage** :

```python
# Modèle Python : library.book
# Table PostgreSQL : library_book

# Champ Python : author_id (Many2one vers res.partner)
# Colonne PostgreSQL : author_id (INTEGER, FK vers res_partner.id)

# Champ Python : tag_ids (Many2many vers library.tag)
# Table intermédiaire : library_book_library_tag_rel
# Colonnes : book_id, tag_id
```

### 2.2 Architecture MVC d'Odoo

Odoo implémente le pattern **MVC (Model-View-Controller)** avec des adaptations :

```
┌──────────────────────────────────────────────────────┐
│                     REQUÊTE                          │
│   (Utilisateur clique sur un bouton/menu)           │
└──────────────────────────────────────────────────────┘
                        │
                        ↓
┌──────────────────────────────────────────────────────┐
│                  CONTROLLER                          │
│            (Gestion des routes HTTP)                 │
│                                                      │
│  @http.route('/library/books', auth='user')         │
│  def list_books(self):                              │
│      books = request.env['library.book'].search([])  │
│      return request.render('template', {             │
│          'books': books                              │
│      })                                              │
│                                                      │
│  Fichier : controllers/main.py                      │
└──────────────────────────────────────────────────────┘
                        │
                        ↓
┌──────────────────────────────────────────────────────┐
│                     MODEL                            │
│              (Logique métier & Données)              │
│                                                      │
│  class LibraryBook(models.Model):                   │
│      _name = 'library.book'                         │
│                                                      │
│      name = fields.Char('Titre')                    │
│      author_id = fields.Many2one('res.partner')     │
│      pages = fields.Integer()                       │
│                                                      │
│      def action_borrow(self):                       │
│          # Logique métier                           │
│          self.state = 'borrowed'                    │
│                                                      │
│  Fichier : models/library_book.py                   │
└──────────────────────────────────────────────────────┘
                        │
                        ↓
┌──────────────────────────────────────────────────────┐
│                   DATABASE                           │
│              (Stockage des données)                  │
│                                                      │
│  Table : library_book                               │
│  Colonnes :                                         │
│    - id (serial primary key)                        │
│    - name (varchar)                                 │
│    - author_id (integer, FK → res_partner)          │
│    - pages (integer)                                │
│    - state (varchar)                                │
│                                                      │
│  PostgreSQL                                         │
└──────────────────────────────────────────────────────┘
                        │
                        ↑ (Données retournées)
                        │
┌──────────────────────────────────────────────────────┐
│                      VIEW                            │
│             (Interface utilisateur)                  │
│                                                      │
│  <record id="view_book_form" model="ir.ui.view">   │
│      <field name="model">library.book</field>       │
│      <field name="arch" type="xml">                 │
│          <form>                                      │
│              <field name="name"/>                    │
│              <field name="author_id"/>               │
│              <field name="pages"/>                   │
│          </form>                                     │
│      </field>                                        │
│  </record>                                           │
│                                                      │
│  Fichier : views/library_book_views.xml            │
└──────────────────────────────────────────────────────┘
                        │
                        ↓
┌──────────────────────────────────────────────────────┐
│                   RÉPONSE                            │
│              (Page HTML rendue)                      │
└──────────────────────────────────────────────────────┘
```

**Explication détaillée de chaque composant** :

#### 🔵 MODEL (Modèle)

**Responsabilités** :
1. **Définir la structure des données** (champs = colonnes)
2. **Logique métier** (calculs, validations, workflows)
3. **Relations entre entités** (Many2one, One2many, Many2many)
4. **Contraintes et validations**
5. **Méthodes CRUD** (Create, Read, Update, Delete)

**Exemple complet** :

```python
# models/library_book.py

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    """
    Modèle principal pour gérer les livres.
    Hérite de models.Model pour devenir une table PostgreSQL.
    """
    
    # ========== MÉTADONNÉES DU MODÈLE ==========
    
    _name = 'library.book'              # Nom technique → table 'library_book'
    _description = 'Livre'              # Description lisible
    _inherit = ['mail.thread']          # Héritage (chatter)
    _order = 'name, date_publication desc'  # Ordre par défaut
    _rec_name = 'name'                  # Champ pour l'affichage
    
    # ========== DÉFINITION DES CHAMPS ==========
    
    # Champs de base
    name = fields.Char('Titre', required=True, index=True)
    isbn = fields.Char('ISBN', size=13)
    pages = fields.Integer('Nombre de pages', default=0)
    price = fields.Float('Prix', digits=(10, 2))
    description = fields.Text('Résumé')
    date_publication = fields.Date('Date de publication')
    
    # Champs relationnels
    author_id = fields.Many2one('res.partner', 'Auteur')
    category_id = fields.Many2one('library.category', 'Catégorie')
    tag_ids = fields.Many2many('library.tag', string='Tags')
    
    # Champs de statut
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('available', 'Disponible'),
        ('borrowed', 'Emprunté'),
    ], default='draft')
    
    # Champs calculés
    page_category = fields.Selection([
        ('short', 'Court'),
        ('medium', 'Moyen'),
        ('long', 'Long')
    ], compute='_compute_page_category', store=True)
    
    # ========== MÉTHODES CALCULÉES ==========
    
    @api.depends('pages')
    def _compute_page_category(self):
        """Calcule la catégorie selon le nombre de pages."""
        for book in self:
            if book.pages < 200:
                book.page_category = 'short'
            elif book.pages < 400:
                book.page_category = 'medium'
            else:
                book.page_category = 'long'
    
    # ========== CONTRAINTES ==========
    
    _sql_constraints = [
        ('isbn_unique', 'UNIQUE(isbn)', 'ISBN doit être unique!')
    ]
    
    @api.constrains('pages')
    def _check_pages(self):
        """Valide que pages >= 0."""
        for book in self:
            if book.pages < 0:
                raise ValidationError('Pages doit être positif!')
    
    # ========== MÉTHODES MÉTIER ==========
    
    def action_borrow(self):
        """Emprunte le livre."""
        self.ensure_one()  # S'assure qu'il n'y a qu'un seul enregistrement
        if self.state != 'available':
            raise ValidationError('Livre non disponible!')
        self.state = 'borrowed'
        self.message_post(body="Livre emprunté")
    
    def action_return(self):
        """Retourne le livre."""
        self.state = 'available'
        self.message_post(body="Livre retourné")
```

#### 🟢 VIEW (Vue)

**Responsabilités** :
1. **Afficher les données** à l'utilisateur
2. **Définir la mise en page** (form, list, kanban, etc.)
3. **Configurer les widgets** (date picker, many2one, etc.)
4. **Définir les actions** (boutons, menus)
5. **Filtres et recherches**

**Types de vues** :

```xml
<!-- views/library_book_views.xml -->

<!-- VUE LISTE (Tree) : Affichage en tableau -->
<record id="view_library_book_tree" model="ir.ui.view">
    <field name="name">library.book.tree</field>
    <field name="model">library.book</field>
    <field name="arch" type="xml">
        <tree string="Livres">
            <field name="name"/>
            <field name="author_id"/>
            <field name="pages"/>
            <field name="state"/>
        </tree>
    </field>
</record>

<!-- VUE FORMULAIRE (Form) : Détail d'un enregistrement -->
<record id="view_library_book_form" model="ir.ui.view">
    <field name="name">library.book.form</field>
    <field name="model">library.book</field>
    <field name="arch" type="xml">
        <form string="Livre">
            <header>
                <button name="action_borrow" type="object"
                        string="Emprunter" class="btn-primary"/>
                <field name="state" widget="statusbar"/>
            </header>
            <sheet>
                <group>
                    <field name="name"/>
                    <field name="author_id"/>
                    <field name="pages"/>
                </group>
            </sheet>
        </form>
    </field>
</record>

<!-- VUE KANBAN : Affichage en cartes -->
<record id="view_library_book_kanban" model="ir.ui.view">
    <field name="name">library.book.kanban</field>
    <field name="model">library.book</field>
    <field name="arch" type="xml">
        <kanban>
            <field name="name"/>
            <field name="author_id"/>
            <templates>
                <t t-name="kanban-box">
                    <div class="oe_kanban_card">
                        <strong><field name="name"/></strong>
                        <div><field name="author_id"/></div>
                    </div>
                </t>
            </templates>
        </kanban>
    </field>
</record>
```

#### 🟡 CONTROLLER (Contrôleur)

**Responsabilités** :
1. **Gérer les routes HTTP** personnalisées
2. **Recevoir les requêtes** web
3. **Appeler les modèles** pour traiter les données
4. **Retourner des réponses** (HTML, JSON, PDF, etc.)
5. **Gérer l'authentification**

**Exemple complet** :

```python
# controllers/main.py

from odoo import http
from odoo.http import request

class LibraryController(http.Controller):
    """Contrôleur pour les routes personnalisées."""
    
    @http.route('/library/books', type='http', auth='user', website=True)
    def list_books(self, **kwargs):
        """
        Page web listant tous les livres.
        URL : http://localhost:8069/library/books
        """
        # Accéder au modèle via request.env
        books = request.env['library.book'].search([
            ('state', '=', 'available')
        ])
        
        # Rendre un template avec les données
        return request.render('library_app.book_list_page', {
            'books': books
        })
    
    @http.route('/api/books', type='json', auth='user', methods=['GET'])
    def api_get_books(self, **kwargs):
        """
        API JSON pour récupérer les livres.
        URL : http://localhost:8069/api/books
        """
        books = request.env['library.book'].search([])
        
        return {
            'status': 'success',
            'data': [{
                'id': book.id,
                'name': book.name,
                'author': book.author_id.name if book.author_id else None,
                'pages': book.pages,
            } for book in books]
        }
    
    @http.route('/library/book/<int:book_id>', type='http', auth='public')
    def book_detail(self, book_id, **kwargs):
        """
        Page de détail d'un livre.
        URL : http://localhost:8069/library/book/1
        """
        book = request.env['library.book'].sudo().browse(book_id)
        
        if not book.exists():
            return request.not_found()
        
        return request.render('library_app.book_detail_page', {
            'book': book
        })
```

### 2.3 Le système de modules

**Qu'est-ce qu'un module ?**

Un module Odoo est un **package Python** qui encapsule une fonctionnalité complète. C'est l'unité de base de l'extensibilité d'Odoo.

**Caractéristiques** :
- ✅ **Indépendant** : Peut être installé/désinstallé séparément
- ✅ **Réutilisable** : Peut être utilisé dans plusieurs projets
- ✅ **Extensible** : Peut hériter et étendre d'autres modules
- ✅ **Versionné** : Suit un schéma de versioning sémantique

**Structure complète d'un module** :

```
mon_module/
│
├── __init__.py                    # Point d'entrée Python
├── __manifest__.py                # Configuration et métadonnées
│
├── models/                        # Modèles (logique métier)
│   ├── __init__.py
│   ├── mon_modele.py
│   └── autre_modele.py
│
├── views/                         # Vues XML
│   ├── mon_modele_views.xml      # Vues form, tree, kanban
│   ├── templates.xml              # Templates QWeb
│   └── menus.xml                  # Menus et actions
│
├── controllers/                   # Contrôleurs HTTP
│   ├── __init__.py
│   └── main.py
│
├── security/                      # Sécurité
│   ├── ir.model.access.csv       # Droits CRUD
│   └── security.xml               # Groupes et règles
│
├── data/                          # Données
│   ├── data.xml                   # Données de base
│   └── demo.xml                   # Données de démonstration
│
├── static/                        # Fichiers statiques
│   ├── description/
│   │   ├── icon.png              # Icône 256x256
│   │   ├── banner.png            # Bannière (large)
│   │   └── index.html            # Description HTML
│   └── src/
│       ├── js/
│       │   └── mon_widget.js     # Widgets JavaScript
│       ├── css/
│       │   └── styles.css        # Styles personnalisés
│       └── xml/
│           └── templates.xml      # Templates QWeb JS
│
├── wizard/                        # Assistants (wizards)
│   ├── __init__.py
│   ├── mon_wizard.py             # Modèle TransientModel
│   └── wizard_views.xml          # Vues du wizard
│
├── report/                        # Rapports
│   ├── __init__.py
│   ├── report.py                 # Logique des rapports
│   └── report_templates.xml      # Templates de rapports PDF
│
├── tests/                         # Tests unitaires
│   ├── __init__.py
│   ├── test_models.py            # Tests des modèles
│   └── test_controllers.py       # Tests des contrôleurs
│
└── i18n/                          # Traductions
    ├── fr.po                      # Traduction française
    ├── ar.po                      # Traduction arabe
    └── en.po                      # Traduction anglaise
```

**Fichier __manifest__.py détaillé** :

```python
# -*- coding: utf-8 -*-
{
    # ========== INFORMATIONS DE BASE ==========
    
    'name': 'Nom du Module',
    'version': '19.0.1.0.0',
    'category': 'Services',  # Catégories : Sales, Accounting, Website, etc.
    'summary': 'Résumé court (1 ligne)',
    'description': """
Titre du Module
===============

Description longue en Markdown.

Fonctionnalités :
-----------------
* Fonctionnalité 1
* Fonctionnalité 2

Notes :
-------
Informations supplémentaires
    """,
    
    # ========== AUTEUR ET LICENCE ==========
    
    'author': 'Votre Nom ou Votre Entreprise',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',  # LGPL-3 (CE) ou OPL-1 (EE)
    'support': 'support@example.com',
    
    # ========== DÉPENDANCES ==========
    
    'depends': [
        'base',           # Module de base (toujours requis)
        'mail',           # Pour le chatter
        'sale',           # Module des ventes
    ],
    
    # ========== DONNÉES ==========
    
    'data': [
        # Ordre important !
        
        # 1. Sécurité (en premier)
        'security/security.xml',
        'security/ir.model.access.csv',
        
        # 2. Données initiales
        'data/sequences.xml',
        'data/categories.xml',
        
        # 3. Vues
        'views/menu.xml',
        'views/mon_modele_views.xml',
        'views/templates.xml',
        
        # 4. Rapports
        'report/report_templates.xml',
        
        # 5. Wizards
        'wizard/wizard_views.xml',
    ],
    
    'demo': [
        'data/demo_data.xml',
    ],
    
    # ========== ASSETS (JS/CSS) ==========
    
    'assets': {
        'web.assets_backend': [
            'mon_module/static/src/js/**/*',
            'mon_module/static/src/css/**/*',
        ],
        'web.assets_frontend': [
            'mon_module/static/src/js/frontend.js',
        ],
    },
    
    # ========== CONFIGURATION ==========
    
    'installable': True,     # Peut être installé
    'application': True,      # Apparaît comme une app
    'auto_install': False,    # Installation automatique si dépendances
    
    # ========== ODOO APP STORE ==========
    
    'price': 0.00,           # Prix en euros (0 = gratuit)
    'currency': 'EUR',
    'images': [
        'static/description/banner.png',
        'static/description/screenshot1.png',
        'static/description/screenshot2.png',
    ],
    
    # ========== AUTRES ==========
    
    'sequence': 10,          # Ordre d'affichage
    'external_dependencies': {
        'python': ['requests', 'pandas'],  # Dépendances Python
        'bin': ['wkhtmltopdf'],           # Binaires système
    },
}
```

---

## <a id="concepts"></a>💡 3. Concepts fondamentaux

### 3.1 L'ORM (Object-Relational Mapping)

L'ORM d'Odoo traduit automatiquement les objets Python en requêtes SQL. Il utilise le pattern **Active Record**.

**Principe** :

```python
# Python : Objet
book = env['library.book'].browse(1)
book.name = "Nouveau titre"

# SQL généré automatiquement :
# UPDATE library_book SET name='Nouveau titre' WHERE id=1;
```

**Avantages** :
- ✅ Pas besoin d'écrire du SQL
- ✅ Protection contre les injections SQL
- ✅ Cache intelligent
- ✅ Code portable entre BDD

**API de l'ORM** :

```python
# ========== CREATE ==========
book = env['library.book'].create({
    'name': 'Mon Livre',
    'pages': 250
})

# ========== READ ==========
# browse() : Charger par ID
book = env['library.book'].browse(1)
books = env['library.book'].browse([1, 2, 3])

# search() : Rechercher avec domaine
books = env['library.book'].search([
    ('author_id', '=', 5),
    ('pages', '>', 200)
])

# search_read() : Rechercher + charger les champs
books = env['library.book'].search_read(
    [('state', '=', 'available')],
    ['name', 'author_id', 'pages']
)

# ========== UPDATE ==========
# write() : Mettre à jour
book.write({'price': 29.99})
books.write({'state': 'available'})

# Assignation directe
book.price = 29.99

# ========== DELETE ==========
book.unlink()
books.unlink()
```

### 3.2 Le système de sécurité

Odoo implémente une **sécurité multi-niveaux** :

#### Niveau 1 : Groupes d'utilisateurs

```python
# Utilisateur appartient à des groupes
user.groups_id = [
    group_user,      # Utilisateur basique
    group_manager,   # Manager
]

# Groupe défini dans security.xml
<record id="group_library_user" model="res.groups">
    <field name="name">Library User</field>
    <field name="category_id" ref="base.module_category_services"/>
</record>
```

#### Niveau 2 : Droits d'accès (CRUD)

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_book_user,access_book_user,model_library_book,group_library_user,1,1,1,0
access_book_manager,access_book_manager,model_library_book,group_library_manager,1,1,1,1
```

**Signification** :
- `perm_read=1` : Peut lire (SELECT)
- `perm_write=1` : Peut modifier (UPDATE)
- `perm_create=1` : Peut créer (INSERT)
- `perm_unlink=1` : Peut supprimer (DELETE)

#### Niveau 3 : Règles d'enregistrement

```xml
<!-- Règle : Un vendeur ne voit que ses propres ventes -->
<record id="sale_order_personal_rule" model="ir.rule">
    <field name="name">Personal Sales Orders</field>
    <field name="model_id" ref="model_sale_order"/>
    <field name="groups" eval="[(4, ref('sales_team.group_sale_salesman'))]"/>
    <field name="domain_force">[('user_id', '=', user.id)]</field>
</record>
```

#### Niveau 4 : Droits sur les champs

```python
# Champ visible seulement pour les managers
price = fields.Float(
    'Prix',
    groups='library_app.group_library_manager'
)
```

### 3.3 L'environnement (env)

**`self.env`** est l'objet central pour accéder à tout dans Odoo :

```python
# Accéder à un modèle
books = self.env['library.book']

# Utilisateur actuel
user = self.env.user

# Entreprise actuelle
company = self.env.company

# Contexte (langue, timezone, etc.)
context = self.env.context

# Base de données actuelle
cursor = self.env.cr

# Changer de contexte
books = self.env['library.book'].with_context(lang='fr_FR')

# Changer d'utilisateur (sudo)
books = self.env['library.book'].sudo()

# Changer d'entreprise
books = self.env['library.book'].with_company(company_id)
```

### 3.4 Les recordsets

Un **recordset** est une collection d'enregistrements d'un même modèle :

```python
# Recordset vide
books = self.env['library.book']

# Recordset avec plusieurs enregistrements
books = self.env['library.book'].search([])

# Itération
for book in books:
    print(book.name)

# Opérations sur recordsets
books1 = self.env['library.book'].browse([1, 2])
books2 = self.env['library.book'].browse([2, 3])

union = books1 | books2        # Union
intersection = books1 & books2  # Intersection
difference = books1 - books2    # Différence

# Méthodes utiles
books.ids                # Liste des IDs
books.ensure_one()       # S'assurer qu'il y a 1 seul record
books.exists()           # Filtrer les records qui existent
books.filtered(lambda b: b.pages > 200)  # Filtrer
books.mapped('name')     # Extraire un champ
books.sorted('name')     # Trier
```

---

## <a id="ecosysteme"></a>🌐 4. Écosystème Odoo

### 4.1 Communauté Odoo

**Forums et ressources** :
- 📝 **Forum officiel** : https://www.odoo.com/forum
- 💬 **GitHub** : https://github.com/odoo/odoo
- 📚 **Documentation** : https://www.odoo.com/documentation/19.0/
- 🎓 **eLearning** : https://www.odoo.com/slides

**Communautés tierces** :
- **OCA (Odoo Community Association)** : https://odoo-community.org/
  - Modules communautaires de qualité
  - Maintenus par la communauté
  - Code review strict
- **Reddit r/Odoo** : Discussions et entraide
- **Stack Overflow** : Questions techniques

### 4.2 Odoo App Store

**Apps officielles** :
- 💰 Apps payantes développées par Odoo S.A.
- ✅ Support officiel
- 🔄 Mises à jour garanties

**Apps communautaires** :
- 🆓 Souvent gratuites
- 👥 Développées par des partenaires
- ⚠️ Qualité variable

### 4.3 Partenaires Odoo

**Niveaux de partenariat** :
- 🥇 **Gold Partner** : Expertise maximale
- 🥈 **Silver Partner** : Expertise confirmée
- 🥉 **Ready Partner** : Partenaire certifié

**Services proposés** :
- 💼 Implémentation
- 🔧 Personnalisation
- 📚 Formation
- 🛠️ Support et maintenance
- ☁️ Hébergement

---

## 📝 Conclusion du Module 0

Vous avez maintenant une compréhension solide de :
- ✅ Ce qu'est Odoo et son écosystème
- ✅ L'architecture trois tiers
- ✅ Le pattern MVC adapté à Odoo
- ✅ La structure d'un module
- ✅ Les concepts fondamentaux (ORM, sécurité, env, recordsets)

**Prochaine étape** : Module 1 - Installation d'Odoo 19 sur Windows et macOS

---

## 🔗 Liens utiles

- 📖 Documentation officielle : https://www.odoo.com/documentation/19.0/
- 💻 Code source : https://github.com/odoo/odoo
- 🎓 Formations : https://www.odoo.com/slides
- 💬 Forum : https://www.odoo.com/forum
- 🐛 Bug tracker : https://github.com/odoo/odoo/issues

