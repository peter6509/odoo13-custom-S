# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotempbarcodewizard(models.TransientModel):
    _name = "alldo_gh_iot.empbarcode_wizard"

    emp_ids = fields.Many2many('hr.employee','alldo_gh_iot_empbarcode_rel','wizard_id','emp_id')

    def run_empbarcode_print(self):
        self.env.cr.execute("""select genempbarcode(%d)""" % self.id)
        self.env.cr.execute("""commit""")

        myrec = self.env['alldo_gh_iot.empinfo'].search([])
        myid = myrec[0].id
        myviewid = self.env.ref('alldo_gh_iot.views_empinfo_action')
        return {'view_name': 'views_empinfo_action',
                'name': (u'employee info  item Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_gh_iot.empinfo',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'target': 'current',
                'view_id': myviewid.id,
                # 'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }