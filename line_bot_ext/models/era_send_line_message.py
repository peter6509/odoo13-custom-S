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


# def init_line_bot():
#     global line_bot_api, handler
#     # 若是chanel_secret 不存在則更新
#     if not handler.parser.signature_validator.channel_secret:
#         line_bot_api.__init__(params('access_token'))
#         handler.parser = WebhookParser(params('channel_secret'))


def params(key):
    return request.env['line.setting'].sudo().get_value(key)

class ERASendLineMessage(models.Model):
    _name = "era.send_line_message"
    _description = "ERA發送公告通知執行表"
    _order = "send_date desc,project_no,member_id"

    @api.depends('member_id','send_message_type','message_text')
    def _get_bill_message(self):
        for rec in self:
            if rec.send_message_type == '2':
                msg = rec.push_ar_message(rec.member_id)
            elif rec.send_message_type == '3':
                msg = rec.push_overdue_message(rec.member_id)
            else:
                msg = ' '
            rec.bill_message=msg

    send_date = fields.Date(string="發送日期")
    project_no = fields.Many2one('era.household_house',string="案場")
    line_user_id = fields.Char(string='Line User ID')
    member_id = fields.Many2one('era.household_member',string="租戶")
    send_status = fields.Boolean(string="已發送?",default=False)
    send_message_type = fields.Selection([('1','訊息通吿'),('2','帳單通知'),('3','逾期催繳')],string="訊息類型",default='1')
    message_text = fields.Text(string="訊息內容")
    bill_message = fields.Text(string="帳單訊息",compute=_get_bill_message)
    active = fields.Boolean(string="ARCHIVE",default=True)
    can_do = fields.Boolean(string="是否可以執行", default=False)

    def name_get(self):
        result = []
        for myrec in self:
            if myrec.send_message_type=='1':
                msgtype='訊息通吿'
            elif myrec.send_message_type=='2':
                msgtype='帳單通知'
            else:
                msgtype='逾期催繳'
            myname = "[%s]%s-%s" % (msgtype, myrec.project_no.project_no,myrec.member_id.member_name)
            result.append((myrec.id, myname))
        return result

    def check_balance(self,memberid):
        user = self.env['era.household_member'].search([('id','=',memberid.id)])
        amount = [
            user.period_start if user.period_start else ' ',
            user.period_end if user.period_end else ' ',
            user.now_ym if user.now_ym else ' ',
            user.period_subtot if user.period_subtot else 0,
            user.period_totrent if user.period_totrent else 0,
            user.period_totrentpay if user.period_totrentpay else 0,
            user.now_totrent_balance if user.now_totrent_balance else 0,
            user.period_totscale if user.period_totscale else 0,
            user.period_totscalepay if user.period_totscalepay else 0,
            user.now_totscalebalance if user.now_totscalebalance else 0,
            user.now_totbalance if user.now_totbalance else 0,

        ]

        msg = f'起租日: {amount[0]:}\n' \
              f'退租日: {amount[1]:}\n' \
              f'目前應結帳年月: {amount[2]:}\n' \
              f'每月固定租金/管理費: {amount[3]:,}\n' \
              f'合計應繳房租/管理費總金額: {amount[4]:,}\n' \
              f'合計已繳房租/管理費總金額: {amount[5]:,}\n' \
              f'結算房租/管理費應繳餘額: {amount[6]:,}\n' \
              f'合計應繳總電費: {amount[7]:,}\n' \
              f'合計已繳總電費: {amount[8]:,}\n' \
              f'結算電費應繳餘額: {amount[9]:,}\n' \
              f'結算總應繳餘額: {amount[10]:,}\n' \
              f'如有任何疑問，請洽詢管理員。'
        return msg

    def push_ar_message(self,memberid):
        user = self.env['era.household_member'].search([('id', '=', memberid.id)])
        amount = [
            user.period_start if user.period_start else ' ',
            user.period_end if user.period_end else ' ',
            user.now_ym if user.now_ym else ' ',
            user.period_subtot if user.period_subtot else 0,
            user.period_totrent if user.period_totrent else 0,
            user.period_totrentpay if user.period_totrentpay else 0,
            user.now_totrent_balance if user.now_totrent_balance else 0,
            user.period_totscale if user.period_totscale else 0,
            user.period_totscalepay if user.period_totscalepay else 0,
            user.now_totscalebalance if user.now_totscalebalance else 0,
            user.now_totbalance if user.now_totbalance else 0,
            user.ar_date if user.ar_date else ' ',
        ]

        msg = f'應繳房租日期:{amount[11]:}\n' \
              f'每月固定租金/管理費: {amount[3]:,}\n' \
              f'結算房租/管理費應繳餘額: {amount[6]:,}\n' \
              f'結算電費應繳餘額: {amount[9]:,}\n' \
              f'結算總應繳餘額: {amount[10]:,}\n' \
              f'本次應繳交房租及管理費的通知訊息。'
        return msg

    def push_overdue_message(self,memberid):
        user = self.env['era.household_member'].search([('id', '=', memberid.id)])
        amount = [
            user.period_start if user.period_start else ' ',
            user.period_end if user.period_end else ' ',
            user.now_ym if user.now_ym else ' ',
            user.period_subtot if user.period_subtot else 0,
            user.period_totrent if user.period_totrent else 0,
            user.period_totrentpay if user.period_totrentpay else 0,
            user.now_totrent_balance if user.now_totrent_balance else 0,
            user.period_totscale if user.period_totscale else 0,
            user.period_totscalepay if user.period_totscalepay else 0,
            user.now_totscalebalance if user.now_totscalebalance else 0,
            user.now_totbalance if user.now_totbalance else 0,
            user.ar_date if user.ar_date else ' ',
        ]

        msg = f'應繳房租日期:{amount[11]:}\n' \
              f'每月固定租金/管理費: {amount[3]:,}\n' \
              f'結算房租/管理費應繳餘額: {amount[6]:,}\n' \
              f'結算電費應繳餘額: {amount[9]:,}\n' \
              f'結算總應繳餘額: {amount[10]:,}\n' \
              f'已逾期超過一個月未繳交房租，請儘快繳交房租及管理費。'
        return msg

    def run_send_line_message(self):  # 每10分鐘 cron job 將 到發送日期 LINE MESSAGE 執行發送
        line_bot_api = LineBotApi('ulVWnHVhjhOGnFlegOqClzM9ta6bHOdjv97jokpxutZWNhNZmSE6DA30wXmor7IsBio7ylRAQqWJYgEACq2FBliC1ab1CQCFe3Cn+om+S9S9R014Qf/ShGDVTrK5tJwy+EJRo6WIaBYvoZnApD7VgAdB04t89/1O/w1cDnyilFU=')
        self.env.cr.execute("""select ckcando()""")
        self.env.cr.execute("""commit""")
        myrec = self.env['era.send_line_message'].sudo().search([('send_status', '=', False),('can_do','=',True),('line_user_id','!=',False)])
        for rec in myrec:
            if rec.send_message_type == '1':  # 訊息通吿
                line_bot_api.push_message(rec.line_user_id, TextSendMessage(text="%s" % rec.message_text))
            if rec.send_message_type == '2':  # 帳單通知
                line_bot_api.push_message(rec.line_user_id, TextSendMessage(text="%s" % rec.bill_message))
            if rec.send_message_type == '3':  # 逾期催繳
                line_bot_api.push_message(rec.line_user_id, TextSendMessage(text="%s"))
            rec.sudo().write({'send_status': True})


    def run_archive_message(self):   # 每天 cron job 將七天以前已送LINE之MESSAGE ARCHIVE
        self.env.cr.execute("""select genlinemsgarchive();""")
        self.env.cr.execute("""commit""")

    def run_member_account_message(self): # 每天 cron job 將三天以內租戶起租日到期發送 LINE帳單 寫 ar_date
        self.env.cr.execute("""select genaccbillmsg()""")
        self.env.cr.execute("""commit""")




