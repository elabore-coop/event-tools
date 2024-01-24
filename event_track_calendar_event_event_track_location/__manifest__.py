# Copyright 2016-2020 Akretion France (<https://www.akretion.com>)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Event track location in calendar event",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "Elabore",
    "website": "https://www.elabore.coop",    
    "category": "",
    'summary': 'Link event tracks locations to calendar event',
    'description': """
Link event tracks locations to calendar event
----------------------------------------------------
* Add Partner field on event track location
* Add partner "location" to calendar event
* Update calendar event if event track location change (or partner in event track location)
* Alert if location is used


""",
    "depends": ["website_event_track","calendar"],
    "data": [    
        'views/event_track_location_views.xml', 
        'views/event_track_views.xml'       
    ],    
    "installable": True,
}
