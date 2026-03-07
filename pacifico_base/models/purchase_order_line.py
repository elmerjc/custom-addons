# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

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
