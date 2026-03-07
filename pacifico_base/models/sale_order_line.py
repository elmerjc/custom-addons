# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    statement = fields.Char(
        related='product_id.statement',
        store=True,
        copy=False
    )
    container = fields.Char(
        related='product_id.container',
        store=True,
        copy=False
    )
    receipt = fields.Char(
        related='product_id.receipt',
        store=True,
        copy=False
    )
    item = fields.Char(
        related='product_id.item',
        store=True,
        copy=False
    )
    
    def _prepare_invoice_line(self, **kwargs):
        result = super(SaleOrderLine, self)._prepare_invoice_line(**kwargs)
        result.update({
            'statement': self.statement,
            'container': self.container,
            'receipt': self.receipt,
            'item': self.item,
        })
        return result
