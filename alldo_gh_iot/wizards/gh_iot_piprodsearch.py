# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class GHIotPIProdSearch(models.TransientModel):
    _name = "alldo_gh_iot.piprod_search_wizard"

    po_no = fields.Char(string="訂單號碼",required=True)

    def run_piprod_search(self):
        self.env.cr.execute("""select genpiprodanalysis('%s')""" % (self.po_no))
        self.env.cr.execute("""commit""")

        myrec = self.env['alldo_gh_iot.piprod_analysis'].search([('po_no','=',self.po_no)])

        return {'view_name': '訂單產能查詢',
                'name': ('訂單產能查詢'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'alldo_gh_iot.piprod_analysis',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'self',
                'res_id': myrec.id,
                'view_mode': 'form',
                'view_type': 'form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }
