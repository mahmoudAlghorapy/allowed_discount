from odoo import models, fields, api


class CompanyInherit(models.Model):
    _inherit = 'res.company'

    allowed_discount_account = fields.Many2one('account.account',
                                               string='Allowed discount account', required=True)
    allowed_discount_product = fields.Many2one('product.product',
                                               required=True,
                                               string='Allowed discount Product',
                                               domain="[('detailed_type','=','service')]")
