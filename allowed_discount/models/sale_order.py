from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SOInherit(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id.allowed_discount > 0:
            discount_line = self.order_line.filtered(lambda line: line.product_id == self.company_id.allowed_discount_product)
            if discount_line:
                discount_line[0].update({
                    'price_unit': self.partner_id.allowed_discount * -1
                })
            else:
                self.order_line = [(0, 0, {
                    'product_id': self.company_id.allowed_discount_product.id,
                    'name': self.company_id.allowed_discount_product.display_name,
                    'price_unit': self.partner_id.allowed_discount * -1,
                    'product_uom': self.company_id.allowed_discount_product.uom_id.id,
                    'product_uom_qty': 1,
                })]


class SOLineInherit(models.Model):
    _inherit = 'sale.order.line'

    def _prepare_invoice_line(self, **optional_values):
        res = super()._prepare_invoice_line(**optional_values)
        if res.get('product_id') == self.env.company.allowed_discount_product.id:
            res.update({'account_id': self.env.company.allowed_discount_account.id})
        return res

