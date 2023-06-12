# -*- coding: utf-8 -*-
# Part of Softhealer Technologies

{
    'name': "Create Single Invoice For Multiple Sale Orders",
    'author': 'Miig Solution',
    'website': 'https://www.miigsolution.so',
    "support": "support@miigsolution.so",
    'category': 'Accounting',
    'version': '16.0.1',
    "license": "OPL-1",
    "summary": "One Invoice From multiple Sale Orders Invoice From Sale Orders Multiple Sale Order Single Invoice One Invoice From Multi Sale Orders single invoice from Multiple delivery single invoice from delivery single invoice from mass delivery order Odoo",
    "description": """Purpose of the module is to create a single invoice from multiple sale orders/delivery orders. Sometimes we have the same customer which are not invoiced so at that time it's easy to maintain one invoice for every sale order. So choose the sales orders from the list view and generate invoice!""",
    "depends": ["sale_management", "account"],
    "data": [
        'security/ir.model.access.csv',
        'wizard/create_single_invoice_wizard.xml',
        'views/sale_order.xml',
    ],

    "auto_install": False,
    "installable": True,
    "application": True,
    'images': ['static/description/background.png', ],
    "price": 30,
    "currency": "EUR",

}
