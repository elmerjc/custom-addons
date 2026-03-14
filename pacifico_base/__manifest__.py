# -*- coding: utf-8 -*-
{
    'name': 'Módulo Base para Distribuidor del Pacífico',
    'version': '1.0.0',
    'summary': """ Registro de configuración base para Distribuidor del Pacífico """,
    'author': 'takana.cloud',
    'website': 'https://takana.cloud',
    'category': 'base',
    'depends': [
        'product',
        'account',
        'sale_management',
        'purchase',
        'stock'
    ],
    'data': [
        'views/product_template_views.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/stock_move_views.xml',
        'views/purchase_order_views.xml',
        'views/stock_picking_layouts.xml',
        'report/stock_picking_report.xml',
    ],
    'sequence': 1,
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
