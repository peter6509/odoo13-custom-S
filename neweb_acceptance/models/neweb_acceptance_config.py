# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebAcceptanceConfig(models.Model):
    _name = "neweb_acceptance.config"
    _description = "模組參數檔"
    _rec_name = "config_key"

    config_key = fields.Char(string="名稱",required=True)
    config_value = fields.Char(string="值",required=True)

    @api.model
    def create(self, vals):
        if 'config_key' in vals and not vals['config_key']:
            raise UserError("""名稱不能空值""")
        mycount = self.env['neweb_acceptance.config'].search_count([('config_key','=',vals['config_key'])])
        if mycount > 0 :
            raise UserError("KEY 已重複了")
        res = super(NewebAcceptanceConfig, self).create(vals)
        return res

class NewebAcceptanceAssist(models.Model):
    _name = "neweb_acceptance.assist"
    _description = "業務助理通知名單"

    sale_assist = fields.Many2one('hr.employee',string="業助")
    assist_email = fields.Char(string="Email Address")

    # @api.onchange('sale_assist')
    # def onchangeassist(self):
    #     self.assist_email = self.sale_assist.work_email

    @api.model
    def create(self, vals):
        if 'sale_assist' in vals and not vals['sale_assist']:
            raise UserError("業助欄位不能空值")
        mycount = self.env['neweb_acceptance.assist'].search_count([('sale_assist','=',vals['sale_assist'])])
        if mycount > 0:
            raise UserError("""業助已重複了""")
        res = super(NewebAcceptanceAssist, self).create(vals)

        return res

