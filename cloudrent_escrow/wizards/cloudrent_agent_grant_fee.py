# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request

class CloudRentAgentGrantFee(models.TransientModel):
    _name = "cloudrent.agent_grant_fee"
    _description ="業者服務/補助費用申請書"

    grant_year = fields.Char(string="民國年",required=True)
    grant_month = fields.Char(string="月份",required=True)

    def run_agent_grant_fee(self):
        myescrowid = self.env.user.escrow_no.id
        if myescrowid:
            self.env.cr.execute("""select gen_agent_grantfee(%d,'%s','%s')""")
            myrec = self.env['cloudrent.agent_grant_fee_list'].search([])
            bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
            url = "%s/report/odt_to_x/agent_applyfor_grant_fee/%s" % (bf_url, self.id)
            return {'name': 'Go to website',
                    'res_model': 'ir.actions.act_url',
                    'type': 'ir.actions.act_url',
                    'target': 'new',
                    'url': url
                    }
