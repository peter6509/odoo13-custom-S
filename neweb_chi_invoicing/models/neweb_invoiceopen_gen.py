# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebinvoiceopengen(models.Model):
    _inherit = "neweb_invoice.invoiceopen"

    is_gen = fields.Boolean(string="產出銷項資料", default=False)
    gen_date = fields.Date(string="銷項產出日期")
    gen_man = fields.Many2one('hr.employee', string="銷項產出人員")


    def write(self, vals):
        if 'is_gen' in vals and vals['is_gen']:
            self.env.cr.execute("""select getexportempid(%d)""" % self.env.user.id)
            vals['gen_man'] = self.env.cr.fetchone()[0]
        res = super(newebinvoiceopengen, self).write(vals)
        return res


class newebinvoiceopengenline(models.Model):
    _inherit = "neweb_invoice.invoiceopen_line"

    receive_date = fields.Date(string="預計收款日")
    receive_date1 = fields.Date(string="實際收款日")
    is_main_gen = fields.Boolean(string="拋出維護資訊")
    is_main_completed = fields.Boolean(string="維護已拋過",default=False)
    sales_no = fields.Char(string="單據號碼")

    @api.model
    def create(self, vals):
        if (vals['invoice_state'] == '2' or vals['invoice_state'] == '3') and not vals['receive_date']:
            raise UserError("""發票開立 生效及驗收狀態,預計收款日不能空白！""")
        res = super(newebinvoiceopengenline, self).create(vals)
        return res

    def write(self, vals):
        res = super(newebinvoiceopengenline, self).write(vals)
        for rec in self:
            if (rec.invoice_state == '2' or rec.invoice_state == '3') and not rec.receive_date:
                raise UserError("""發票開立 生效及驗收狀態,預計收款日不能空白！""")
        return res
