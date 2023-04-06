# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import pickle
import os,os.path
from ..utils.gh_iot_util import IOT_UTIL


class iotinitpicklewizard(models.TransientModel):
    _name = "alldo_gh_iot.iot_init_pickle_wizard"


    iot_server = fields.Many2one('alldo_gh_iot.server_info',string="IOT伺服器",required=True)
    equipment_ids = fields.Many2many('maintenance.equipment', 'gh_iot_init_pickle_rel', 'wizard_id',
                                     'equipment_id', string="IOT 設備")
    passcode = fields.Char(string="執行碼", required=True)



    def run_iot_init_pickle(self):
        if self.passcode != '!99999ibm':
            raise UserError("執行碼錯誤！")
        myiotserverrec = self.env['alldo_gh_iot.server_info'].search([('id','=',self.iot_server.id)])




        for rec in self.equipment_ids:

            myip = rec.iot_ip
            self.env.cr.execute("""select ipgetequipmentno('%s')""" % myip)
            mynodename = self.env.cr.fetchone()[0]
            iot_server_array = []
            if myiotserverrec:
                iot_server_array.append({'iot_server_name': myiotserverrec.iot_server_name,
                                         'iot_server_ip': myiotserverrec.iot_server_ip,
                                         'iot_db_name': myiotserverrec.iot_db_name,
                                         'iot_db_username': myiotserverrec.iot_db_username,
                                         'iot_db_passwd': myiotserverrec.iot_db_passwd,
                                         'iot_node_name': mynodename
                                         })
            else:
                iot_server_array.append({'iot_server_name': ' ',
                                         'iot_server_ip': ' ',
                                         'iot_db_name': ' ',
                                         'iot_db_username': ' ',
                                         'iot_db_passwd': ' ',
                                         'iot_node_name': mynodename
                                         })

            if myiotserverrec.server_path[-1:] != '/':
                mylocalfile = myiotserverrec.server_path + '/iot_server_info.pickle'
            else:
                mylocalfile = myiotserverrec.server_path + 'iot_server_info.pickle'
            with open(mylocalfile, 'wb') as iot_server_info:
                pickle.dump(iot_server_array, iot_server_info)
            iot_server_info.close()
            # mylocalfile= '/Users/odoo/alldo_config/iot_server_info.pickle'
            if myiotserverrec.client_path[-1:] != '/':
                myremotefile =  myiotserverrec.client_path + '/iot_server_info.pickle'
            else:
                myremotefile = myiotserverrec.client_path + 'iot_server_info.pickle'
            IOT_UTIL.iot_push_file(myip,mylocalfile,myremotefile)

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='IOT裝置啟動設定主機資訊運作！'
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

    def run_all_iot_init_pickle(self):
        if self.passcode != '!99999ibm':
            raise UserError("執行碼錯誤！")
        myiotserverrec = self.env['alldo_gh_iot.server_info'].search([('id', '=', self.iot_server.id)])


        if myiotserverrec.server_path[-1:] != '/':
            mylocalfile = myiotserverrec.server_path + '/iot_server_info.pickle'
        else:
            mylocalfile = myiotserverrec.server_path + 'iot_server_info.pickle'

        if myiotserverrec.client_path[-1:] != '/':
            myremotefile = myiotserverrec.client_path + '/iot_server_info.pickle'
        else:
            myremotefile = myiotserverrec.client_path + 'iot_server_info.pickle'

        myrec = self.env['maintenance.equipment'].search([])
        for rec in myrec:
            myip = rec.iot_ip
            self.env.cr.execute("""select ipgetequipmentno('%s')""" % myip)
            mynodename = self.env.cr.fetchone()[0]
            iot_server_array = []
            if myiotserverrec:
                iot_server_array.append({'iot_server_name': myiotserverrec.iot_server_name,
                                         'iot_server_ip': myiotserverrec.iot_server_ip,
                                         'iot_db_name': myiotserverrec.iot_db_name,
                                         'iot_db_username': myiotserverrec.iot_db_username,
                                         'iot_db_passwd': myiotserverrec.iot_db_passwd,
                                         'iot_node_name': mynodename
                                         })
            else:
                iot_server_array.append({'iot_server_name': ' ',
                                         'iot_server_ip': ' ',
                                         'iot_db_name': ' ',
                                         'iot_db_username': ' ',
                                         'iot_db_passwd': ' ',
                                         'iot_node_name': ' '
                                         })
            with open(mylocalfile, 'wb') as iot_server_info:
                pickle.dump(iot_server_array, iot_server_info)
            iot_server_info.close()

            IOT_UTIL.iot_push_file(myip, mylocalfile, myremotefile)

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
