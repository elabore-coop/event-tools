# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging

from odoo import models

_logger = logging.getLogger(__name__)


class EventEvent(models.Model):
    _inherit = "event.event"

    def write(self, vals):
        res = super().write(vals)
        for event in self:
            for track in event.track_ids:
                track.sync_calendar_event()
        return res
