# -*- coding: utf-8 -*-

from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_description_without_product_code(self, product, description):
        if product and product.default_code:
            description = str(description).replace("[" + product.default_code + "]", "").strip()
        return description.strip()
