# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    speaker_ids = fields.Many2many(
        'res.partner', "calendar_event_speaker_rel", "calendar_event_id", "speaker_id", string="Intervenants", domain="[('is_company','=',False)]"
    )
