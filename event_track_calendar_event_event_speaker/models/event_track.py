# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command


class EventTrack(models.Model):
    _inherit = "event.track"    

    speaker_ids = fields.Many2many(
        'res.partner', string="Speakers", compute="compute_speaker_ids"
    )

    def compute_speaker_ids(self):
        """set speaker_ids as concat of all speakers of all events"""
        for track in self:
            speaker_ids = set()
            for event in track.calendar_event_ids:
                speaker_ids.update(event.speaker_ids.ids)
            track.speaker_ids = list(speaker_ids)
                

    def get_calendar_event_partner_value(self):
        """Add speaker ids to calendar event partners
        """
        res = super(EventTrack, self).get_calendar_event_partner_value()
        res.extend(self.speaker_ids.ids)
        return res


