# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class AcmeOutSuborderKpi(models.Model):
    _name = "alldo_acme_iot.outsuborder_kpi"
    _description = "委外加工交貨達成率表"

    partner_id = fields.Many2one('res.partner',string="委外加工商")
    outsub_id = fields.Many2one('alldo_acme_iot.outsuborder',string="委外加工單")
    product_no = fields.Many2one('product.product', string="產品料號")
    outsub_num = fields.Float(digits=(10,0),string="工單數量")
    kpi_ratio = fields.Float(digits=(6,2),string="達成率")
    ng_ratio = fields.Float(digits=(6,2),string="NG率")
    kpi_deduction = fields.Float(digits=(6,2),string="扣點")
    supply_line = fields.One2many('alldo_acme_iot.outsuborder_kpi_line1','supply_id',string="委外供貨明細",copy=False)
    delivery_line = fields.One2many('alldo_acme_iot.outsuborder_kpi_line','delivery_id',string="委外交貨明細",copy=False)
    quant_line = fields.One2many('alldo_acme_iot.outsuborder_kpi_quant','quant_id',string="委外交貨拆批試算",copy=False)

class AcmeOutSuborderKpiLine(models.Model):
    _name = "alldo_acme_iot.outsuborder_kpi_line"

    delivery_id = fields.Many2one('alldo_acme_iot.outsuborder_kpi',ondelete='cascade')
    date_delivery = fields.Date(string="交貨日期")
    delivery_num = fields.Float(digits=(10,0),string="交貨數量")
    good_num = fields.Float(digits=(10,0),string="GOOD數量")
    ng_num = fields.Float(digits=(10,0),string="NG數量")


class AcmeOutSuborderKpiline1(models.Model):
    _name = "alldo_acme_iot.outsuborder_kpi_line1"

    supply_id = fields.Many2one('alldo_acme_iot.outsuborder_kpi',ondelete='cascade')
    supply_num = fields.Float(digits=(10, 0), string="供料數量")
    date_supply = fields.Date(string="供料日期")
    date_due = fields.Date(string="應交日期")

class AcmeOutSuborderKpisheet(models.Model):
    _name = "alldo_acme_iot.outsuborder_kpi_quant"

    quant_id = fields.Many2one('alldo_acme_iot.outsuborder_kpi',ondelete='cascade')
    quant_seq = fields.Integer(string="序")
    supply_num = fields.Float(digits=(10, 0), string="供料數量",default=0)
    date_supply = fields.Date(string="供料日期")
    date_due = fields.Date(string="應交日期")
    date_delivery = fields.Date(string="實際交貨日期")
    date_last = fields.Date(string="最遲交貨日期")
    date_duration = fields.Integer(string="遲交日數")
    delivery_num = fields.Float(digits=(10, 0), string="交貨數量",default=0)
    kpi_ratio = fields.Float(digits=(6, 2), string="達成率",default=0.00)
    ng_ratio = fields.Float(digits=(6, 2), string="NG率",default=0.00)
    kpi_deduction = fields.Float(digits=(6, 2), string="扣點",default=0.00)
    is_complete = fields.Boolean(string="完成",default=False)