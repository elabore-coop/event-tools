# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command
_logger = logging.getLogger(__name__)

class EventEvent(models.Model):
    _inherit = "event.event"
    
    def write(self, vals):
        _logger.warning("call write...")
        res = super().write(vals)        
        for event in self:
            for track in event.track_ids:
                track.sync_calendar_event()
        _logger.warning("called !")
        return res
