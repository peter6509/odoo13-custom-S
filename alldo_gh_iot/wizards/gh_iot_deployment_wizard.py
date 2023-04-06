# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
from ..utils.gh_iot_util import IOT_UTIL

class ghiotdeploymentwizard(models.TransientModel):
    _name = "alldo_gh_iot.deployment_wizard"

    equipment_ids = fields.Many2many('maintenance.equipment','main_equip_deploy_rel','wiz_id','main_id',string="節點名稱")
    source_file = fields.Char(string="來源程式檔名",required=True,default="/opt/odoo13/iotpy/")
    destination_file = fields.Char(string="目的程式檔名",required=True,default="/home/pi/cnc_mes/")
    restart_node = fields.Boolean(string="拓普後重啟節點",default=True)

    def run_deployment(self):
        for rec in self.equipment_ids:
            myip = rec.iot_ip
            IOT_UTIL.iot_push_file(myip,self.source_file,self.destination_file)
        if self.restart_node:
            for rec in self.equipment_ids:
                myip = rec.iot_ip
                IOT_UTIL.wip_reboot(myip)

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = 'IOT裝置全線已程式佈置完成並重啟動作！'
        return {
            'name': '系統通知訊息',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }