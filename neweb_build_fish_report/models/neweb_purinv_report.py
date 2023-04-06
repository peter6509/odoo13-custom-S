# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request
import pytz

class newebpurinvreport(models.Model):
    _inherit = "neweb_purinv.invoice"


    def action_purinv_print(self):
        self.ensure_one()
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_purinv_report/%s" % (bf_url,self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }



class newebpurinvlinereport(models.Model):
    _inherit = "neweb_purinv.invoiceline"

    @api.depends('invoice_partner')
    def _get_sname(self):
        for rec in self:
            if not rec.invoice_partner:
                mysname = ' '
            else:
                mysname = rec.invoice_partner.comp_sname
            rec.compsname = mysname
            return mysname

    compsname = fields.Char(string="廠商簡稱", compute=_get_sname)


