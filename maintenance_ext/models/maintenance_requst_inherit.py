# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class MaintenanceRequestInherit(models.Model):
    _inherit = "maintenance.request"

    maintenance_line = fields.One2many('maintenance.request_check_list','request_id',copy=False)
    maintenance_line1 = fields.One2many('maintenance.request_check_list1','request_id',copy=False)
    maintenance_parts = fields.One2many('maintenance.request_parts','request_id',copy=False)
    main_type = fields.Selection([('1','每日巡檢'),('2','額定保養')],string="維護類型")


class MaintenanceRequestCheckList(models.Model):
    _name = "maintenance.request_check_list"
    _description = "每日巡檢清單"
    _order = "check_seq"

    request_id = fields.Many2one('maintenance.request',ondelete='cascade')
    check_seq = fields.Integer(string='項次')
    check_item = fields.Char(string="檢驗項目名稱")
    check_value = fields.Selection([('1', 'OK/NG'), ('2', '輸入檢測數據')], string="檢測模式", default='1')
    check_result1 = fields.Selection([('ok','OK'),('ng','NG')],string="檢驗結果")
    check_result2 = fields.Float(digits=(12,5),string="檢測值")
    h_value = fields.Float(digits=(12, 5), string="上限值")
    l_value = fields.Float(digits=(12, 5), string="下限值")
    check_man = fields.Many2one('res.users',string="維護人員",default=lambda self:self.env.uid)

class MaintenanceRequestCheckList1(models.Model):
    _name = "maintenance.request_check_list1"
    _description = "額定定期保養清單"
    _order = "check_seq"

    request_id = fields.Many2one('maintenance.request',ondelete='cascade')
    check_seq = fields.Integer(string='項次')
    check_item = fields.Char(string="檢驗項目名稱")
    maintenance_result = fields.Text(string="維護保養說明")
    check_man = fields.Many2one('res.users',string="維護人員",default=lambda self:self.env.uid)


class MaintenanceRequestParts(models.Model):
    _name = "maintenance.request_parts"
    _description = "維護耗用材料清單"

    request_id = fields.Many2one('maintenance.request', ondelete='cascade')
    prod_id = fields.Many2one('product.product',string="零件料號")
    prod_uom = fields.Many2one('uom.uom',string="單位")
    prod_num = fields.Float(digits=(10,2),string="數量")
    request_man = fields.Many2one('res.users',string="領用人",default=lambda self:self.env.uid)




