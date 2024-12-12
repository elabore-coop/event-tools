# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command
import logging
_logger = logging.getLogger(__name__)

class EventRegistration(models.Model):
    _inherit = "event.registration"
    
    financier_ids = fields.One2many('event.registration.financier', 'registration_id', string="Financements")


    def generate_quotation(self):
        for registration in self:
            for financier in registration.financier_ids:
                if not financier.quotation_id:
                    sale_order = self.env['sale.order'].create(financier.get_sale_order_values())
                    financier.quotation_id = sale_order
                else:
                    order_lines = self.env['sale.order.line'].search([
                        ('order_id','=',financier.quotation_id.id), 
                        ('product_id','=',financier.get_product_id())
                    ])
                    if order_lines:
                        order_lines[0].price_unit = financier.amount