# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    quantity_total = fields.Integer(
        string='Cantidad de pares',
        store=True,
        compute='_compute_quantity_total'
    )

    @api.depends('order_line.product_uom_qty')
    def _compute_quantity_total(self):
        for order in self:
            order.quantity_total = sum(line.product_uom_qty for line in order.order_line)
