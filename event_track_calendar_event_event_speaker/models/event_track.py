# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class EventTrack(models.Model):
    _inherit = "event.track"

    speaker_ids = fields.Many2many(
        "res.partner", string="Intervenants", compute="_compute_speaker_ids"
    )

    def _compute_speaker_ids(self):
        """
        Set speaker_ids as concat of all speakers of all events.
        """
        for track in self:
            speaker_ids = set()
            for event in track.calendar_event_ids:
                speaker_ids.update(event.speaker_ids.ids)
            track.speaker_ids = list(speaker_ids)

    def get_calendar_event_partner_value(self):
        """
        Add speaker ids to calendar event partners.
        """
        res = super().get_calendar_event_partner_value()
        res.extend(self.speaker_ids.ids)
        return res
