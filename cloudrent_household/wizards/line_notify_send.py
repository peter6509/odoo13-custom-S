# -*- coding: utf-8 -*-
# Author: Jason Wu (jaronemo@msn.com)

from odoo import api, fields, models, _
import requests
import base64
import os

class LineNotifySend(models.TransientModel):
    _name = 'cloudrent.line_notify_send'
    _description = '使用Line Notify 發送消息等'

    messages_text = fields.Text(string='消息內容', required=True)
    messages_pic = fields.Binary(string='消息圖片')
    member_ids = fields.Many2many('cloudrent.household_member','line_notify_tw_line_send_rel','send_id','member_id',string='訊息接收者')

    # @api.multi
    def send_line_notify_messages(self):
        # 權杖，Bearer 的空白不能刪除
        for rec in self.member_ids:
            headers = {
                'Authorization': "Bearer " + rec.line_access_token,
                # 'Content-Type': "application/x-www-form-urlencoded"
                # 'Content-Type': "multipart/form-data"
            }
            messages_context = ''
            if self.messages_text:
                messages_context += '\r\n' + self.messages_text
            message_load = {'message': messages_context}
            path = os.getcwd()
            if self.messages_pic:
                with open('z.png', 'wb+') as f:
                    f.write(base64.b64decode(self.messages_pic))
                    f.close()
            # 送 File 例子
            # files = {'imageFile': open(img, 'rb')} if img else None
            # img = path + '/' + 'z.png'
            # files = {'imageFile': open(img, 'rb')} if img else None
            # r = requests.post("https://notify-api.line.me/api/notify",
            #                   headers=headers, params=message_load, files=files)
            # if files:
            #     files['imageFile'].close()
            # img = path + '/' + 'z.png'
            # files = {'imageFile': open(img, 'rb')} if img else None
            r = requests.post("https://notify-api.line.me/api/notify",
                              headers=headers, params=message_load)
            # if files:
            #     files['imageFile'].close()
            return r.status_code
