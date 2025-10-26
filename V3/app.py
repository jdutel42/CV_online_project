from flask import Flask, redirect, render_template, url_for, send_from_directory
import datetime
import calendar

app = Flask(__name__)




##########################################################################################
# Gestion des erreurs
##########################################################################################

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404




##########################################################################################
# Création des routes / vues
##########################################################################################

# ---------------------------------------------------------------------------------------
# Vue principale root
# ---------------------------------------------------------------------------------------

# The following code is for the all sections of the website
# On peut accéder à toutes les sections du site en une seule page

def date():
    date_heure = datetime.datetime.now()
    jour = date_heure.day
    mois = calendar.month_name[date_heure.month]
    annee = date_heure.year
    return jour, mois, annee


@app.route("/")
def root():
    jour, mois, annee = date()  # Décompose toutes les valeurs retournées
    return render_template(
        "all_section.html", jour=jour, mois=mois, annee=annee)


# ---------------------------------------------------------------------------------------
# Une vue pour chaque section (en soit pas nécessaire car toutes
# les sections sont accessibles à partir de la vue root
# ---------------------------------------------------------------------------------------

# The following code is for the individual sections of the website
# Techniquement ces pages ne sont pas nécessaires, mais elles permettent de tester chaque section individuellement
# Cela m'entraine à créer des routes et des templates

@app.route("/section/<section_name>")
def section(section_name):
    sections = {
        "home": "hero_section.html",
        "about": "about_section.html",
        "stats": "stats_section.html",
        "skills": "skills_section.html",
        "resume": "resume_section.html",
        "portfolio": "portfolio_section.html",
        "services": "services_section.html",
        "testimonials": "testimonials_section.html",
        "contact": "contact_section.html"
    }
    template = sections.get(section_name)
    if template:
        return render_template(template)
    else:
        return render_template("404.html"), 404


# ---------------------------------------------------------------------------------------
# Une vue pour chacun des projets
# ---------------------------------------------------------------------------------------

@app.route("/portfolio/Project_<int:project_id>")
def portfolio_project(project_id):
    if project_id == 1:
        return render_template("portfolio-details_project1.html", project_id=project_id)
    elif project_id == 2:
        return render_template("portfolio-details_project2.html", project_id=project_id)
    elif project_id == 3:
        return render_template("portfolio-details_project3.html", project_id=project_id)
    elif project_id == 4:
        return render_template("portfolio-details_project4.html", project_id=project_id)
    else:
        return render_template("404.html"), 404

# ---------------------------------------------------------------------------------------
# Utilisation de la fonction redirect 
# ---------------------------------------------------------------------------------------
@app.route("/master_bioinfo")
def redirect_page():
    return redirect(url_for('https://www.bioinfo-lyon.fr/')) 


# ---------------------------------------------------------------------------------------
# Vue pour download mon cv
# ---------------------------------------------------------------------------------------

@app.route("/download-cv")
def download_cv():
    # Spécifiez le chemin vers le fichier
    cv_directory = "static/cv"
    cv_filename = "CV_Dutel_2025_EN.pdf"
    return send_from_directory(cv_directory, cv_filename, as_attachment=True)


# Serve sitemap and robots at site root (helpful for crawlers)
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')


@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

# ---------------------------------------------------------------------------------------
# Easter Egg
# ---------------------------------------------------------------------------------------

@app.route("/surprise")
def surprise():
    return redirect("https://youtu.be/dQw4w9WgXcQ")


# ---------------------------------------------------------------------------------------
# Vue pour test les fonctionnalités
# ---------------------------------------------------------------------------------------

@app.route("/test")
def test():
    h, m, s = date()
    return render_template("test.html", heure=h, minute=m, seconde=s)




##########################################################################################
# Fonctionnalités non intégrées
##########################################################################################

# @app.context_processor
# def inject_navigation():
#     navigation = [
#         {"name": "Root", "url": "/"},
#         {"name": "Home", "url": "/section/home"},
#         {"name": "About", "url": "/section/about"},
#         {"name": "Stats", "url": "/section/stats"},
#         {"name": "Skills", "url": "/section/skills"},
#         {"name": "Resume", "url": "/section/resume"},
#         {"name": "Portfolio", "url": "/section/portfolio"},
#         {"name": "Services", "url": "/section/services"},
#         {"name": "Testimonials", "url": "/section/testimonials"},
#         {"name": "Contact", "url": "/section/contact"}
#     ]
#     return {"navigation": navigation}



# @app.route("/test")
# def test():
#     team_members = [
#         {"name": "Jordan", "role": "Bioinformatician"},
#         {"name": "Alice", "role": "Data Scientist"},
#         {"name": "Bob", "role": "Developer"}
#     ]
#     return render_template("test.html", team=team_members)




##########################################################################################
# Lancement de l'application
##########################################################################################

if __name__ == "__main__":
    # Use port 8000 for local testing to avoid conflicts with other services
    app.run(debug=True, port=8000)