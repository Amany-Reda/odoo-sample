from odoo import api, fields, models

PROCUREMENT_PRIORITIES = [('0', 'Normal'), ('1', 'Urgent')]
class SaleOrder(models.Model):
        _inherit = "sale.order"

        driver = fields.Many2one('hr.employee' , string="Driver", store=True, readonly=False, tracking=True , required=True)
        previos_balance = fields.Float(string="Previos Balance", related='partner_id.payment_amount_due', store=False, readonly=True)
        current_balance = fields.Float(string="Current Balance", related='partner_id.payment_amount_due', store=False, readonly=True)

       