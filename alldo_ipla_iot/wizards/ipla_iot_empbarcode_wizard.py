# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotempbarcodewizard(models.TransientModel):
    _name = "alldo_ipla_iot.empbarcode_wizard"

    emp_ids = fields.Many2many('hr.employee','alldo_ipla_iot_empbarcode_rel','wizard_id','emp_id')

    def run_empbarcode_print(self):
        self.env.cr.execute("""select genempbarcode(%d)""" % self.id)
        self.env.cr.execute("""commit""")

        myrec = self.env['alldo_ipla_iot.empinfo'].search([])
        myid = myrec[0].id
        myviewid = self.env.ref('alldo_ipla_iot.views_empinfo_action')
        return {'view_name': 'views_empinfo_action',
                'name': (u'employee info  item Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_ipla_iot.empinfo',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'target': 'current',
                'view_id': myviewid.id,
                # 'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }