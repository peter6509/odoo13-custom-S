# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class AlldoGhIotProofing(models.Model):
    _name = "alldo_gh_iot.proofing"
    _description = "客戶打樣記錄"

    name = fields.Char(string="打樣號碼", default=lambda self: _('New'), copy=False, required=True, readonly=True)
    proofing_sdate = fields.Date(string="起始日")
    proofing_edate = fields.Date(string="截止日")
    partner_id = fields.Many2one('res.partner',string="客戶")
    product_id = fields.Many2one('product.product',string="產品")
    product_no = fields.Char(string="品名規格")
    is_order = fields.Boolean(string="是否接獲訂單?",default=False)
    proofing_num = fields.Integer(string="數量")
    proofing_desc = fields.Text(string="打樣說明")
    proofing_man = fields.Many2one('hr.employee',string="作業人員")
    proofing_attach = fields.Many2many('ir.attachment',string="打樣文件夾檔",attachment="false")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('alldo_gh_iot.proofing') or _('New')
        res = super(AlldoGhIotProofing, self).create(vals)
        return res
