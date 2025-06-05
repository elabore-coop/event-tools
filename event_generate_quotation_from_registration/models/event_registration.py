# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api, Command
import logging
_logger = logging.getLogger(__name__)

class EventRegistration(models.Model):
    _inherit = "event.registration"
    
    financier_ids = fields.One2many('event.registration.financier', 'registration_id', string="Financements")

    def name_get(self):
        result = []
        for registration in self:
            if registration.partner_id and registration.event_id:
                name = f"{registration.partner_id.name} ({registration.event_id.name})"
                result.append((registration.id, name))
        return result
    
    @api.depends("partner_id", "event_id")
    def _compute_display_name(self):
        for registration in self:
            if registration.partner_id and registration.event_id:
                registration.display_name = f"{registration.partner_id.name} ({registration.event_id.name})"
            else:
                registration.display_name = super(EventRegistration, registration)._compute_display_name()



    def generate_quotation(self):
        for registration in self:
            for financier in registration.financier_ids:
                if not financier.quotation_id:
                    so_values = financier.get_sale_order_values()
                    so_values['order_line'] = financier.get_sale_order_line_values()
                    sale_order = self.env['sale.order'].create(so_values)
                    financier.quotation_id = sale_order
                else:
                    order_lines = self.env['sale.order.line'].search([
                        ('order_id','=',financier.quotation_id.id),
                        ('product_id','=',financier.get_product_id()),
                        ('state', '!=', 'done'),
                    ])
                    if order_lines:
                        order_lines[0].price_unit = financier.amount
                    financier.quotation_id.write(financier.get_sale_order_values())
                    