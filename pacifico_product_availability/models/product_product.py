# Copyright 2020 Tecnativa - Ernesto Tejeda
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging

from odoo import models, api

_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.depends('receipt', 'item')
    def _compute_display_name(self):
        res = super()._compute_display_name()
        for record in self:
            record.display_name = f"{record.display_name} {record.receipt}-{record.item}"

        if self.env.context.get("so_product_stock_inline"):
            self = self.with_context(warehouse=self.env.context.get("warehouse"))
            availability = {r.id: [r.free_qty, r.uom_id.display_name] for r in self}
            precision = self.env["decimal.precision"].precision_get(
                "Product Unit of Measure"
            )
            for record in self:
                name = "{} ({:.{}f} {})".format(
                    record.display_name,
                    availability[record.id][0],
                    precision,
                    availability[record.id][1],
                )
                record.display_name = name
        return res


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.depends('receipt', 'item')
    @api.depends_context('so_product_stock_inline', 'warehouse')
    def _compute_display_name(self):
        super()._compute_display_name()
        if self.env.context.get("so_product_stock_inline"):
            self = self.with_context(warehouse=self.env.context.get("warehouse"))
            availability = {r.id: [r.qty_available] for r in self}

        for record in self:
            # Avoid duplicating if already added (though standard Odoo flow recomputes cleanly)
            # But since we are appending to self.display_name which was just set by super(),
            # we are fine.
            # Check if fields exist to avoid False-False
            receipt = record.receipt or ''
            item = record.item or ''
            suffix = f" {receipt}-{item}" if receipt or item else ""

            if self.env.context.get("so_product_stock_inline"):
                name = "{} {} ({})".format(
                    record.display_name,
                    suffix,
                    availability[record.id][0]
                )
                record.display_name = name
            else:
                record.display_name = record.display_name
