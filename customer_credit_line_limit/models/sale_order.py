from odoo import models, fields, api,_
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        if self.partner_id.set_sales_limit:
            total_credit_limit = self.env['res.partner']._get_spent_credit(self.partner_id)
            credit_limit = self.partner_id.credit_limit
            if (total_credit_limit >= credit_limit):
                raise ValidationError(_('You have exceeded the sales limit with this customer'))
        return super(SaleOrder, self).action_confirm()

