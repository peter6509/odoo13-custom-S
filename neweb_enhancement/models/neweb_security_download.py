# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class newebsecuritydownload(models.Model):
    _name = "neweb_enhancement.security_download"
    _order = "create_date desc"
    _description = "使用者權限表 Excel Download"

    xls_file = fields.Binary(string='下載檔案',attachment=False)
    xls_file_name = fields.Char(string='檔案說明')



class newebsecuritycategory(models.Model):
    _name = "neweb_enhancement.security_category"
    _order = "seq"

    category_name = fields.Char(string="Category Name")
    category_id = fields.Integer(string="Category ID")
    group_id = fields.Integer(string="Group ID")
    group_name = fields.Char(string="Group Name")
    seq = fields.Integer(string="Sequence")



class newebsecuritygroup(models.Model):
    _name = "neweb_enhancement.security_group"
    _order = "user_id,group_id"

    login = fields.Char(string="login")
    group_id = fields.Integer(string="Group ID")
    user_id = fields.Integer(string="User ID")
    partner_id = fields.Integer(string="Partner ID")
    category_name = fields.Char(string="Category Name")
    group_name = fields.Char(string="Group Name")
    emp_name = fields.Char(string="Emp Name")
    seq = fields.Integer(string="Sequence")


class newebsalepurchaseaccount(models.Model):
    _name = "neweb_enhancement.sale_purchase_account"

    sale_id = fields.Many2one('account.account',string="應收科目")
    purchase_id = fields.Many2one('account.account',string="應付科目")

    @api.model
    def create(self, vals):
        mycount = self.env['neweb_enhancement.sale_purchase_account'].search_count([])
        if mycount > 0 :
            raise UserError("只能存在一筆記錄")
        res = super(newebsalepurchaseaccount, self).create(vals)
        return res
