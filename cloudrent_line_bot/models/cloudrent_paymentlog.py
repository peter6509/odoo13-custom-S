# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class CloudRentPaymentLog(models.Model):
    _name = "cloudrent.paymentlog"
    _description = "CloudRent Line Payment Log"
    _order = "date desc"

    line_id = fields.Char(string="LINE ID")
    member_id = fields.Many2one('cloudrent.household_member',string="人員",ondelete='cascade')
    member_type = fields.Selection([('1', '物業'), ('2', '房東'), ('3', '房客'), ('4', '供應商')], string="人員屬性")
    date = fields.Datetime(string="日期時間")
    content_text = fields.Text(string="訊息內容")
    content_img = fields.Binary(string="照片",attachment=False)
    status = fields.Selection([('1', '未讀'), ('2', '已讀'), ('3', '已處理')], string="訊息狀態", default='1')