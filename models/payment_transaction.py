# -*- coding: utf-8 -*-

from odoo import models


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        """Provides the values needed to render the QWeb redirect form."""
        res = super()._get_specific_rendering_values(processing_values)

        if self.provider_code != 'multisafepay':
            return res
        import requests

        url = "https://testapi.multisafepay.com/v1/json/orders?api_key=cd0e81e3b534d7a9400aba384c23fba5d422328f"

        payload = {
            "type": "redirect",
            "order_id": "my-order-id-1",
            "currency": "USD",
            "amount": processing_values['amount'] * 100,
            "description": "Test Order Description",
            "payment_options": {
                "notification_method": "POST",
                "notification_url": "https://www.example.com/webhooks/payment",
                "redirect_url": "https://www.example.com/order/success",
                "cancel_url": "http://localhost:8019/shop/payment",
                "close_window": False
            },
            "customer": {
                "locale": "en_US",
                "disable_send_email": False
            },
            "checkout_options": {"validate_cart": False},
            "days_active": 30,
            "seconds_active": 2592000
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers).json()
        print('response',response)
        response1 = requests.get(url, headers=headers)

        print('res',response1.text)

        if response['success']:
            return {
                'api_url': response['data']['payment_url'],
                'reference': self.reference,
            }

    def _extract_amount_data(self, payment_data):
        """Skip amount validation for simulated providers."""
        if self.provider_code in ('multisafepay'):
            return None
        return super()._extract_amount_data(payment_data)

    def _apply_updates(self, payment_data):
        """Set the transaction state based on the simulated status."""
        print(payment_data)
        super()._apply_updates(payment_data)
        if self.provider_code not in ('multisafepay'):
            return
        status = payment_data.get('status')

        if status == 'done':
            self._set_done()
        elif status == 'cancel':
            self._set_canceled()
