# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command
import logging
_logger = logging.getLogger(__name__)

class EventEvent(models.Model):
    _inherit = "event.event"
    
    track_ids = fields.One2many(copy=True) #enable copy for event tracks