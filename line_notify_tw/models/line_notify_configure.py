# -*- coding: utf-8 -*-
# Author: Jason Wu (jaronemo@msn.com)

from odoo import api, fields, models


class LineNotifyConfigure(models.Model):
    _name = 'line.notify.configure'
    _description = 'Line Configure For Line Client ID & ClientSecret'

    active = fields.Boolean(string='是否啟用', default=True)
    name = fields.Char(string='Line Notify 服務名')
    client_id = fields.Char(string='Client ID', help='請填入Line Notify註冊完成時，給予的Client ID')
    client_secret = fields.Char(string='Client Secret', help='請填入Line Notify註冊完成時，給予的Client Secret')
    redirect_url = fields.Char(string='Redirect Url', help='請填入Line Notify註冊時所填入的CallBack Url')
    notify_url = fields.Char(string='請填入Line Notify服務的網址', help='請參閱Line Notify官方文件',
                             default='https://notify-bot.line.me/oauth/authorize?')
    test_mode = fields.Boolean(string='是否為測試使用', default=False)
