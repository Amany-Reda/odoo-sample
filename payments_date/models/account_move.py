from odoo import api, fields, models

from odoo import models, fields


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    payment_date = fields.Char(compute='_compute_payment_date')

    def _compute_payment_date(self):
        self.payment_date = False
        for inv in self:
            dates = []
            if inv.invoice_payments_widget:
                payment = inv.invoice_payments_widget.get('content')
                for payment_info in payment:
                    dates.append(str(payment_info.get('date', '')))
                inv.payment_date = ', '.join(dates)

       