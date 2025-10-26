# Déploiement — instructions rapides

Ce dépôt contient une application Flask (dans `app.py`) servant un CV en ligne. Ci‑dessous des étapes simples pour déployer sur un service PaaS (Render, Railway, Fly.io, etc.). Je donne un exemple pour Render (simple et bien adapté pour Flask).

1) Préparer le dépôt
  - Créez un repo Git et poussez `V3/` dessus (ou depuis la racine si vous préférez). Assurez‑vous que `requirements.txt` et `Procfile` sont présents.

2) Déployer sur Render (méthode recommandée)
  - Créez un compte sur https://render.com.
  - Connectez votre dépôt GitHub/GitLab/Bitbucket.
  - Créez un "Web Service" et sélectionnez la branche à déployer.
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `gunicorn app:app`
  - Render gérera l'environnement et exposera votre application.

3) Tester localement avant déploiement
  - Activez l'environnement virtuel et installez les deps:
    ```bash
    source PWEB_env/bin/activate
    pip install -r requirements.txt
    gunicorn app:app
    ```
  - Ouvrez http://127.0.0.1:8000/ (gunicorn par défaut écoute sur 8000).

4) Nom de domaine & SEO
  - Acheter un nom de domaine (ex. `jordandutel.com`) chez un registrar (OVH, Gandi, Namecheap, etc.).
  - Dans Render (ou autre), ajoutez le domaine personnalisé et suivez les instructions DNS (A/ CNAME).
  - Pour apparaître sur Google en tapant votre nom : ajoutez des meta tags, un sitemap.xml, et soumettez votre site à Google Search Console. Le SEO prend quelques jours/semaines.

5) Autres options
  - Fly.io: bon pour petites applis, nécessite `flyctl` et parfois un `Dockerfile`.
  - Railway: simple, connectez le repo et configurez start command.
  - PythonAnywhere: simple pour petits sites (limité pour les comptes gratuits).

Si tu veux, je peux :
- créer un `sitemap.xml` et ajouter des meta tags SEO dans `templates/layout.html` ;
- créer un `Dockerfile` pour Fly.io ;
- ou lancer le serveur localement ici pour vérifier.
