# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotworkorderperformance(models.Model):
    _name = "alldo_ipla_iot.workorder_performance_list"

    order_id = fields.Many2one('alldo_ipla_iot.workorder',string="工單")
    iot_date = fields.Char(string="日期")
    iot_node = fields.Many2one('maintenance.equipment',string="機台")
    iot_owner = fields.Many2one('hr.employee',string="作業者")
    good_num = fields.Integer(string="生產數量")
    ng_num = fields.Integer(string="NG數量")
    iot_duration = fields.Float(digits=(10,2),string="實際總工時(分鐘)")
    std_duration = fields.Float(digits=(10,2),string="標準總工時(分鐘)")
    owner_perfrate = fields.Float(digits=(4,2),string="作業者效率%")
    product_no = fields.Many2one('product.product',string="產品")
    eng_type = fields.Char(string="工序")

class iplaiotworkorderperformance1(models.Model):
    _name = "alldo_ipla_iot.workorder_performance_list1"
    _order = "iot_date,iot_node"

    iot_date = fields.Char(string="日期")
    iot_owner = fields.Many2one('hr.employee', string="責任者")
    iot_node = fields.Many2one('maintenance.equipment', string="機台")
    wkorder_id = fields.Many2one('alldo_gh_iot.workorder', string="工單號碼")
    iot_start = fields.Char(string="起始時間")
    iot_end = fields.Char(string="截止時間")
    product_no = fields.Many2one('product.product', string="產品")
    eng_type = fields.Char(string="工程別")
    total_amount_num = fields.Float(digits=(13, 2), string="生產量", default=0)
    material_ng_num = fields.Float(digits=(13, 2), string="料不良數", default=0)
    processing_ng_num = fields.Float(digits=(13, 2), string="工不良數", default=0)
    std_num = fields.Float(digits=(6, 0), string="標準量")
    performance_rate = fields.Float(digits=(4, 2), string="達成率")
    iot_duration = fields.Float(digits=(6, 2), string="工時(H)")
    product_num = fields.Float(digits=(6, 0), string="產能/(H)")