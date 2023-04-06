# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import xlrd
import xlsxwriter
# import odoo.addons.decimal_precision as dp

class newebprojsaleitemexport(models.Model):
    _name = "neweb.projsaleitem_export"

    seqid = fields.Integer(string="項次")
    saleitem_item = fields.Char(string="項次")
    prodset = fields.Char(string="產品組別")
    prodbrand = fields.Char(string="品牌")
    prodmodeltype = fields.Char(string="機種-機型/料號")
    prodmodeltype1 = fields.Char(string="機型名稱")
    prodserial = fields.Char(string="序號")
    maintenance_term = fields.Char(string="維護期間")
    proddesc = fields.Char(string="規格說明")
    prodnum = fields.Float(digits=(10,0), string="數量", default=1)
    dis_price = fields.Float(digits=(13,2), string="優惠單價")
    dis_sumtot = fields.Float(digits=(13,2), string="優惠總價")
    prod_price = fields.Float(digits=(13,2), string="成本單價")
    supplier = fields.Char(size=20, string="報價廠商")
    costtype = fields.Char(string="成本類型")
    prod_sumtot = fields.Float(digits=(13,2), string="成本*數量")
    prod_profit = fields.Float(digits=(13,2),string="毛利")
    prod_profitrate = fields.Float(digits=(5,2),string="毛利率")
    cost_dept = fields.Char(string="部門")



