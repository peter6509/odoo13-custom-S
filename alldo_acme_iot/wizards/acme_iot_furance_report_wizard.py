# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmeiotfurancereportwizard(models.TransientModel):
    _name = "alldo_acme_iot.furance_report_wizard"

    report_user = fields.Many2one('res.users',string="製表人",default = lambda self:self.env.uid)

    def run_furance_print(self):
        myrec = self.env['alldo_acme_iot.furance_report'].search([])
        myid = myrec[0].id
        # myviewid = self.env.ref('alldo_acme_iot.acme_iot_furance_tree')
        return {'view_name': 'views_furance_action',
                'name': (u'Furance Data'),
                'views': [[False, 'tree'],[False, 'form']],
                'res_model': 'alldo_acme_iot.furance_report',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'domain': [(1,'=',1)],
                # 'res_id': myid,
                'target': 'current',
                # 'view_id': myviewid.id,
                # 'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }