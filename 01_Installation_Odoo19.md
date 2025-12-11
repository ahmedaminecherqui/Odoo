# 💻 Formation Odoo 19 - Installation

**Module 1 : Installation sur Windows et macOS**

---

## 📋 Table des matières

1. [Prérequis système](#prerequis)
2. [Installation sur Windows](#windows)
3. [Installation sur macOS](#macos)
4. [Configuration avancée](#configuration)
5. [Vérification et dépannage](#verification)
6. [Configuration de l'IDE](#ide)

---

## <a id="prerequis"></a>⚙️ 1. Prérequis système

### 1.1 Configuration matérielle minimale

**Développement** :
- 💾 **RAM** : 8 GB minimum (16 GB recommandé)
- 💿 **Disque** : 20 GB d'espace libre (SSD recommandé)
- 🖥️ **CPU** : 2 cœurs minimum (4 cœurs recommandé)
- 🌐 **Connexion internet** : Pour télécharger les dépendances

**Production** :
- 💾 **RAM** : 16 GB minimum (32+ GB recommandé)
- 💿 **Disque** : 100+ GB (SSD obligatoire)
- 🖥️ **CPU** : 4+ cœurs
- 🌐 **Bande passante** : Stable et rapide

### 1.2 Logiciels requis

**Tous systèmes** :
- 🐍 **Python 3.10 ou 3.11** (pas 3.12 encore)
- 🗄️ **PostgreSQL 12+** (14 ou 15 recommandé)
- 📦 **Git** (pour cloner le dépôt)
- 🖼️ **wkhtmltopdf** (pour générer des PDFs)

**Optionnels mais recommandés** :
- 🔧 **Node.js & npm** (pour certains modules)
- 📝 **VS Code** ou PyCharm (IDE)
- 🐳 **Docker** (pour environnements isolés)

### 1.3 Connaissances préalables

✅ Utilisation de la ligne de commande  
✅ Installation de logiciels  
✅ Notions de base en réseau (ports, localhost)  
✅ Gestion de variables d'environnement (PATH)  

---

## <a id="windows"></a>🪟 2. Installation sur Windows

### 2.1 Installer Python 3.10

#### Étape 1 : Télécharger Python

1. Aller sur **https://www.python.org/downloads/**
2. Télécharger **Python 3.10.x** (version stable)
   - ⚠️ Ne pas prendre Python 3.12 (incompatibilités)
3. Lancer l'installateur

#### Étape 2 : Installation

```
🔴 CRITIQUE : Cocher "Add Python to PATH"
```

Options d'installation recommandées :
- ✅ Install for all users
- ✅ Add Python to PATH
- ✅ pip (inclus par défaut)
- ✅ py launcher

Chemin d'installation suggéré : `C:\Python310`

#### Étape 3 : Vérification

Ouvrir **PowerShell** ou **cmd** :

```powershell
# Vérifier Python
python --version
# Sortie attendue : Python 3.10.x

# Vérifier pip
pip --version
# Sortie attendue : pip 23.x.x from ...

# Vérifier que Python est dans le PATH
where python
# Sortie : C:\Python310\python.exe
```

**En cas de problème** :
```powershell
# Si "python" n'est pas reconnu, ajouter manuellement au PATH
# Panneau de configuration > Système > Paramètres système avancés
# Variables d'environnement > PATH > Modifier > Nouveau
# Ajouter : C:\Python310 et C:\Python310\Scripts
```

### 2.2 Installer PostgreSQL

#### Étape 1 : Téléchargement

1. Aller sur **https://www.postgresql.org/download/windows/**
2. Télécharger l'installateur **EDB PostgreSQL 15**
3. Lancer l'installateur

#### Étape 2 : Installation

**Configuration recommandée** :
- **Composants** : Tous cochés
- **Dossier** : `C:\Program Files\PostgreSQL\15`
- **Mot de passe postgres** : `odoo` (ou autre, à noter !)
- **Port** : `5432` (par défaut)
- **Locale** : `French, France` ou `English, United States`

#### Étape 3 : Ajouter PostgreSQL au PATH

```powershell
# Méthode 1 : Manuellement
# Panneau de configuration > Système > Variables d'environnement
# PATH > Modifier > Nouveau
# Ajouter : C:\Program Files\PostgreSQL\15\bin

# Méthode 2 : PowerShell (en Admin)
[Environment]::SetEnvironmentVariable(
    "Path",
    $env:Path + ";C:\Program Files\PostgreSQL\15\bin",
    "Machine"
)
```

#### Étape 4 : Vérification

```powershell
# Vérifier PostgreSQL
psql --version
# Sortie : psql (PostgreSQL) 15.x

# Tester la connexion
psql -U postgres
# Entrer le mot de passe : odoo
# Si succès : postgres=#
# Quitter : \q
```

#### Étape 5 : Créer un utilisateur Odoo

```powershell
# Se connecter à PostgreSQL
psql -U postgres

# Dans psql (prompt: postgres=#)
CREATE USER odoo WITH CREATEDB PASSWORD 'odoo';

# Vérifier
\du
# Doit afficher l'utilisateur "odoo"

# Quitter
\q
```

**Explication** :
- `CREATE USER odoo` : Crée un utilisateur nommé "odoo"
- `WITH CREATEDB` : Permet à cet utilisateur de créer des bases de données
- `PASSWORD 'odoo'` : Définit le mot de passe

### 2.3 Installer Git

#### Étape 1 : Téléchargement

1. Aller sur **https://git-scm.com/download/win**
2. Télécharger l'installateur
3. Lancer l'installation

#### Étape 2 : Configuration

Options recommandées :
- ✅ Use Git from Windows Command Prompt
- ✅ Checkout Windows-style, commit Unix-style line endings
- ✅ Use Windows' default console window

#### Étape 3 : Vérification

```powershell
git --version
# Sortie : git version 2.x.x
```

### 2.4 Télécharger Odoo 19

#### Étape 1 : Créer la structure de dossiers

```powershell
# Créer le dossier principal
mkdir C:\odoo19
cd C:\odoo19

# Créer le dossier pour les modules personnalisés
mkdir custom_addons
```

#### Étape 2 : Cloner le dépôt Odoo

```powershell
# Cloner la branche 19.0 (version stable)
git clone https://github.com/odoo/odoo.git --depth 1 --branch 19.0 odoo

# Explications :
# --depth 1 : Ne télécharge que le dernier commit (plus rapide)
# --branch 19.0 : Clone la branche Odoo 19
# odoo : Nom du dossier de destination
```

**Temps de téléchargement** : 5-15 minutes selon la connexion

#### Étape 3 : Vérifier le téléchargement

```powershell
cd odoo
dir
# Doit afficher : addons, debian, doc, odoo, odoo-bin, requirements.txt, etc.
```

### 2.5 Créer un environnement virtuel Python

**Pourquoi un environnement virtuel ?**
- ✅ Isoler les dépendances d'Odoo
- ✅ Éviter les conflits avec d'autres projets Python
- ✅ Faciliter la gestion des versions

```powershell
# Se placer dans le dossier odoo
cd C:\odoo19\odoo

# Créer l'environnement virtuel (nommé "venv")
python -m venv venv

# Activer l'environnement virtuel
.\venv\Scripts\activate

# Le prompt devrait changer pour afficher (venv)
# Exemple : (venv) C:\odoo19\odoo>
```

**Commandes utiles** :
```powershell
# Activer
.\venv\Scripts\activate

# Désactiver
deactivate

# Supprimer (si besoin de recommencer)
Remove-Item -Recurse -Force venv
```

### 2.6 Installer les dépendances Python

#### Étape 1 : Mettre à jour pip

```powershell
# S'assurer que l'environnement virtuel est activé
# Le prompt doit afficher (venv)

# Mettre à jour pip
python -m pip install --upgrade pip setuptools wheel
```

#### Étape 2 : Installer les dépendances Odoo

```powershell
# Installer depuis requirements.txt
pip install -r requirements.txt

# Temps d'installation : 5-10 minutes
# Nombreux packages seront installés (60+)
```

**Dépendances principales** :
- `psycopg2` : Connexion PostgreSQL
- `werkzeug` : Serveur WSGI
- `lxml` : Parsing XML
- `Pillow` : Traitement d'images
- `reportlab` : Génération de PDF
- `babel` : Internationalisation
- `python-dateutil` : Manipulation de dates

#### Étape 3 : Installer psycopg2-binary (si erreur)

Si l'installation de `psycopg2` échoue :

```powershell
pip install psycopg2-binary
```

### 2.7 Installer wkhtmltopdf

**wkhtmltopdf** permet de générer des PDF à partir de HTML.

#### Étape 1 : Téléchargement

1. Aller sur **https://wkhtmltopdf.org/downloads.html**
2. Télécharger la version Windows (64-bit)
3. Installer dans `C:\Program Files\wkhtmltopdf`

#### Étape 2 : Ajouter au PATH

```powershell
# Panneau de configuration > Système > Variables d'environnement
# PATH > Modifier > Nouveau
# Ajouter : C:\Program Files\wkhtmltopdf\bin
```

#### Étape 3 : Vérification

```powershell
wkhtmltopdf --version
# Sortie : wkhtmltopdf 0.12.x
```

### 2.8 Configurer Odoo

#### Créer le fichier de configuration

```powershell
# Créer odoo.conf dans C:\odoo19\odoo
notepad odoo.conf
```

**Contenu de `odoo.conf`** :

```ini
[options]

# ==================== CHEMINS ====================

# Dossiers des modules (séparés par des virgules)
# Odoo cherchera les modules dans ces dossiers
addons_path = C:\odoo19\odoo\addons,C:\odoo19\custom_addons

# Dossier de stockage des fichiers uploadés
# Contient les attachments, images, documents
data_dir = C:\odoo19\odoo\filestore

# ==================== BASE DE DONNÉES ====================

# Hôte de la base de données PostgreSQL
db_host = localhost

# Port PostgreSQL (par défaut : 5432)
db_port = 5432

# Nom d'utilisateur PostgreSQL
db_user = odoo

# Mot de passe PostgreSQL
db_password = odoo

# Filtre sur les noms de bases de données (regex)
# Exemple : dbfilter = ^test_.*$ (seulement les BDD commençant par "test_")
# Laisser vide pour toutes
# dbfilter = 

# Nom de la base de données par défaut (optionnel)
# db_name = 

# ==================== SERVEUR WEB ====================

# Port HTTP principal (interface web)
http_port = 8069

# Interface d'écoute (0.0.0.0 = toutes les interfaces)
# Utiliser 127.0.0.1 pour n'écouter que localement
http_interface = 0.0.0.0

# Port pour longpolling (websocket : chat, notifications)
longpolling_port = 8072

# ==================== PERFORMANCE ====================

# Nombre de workers (processus)
# 0 = mono-thread (idéal pour développement)
# Production : (nb_cpu * 2) + 1
workers = 0

# Nombre maximum de threads cron
# Cron = tâches planifiées (sauvegarde, envoi emails, etc.)
max_cron_threads = 1

# Limites mémoire par worker (en octets)
# 2.5 GB hard limit
limit_memory_hard = 2684354560
# 2 GB soft limit
limit_memory_soft = 2147483648

# Timeout requête (secondes)
limit_time_cpu = 60
limit_time_real = 120

# ==================== LOGS ====================

# Fichier de log
logfile = C:\odoo19\odoo\odoo.log

# Niveau de log
# debug : Très verbeux (développement)
# info : Informations générales (par défaut)
# warning : Avertissements seulement
# error : Erreurs seulement
# critical : Erreurs critiques seulement
log_level = info

# Format du log
# %(asctime)s %(pid)s %(levelname)s %(name)s: %(message)s
# log_handler = :INFO

# ==================== DÉVELOPPEMENT ====================

# Recharger automatiquement le code (développement)
# dev_mode = reload

# Mode debug
# dev_mode = all

# ==================== SÉCURITÉ ====================

# Liste des origines autorisées pour CORS (optionnel)
# Exemple : proxy_mode = True
# proxy_mode = 

# Durée de validité du token de session (secondes)
# Par défaut : 7 jours
# session_timeout = 604800

# ==================== AUTRES ====================

# Langue par défaut
# lang = fr_FR

# Fuseau horaire
# timezone = UTC

# Désactiver la page de sélection de BDD
# list_db = False

# Mot de passe admin (pour créer/gérer les BDD)
# IMPORTANT : À changer en production !
admin_passwd = admin

# Serveur d'email sortant (SMTP)
# smtp_server = smtp.gmail.com
# smtp_port = 587
# smtp_user = votre_email@gmail.com
# smtp_password = votre_mot_de_passe
# smtp_ssl = True

# ==================== ENTREPRISE (EE uniquement) ====================

# server_wide_modules = base,web,web_kanban
```

**Explication des paramètres importants** :

| Paramètre | Description | Valeur dev | Valeur prod |
|-----------|-------------|------------|-------------|
| `workers` | Nombre de processus | 0 | (CPU×2)+1 |
| `log_level` | Verbosité des logs | `info` ou `debug` | `info` |
| `db_filter` | Filtre BDD visibles | Vide | `^prod.*$` |
| `admin_passwd` | Mot de passe master | `admin` | Fort + aléatoire |
| `limit_time_real` | Timeout requête | 120 | 300 |

### 2.9 Lancer Odoo pour la première fois

#### Étape 1 : Vérifier que tout est prêt

```powershell
# 1. Environnement virtuel activé ?
# Le prompt doit afficher (venv)

# 2. Dans le bon dossier ?
cd C:\odoo19\odoo

# 3. PostgreSQL fonctionne ?
psql -U odoo -d postgres -c "SELECT version();"
# Doit afficher la version de PostgreSQL
```

#### Étape 2 : Lancer Odoo

```powershell
# Lancer Odoo avec le fichier de configuration

# Sortie attendue après quelques secondes :
# INFO ... odoo.service.server: HTTP service (werkzeug) running on 0.0.0.0:8069
```

**Messages importants** :
```
INFO odoo.service.server: Listening on 0.0.0.0:8069
```
→ Serveur lancé avec succès

```
INFO odoo.modules.loading: Modules loaded.
```
→ Modules chargés

```
WARNING odoo.modules.loading: Some modules are not loaded
```
→ Modules manquants (normal si première installation)

#### Étape 3 : Arrêter Odoo

Pour arrêter proprement le serveur :
```
Ctrl + C (une seule fois)
```

Attendre que les processus se terminent proprement.

### 2.10 Premier accès à l'interface

#### Étape 1 : Ouvrir le navigateur

1. Lancer le navigateur (Chrome, Firefox, Edge)
2. Aller sur : **http://localhost:8069**

#### Étape 2 : Créer une base de données

**Formulaire de création** :

| Champ | Valeur suggérée | Description |
|-------|----------------|-------------|
| Master Password | `admin` | Mot de passe du fichier de config |
| Database Name | `library_db` | Nom technique (snake_case) |
| Email | `admin@example.com` | Login administrateur |
| Password | `admin` | Mot de passe admin (à changer après) |
| Language | `Français` | Langue de l'interface |
| Country | `Maroc` | Pays de l'entreprise |
| Demo data | ☑ Coché | Données de démonstration (pratique pour apprendre) |

**Cliquer sur "Create database"**

⏱️ Temps de création : 2-5 minutes

#### Étape 3 : Explorer l'interface

Une fois la base créée, vous arrivez sur la page d'accueil d'Odoo :

**Éléments de l'interface** :
- 🏠 **Apps** : Liste des applications installables
- ⚙️ **Settings** : Configuration générale
- 👤 **Profil utilisateur** (coin supérieur droit)
- 🔍 **Barre de recherche** globale
- 📱 **Apps disponibles** : CRM, Sales, Accounting, etc.

**Première exploration** :
1. Installer l'application **CRM** (pour voir un exemple)
2. Créer une opportunité de test
3. Explorer les vues (List, Kanban, Form)

### 2.11 Commandes utiles

```powershell
# ========== LANCER ODOO ==========

# Lancement normal
python odoo-bin -c odoo.conf

# Lancement avec une base spécifique
python odoo-bin -c odoo.conf -d library_db

# Lancement en mode debug
python odoo-bin -c odoo.conf --dev=all

# ========== INSTALLER UN MODULE ==========

# Installer un module à la création de BDD
python odoo-bin -c odoo.conf -d library_db -i base,sale

# Installer dans une BDD existante
python odoo-bin -c odoo.conf -d library_db -i library_app

# ========== METTRE À JOUR UN MODULE ==========

# Mettre à jour un module
python odoo-bin -c odoo.conf -d library_db -u library_app

# Mettre à jour tous les modules
python odoo-bin -c odoo.conf -d library_db -u all

# ========== GESTION DES BASES ==========

# Lister les bases de données
python odoo-bin -c odoo.conf --list

# Créer une base vide (sans démo)
python odoo-bin -c odoo.conf -d library_db -i base --without-demo=all

# ========== OPTIONS DE DÉVELOPPEMENT ==========

# Mode reload : recharge auto du code Python
python odoo-bin -c odoo.conf --dev=reload

# Mode qweb : recharge auto des templates
python odoo-bin -c odoo.conf --dev=qweb

# Mode xml : recharge auto des vues
python odoo-bin -c odoo.conf --dev=xml

# Tous les modes dev
python odoo-bin -c odoo.conf --dev=all

# ========== TESTS ==========

# Lancer les tests d'un module
python odoo-bin -c odoo.conf -d test_db -i library_app --test-enable

# Tests avec log détaillé
python odoo-bin -c odoo.conf -d test_db -i library_app --test-enable --log-level=test

# ========== AUTRES ==========

# Shell interactif Python dans le contexte Odoo
python odoo-bin shell -c odoo.conf -d library_db

# Générer un module vide
python odoo-bin scaffold library_app custom_addons/

# Version d'Odoo
python odoo-bin --version
```

---

## <a id="macos"></a>🍎 3. Installation sur macOS

### 3.1 Installer Homebrew

**Homebrew** est le gestionnaire de paquets pour macOS.

```bash
# Installer Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Suivre les instructions post-installation
# (ajouter Homebrew au PATH)

# Vérifier
brew --version
# Sortie : Homebrew 4.x.x
```

### 3.2 Installer Python 3.10

```bash
# Installer Python 3.10
brew install python@3.10

# Créer un lien symbolique
brew link python@3.10

# Vérifier
python3 --version
# Sortie : Python 3.10.x

# Vérifier pip
pip3 --version
```

### 3.3 Installer PostgreSQL

```bash
# Installer PostgreSQL 15
brew install postgresql@15

# Démarrer PostgreSQL
brew services start postgresql@15

# Vérifier
psql --version
# Sortie : psql (PostgreSQL) 15.x

# Créer un utilisateur Odoo
psql postgres

# Dans psql :
CREATE USER odoo WITH CREATEDB PASSWORD 'odoo';
\q
```

### 3.4 Installer Git et autres outils

```bash
# Git (souvent déjà installé)
brew install git

# wkhtmltopdf pour les PDFs
brew install wkhtmltopdf

# Node.js (optionnel)
brew install node

# Vérifications
git --version
wkhtmltopdf --version
node --version
```

### 3.5 Télécharger Odoo 19

```bash
# Créer la structure
mkdir ~/odoo19
cd ~/odoo19
mkdir custom_addons

# Cloner Odoo
git clone https://github.com/odoo/odoo.git --depth 1 --branch 19.0 odoo

cd odoo
```

### 3.6 Environnement virtuel et dépendances

```bash
# Créer l'environnement virtuel
python3 -m venv venv

# Activer
source venv/bin/activate

# Mettre à jour pip
pip install --upgrade pip setuptools wheel

# Installer les dépendances
pip install -r requirements.txt
pip install psycopg2-binary
```

### 3.7 Configurer Odoo

Créer `~/odoo19/odoo/odoo.conf` :

```bash
nano odoo.conf
```

Contenu (adapter les chemins) :

```ini
[options]
addons_path = /Users/VOTRE_USER/odoo19/odoo/addons,/Users/VOTRE_USER/odoo19/custom_addons
data_dir = /Users/VOTRE_USER/odoo19/odoo/filestore
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo
http_port = 8069
longpolling_port = 8072
workers = 0
log_level = info
logfile = /Users/VOTRE_USER/odoo19/odoo/odoo.log
admin_passwd = admin
```

### 3.8 Lancer Odoo

```bash
# Activer l'environnement
source venv/bin/activate

# Lancer Odoo
python3 odoo-bin -c odoo.conf
```

Accéder à : **http://localhost:8069**

---

## <a id="configuration"></a>⚙️ 4. Configuration avancée

### 4.1 Configuration multi-bases

Pour gérer plusieurs bases de données avec des configurations différentes :

```ini
# odoo_prod.conf
[options]
db_name = prod_db
logfile = /path/to/prod.log
workers = 4
```

```ini
# odoo_dev.conf
[options]
db_name = dev_db
logfile = /path/to/dev.log
workers = 0
dev_mode = all
```

Lancement :
```bash
python odoo-bin -c odoo_prod.conf
python odoo-bin -c odoo_dev.conf
```

### 4.2 Configuration pour développement

```ini
[options]
# Recharger le code automatiquement
dev_mode = all

# Log détaillé
log_level = debug

# Pas de workers (mono-thread)
workers = 0

# Désactiver le cache
http_enable = True
```

### 4.3 Configuration pour production

```ini
[options]
# Workers selon CPU
workers = 9  # (4 CPU * 2) + 1

# Limites mémoire
limit_memory_hard = 2684354560
limit_memory_soft = 2147483648

# Timeouts
limit_time_cpu = 300
limit_time_real = 600

# Sécurité
admin_passwd = MOT_DE_PASSE_FORT_ALEATOIRE
db_filter = ^prod_.*$
list_db = False

# Proxy (si derrière nginx/apache)
proxy_mode = True
```

### 4.4 Serveur d'email (SMTP)

Pour envoyer des emails depuis Odoo :

```ini
[options]
# Gmail
smtp_server = smtp.gmail.com
smtp_port = 587
smtp_user = votre_email@gmail.com
smtp_password = votre_mot_de_passe_app
smtp_ssl = True

# Outlook
# smtp_server = smtp-mail.outlook.com
# smtp_port = 587

# Serveur SMTP personnalisé
# smtp_server = mail.example.com
# smtp_port = 465
```

---

## <a id="verification"></a>✅ 5. Vérification et dépannage

### 5.1 Vérifier l'installation

**Checklist** :
```bash
# Python
python --version  # 3.10.x
pip --version

# PostgreSQL
psql --version  # 12+
psql -U odoo -d postgres -c "SELECT 1;"

# Git
git --version

# wkhtmltopdf
wkhtmltopdf --version

# Odoo
cd ~/odoo19/odoo  # ou C:\odoo19\odoo
python odoo-bin --version
```

### 5.2 Problèmes courants

#### Problème 1 : "Python n'est pas reconnu"

**Windows** :
```powershell
# Vérifier le PATH
echo $env:Path

# Ajouter Python au PATH
[Environment]::SetEnvironmentVariable(
    "Path",
    $env:Path + ";C:\Python310;C:\Python310\Scripts",
    "User"
)
```

#### Problème 2 : Erreur psycopg2

```bash
# Solution : Installer la version binaire
pip install psycopg2-binary
```

#### Problème 3 : Port 8069 déjà utilisé

```bash
# Trouver le processus utilisant le port
# Windows
netstat -ano | findstr :8069

# macOS/Linux
lsof -i :8069

# Changer le port dans odoo.conf
http_port = 8070
```

#### Problème 4 : "Could not connect to database"

```bash
# Vérifier PostgreSQL
# Windows
net start postgresql-x64-15

# macOS
brew services start postgresql@15

# Tester la connexion
psql -U odoo -d postgres
```

#### Problème 5 : Module non trouvé

```bash
# Vérifier addons_path dans odoo.conf
# Lister les modules disponibles
python odoo-bin -c odoo.conf --list
```

### 5.3 Logs et débogage

**Lire les logs** :
```bash
# Tail en temps réel
# Windows
Get-Content odoo.log -Wait -Tail 50

# macOS/Linux
tail -f odoo.log

# Filtrer les erreurs
grep ERROR odoo.log
grep CRITICAL odoo.log
```

**Augmenter la verbosité** :
```ini
# odoo.conf
log_level = debug
```

---

## <a id="ide"></a>🔧 6. Configuration de l'IDE

### 6.1 Visual Studio Code

#### Installation

1. Télécharger depuis **https://code.visualstudio.com/**
2. Installer

#### Extensions recommandées

```
1. Python (Microsoft)
2. Pylance (Microsoft)
3. XML Tools
4. Odoo Snippets
5. GitLens
6. Better Comments
7. Path Intellisense
8. Material Icon Theme
```

#### Configuration

Créer `.vscode/settings.json` :

```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.linting.pylintEnabled": true,
    "python.linting.enabled": true,
    "python.formatting.provider": "black",
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_odoo",
        "--max-line-length=120"
    ],
    "files.associations": {
        "*.xml": "xml",
        "*.po": "gettext"
    },
    "[python]": {
        "editor.rulers": [79],
        "editor.tabSize": 4,
        "editor.insertSpaces": true
    },
    "[xml]": {
        "editor.tabSize": 4,
        "editor.formatOnSave": true
    },
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true,
        "**/.pytest_cache": true,
        "**/venv": true
    }
}
```

#### Snippets Odoo personnalisés

Créer `.vscode/odoo.code-snippets` :

```json
{
    "Odoo Model": {
        "prefix": "odoomodel",
        "body": [
            "from odoo import models, fields, api",
            "",
            "class ${1:ClassName}(models.Model):",
            "    _name = '${2:module.name}'",
            "    _description = '${3:Description}'",
            "",
            "    name = fields.Char(string='${4:Name}')",
            "    $0"
        ]
    }
}
```

### 6.2 PyCharm

#### Configuration

1. **File > Settings > Project > Python Interpreter**
2. Ajouter l'interpréteur : `./venv/bin/python`
3. **Project Structure** :
   - Marquer `odoo/addons` comme **Sources Root**
   - Marquer `custom_addons` comme **Sources Root**

#### Plugin Odoo

1. **Settings > Plugins**
2. Chercher "Odoo"
3. Installer le plugin officiel

#### Run Configuration

**Run > Edit Configurations > + > Python**
```
Name: Odoo Server
Script: odoo-bin
Script parameters: -c odoo.conf
Working directory: /path/to/odoo
```

---

## 🎉 Conclusion

Vous avez maintenant :
- ✅ Odoo 19 installé et fonctionnel
- ✅ Environnement de développement configuré
- ✅ IDE prêt pour coder
- ✅ Base de données créée

**Prochaine étape** : Module 2 - Créer votre premier module Odoo

---

## 📝 Checklist finale

- [ ] Python 3.10+ installé
- [ ] PostgreSQL installé et en cours d'exécution
- [ ] Git installé
- [ ] Odoo 19 cloné
- [ ] Environnement virtuel créé et activé
- [ ] Dépendances installées
- [ ] odoo.conf configuré
- [ ] Odoo démarre sans erreur
- [ ] Base de données créée
- [ ] IDE configuré

