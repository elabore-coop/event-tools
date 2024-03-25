# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class EventTrack(models.Model):
    _inherit = "event.track"

    speaker_ids = fields.Many2many(
        'res.partner', string="Speakers", domain="[('is_company','=',False)]"
    )
