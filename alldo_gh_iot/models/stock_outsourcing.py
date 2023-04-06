# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api, _
from odoo.exceptions import UserError

class stockoutsourcingdata(models.Model):
    _name = "alldo_gh_iot.outsourcing_report"

    partner_id = fields.Many2one('res.partner',string="委外加工廠商")
    name = fields.Char(string="委外加工單號",default=lambda self: _('New'))
    report_date = fields.Date(string="製表日期")
    report_line = fields.One2many('alldo_gh_iot.outsourcing_report_line','rep_id',copy=False)
    report_memo = fields.Char(string="備註")


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('alldo_gh_iot.outsourcing_out') or _('New')
        res = super(stockoutsourcingdata, self).create(vals)
        return res


class stockoutsourcingline(models.Model):
    _name = "alldo_gh_iot.outsourcing_report_line"

    rep_id = fields.Many2one('alldo_gh_iot.outsourcing_report',ondelete='cascade')
    item = fields.Integer(string="ITEM")
    prod_no = fields.Many2one('product.product',string="料號")
    prod_num = fields.Float(digits=(6,0),string="數量")
    prod_uom = fields.Char(string="單位",default='PCS')
    line_memo = fields.Char(string="加工說明")
    out_return_date = fields.Date(string="交期")
    item1 = fields.Integer(string="ITEM2")
    prod_no1 = fields.Many2one('product.product', string="料號2")
    prod_num1 = fields.Float(digits=(6, 0), string="數量2")
    prod_uom1 = fields.Char(string="單位2", default='PCS')
    line_memo1 = fields.Char(string="加工說明2")
    out_return_date1 = fields.Date(string="交期2")
    item2 = fields.Integer(string="ITEM3")
    prod_no2 = fields.Many2one('product.product', string="料號3")
    prod_num2 = fields.Float(digits=(6, 0), string="數量3")
    prod_uom2 = fields.Char(string="單位3", default='PCS')
    line_memo2 = fields.Char(string="加工說明3")
    out_return_date2 = fields.Date(string="交期3")
    item3 = fields.Integer(string="ITEM4")
    prod_no3 = fields.Many2one('product.product', string="料號4")
    prod_num3 = fields.Float(digits=(6, 0), string="數量4")
    prod_uom3 = fields.Char(string="單位4", default='PCS')
    line_memo3 = fields.Char(string="加工說明4")
    out_return_date3 = fields.Date(string="交期4")
    item4 = fields.Integer(string="ITEM5")
    prod_no4 = fields.Many2one('product.product', string="料號5")
    prod_num4 = fields.Float(digits=(6, 0), string="數量5")
    prod_uom4 = fields.Char(string="單位5", default='PCS')
    line_memo4 = fields.Char(string="加工說明5")
    out_return_date4 = fields.Date(string="交期5")
