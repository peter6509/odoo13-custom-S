# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import pickle
import os,os.path
from ..utils.ipla_iot_util import IOT_UTIL


class iotmostartwizard(models.TransientModel):
    _name = "alldo_ipla_iot.iot_mo_start_wizard"

    equipment_id = fields.Many2one('maintenance.equipment',string="設備",required=True)
    emp_no = fields.Many2one('hr.employee',string="操作員",required=True)
    wkorder_id = fields.Many2one('alldo_ipla_iot.workorder',string="工單",required=True)


    def run_start_mo(self):
        myiotserverrec = self.env['alldo_ipla_iot.server_info'].search([])
        myip = self.equipment_id.iot_ip
        self.env.cr.execute("""select ipgetequipmentno('%s')""" % myip)
        mynodename = self.env.cr.fetchone()[0]
        myempcode = self.emp_no.emp_code
        myempname = self.emp_no.name
        mywkorder = self.wkorder_id.name
        iot_mo_action_array = []

        iot_mo_action_array.append({'node_name': mynodename,
                                   'empcode': myempcode,
                                   'wkorder': mywkorder,
                                    'action_type':'1',
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
        context['message'] = '機台:%s 工單:%s 人員:%s 啟動開工 ！' % (mynodename,mywkorder,myempname)
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
