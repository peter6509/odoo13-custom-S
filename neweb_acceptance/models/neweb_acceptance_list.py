# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebAcceptanceAccList(models.Model):
    _name = "neweb_acceptance.acc_list"
    _description = "貨品狀態履歷記錄表"
    _rec_name = "keyin_date"
    _order = "proj_sale,project_no"

    acceptance_id = fields.Many2one('neweb.acceptance',string="ACC")
    keyin_date = fields.Date(string="填單日")
    purchase_no = fields.Char(string="採購單號")
    purchase_date = fields.Date(string="採購日期")
    stockout_no = fields.Many2one('stock.picking', string="出貨單號")
    project_no = fields.Many2one('neweb.project', string="專案編號")
    project_no1 = fields.Char(string="專案編號C")
    acceptance_status = fields.Selection([('1', '未驗收'), ('2', '已驗收')], string="驗收狀態", default='1')
    proj_sale = fields.Many2one('hr.employee', string="業務")
    cus_name = fields.Many2one('res.partner', string="客戶名稱")
    cus_project = fields.Char(string="客戶專案/標案名稱")
    prod_no = fields.Char(string="產品料號")
    prod_modeltype = fields.Char(string="機種-機型/料號")
    prod_desc = fields.Text(string="規格說明")
    prod_num = fields.Float(digits=(10, 0), string="數量")
    supplier = fields.Char(string="供應商")
    acceptanced_date1 = fields.Date(string="預計驗收日")
    stockin_date = fields.Date(string="收貨日期")
    stockout_date = fields.Date(string="出貨日期")
    acceptanced_date2 = fields.Date(string="結案日")
    projsaleitem_status = fields.Selection(
        [('1', '貨在公司待貨齊'), ('2', '貨在公司待出貨'), ('3', '貨在公司測試安裝中'), ('4', '貨在客戶端待貨齊'), ('5', '貨在客戶端待裝機'),
         ('6', '貨在客戶端裝機中'), ('7', '貨在客戶端待驗收'), ('8', '貨在客戶端驗收中')], string="狀態", default='1')
    memo = fields.Text(string="狀態說明")
    accym = fields.Char(string="年月")
    active = fields.Boolean(string="ACTIVE", default=True)
    projsaleitem_id = fields.Integer(string="projsaleitem id")
