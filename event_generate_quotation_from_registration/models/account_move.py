from odoo import _, api, Command, fields, models

class AccountMove(models.Model):
    _inherit = "account.move"

    event_registration_id = fields.Many2one('event.registration', string="Stagiaire")