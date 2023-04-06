# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebInvoiceIhherit(models.Model):
    _inherit = "neweb_invoice.invoiceopen"

    @api.depends('project_no')
    def _get_mix(self):
        for rec in self:
            self.env.cr.execute("""select getcosttypemix(%d)""" % rec.project_no.id)
            rec.is_mix = self.env.cr.fetchone()[0]


    acc_sale_close = fields.Boolean(string="銷貨存貨已結",default=False)
    is_mix = fields.Boolean(string="混合案",compute=_get_mix)
