# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    price_unit = fields.Float('Precio Unitario', readonly=True, group_operator='avg')

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['price_unit'] = "l.price_unit"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += ", l.price_unit"
        return res
