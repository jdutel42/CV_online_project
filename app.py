from flask import Flask, redirect, render_template, url_for, send_from_directory, request
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


# -----------------------
# Minimal i18n support
# -----------------------
translations = {
    'en': {
        'Home': 'Home',
        'About': 'About',
        'Resume': 'Resume',
        'Portfolio': 'Portfolio',
        'Title_project1': 'ARG Detection',
        'Title_project2': 'pDC RNAseq',
        'Title_project3': 'PeptideFinder',
        'Title_project4': 'Spatial OMICS',
        'Context': 'Context',
        'Deliverable': 'Deliverable',
        'Contact': 'Contact',
        'hero_description': 'I am',
        'hero_keywords': 'bioinformatician, immunologist, data scientist, multi-omics analyst, RNA‑seq specialist, machine learning engineer, reproducible research advocate',
        'Definition_about_Jordan': 'Bioinformatics Engineer | Data Scientist',
        'Birthday': 'Birthdate',
        'Birthday_date': 'June, 28th 1998',
        'Degree': 'Degree',
        'Degree_name': 'Bioinformatics & Data Science Master\'s',
        'Phone': 'Phone',
        'Phone_number': '+33 (0)6 36 85 52 78',
        'Localisation': 'Localisation',
        'Localisation_name': 'Lyon, Toulouse (France)',
        'Age': 'Age',
        'Establishment': 'Establishment',
        'Establishment_name': 'University Claude Bernard Lyon 1',
        'Email': 'Email',
        'Languages': 'Languages',
        'Language_list': 'French (native) | English (fluent)',
        'CCL_About_Jordan': 'Driven by a passion for leveraging bioinformatics and cutting-edge technologies to revolutionize cancer research and therapy, I aspire to contribute to impactful advancements in immunotherapy and multi-omics analysis. My long-term goal is to establish a pioneering biotech company that excels in innovative treatments, competes globally, and fosters open access to knowledge for the benefit of society.',
        'Stat1_title': 'Training Courses',
        'Stat1_meaning': 'Hours of bioinformatic training duration',
        'Stat2_title': 'Projects',
        'Stat2_meaning': 'Academic Projects Completed',
        'Stat3_title': 'Internships',
        'Stat3_meaning': 'Number of internships realizeds',
        'Stat4_title': 'Publications',
        'Stat4_meaning': 'Papers and articles published',
        'Stats': 'Stats',
        'Skills': 'Skills',
        'Skills_sentence': 'Skills developed throughout my training in bioinformatics, during my academic projects and my professional internships. Here are a few of my technical skills and tools I master:',
        'Skill_1': 'Python',
        'Skill_2': 'R',
        'Skill_3': 'Statistics',
        'Skill_4': 'Spatial & Multiomics analysis',
        'Skill_5': 'SQL Databases',
        'Skill_6': 'Machine Learning',
        'resume_desc': "Bioinformatics Engineer with a strong passion for immunology, drug design, and multi-omics analyses.",
        'download_cv': 'Download my resume',
        'Summary': 'Summary',
        'Summary_sentence': 'I am autonomous, proactive, and curious with expertise in bioinformatics, multi-omics data analysis, and molecular biology. Motivated by innovation and scientific challenges.',
        'Education': 'Education',
        'Education_name_1': 'Master’s Degree in Bioinformatics',
        'Education_establishment_1': 'University Claude Bernard Lyon 1',
        'Education_skills_1': 'Skills: Machine learning techniques, bayesian statistics, structural bioinformatics & drug design, multi-omics data analysis (genomics, metagenomics, transcriptomics, and proteomics), database management, web programming, advanced algorithmics.',
        'Education_name_2': 'Master’s Degree in Molecular Biology & Immunology',
        'Education_establishment_2': 'University Claude Bernard Lyon 1',
        'Education_skills_2': 'Skills: Immunology, immunopathology, cancer biology, genetic mapping, microscopy (electron, epifluorescence, confocal), RNA interference (Zebrafish embryo microinjection).',
        'Prof_experience': 'Professional Experience',
        'Prof_experience_name_1': 'Data Science Research Intern',
        'Prof_experience_establishment_1': 'Centre Léon Bérard, Prevention & Public Health Team, Lyon',
        'Prof_experience_duration_1': 'April - June 2024',
        'Prof_experience_description_1_skill_1': 'Performed in-depth OMICS data analysis on a patient cohort to study mutational and immunological profiles.',
        'Prof_experience_description_1_skill_2': 'Used advanced factorial analysis (MOFA) to characterize patient subgroups and optimize personalized therapeutic strategies.',
        'Prof_experience_name_2': 'Research Intern in Immuno-Oncology',
        'Prof_experience_establishment_2': 'CRCL (Cancer Research Center of Lyon), GRINBERG Team, Lyon',
        'Prof_experience_duration_2': 'January - June 2023',
        'Prof_experience_description_2_skill_1': 'Studied NF-kB transcription factor subunits in CD4+ T lymphocytes and their implications in autoimmune diseases and cancer.',
        'Prof_experience_description_2_skill_2': 'Performed gene knockout via CRISPR-Cas9, flow cytometry (BD LSR Fortessa), and protein detection using ELISA (TransAM Assay).',
        'Prof_experience_name_3': 'Virology Research Intern',
        'Prof_experience_establishment_3': 'CIRI (International Center for Infectiology Research), REVE Team, Lyon',
        'Prof_experience_duration_3': 'January - March 2022',
        'Prof_experience_description_3_skill_1': 'Developed a novel RNA vectorization system using the human pseudo-viral protein hPEG10.',
        'Prof_experience_description_3_skill_2': 'Performed plasmid cloning, RT-PCR, qPCR primer design, enzymatic digestion, and plasmid transfection.',
        'Prof_experience_name_4': 'Spatial-Omics Research Intern',
        'Prof_experience_establishment_4': 'CRCL (Cancer Research Center of Lyon), SAINTIGNY Team, Lyon',
        'Prof_experience_duration_4': 'January - August 2025',
        'Prof_experience_description_4_skill_1': 'Spatial transcriptomics data analysis using Seurat and Scanpy packages.',
        'Prof_experience_description_4_skill_2': 'Identification of 5+ key spatial gene expression patterns associated with tumor subtypes.',
        'Portfolio_description': 'In this section, you can find all the projects I have worked on and developed.',
        'All': 'All',
        'More_details': 'More details',
        'Project': 'Project',
        'Portfolio_details': 'Portfolio Details',
        'Portfolio_keyword_project_1': 'Metagenomics',
        'Portfolio_keyword_2_project_1': 'Microbial Ecology',
        'Portfolio_description_project_1': 'Plasmid and ARG Analysis in Soil Metagenomes',
        'Portfolio_description_text_project_1': 'This project leverages advanced bioinformatics tools to analyze plasmids and antibiotic resistance genes (ARGs) in soil metagenomes. Our aim is to elucidate the dynamics of ARGs within plasmid populations and their response to environmental factors.',
        'Portfolio_keyword_project_2': 'RNAseq Analysis',
        'Portfolio_keyword_2_project_2': 'Alternative Splicing, Immunology',
        'Portfolio_description_project_2': 'Alternative splicing analysis in plasmacytoïd dendritics cells and impact on antiviral response',
        'Portfolio_description_text_project_2': 'Since the last few decades, urban expansion and human activities have led humans to interact with more and more species that we have ever face yet. This interaction with different species shows us that zoonoses (like virus CoVID19) can appear. So, understanding immune system mechanisms, especially in the context of viral infection have become a public health issue. In human species, viral infections are mostly managed by immune cells called plasmacytoid dendritic cells (pDC). Thoses cells are huge producers of type 1 interferon, a very efficient alarming cytokine that put cells in a virus-aware state, ready to resist viral infection. Several other proteins are synthetised by pDC, and this will allow a very specific immune response against the virus. Thus, in context of viral infection, these proteins produced by pDC are essential and so, really regulated. Among these regulatory mechanisms, alternative splicing remodeling could explain how pDC can adapt their response according to the virus they face. Such mechanisms have already been showned in other immune cells, but as of now, mechanisms in pDC aren\'t well known.',
        'Portfolio_keyword_project_3': 'Proteomics',
        'Portfolio_keyword_2_project_3': 'Peptide Identification, Phylogeny',
        'Portfolio_description_project_3': 'Development of PeptideFinder, a tool for peptide identification from mass spectrometry data',
        'Portfolio_description_text_project_3': 'This project focuses on identifying proteomic biomarkers from the chemical defensome of wild fish species. By integrating bioinformatics tools and computational workflows, we aim to analyze genomic and proteomic data to understand the responses of these species to environmental stressors. The project also explores potential biomarkers for ecological monitoring and risk assessment.',
        'Portfolio_keyword_project_4': 'Spatial OMICS',
        'Portfolio_keyword_2_project_4': 'Spatial Transcriptomics, Cancer Research',
        'Portfolio_description_project_4': 'Integration and analysis of spatial transcriptomics data in breast cancer research',
        'Portfolio_description_text_project_4': 'This project analyzes spatial transcriptomics data from 15 metaplastic breast carcinoma (MpBC) samples using 10x Genomics Visium. It aims to explore tumor heterogeneity and transdifferentiation, leveraging expert-labeled cell types to identify spatial clusters and biomarkers. ',
        'Address': 'Address',
        'Call Me': 'Call Me',
        'Email Me': 'Email Me',
        'January': 'January',
        'February': 'February',
        'March': 'March',
        'September': 'September',


        'Services': 'Services',
        'Testimonials': 'Testimonials',
        'about_desc': 'Passionate bioinformatician with expertise in multi-omics, immunology, and advanced computational pipelines, aiming to drive innovation in cancer research and biotechnology.',
        'typed_items': 'Bioinformatician, Immunologist, Data Scientist, Multi-omics Analyst',
        'resume_title': "Resume",
        'contact_desc': 'If you are interested in connecting, feel free to reach out via email or LinkedIn'
    },
    'fr': {
        'Home': 'Accueil',
        'About': 'À propos',
        'Resume': 'CV',
        'Portfolio': 'Portfolio',
        'Title_project1': 'Détection des ARG',
        'Title_project2': 'pDC RNAseq',
        'Title_project3': 'PeptideFinder',
        'Title_project4': 'Spatial OMICS',
        'Context': 'Contexte',
        'Deliverable': 'Livrable',
        'Contact': 'Contact',
        'hero_description': 'Je suis',
        'hero_keywords': 'bioinformaticien, immunologiste, data scientist, analyste multi-omics, spécialiste RNA‑seq, ingénieur en apprentissage automatique, partisan d\'une recherche libre et ouverte',
        'Definition_about_Jordan': 'Ingénieur en Bioinformatique | Data Scientist',
        'Birthday': 'Date de naissance',
        'Birthday_date': '28 Juin 1998',
        'Degree': 'Diplôme',
        'Degree_name': 'Master Bioinformatique & Data Science',
        'Phone': 'Téléphone',
        'Phone_number': '+33 (0)6 36 85 52 78',
        'Localisation': 'Localisation',
        'Localisation_name': 'Lyon, Toulouse (France)',
        'Age': 'Âge',
        'Establishment': 'Établissement',
        'Establishment_name': 'Université Claude Bernard Lyon 1',
        'Email': 'Email',
        'Languages': 'Langues',
        'Language_list': 'Français (natif) | Anglais (courant)',
        'CCL_About_Jordan': "Animé par une passion pour l'exploitation de la bioinformatique et des technologies de pointe afin de révolutionner la recherche et la thérapie contre le cancer, j'aspire à contribuer à des avancées significatives en immunothérapie et en analyse multi-omics. Mon objectif à long terme est de créer une entreprise biotechnologique pionnière qui excelle dans les traitements innovants, concurrence à l'échelle mondiale et favorise l'accès libre aux connaissances au bénéfice de la société.",
        'Stats': 'Statistiques',
        'Stat1_title': 'Cours de formation',
        'Stat1_meaning': 'Heures de formation en bioinformatique',
        'Stat2_title': 'Projets',
        'Stat2_meaning': 'Projets académiques réalisés',
        'Stat3_title': 'Stages',
        'Stat3_meaning': 'Nombre de stages réalisés',
        'Stat4_title': 'Publications',
        'Stat4_meaning': 'Articles et papiers publiés',
        'Skills': 'Compétences',
        'Skills_sentence': "Compétences développées tout au long de ma formation en bioinformatique, lors de mes projets académiques et de mes stages professionnels. Voici quelques-unes de mes compétences techniques et des outils que je maîtrise :",
        'Skill_1': 'Python',
        'Skill_2': 'R',
        'Skill_3': 'Statistiques',
        'Skill_4': 'Analyse spatiale & multi-omics',
        'Skill_5': 'Bases de données SQL',
        'Skill_6': "Apprentissage automatique",
        'resume_desc': "Ingénieur en Bioinformatique passionné par l'immunologie, le drug design et l'analyse multi‑omics.",
        'download_cv': 'Télécharger mon CV',
        'Summary': 'Résumé',
        'Summary_sentence': "Je suis autonome, proactif et curieux, avec une expertise en bioinformatique, analyse de données multi-omics et biologie moléculaire. Motivé par l'innovation et les défis scientifiques.",
        'Education': 'Formation',
        'Education_name_1': 'Master en Bioinformatique',
        'Education_establishment_1': 'Université Claude Bernard Lyon 1',
        'Education_skills_1': "Compétences : techniques d'apprentissage automatique, statistiques bayésiennes, bioinformatique structurale & drug design, analyse de données multi-OMICS (genomiques, metagenomiques, transcriptomiques et proteomiques), gestion de base de données, programmation web, algorithmique avancée.",
        'Education_name_2': 'Master en Biologie Moléculaire & Immunologie',
        'Education_establishment_2': 'Université Claude Bernard Lyon 1',
        'Education_skills_2': "Compétences : immunologie, immunopathologie, biologie du cancer, cartographie génétique, microscopie (électronique, épifluorescence, confocale), interférence par ARN (microinjection d'embryons de poisson zèbre).",
        'Prof_experience': 'Expérience Professionnelle',
        'Prof_experience_name_1': 'Stagiaire en Recherche Data Science',
        'Prof_experience_establishment_1': 'Centre Léon Bérard, Équipe Prévention & Santé Publique, Lyon',
        'Prof_experience_duration_1': 'Avril - Juin 2024',
        'Prof_experience_description_1_skill_1': "Réalisation d'une analyse approfondie des données OMICS sur une cohorte de patients pour étudier les profils mutationnels et immunologiques.",
        'Prof_experience_description_1_skill_2': "Utilisation d'une analyse factorielle avancée (MOFA) pour caractériser les sous-groupes de patients et optimiser les stratégies thérapeutiques personnalisées.",
        'Prof_experience_name_2': "Stagiaire en Recherche en Immuno-Oncologie",
        'Prof_experience_establishment_2': 'CRCL (Centre de Recherche en Cancérologie de Lyon), Équipe GRINBERG, Lyon',
        'Prof_experience_duration_2': 'Janvier - Juin 2023',
        'Prof_experience_description_2_skill_1': "Étude des sous-unités du facteur de transcription NF-kB dans les lymphocytes T CD4+ et leurs implications dans les maladies auto-immunes et le cancer.",
        'Prof_experience_description_2_skill_2': "Analyse des voies de signalisation impliquées dans la régulation de l'immunité tumorale.",
        'Prof_experience_name_3': 'Stagiaire en Recherche Virologie',
        'Prof_experience_establishment_3': "CIRI (Centre International de Recherche en Infectiologie), Équipe REVE, Lyon",
        'Prof_experience_duration_3': 'Janvier - Mars 2022',
        'Prof_experience_description_3_skill_1': "Développement d'un nouveau système de vectorisation d'ARN utilisant la protéine pseudo-virale humaine hPEG10.",
        'Prof_experience_description_3_skill_2': "Réalisation de clonage de plasmides, conception d'amorces RT-PCR et qPCR, digestion enzymatique et transfection de plasmides.",
        'Prof_experience_name_4': 'Stagiaire en Recherche Spatial-Omics',
        'Prof_experience_establishment_4': 'CRCL (Centre de Recherche en Cancérologie de Lyon), Équipe SAINTIGNY, Lyon',
        'Prof_experience_duration_4': 'Janvier - Août 2025',
        'Prof_experience_description_4_skill_1': "Analyse de données de transcriptomique spatiale utilisant les packages Seurat et Scanpy.",
        'Prof_experience_description_4_skill_2': "Identification de plus de 5 motifs clés d'expression génique spatiale associés aux sous-types tumoraux.",
        'Portfolio_description': "Dans cette section, vous pouvez trouver tous les projets sur lesquels j'ai travaillé et développé.",
        'All': 'Tous',
        'More_details': 'Plus de détails',
        'Project': 'Projet',
        'Portfolio_details': 'Détails du Portfolio',
        'Portfolio_keyword_project_1': 'Métagénomique',
        'Portfolio_keyword_2_project_1': 'Écologie Microbienne',
        'Portfolio_description_project_1': 'Analyse des plasmides et des gènes de résistance aux antibiotiques dans les métagénomes du sol.',
        'Portfolio_description_text_project_1': 'Ce projet utilise des outils bioinformatiques avancés pour analyser des plasmides et des gènes de résistance aux antibiotiques (ARG) dans des métagénomes du sol. Notre objectif est d\'élucider la dynamique des ARG au sein des populations de plasmides et leur réponse aux facteurs environnementaux.',
        'Portfolio_keyword_project_2': 'Analyse RNAseq',
        'Portfolio_keyword_2_project_2': 'Épissage alternatif, Immunologie',
        'Portfolio_description_project_2': 'Analyse de l\'épissage alternatif dans les cellules dendritiques plasmacytoïdes et impact sur la réponse antivirale.',
        'Portfolio_description_text_project_2': "Depuis quelques décennies, l'expansion urbaine et les activités humaines ont conduit à des interactions accrues entre les humains et des espèces qu'ils n'avaient jamais rencontrées auparavant. Cette interaction avec différentes espèces montre que les zoonoses (comme le virus CoVID19) peuvent apparaître. Ainsi, comprendre les mécanismes du système immunitaire, en particulier dans le contexte des infections virales, est devenu un enjeu de santé publique. Chez l'espèce humaine, les infections virales sont principalement gérées par des cellules immunitaires appelées cellules dendritiques plasmacytoïdes (pDC). Ces cellules sont de grands producteurs d'interféron de type 1, une cytokine d'alerte très efficace qui met les cellules en état de vigilance contre les virus, prête à résister à l'infection virale. Plusieurs autres protéines sont synthétisées par les pDC, ce qui permet une réponse immunitaire très spécifique contre le virus. Ainsi, dans le contexte d'une infection virale, ces protéines produites par les pDC sont essentielles et donc fortement régulées. Parmi ces mécanismes de régulation, le remodelage de l'épissage alternatif pourrait expliquer comment les pDC peuvent adapter leur réponse en fonction du virus auquel elles sont confrontées. De tels mécanismes ont déjà été démontrés dans d'autres cellules immunitaires, mais à ce jour, les mécanismes dans les pDC ne sont pas bien connus.",
        'Portfolio_keyword_project_3': 'Protéomique',
        'Portfolio_keyword_2_project_3': 'Identification de peptides, Phylogénie',
        'Portfolio_description_project_3': 'Développement de PeptideFinder, un outil d\'identification de peptides à partir de données de spectrométrie de masse.',
        'Portfolio_description_text_project_3': "Ce projet se concentre sur l'identification de biomarqueurs protéomiques à partir du défensome chimique d'espèces de poissons sauvages. En intégrant des outils bioinformatiques et des flux de travail computationnels, nous visons à analyser les données génomiques et protéomiques pour comprendre les réponses de ces espèces aux facteurs de stress environnementaux. Le projet explore également des biomarqueurs potentiels pour la surveillance écologique et l'évaluation des risques.",
        'Portfolio_keyword_project_4': 'Spatial OMICS',
        'Portfolio_keyword_2_project_4': 'Transcriptomique spatiale, Recherche sur le cancer',
        'Portfolio_description_project_4': 'Intégration et analyse des données de transcriptomique spatiale dans la recherche sur le cancer du sein.',
        'Portfolio_description_text_project_4': "Ce projet analyse les données de transcriptomique spatiale provenant de 15 échantillons de carcinome mammaire métaplasique (MpBC) utilisant la technologie 10x Genomics Visium. Il vise à explorer l'hétérogénéité tumorale et la transdifférenciation, en s'appuyant sur des types cellulaires étiquetés par des experts pour identifier des clusters spatiaux et des biomarqueurs.",
        'Address': 'Adresse',
        'Call Me': 'Appelez-moi',
        'Email Me': 'Envoyez-moi un e-mail',
        'January': 'Janvier',
        'February': 'Février',
        'March': 'Mars',
        'September': 'Septembre',
        

        'Services': 'Services',
        'Testimonials': 'Témoignages',
        'about_desc': "Bioinformaticien passionné avec une expertise en multi‑omics, immunologie et pipelines computationnels avancés, visant à promouvoir l'innovation en recherche sur le cancer et en biotechnologie.",
        'typed_items': "Bioinformaticien, Immunologiste, Data Scientist, Analyste Multi‑omics",
        'resume_title': 'CV',
        'contact_desc': "Si vous souhaitez me contacter, n'hésitez pas à m'écrire par e-mail ou LinkedIn"
    }

}

