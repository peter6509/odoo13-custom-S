# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api, _
from odoo.exceptions import UserError

class stockngreturndata(models.Model):
    _name = "alldo_acme_iot.ngreturn_report"

    partner_id = fields.Many2one('res.partner',string="客戶")
    name = fields.Char(string="退料單號",default=lambda self: _('New'))
    report_date = fields.Date(string="製表日期")
    report_line = fields.One2many('alldo_acme_iot.ngreturn_report_line','rep_id',copy=False)
    report_memo = fields.Char(string="備註")


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('alldo_acme_iot.return_ng') or _('New')
        res = super(stockngreturndata, self).create(vals)
        return res


class stockngreturnline(models.Model):
    _name = "alldo_acme_iot.ngreturn_report_line"

    rep_id = fields.Many2one('alldo_acme_iot.ngreturn_report',ondelete='cascade')
    item = fields.Integer(string="ITEM")
    prod_no = fields.Many2one('product.product',string="料號")
    m_ng_num = fields.Float(digits=(6,0),string="材料不良數量")
    p_ng_num = fields.Float(digits=(6,0),string="加工不良數量")
    prod_uom = fields.Char(string="單位",default='PCS')
    line_memo = fields.Char(string="說明")
    item1 = fields.Integer(string="ITEM1")
    prod_no1 = fields.Many2one('product.product',string="料號1")
    m_ng_num1 = fields.Float(digits=(6, 0), string="材料不良數量1")
    p_ng_num1 = fields.Float(digits=(6, 0), string="加工不良數量1")
    prod_uom1 = fields.Char(string="單位1", default='PCS')
    line_memo1 = fields.Char(string="說明1")
    item2 = fields.Integer(string="ITEM2")
    prod_no2 = fields.Many2one('product.product',string="料號2")
    m_ng_num2 = fields.Float(digits=(6, 0), string="材料不良數量2")
    p_ng_num2 = fields.Float(digits=(6, 0), string="加工不良數量2")
    prod_uom2 = fields.Char(string="單位2", default='PCS')
    line_memo2 = fields.Char(string="說明2")
    item3 = fields.Integer(string="ITEM3")
    prod_no3 = fields.Many2one('product.product',string="料號3")
    m_ng_num3 = fields.Float(digits=(6, 0), string="材料不良數量3")
    p_ng_num3 = fields.Float(digits=(6, 0), string="加工不良數量3")
    prod_uom3 = fields.Char(string="單位3", default='PCS')
    line_memo3 = fields.Char(string="說明3")
    item4 = fields.Integer(string="ITEM4")
    prod_no4 = fields.Many2one('product.product',string="料號4")
    m_ng_num4 = fields.Float(digits=(6, 0), string="材料不良數量4")
    p_ng_num4 = fields.Float(digits=(6, 0), string="加工不良數量4")
    prod_uom4 = fields.Char(string="單位4", default='PCS')
    line_memo4 = fields.Char(string="說明4")
    item5 = fields.Integer(string="ITEM5")
    prod_no5 = fields.Many2one('product.product',string="料號5")
    m_ng_num5 = fields.Float(digits=(6, 0), string="材料不良數量5")
    p_ng_num5 = fields.Float(digits=(6, 0), string="加工不良數量5")
    prod_uom5 = fields.Char(string="單位5", default='PCS')
    line_memo5 = fields.Char(string="說明5")