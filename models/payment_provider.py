# -*- coding: utf-8 -*-
from odoo import fields, models


class PaymentProvider(models.Model):

    _inherit = 'payment.provider'
    
    code = fields.Selection(selection_add=[
        ('multisafepay', 'MultiSafePay Online'),
    ], ondelete={
        'multisafepay': 'set default',
    })

    multisafepay_api_key = fields.Char(string='API Key')

    def _get_default_payment_method_codes(self):
        res = super()._get_default_payment_method_codes()
        if self.code == 'multisafepay':        return {'multisafepay'}
        return res
