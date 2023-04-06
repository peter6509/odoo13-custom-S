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