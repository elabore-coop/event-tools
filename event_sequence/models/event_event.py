from odoo import fields, models


class EventEvent(models.Model):
    _inherit = "event.event"

    sequence_number = fields.Integer("Number of sequences", default="5")
    current_sequence_id = fields.Many2one("event.sequence", "Current sequence")
