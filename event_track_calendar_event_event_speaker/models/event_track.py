# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command


class EventTrack(models.Model):
    _inherit = "event.track"    

    def get_calendar_event_partner_value(self):
        """Add speaker ids to calendar event partners
        """
        res = super(EventTrack, self).get_calendar_event_partner_value()
        res.extend(self.event_id.speaker_ids.ids)
        return res


