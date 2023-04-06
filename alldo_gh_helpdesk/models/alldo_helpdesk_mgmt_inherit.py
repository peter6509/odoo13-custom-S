# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class AlldoHelpDeskMgmtInherit(models.Model):
    _inherit = "helpdesk.ticket"

    prod_id = fields.Many2one('product.product',string="產品名稱")
    prod_spec = fields.Char(string="材質規格")
    alert_num = fields.Integer(string="(客訴/異常/不良)數量")
    alert_desc = fields.Text(string="客訴不良原因")
    operation_man = fields.Many2one('hr.employee',string="操作人員")
    op_management = fields.Many2one('hr.employee',string='部門主管')
    operation_equip = fields.Many2one('maintenance.equipment',string="操作機台")
    operation_dept = fields.Selection([('1','車床'),('2','銑床'),('3','倉管'),('4','品管'),('5','委外')],string="所屬部門")
    process_method = fields.Selection([('1','重修'),('2','當下腳料'),('3','報廢'),('4','其他')],string="處理方式")
    p_other_desc = fields.Char(string="處理方式其他說明")
    add_blank = fields.Selection([('Y','是'),('N','否')],string="是否補胚",default='N')
    alert_reason = fields.Text(string="原因分析")
    improve_strategy = fields.Text(string="改善結果")
    management_desc = fields.Text(string="主管說明")
    stock_process = fields.Text(string="庫存處理")
    unusual_item = fields.Selection([('1','外觀'),('2','砂孔'),('3','公差'),('4','漏工程'),('5','其他')],string="異常項目")
    un_other_desc = fields.Char(string="異常項目其他說明")
    complaint_method = fields.Selection([('1','重修'),('2','退換'),('3','退貨銷單'),('4','買收'),('5','其他')],string="客訴異常處理")
    co_other_desc = fields.Char(string="客訴異常處理其他說明")
    restock_process = fields.Selection([('1','當庫存品'),('2','當下腳料'),('3','報廢'),('4','其他')],string="回貨處理")
    restock_other_desc = fields.Char(string="回貨處理其他說明")
    description = fields.Html(string="簡述",required=False)
    alert_num_desc = fields.Text(string="客訴數量&處理方式")
    stock_num_desc = fields.Text(string="庫存數量&處理方式")
    process_num_desc = fields.Text(string="在製數量&處理方式")
    response_date = fields.Date(string="回覆日期")
    complete_date = fields.Date(string="結案日期")

    # @api.model
    # def create(self, vals):
    #
    #     vals['description']= ' '
    #     res = super(AlldoHelpDeskMgmtInherit, self).create(vals)
    #     return res



