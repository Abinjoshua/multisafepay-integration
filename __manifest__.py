# -*- coding: utf-8 -*-
{
    'name': 'MultiSafePay Payment Provider',
    'version': '1.0.0',
    'category': 'Accounting/Payment Providers',
    'depends': ['payment', 'account_payment'],
    'data': [
        'views/payment_provider_views.xml',
        'views/payment_multisafepay_templates.xml',
        'data/payment_method_data.xml',
        'data/payment_provider_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'payment_multisafepay/static/src/js/payment_form.js',
        ],
    },
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3',
}
