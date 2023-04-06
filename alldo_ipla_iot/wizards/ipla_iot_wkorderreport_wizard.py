# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class iotnewwkorderreportwizard(models.TransientModel):
    _name = "alldo_ipla_iot.wkordernewreport_wizard"
    # 目前取消無用

    print_type = fields.Selection([('1','新工單列印'),('2','工單重印')],string="印表類別",required=True)
    workorder_ids = fields.Many2many('alldo_ipla_iot.workorder','alldo_workorder_newreport_rel','wkorder_id','wizard_id',string="列印工單",domain="[('state','in',['2','3','4'])]")


    def run_workorder_report(self):
        if self.print_type == '1':
            self.env.cr.execute("""select gennewwkorderreport(%d)""" % self.env.uid)
            self.env.cr.execute("""commit;""")

        else:
            self.env.cr.execute("""select genoldwkorderreport(%d,%d)""" % (self.env.uid,self.id))
            self.env.cr.execute("""commit;""")

        myrec = self.env['alldo_ipla_iot.wkorder_selectitem'].search([])
        myid=myrec[0].id
        myviewid = self.env.ref('alldo_ipla_iot.action_wkorder_select_item_view')
        return {'view_name': 'wkorder_select_item',
                'name': (u'wkordr item Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_ipla_iot.wkorder_selectitem',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'target': 'current',
                'view_id': myviewid.id,
                # 'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }