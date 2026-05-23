# AGENTS.md

## Contexte du projet
- Application web Python basée sur Flask.
- Fichier principal : `app.py`.
- Vues HTML statiques : `templates/*.html`.
- Ressources front-end : `static/css/style.css`, `static/js/script.js`, `static/images/*`.
- Envoi d'e-mails géré par Flask-Mail.
- Environnement virtuel local : `venv/` (ne pas modifier).

## Exigences importantes pour l'agent
- **Toujours répondre en français** avec l'utilisateur.
- **Ne pas modifier** le dossier `venv/` ni créer de dépendances inutiles.
- Préférer les corrections simples et fiables pour un site Flask léger.
- Vérifier et suggérer l'extraction des données sensibles (`MAIL_USERNAME`, `MAIL_PASSWORD`) en variables d'environnement.
- Rechercher les exceptions courantes de Flask et les problèmes de routage / de modèles.

## Règles de travail
- Lorsque vous modifiez du code, testez mentalement les routes et les formulaires, puis suggérez de lancer le serveur avec `python app.py`.
- Si vous recommandez un nouveau fichier de documentation, expliquez pourquoi il est nécessaire et évitez la duplication.
- Si le projet nécessite un fichier de configuration (`.env`, `requirements.txt`), proposez-le clairement.

## Points clés
- Routes exposées : `/`, `/a_propos`, `/alimentaire`, `/cosmétique`, `/recettes`, `/contact`.
- La page de contact accepte `POST` et envoie un email.
- Le projet n’a pas de `README.md` ni de documentation existante.
- Ne pas inventer d’architecture complexe ; c’est un site simple avec backend Flask et templates Jinja.
