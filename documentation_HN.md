# Documentation Technique — Healthy & Natural

## Présentation du projet

**Healthy & Natural** est un site web e-commerce présentant une gamme de produits naturels et biologiques (cosmétiques et alimentaires) fabriqués au Sénégal. Le site permet aux visiteurs de découvrir les produits, l'histoire de la marque, et de contacter directement la boutique.

---

## Technologies utilisées

### Backend
| Technologie | Usage |
|---|---|
| **Python 3** | Langage principal |
| **Flask** | Framework web |
| **Flask-Mail** | Envoi d'emails via SMTP |
| **Jinja2** | Moteur de templates HTML |

### Frontend
| Technologie | Usage |
|---|---|
| **HTML5** | Structure des pages |
| **CSS3** | Mise en page et animations |
| **JavaScript (Vanilla)** | Menu hamburger interactif |
| **Google Fonts** | Typographie (Playwrite US Modern) |

### Déploiement
| Technologie | Usage |
|---|---|
| **PythonAnywhere** | Hébergement du serveur Flask |
| **GitHub** | Versioning du code source |

---

## Architecture du projet

```
Healthy_And_Natural/
├── app.py                  # Application Flask principale
├── static/
│   ├── css/
│   │   └── style.css       # Feuille de styles globale
│   ├── js/
│   │   └── script.js       # JavaScript (menu hamburger)
│   └── images/             # Images des produits et logo
└── templates/
    ├── base.html           # Template de base (navbar + footer)
    ├── accueil.html        # Page d'accueil
    ├── alimentaire.html    # Page produits alimentaires
    ├── cosmétique.html     # Page produits cosmétiques
    ├── a_propos.html       # Page à propos
    ├── recettes.html       # Page recettes et astuces
    └── contact.html        # Page contact avec formulaire
```

---

## Pages et fonctionnalités

### 1. Navigation (base.html)
- Navbar fixe avec logo cliquable
- Menu de navigation avec 6 liens
- **Menu hamburger responsive** en JavaScript — au clic, le menu se déploie verticalement sur mobile
- Footer à 3 colonnes : présentation de la marque, liens de navigation, engagements qualité
- Template Jinja2 partagé entre toutes les pages (`{% extends %}` / `{% block %}`)

### 2. Page d'accueil (accueil.html)
- Section hero avec slogan et deux boutons de navigation vers les catégories produits
- Aperçu des **produits cosmétiques** : Crème de karité, Sérum capillaire, Beurre
- Aperçu des **produits alimentaires** : Poudre de dattes, Bissap instantané, Miel citronné
- Section "Pourquoi nous choisir" avec 3 cartes : 100% Naturel, Sans Additifs, Qualité Premium
- Section teaser "Découvrez Notre Histoire" avec bouton vers la page À propos
- Animations hover sur les images (effet zoom CSS)

### 3. Page Alimentaire
- Présentation détaillée de 4 produits : Bissap instantané, Miel citronné, Poudre de dattes, Nokoss
- Disposition alternée image/texte pour chaque produit
- Descriptions professionnelles mettant en avant les bienfaits santé

### 4. Page Cosmétique
- Présentation des produits cosmétiques : Beurre de karité, Sérum capillaire
- Même disposition alternée image/texte

### 5. Page À propos
- Histoire de la fondatrice Mame Coumba Sene Dieng
- 3 sections : Notre Histoire, Notre engagement pour le naturel, Une marque qui voyage

### 6. Page Contact
- **Formulaire de contact** avec les champs : Nom, Email, Téléphone, Sujet (liste déroulante), Message
- **Liens vers les réseaux sociaux** : WhatsApp (2 numéros), Instagram, Snapchat, Facebook, Email
- **Envoi automatique d'email** via Flask-Mail lors de la soumission du formulaire
- Message de confirmation affiché après envoi réussi (`{% if success %}`)

---

## Fonctionnalité email

Lors de la soumission du formulaire de contact :

1. Flask reçoit les données via `request.form` (méthode POST)
2. Flask-Mail compose un email avec les informations du visiteur
3. L'email est envoyé au compte Gmail de la boutique
4. La page se recharge avec un message de confirmation

```
Expéditeur  : healthyandnatural221@gmail.com
Destinataire: healthyandnatural221@gmail.com
Objet       : "Nouveau message de {nom} - {sujet}"
Contenu     : Nom, Téléphone, Email, Objet, Message
```

---

## Design & Responsive

- **Palette de couleurs** : Vert (#4A7C2C), Or (#D4AF37), Blanc (#ffffff)
- **Typographie** : Google Fonts — Playwrite US Modern
- **Responsive** géré avec des media queries pour 4 breakpoints :
  - Tablette : max-width 768px
  - Mobile L : max-width 425px
  - Mobile M : max-width 375px
  - Mobile S : max-width 320px
- Animations CSS : hover sur les images (zoom), hover sur les boutons, transitions sur les liens

---

## Routes Flask

| Route | Méthode | Description |
|---|---|---|
| `/` | GET | Page d'accueil |
| `/a_propos` | GET | Page À propos |
| `/alimentaire` | GET | Page produits alimentaires |
| `/cosmétique` | GET | Page produits cosmétiques |
| `/recettes` | GET | Page recettes et astuces |
| `/contact` | GET + POST | Page contact + traitement formulaire |
