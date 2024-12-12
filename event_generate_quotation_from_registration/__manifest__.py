# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "event_generate_quotation_from_registration",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "Elabore",
    "website": "https://www.elabore.coop",    
    "category": "",
    'summary': 'Generate quotation from event registration',
    'description': """
        Generate quotation from event registration : 
    """,
    "depends": ["event_sale"],
    "data": [     
        'security/ir.model.access.csv',
        'views/event_registration_views.xml',
    ],    
    "installable": True,
}
