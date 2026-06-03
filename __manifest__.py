# -*- coding: utf-8 -*-
{
    'name': 'MultiSafePay Payment Provider',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'author': "Cybrosys",
    'category': 'Accounting/Payment Providers',
    'depends': ['payment', 'account_payment'],
    'data': [
        'views/payment_provider_views.xml',
        'data/payment_method_data.xml',
        'data/payment_provider_data.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3',
}
