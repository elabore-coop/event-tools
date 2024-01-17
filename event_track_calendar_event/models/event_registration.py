# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command


class EventRegistration(models.Model):
    _inherit = "event.registration"
    
    def write(self, vals):
        res = super().write(vals)        
        for registration in self:
            for track in registration.event_id.track_ids:
                track.sync_calendar_event()
        return res

    @api.model_create_multi
    def create(self, vals_list):
        res = super(EventRegistration, self).create(vals_list)
        for registration in res:
            for track in registration.event_id.track_ids:
                track.sync_calendar_event()
        return res