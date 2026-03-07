# -*- coding: utf-8 -*-
{
    'name' : 'Pacifico - Impresión de Cotizaciones',
    'version' : '0.1.0',
    'category': 'Sales',
    'author' : 'takana.cloud',
    'website': "https://takana.cloud",
    'summary' : 'Impresión de cotizaciones',
    'depends' : [
        'sale',
        'sale_product_pack',
        'odoope_ruc_validation'
    ],
    'data' : [
        'views/quotation_layouts_custom.xml',
        'report/report.xml',
        'report/report_quotation_custom.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'pacifico_sale_report/static/src/css/*',
        ],
    },
    'sequence': 1,
    'installable' : True,
    'application' : True,
    'license': 'LGPL-3'
}
