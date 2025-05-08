# -*- coding: utf-8 -*-
{
    'name': 'Gestion Parc Informatique',
    'version': '1.0',
    'summary': 'Module de gestion de parc informatique pour prestataire IT',
    'description': """Gestion de parcs informatiques avec contrats.""",
    'author': 'Kablan Marie-Agnès',
    'category': 'Services/IT',
    'depends': ['base', 'mail','portal','website','hr', 'stock','purchase', 'account',],
    'data': [
        'security/gestion_parc_security.xml',
        'security/ir.model.access.csv',
        'views/parc_views.xml',       # Fichier séparé
        'views/equipement_views.xml',  # Fichier séparé
        'views/contrat_views.xml',
        'views/intervention_views.xml',
        'views/facture_views.xml',
        'views/client_views.xml',
        'report/report_contrat.xml',
        'report/contrat_template.xml',
    ],

    "application": True,
    'installable': True,
    'license': 'LGPL-3',
    'images': ['static/description/icon.png'],
}
