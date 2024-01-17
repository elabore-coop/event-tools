# Copyright 2016-2020 Akretion France (<https://www.akretion.com>)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Event track calendar event",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "Elabore",
    "website": "https://www.elabore.coop",    
    "category": "",
    'summary': 'Link event tracks to calendar event',
    'description': """
Link event tracks to calendar event
----------------------------------------------------
* Create calendar event on event track creation
* Update calendar event on event track update
* Update event track when calendar event updated

""",
    "depends": ["website_event_track","calendar"],
    "data": [                
    ],    
    "installable": True,
}
