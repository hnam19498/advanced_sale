from odoo import api, fields, models
import json


class SaleVip(models.Model):
    _inherit = 'sale.order'

    sale_order_discount_estimated = fields.Float(string='Sale order discount estimated', compute='sale_vip_int')

    def sale_vip_int(self):
        if 'vip 10' in self.partner_id.customer_discount_code:
            self.sale_order_discount_estimated = json.loads(self.tax_totals_json)['amount_total'] * -0.1
        elif 'vip 20' in self.partner_id.customer_discount_code:
            self.sale_order_discount_estimated = json.loads(self.tax_totals_json)['amount_total'] * -0.2
        else:
            self.sale_order_discount_estimated = 0

    # def _compute_tax_totals_json(self):
    #     pass
