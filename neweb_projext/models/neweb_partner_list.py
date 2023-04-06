# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class newebpartnerlist(models.Model):
    _name = "neweb.partner_list"

    cus_name = fields.Char(string="客戶名稱")
    vat = fields.Char(string="統編")
    tel = fields.Char(string="電話")
    address = fields.Char(string="地址")
    contact = fields.Char(string="聯絡人")
    contact_type = fields.Many2one('neweb.contacttype',string="人員別")
    function = fields.Char(string="職稱")
    tel1 = fields.Char(string="聯絡人電話")
    mobile = fields.Char(string="手機")
    email = fields.Char(string="EMAIL")
    birthday = fields.Char(string="生日")
    comment = fields.Text(string="MEMO")
    sales = fields.Char(string="業務代表")
    payment_days = fields.Integer(string="付款天數",default=0)