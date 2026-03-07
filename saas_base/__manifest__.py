{
    'name': 'SaaS Base',
    'version': '17.0.1.0.0',
    'summary': 'Module to create Odoo databases',
    'description': 'Allows creating new Odoo databases via a website form.',
    'category': 'SaaS',
    'author': 'Takana Cloud',
    'depends': ['website'],
    'data': [
        'views/website_templates.xml',
    ],
    'installable': True,
    'application': True,
}
