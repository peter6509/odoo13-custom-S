# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError
import pickle
import os, os.path
from ..utils.ipla_iot_util import IOT_UTIL


class iotmostopwizard(models.TransientModel):
    _name = "alldo_ipla_iot.iot_mo_stop_wizard"
    _description = "IOT裝置主控變更動作精靈"

    equipment_ids = fields.Many2many('maintenance.equipment', 'ipla_iot_mo_stop_rel', 'wizard_id','equipment_id', string="機台",required=True)
    action_type = fields.Selection([('1','暫停後重啟'),('2','暫停'),('3','停機')],string="執行類別",required=True)

    def run_action_iot(self):
        myiotserverrec = self.env['alldo_ipla_iot.server_info'].search([])
        for rec in self.equipment_ids:
            myip = rec.equipment_id.iot_ip
            self.env.cr.execute("""select ipgetequipmentno('%s')""" % myip)
            mynodename = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select getlastinfo(%d)""" % rec.equipment_id.id)
            mylastinfo = self.env.cr.fetchone()[0]
            myindex = mylastinfo.find('-')
            myempcode = mylastinfo[myindex+1:]
            mywkorder = mylastinfo[0:myindex]

            iot_mo_action_array = []

            iot_mo_action_array.append({'node_name': mynodename,
                                        'empcode': myempcode,
                                        'wkorder': mywkorder,
                                        'action_type': self.action_type,
                                        })

            if myiotserverrec[0].server_path[-1:] != '/':
                mylocalfile = myiotserverrec.server_path + '/iot_mo_action.pickle'
            else:
                mylocalfile = myiotserverrec.server_path + 'iot_mo_action.pickle'

            with open(mylocalfile, 'wb') as iot_mo_action:
                pickle.dump(iot_mo_action_array, iot_mo_action)
            iot_mo_action.close()
            # mylocalfile = '/Users/odoo/alldo_config/iot_mo_action.pickle'
            if myiotserverrec[0].client_path[-1:] != '/':
                myremotefile = myiotserverrec.client_path + '/iot_mo_action.pickle'
            else:
                myremotefile = myiotserverrec.client_path + 'iot_mo_action.pickle'
            IOT_UTIL.iot_push_file(myip, mylocalfile, myremotefile)

            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = '機台已變更動作 ！'
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

