# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebProdPriceList(models.Model):
    _name = "neweb.prod_price_list"
    _description = "業務價格與採購價格差異"

    @api.depends('prod_origin_price','prod_price')
    def _get_dif(self):
        for rec in self:
            if not rec.prod_origin_price :
                myoriginprice = 0
            else:
                myoriginprice = rec.prod_origin_price
            if not rec.prod_price :
                myprodprice = 0
            else:
                myprodprice = rec.prod_price
            rec.prod_dif = myprodprice - myoriginprice

    proj_no = fields.Many2one('neweb.project',string="成本分析")
    prod_set = fields.Many2one('neweb.prodset', string="產品組別")
    prod_modeltype = fields.Char(string="機種-機型/料號")
    prod_modeltype1 = fields.Many2one('neweb.sitem_modeltype1', string="機型名稱")
    prod_serial = fields.Text(string="序號")
    prod_no = fields.Char(string="料號")
    prod_desc = fields.Text(string="規格說明")
    prod_num = fields.Float(digits=(10, 0), string="數量", default=1)
    prod_origin_price = fields.Float(digits=(13,2),string="業務初始價格")
    prod_price = fields.Float(digits=(13, 2), string="採購議定價格")
    supplier = fields.Many2one('res.partner', string="廠商",domain=[('supplier_rank', '=', 1), ('parent_id', '=', False)])
    prod_dif = fields.Float(digits=(13,2),string="價格差異",compute=_get_dif)