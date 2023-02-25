# -*- coding: utf-8 -*-
{
    'name': "Allowed Discount",

    'summary': """
        Discount in po """,

    'description': """
        Discount in po
    """,
    'author': "My Company",
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'product', 'sale'],
    # always loaded
    'data': [

        'views/partner.xml',
        'views/account_setting.xml',
    ],
}
