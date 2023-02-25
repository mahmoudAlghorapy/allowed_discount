from odoo import models, fields, api


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    allowed_discount = fields.Float(string='Allowed Discount')
