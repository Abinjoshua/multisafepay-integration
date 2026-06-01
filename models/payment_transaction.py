# -*- coding: utf-8 -*-

from odoo import models


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        """Provides the values needed to render the QWeb redirect form."""
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'multisafepay':
            return res
        return {
            'api_url': '/payment/multisafepay/simulate_payment',
            'reference': self.reference,
        }

    def _extract_amount_data(self, payment_data):
        """Skip amount validation for simulated providers."""
        if self.provider_code in ('multisafepay', 'multisafepay_direct'):
            return None
        return super()._extract_amount_data(payment_data)

    def _apply_updates(self, payment_data):
        """Set the transaction state based on the simulated status."""
        super()._apply_updates(payment_data)
        if self.provider_code not in ('multisafepay', 'multisafepay_direct'):
            return
        status = payment_data.get('status')
        if status == 'done':
            self._set_done()
        elif status == 'cancel':
            self._set_canceled()
