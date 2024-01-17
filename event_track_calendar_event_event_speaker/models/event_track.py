# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command


class EventTrack(models.Model):
    _inherit = "event.track"    


    def get_calendar_event_values(self):
        self.ensure_one()

        res = super(EventTrack, self).get_calendar_event_values()

        # add speakers
        res['partner_ids'].extend(self.event_id.speaker_ids.ids)

        return res

