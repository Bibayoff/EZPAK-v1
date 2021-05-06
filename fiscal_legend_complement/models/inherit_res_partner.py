# -*- encoding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
   _inherit = 'res.partner'

   has_addenda_fiscal_legend = fields.Boolean(
       string="Has Fiscal Legend Addenda?"
   )
