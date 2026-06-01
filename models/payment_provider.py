# -*- coding: utf-8 -*-
from odoo import fields, models


class PaymentProvider(models.Model):

    _inherit = 'payment.provider'
    
    code = fields.Selection(selection_add=[
        ('multisafepay', 'MultiSafePay Online'),
        ('multisafepay_direct', 'MultiSafePay Direct'),
    ], ondelete={
        'multisafepay': 'set default',
        'multisafepay_direct': 'set default',
    })

    def _get_default_payment_method_codes(self):
        res = super()._get_default_payment_method_codes()
        if self.code == 'multisafepay':        return {'multisafepay'}
        if self.code == 'multisafepay_direct': return {'multisafepay_direct'}
        return res
