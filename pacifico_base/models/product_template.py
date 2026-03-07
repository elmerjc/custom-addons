# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    model = fields.Char(string='Modelo')
    statement = fields.Char(string='Declaración')
    container = fields.Char(string='Container')
    receipt = fields.Char(string='Recibo')
    item = fields.Char(string='Item')
