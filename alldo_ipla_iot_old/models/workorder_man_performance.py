# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class workordermanperformance(models.Model):
    _name = "alldo_ipla_iot.man_performance"

    order_id = fields.Many2one('alldo_ipla_iot.workorder',string="工單號碼")
    prod_date = fields.Date(string="入庫日期")
    prod_duration = fields.Float(digits=(7, 1), string="實際總工時")
    std_duration = fields.Float(digits=(7, 1), string="標準總工時")
    prod_performance = fields.Float(digits=(4,2),string="生產效率%")
    prod_owner = fields.Many2one('hr.employee', string="擔當者")
    prod_num = fields.Float(digits=(13, 2), string="總數量")


class wkorderequipperformance(models.Model):
    _name = "alldo_ipla_iot.equipment_performance"

    equip_id = fields.Many2one('maintenance.equipment',string="機台")
    order_id = fields.Many2one('alldo_ipla_iot.workorder',string="工單號碼")
    equip_duration = fields.Float(digits=(7, 1), string="實際總工時")


class workordermanperformancelist(models.Model):
    _name = "alldo_ipla_iot.man_performance_list"
    _order = "prod_owner"

    prod_owner = fields.Many2one('hr.employee',string="人員")
    prod_performance = fields.Float(digits=(5,1),string="達成率%")


class equipmentperformancelist(models.Model):
    _name = "alldo_ipla_iot.equipment_performance_list"
    _description = "機台稼動時間"
    _order = "equip_no"

    equip_no = fields.Many2one('maintenance.equipment',string="機台")
    equipment_duration = fields.Float(digits=(10,2),string="總稼動工時(H)")

class workordermanperformancetrmp(models.Model):
    _name = "alldo_ipla_iot.man_performance_temp"

    prod_owner = fields.Many2one('hr.employee',string="人員")
    prod_performance = fields.Float(digits=(5,1),string="達成率%")

