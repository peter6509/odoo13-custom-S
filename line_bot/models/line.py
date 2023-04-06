# -*- coding: utf-8 -*-

from odoo import models, fields
from linebot import LineBotApi, WebhookHandler
from linebot.models import *
from ..controller.main import check_balance


class LineRichMenu(models.Model):
    _name = 'line.rich.menu'

    name = fields.Char()
    rich_menu_id = fields.Char('Rich Menu ID')
    setting = fields.Text('Menu Setting')
    remark = fields.Char()


class LineSetting(models.Model):
    _name = 'line.setting'

    key = fields.Char(require=True)
    value = fields.Char()

    def get_value(self, key):
        line = self.search([('key', '=', key)], limit=1)
        return line.value if any(line) else ''


class LineCron(models.Model):
    _name = 'line.cron'
    _description = 'line 自動化流程'
    _auto = False

    def _init_line_api(self):
        setting = self.env['line.setting']
        line_bot_api = LineBotApi(setting.get_value('access_token'))
        return line_bot_api

    def notify_the_latest_amount_payable(self):
        # 通知最新繳費訊息
        line_bot_api = self._init_line_api()

        users = self.env['era.household_member'].search([('line_user_id', '!=', False)])
        for user in users:
            msg = check_balance(user)
            line_bot_api.push_message(
                user.line_user_id,
                TextSendMessage(text=msg)
            )
