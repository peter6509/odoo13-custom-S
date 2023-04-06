# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import logging
import re
from datetime import datetime as dt

from linebot import LineBotApi, WebhookHandler, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from odoo.http import request, route, Controller, Response
from odoo.modules.module import get_module_resource

def params(key):
    return request.env['line.setting'].sudo().get_value(key)

class ERASendMessageWizard(models.TransientModel):
    _name = "era.manual_send_line_message"
    _description = "手動發布通知訊息精靈"

    project_no = fields.Many2one('era.household_house', string="案場", required=True)
    member_id = fields.Many2many('era.household_member', 'era_manual_line_member_rel', 'message_id','member_id', string="租戶")
    msg_text = fields.Text(string="通吿內容", required=True)
    send_status = fields.Selection([('1', '立即傳送'), ('2', '排程傳送')], string="模式", default='1')
    send_date = fields.Date(string="LINE發送日期", required=True, default=lambda self: fields.Date.today())

    @api.onchange('project_no')
    def onchangeprojectno(self):
        myrec = self.env['era.household_member'].search([('house_id.house_id','=',self.project_no.id)])
        myids = []
        for rec in myrec:
            myids.append(rec.id)
        return {'domain': {'member_id': [('id', 'in', myids)]}}


    def run_message_send(self):
        self.env.cr.execute("""select gensendmessage(%d,%d,'%s','%s')""" % (self.project_no.id,self.id,self.send_date,self.msg_text))
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select ckcando()""")
        self.env.cr.execute("""commit""")
        if self.send_status=='1':
            line_bot_api = LineBotApi('ulVWnHVhjhOGnFlegOqClzM9ta6bHOdjv97jokpxutZWNhNZmSE6DA30wXmor7IsBio7ylRAQqWJYgEACq2FBliC1ab1CQCFe3Cn+om+S9S9R014Qf/ShGDVTrK5tJwy+EJRo6WIaBYvoZnApD7VgAdB04t89/1O/w1cDnyilFU=')
            myrec = self.env['era.send_line_message'].sudo().search([('send_status', '=', False),('can_do','=',True),('line_user_id','!=',False)])
            for rec in myrec:
                if rec.send_message_type == '1':  # 訊息通吿
                    line_bot_api.push_message(rec.line_user_id, TextSendMessage(text="%s" % rec.message_text))
                if rec.send_message_type == '2':  # 帳單通知
                    line_bot_api.push_message(rec.line_user_id, TextSendMessage(text="%s" % rec.bill_message))
                if rec.send_message_type == '3':  # 逾期催繳
                    line_bot_api.push_message(rec.line_user_id, TextSendMessage(text="%s"))
                rec.sudo().write({'send_status': True})
            context = dict(self._context or {})
            context['message'] = 'LINE 訊息已傳送到伺服主機,LINE訊息已發送！'
        else:
            context = dict(self._context or {})
            context['message'] = 'LINE 訊息已傳送到伺服主機,等候排程發送！'
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        return {
            'name':'Success',
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'sh.message.wizard',
            'views':[(view.id,'form')],
            'view_id':view.id,
            'target':'new',
            'context':context,
            }




