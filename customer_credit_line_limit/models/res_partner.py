from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    credit_limit = fields.Float()
    spent_credit_limit = fields.Float(compute="_get_spent_credit_limit")
    set_sales_limit = fields.Boolean()

    @api.depends("credit_limit")
    def _get_spent_credit_limit(self):
        for partner in self:
            partner.spent_credit_limit = partner._get_spent_credit(partner)

    def _get_spent_credit(self, partner):
        orders = self.env['sale.order'].search([('partner_id', '=', partner.id), ('invoice_status', '!=', 'invoiced')]).mapped('amount_total')
        total = 0
        for order in orders:
            total += order
        return total