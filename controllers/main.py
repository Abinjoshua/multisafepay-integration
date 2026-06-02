# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class MultiSafePayController(http.Controller):
    @http.route('/payment/multisafepay/simulate_payment',
                type='http', auth='public',
                methods=['POST'], csrf=False)
    def multisafepay_simulate_payment(self, **data):
        print('working')
        payment_data = {
            'reference': data.get('reference'),
            'status': data.get('status', 'done'),
        }
        request.env['payment.transaction'].sudo() \
            ._process('multisafepay', payment_data)
        return request.redirect('/payment/status')