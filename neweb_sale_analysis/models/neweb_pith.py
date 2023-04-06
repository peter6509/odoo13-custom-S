# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api,_
from odoo import exceptions
import datetime


class newebpith(models.Model):
    _name = "neweb_sale_analysis.pith"
    _description = "用印申請單"

    name = fields.Char(string="編號")
    customer = fields.Many2one('res.partner',string="客戶名稱")
    project = fields.Char(string="專案名稱")
    app_human = fields.Many2one('res.users', string="申請人")
    doc_date = fields.Date(string="日期")
    doc_date_y = fields.Char(string="年")
    doc_date_m = fields.Char(string="月")
    doc_date_d = fields.Char(string="日")
    b_stamp = fields.Boolean(string="大小章",default=False)
    s_stamp = fields.Boolean(string="印鑑章",default=False)
    i_stamp = fields.Boolean(string="發票章",default=False)
    o_stamp = fields.Boolean(string="橢圓章",default=False)

