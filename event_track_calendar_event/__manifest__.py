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
    'summary': 'Replace date of event track with list of calendar events',
    'description': """
Replace date of event track with list of calendar events
----------------------------------------------------
* Create calendar events on event track form
* Sync calendar event attendees with event track registration

""",
    "depends": ["website_event_track","calendar"],
    "data": [     
        "views/event_track_views.xml"           
    ],    
    "installable": True,
}
