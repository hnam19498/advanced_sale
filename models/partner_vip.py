from odoo import api, fields, models


class PartnerVip(models.Model):
    _inherit = 'res.partner'

    customer_discount_code = fields.Char(string='Discount code', default='')
