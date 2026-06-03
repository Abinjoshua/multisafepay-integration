# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import requests


class MultiSafePayController(http.Controller):
    @http.route('/shop/payment/success',
                type='http', auth='public',
                methods=['GET'], csrf=False)
    def multisafepay_simulate_payment(self, **data):

        url = "https://testapi.multisafepay.com/v1/json/orders/"+data['transactionid']+"?api_key=1fec9c037d81e37646771b97c20073298ba76e0c"

        headers = {"accept": "application/json"}

        response = requests.get(url, headers=headers).json()

        if response['success']:
            transaction = self.env['payment.transaction'].browse(int(response['data']['custom_info']['custom_1']))
            transaction.write({'state': 'done'})

        return request.redirect('/payment/status')