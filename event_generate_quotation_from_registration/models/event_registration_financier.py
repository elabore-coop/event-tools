# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command
import logging

from odoo.exceptions import UserError
_logger = logging.getLogger(__name__)

class EventRegistrationFinancier(models.Model):
    _name = "event.registration.financier"

    _rec_name = 'financier_id'

    company_id = fields.Many2one("res.company")
    company_currency_id = fields.Many2one('res.currency', related="company_id.currency_id")
    registration_id = fields.Many2one('event.registration')
    quotation_id = fields.Many2one('sale.order', string="Devis")
    financier_id = fields.Many2one('res.partner', string="Financeur", required=True)
    terms = fields.Char('Modalités')
    amount = fields.Monetary('Montant', currency_field="company_currency_id")
    state = fields.Selection(
        related='quotation_id.state',
        string="Order Status",
        copy=False, store=True, precompute=True)


    def get_product_id(self):
        if self.registration_id.event_ticket_id:
            return self.registration_id.event_ticket_id.product_id.id
        elif self.registration_id.event_id.event_ticket_ids:
            return self.registration_id.event_id.event_ticket_ids[0].product_id.id
        raise UserError('Un ticket doit être défini dans la session de formation afin de générer le devis')

    def get_sale_order_values(self):
        return {
            'event_registration_id':self.registration_id.id,
            'partner_id':self.financier_id.id,             
        }
    
    def get_sale_order_line_values(self):
        return [Command.create({
                    "price_unit": self.amount,
                    "product_id": self.get_product_id()
                })]
    
