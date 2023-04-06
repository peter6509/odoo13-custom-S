# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request

class newebexpensereport(models.Model):
    _inherit = "neweb_sale_analysis.expense_report"

    def action_print_expense(self):
        self.ensure_one()
        # base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_expense_report/%s" % (bf_url,self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }
