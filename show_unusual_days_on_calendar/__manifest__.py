# Copyright 2022 Stéphan Sainléger (Elabore)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "show_unusual_days_on_calendar",
    "version": "14.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Clément Thomas / Laetitia Da Costa",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "show unusual days such as leaves or holidays on event calendar in the same way it does in hr_leave calendar \n (event in gray background and white borders)",
    # any module necessary for this one to work correctly
    "depends": [
        "calendar",
        "hr_holidays",
    ],
    "qweb": [
    ],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        'views/calendar_event_views.xml',
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}