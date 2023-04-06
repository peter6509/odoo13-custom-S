# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError, RedirectWarning
import paramiko
from ..utils.ipla_iot_util import IOT_UTIL



class iplaiotrestartwizard(models.TransientModel):
    _name = "alldo_ipla_iot.iot_restart_wizard"

    equipment_ids = fields.Many2many('maintenance.equipment','ipla_iot_restart_equipment_rel', 'wizard_id',
                                     'equipment_id', string="IOT 設備")
    passcode = fields.Char(string="執行碼", required=True)

    def run_iot_restart(self):
        if self.passcode != '!99999ibm':
            raise UserError("執行碼錯誤！")
        for rec in self.equipment_ids:
            myip = rec.iot_ip
            print(myip)
            if len(myip)>0:
                myres = IOT_UTIL.check_iot(myip)
                if myres:
                    IOT_UTIL.wip_reboot(myip)

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='IOT裝置已重啟動作！'
        return {
            'name':'系統通知訊息',
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'sh.message.wizard',
            'views':[(view.id,'form')],
            'view_id':view.id,
            'target':'new',
            'context':context,
            }


    def run_all_restart(self):
        if self.passcode != '!99999ibm':
            raise UserError("執行碼錯誤！")
        myrec = self.env['maintenance.equipment'].search([])
        for rec in myrec:
            myip = rec.iot_ip
            print(myip)
            if len(myip) > 0 :
                myres = IOT_UTIL.check_iot(myip)
                if myres:
                    IOT_UTIL.wip_reboot(myip)

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='IOT裝置全線已重啟動作！'
        return {
            'name':'系統通知訊息',
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'sh.message.wizard',
            'views':[(view.id,'form')],
            'view_id':view.id,
            'target':'new',
            'context':context,
            }