# Additional per-page labels used by portfolio details templates
for lang_map in (translations['en'], translations['fr']):
    # only add defaults if not present
    lang_map.setdefault('portfolio_details_title', 'Portfolio Details' if lang_map is translations['en'] else 'Détails du Portfolio')
    lang_map.setdefault('project_information', 'Project information' if lang_map is translations['en'] else 'Informations sur le projet')
    lang_map.setdefault('category', 'Category' if lang_map is translations['en'] else 'Catégorie')
    lang_map.setdefault('laboratory', 'Laboratory' if lang_map is translations['en'] else 'Laboratoire')
    lang_map.setdefault('project_date', 'Project date' if lang_map is translations['en'] else 'Date du projet')
    lang_map.setdefault('project_url', 'Project URL' if lang_map is translations['en'] else "URL du projet")


@app.context_processor
def inject_translations():
    # Determine language from URL prefix (/fr/) first, then cookie, default to english
    path = request.path or ''
    if path.startswith('/fr'):
        lang = 'fr'
    else:
        lang = request.cookies.get('lang', 'en')
        if lang not in translations:
            lang = 'en'
    trans = translations[lang]

    def t(key):
        return trans.get(key, key)

    return {'t': t, 'current_lang': lang}


@app.context_processor
def inject_alternates():
    """Provide per-request alternate URLs for English and French versions.

    This builds two absolute URLs and exposes them as `alternate_urls` to templates
    so `layout.html` can render hreflang tags dynamically.
    """
    try:
        base = request.url_root.rstrip('/')
        path = request.path or '/'
        # canonicalize simple cases
        if path.startswith('/fr'):
            fr = base + path
            en_path = path[3:] or '/'
            en = base + en_path
        else:
            en = base + path
            if path == '/':
                fr = base + '/fr/'
            else:
                # prefix /fr to path
                fr = base + '/fr' + path
        return {'alternate_urls': {'en': en, 'fr': fr}}
    except RuntimeError:
        # request context not available (e.g. from CLI) — return sensible defaults
        return {'alternate_urls': {'en': '/', 'fr': '/fr/'}}


@app.route('/set_language/<lang>')
def set_language(lang):
    # set language cookie and redirect back
    next_url = request.args.get('next') or request.referrer or url_for('root')
    resp = redirect(next_url)
    if lang not in translations:
        lang = 'en'
    resp.set_cookie('lang', lang, max_age=60*60*24*30)  # 30 days
    return resp


@app.route("/")
def root():
    jour, mois, annee = date()  # Décompose toutes les valeurs retournées
    return render_template(
        "all_section.html", jour=jour, mois=mois, annee=annee)


# French-prefixed routes for SEO (mirror of main routes under /fr/)
@app.route('/fr/')
def root_fr():
    jour, mois, annee = date()
    return render_template('all_section.html', jour=jour, mois=mois, annee=annee)


@app.route('/fr/section/<section_name>')
def section_fr(section_name):
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


@app.route('/fr/portfolio/Project_<int:project_id>')
def portfolio_project_fr(project_id):
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


# Serve favicon at root so crawlers and Google can easily find it
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'assets/img/favicon.ico', mimetype='image/vnd.microsoft.icon')


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