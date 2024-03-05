# Copyright 2016-2020 Akretion France (<https://www.akretion.com>)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Event sequences",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "Elabore",
    "website": "https://www.elabore.coop",
    "category": "",
    "depends": ["event", "website_event_track"],
    "data": [       
        'security/ir.model.access.csv', 
        'views/event_sequence_views.xml',         
        'views/event_track_views.xml',     
        'views/event_event_views.xml',     
        'views/event_sequence_menu.xml',         
        'data/event_sequence_data.xml',   
    ],    
    "installable": True,
}
