# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class alldorespartnerinherit(models.Model):
    _inherit = "res.partner"

    outsourcing_out_line = fields.One2many('alldo_ipla_iot.partner_prodout','partner_id',string="委外供應商加工給料記錄")
    outsourcing_in_line = fields.One2many('alldo_ipla_iot.partner_prodin','partner_id',string="委外供應商加工回廠記錄")


class partneroutprodin(models.Model):
    _name = "alldo_ipla_iot.partner_prodin"
    _description = "委外入庫記錄明細"
    _order = "prodin_datetime desc"

    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    prodin_datetime = fields.Datetime(string="時間")
    product_no = fields.Many2one('product.product', string="產品")
    in_good_num = fields.Float(digits=(10, 2), string="良品數量", default=0.00)
    in_ng_num = fields.Float(digits=(10, 2), string="NG數量", default=0.00)
    loss_num = fields.Float(digits=(10,2),string="毛胚短少數量", default=0.00)
    process_num = fields.Float(digits=(10, 2), string="目前已加工數", default=0.00)
    in_stock_num = fields.Float(digits=(10,2),string="已入庫數量", default=0.00)
    in_loc = fields.Char(string="說明")
    in_owner = fields.Many2one('res.users', string="建檔人員")
    picking_no = fields.Many2one('stock.picking',string="調撥單號")

class partneroutprodout(models.Model):
    _name = "alldo_ipla_iot.partner_prodout"
    _description = "委外加工給料記錄明細"
    _order = "prodout_datetime desc"

    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    prodout_datetime = fields.Datetime(string="時間")
    product_no = fields.Many2one('product.product', string="產品")
    out_good_num = fields.Float(digits=(10, 2), string="給料數量", default=0.00)
    out_ng_num = fields.Float(digits=(10, 2), string="給料NG數量", default=0.00)
    out_loc = fields.Char(string="說明")
    out_owner = fields.Many2one('res.users', string="建檔人員")
    out_return_date = fields.Date(string="交期")
    out_memo = fields.Text(string="備註")
    report_date = fields.Date(string="製表日期")
    report_no = fields.Char(string="託工單號")
    picking_no = fields.Many2one('stock.picking',string="調撥單號")