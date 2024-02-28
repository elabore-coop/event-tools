# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    event_track_id = fields.Many2one('event.track', "Event track")

    @api.model_create_multi
    def create(self, vals_list):        
        res = super(CalendarEvent,self).create(vals_list)
        for event in res:
            if event.event_track_id:
                event.event_track_id.sync_calendar_event()
    
   
