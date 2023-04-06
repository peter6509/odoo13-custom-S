# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import mysql.connector
from mysql.connector import Error

class connmysqlwizard(models.TransientModel):
    _name = "era_household.conn_mysql_wizard"

    passcode = fields.Char(string="PASSWORD",required=True)
    conn_status = fields.Text(string="STATUS")

    def conn_mysql(self):
        import mysql.connector
        if self.passcode=='!99999ibm':
            mydb = mysql.connector.connect(host="localhost", user="yhdai77", passwd="@Dmt63611570", database="energy")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT count(*) from device_now_v2 ;")
            myrec = mycursor.fetchone()[0]
            if myrec > 0 :
                view = self.env.ref('sh_message.sh_message_wizard')
                view_id = view and view.id or False
                context = dict(self._context or {})
                context['message'] = 'IOT Mysql 連線OK！'
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
            else:
                view = self.env.ref('sh_message.sh_message_wizard')
                view_id = view and view.id or False
                context = dict(self._context or {})
                context['message'] = 'IOT Mysql 連線 Fail！'
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
        else:
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'PASSCODE 錯誤'
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