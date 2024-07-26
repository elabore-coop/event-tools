# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command
from datetime import timedelta
import logging

_logger = logging.getLogger(__name__)


class EventTrack(models.Model):
    _inherit = "event.track"

    event_id = fields.Many2one(ondelete='cascade') #delete event tracks when delete event
