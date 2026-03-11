# -*- coding: utf-8 -*-

from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_description_without_product_code(self, product, description):
        name = ""
        if product and product.default_code:
            description = str(description).replace("[" + product.default_code + "]", "").strip()
        name = f"{description} {product.receipt or ''}-{product.item or ''}"
        return name.strip()
