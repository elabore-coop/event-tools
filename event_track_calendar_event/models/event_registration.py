# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command
import logging
_logger = logging.getLogger(__name__)

class EventRegistration(models.Model):
    _inherit = "event.registration"
    
    def write(self, vals):
        _logger.warning("call write...")
        res = super(EventRegistration,self).write(vals)       
        _logger.warning("Super Write OK") 
        for registration in self:
            for track in registration.event_id.track_ids:
                track.sync_calendar_event()
        _logger.warning("called !")
        return res

    @api.model_create_multi
    def create(self, vals_list):
        res = super(EventRegistration, self).create(vals_list)
        for registration in res:
            for track in registration.event_id.track_ids:
                track.sync_calendar_event()
        return res