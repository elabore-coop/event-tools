# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class EventSequence(models.Model):
    _name = "event.sequence"

    name = fields.Char("name")
    sequence = fields.Integer("Sequence")
