# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebRPSSchedule(models.Model):
    _name = "neweb.rps_schedule"
    _description = "申購-採購-進貨進度表"


    rp_no = fields.Many2one('neweb.require_purchase',string="申購單號")
    rp_modeltype = fields.Char(string="機種-機型/料號")
    rp_pid = fields.Many2one('product.template', string="庫存料號")
    rp_pitemspec = fields.Char(string="規格說明")
    rp_date = fields.Date(string="申購日期")
    rp_num = fields.Integer(string="申購數量")
    po_no = fields.Many2one('purchase.order',string="採購單號")
    po_date = fields.Date(string="採購日期")
    po_num = fields.Integer(string="採購數量")
    stockin_no = fields.Many2one('stock.picking',string="進貨單據")
    stockin_num = fields.Integer(string="收貨量")
    stockin_date = fields.Date(string="進貨驗收日")
    rp_budget = fields.Integer(string="預算")
    po_partner = fields.Many2one('res.partner',string="供應商")
