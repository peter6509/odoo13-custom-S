# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request
import pytz

class newebinvoiceopenreport(models.Model):
    _inherit = "neweb_invoice.invoiceopen"

    def custom_report(self):
        obj_precision = self.env['decimal.precision']
        prec=obj_precision.precision_get('Neweb Price')
        lang=self._context.get('lang')
        record_lang=self.env['res.lang'].search([('code','=',lang)],limit=1)
        strftime_format="%s %s" % (record_lang.date_format,record_lang.time_format)
        user_tz = pytz.timezone(self.env.get('tz') or self.env.user.tz or 'UTC')
        mainstart=' '
        mainend = ' '
        if self.contract_main_start:
            mainstart = self.contract_main_start
        if self.contract_main_end:
            mainend = self.contract_main_end
        lines=[]
        for item in self.invoice_open_lines:
            if item.invoice_costtype:
                myinvoicecosttype = item.invoice_costtype.name
            else:
                myinvoicecosttype = ' '
            lines.append(
                {"costtypename" : myinvoicecosttype,
                 })
        if not self.project_no :
            myprojectno = ' '
        else:
            myprojectno = self.project_no.name
        if not self.contract_no :
            mycontractno = ' '
        else:
            mycontractno = self.contract_no.name
        if not self.invoice_contact1 :
            myinvoicecontact1=' '
        else:
            myinvoicecontact1 = self.invoice_contact1.name

        values = {"invoice_open_lines": lines,
                  "myprojectno": myprojectno,
                  "mycontractno": mycontractno,
                  "mainstart": mainstart,
                  "mainend": mainend,
                  "myinvoicecontact1": myinvoicecontact1,
                 }
        return values

    def action_print_invoiceopen(self):
        self.ensure_one()
        # base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_invoiceopen_report/%s" % (bf_url,self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }
