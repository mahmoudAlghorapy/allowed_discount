from odoo import api, fields, models, _


class AccountSettingsInherit(models.TransientModel):
    _inherit = 'res.config.settings'

    allowed_discount_account = fields.Many2one('account.account',
                                               string='Allowed discount account', required=True,
                                               related='company_id.allowed_discount_account',
                                               readonly=False)
    allowed_discount_product = fields.Many2one('product.product',
                                               required=True,
                                               string='Allowed discount Product',
                                               related='company_id.allowed_discount_product',
                                               readonly=False,
                                               domain="[('detailed_type','=','service')]")

