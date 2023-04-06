# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request

class newebrequirepurchaseinherit(models.Model):
    _inherit = "neweb.require_purchase"

    def custom_report(self):
        puritem = []
        for item in self.require_line:
            puritem.append(
                {"pitemseq": item.pitem_seq,
                 "pitemmodeltype": item.pitem_modeltype if item.pitem_modeltype else ' ',
                 "pitemdesc": item.pitem_desc if item.pitem_desc else ' ',
                 "pitemnum": int(item.pitem_num),
                 "pitemprice": '{:,d}'.format(int(item.pitem_price)),
                 "pitembudget": '{:,d}'.format(int(item.pitem_budget)),
                 "suppliername": item.supplier.name if  item.supplier else ' ',
                 })

        totpitemsum = '{:,d}'.format(int(self.tot_pitem_sum)),

        values = {"require_line": puritem,
                  "totpitemsum":totpitemsum,
                  }
        return values

    def action_print_require_purchase(self):
        self.ensure_one()
        # base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_require_purchase_report/%s" % (bf_url,self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }

