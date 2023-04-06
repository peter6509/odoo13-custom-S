# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotequipstatusbarcodewizard(models.TransientModel):
    _name = "alldo_ipla_iot.equipstatus_barcode_wizard"

    print_num = fields.Integer(string=u"列印份數",default=1)

    def run_equipstatus_barcode_print(self):
        self.env.cr.execute("""select genequipstatusbarcode(%d)""" % self.id)
        self.env.cr.execute("""commit""")

        myrec = self.env['alldo_ipla_iot.equipstatusinfo'].search([])
        myid = myrec[0].id
        myviewid = self.env.ref('alldo_ipla_iot.views_equipstatusinfo_action')
        return {'view_name': 'views_equipstatusinfo_action',
                'name': (u'equipment status info  item Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_ipla_iot.equipstatusinfo',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'target': 'current',
                'view_id': myviewid.id,
                # 'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }