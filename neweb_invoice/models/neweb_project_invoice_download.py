# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class projectinvoicedownload(models.Model):
    _name = "neweb_invoice.proj_inv_excel_download"
    _order = "create_date desc"
    _description = "成本分析-發票彙整Excel Download"

    xls_file = fields.Binary(string='下載檔案',attachment=False)
    xls_file_name = fields.Char(string='檔案說明')

class projecttempdata(models.Model):
    _name = "neweb_invoice.projectdata"
    _description = "專案-成本分析彙整檔"

    project_no = fields.Many2one('neweb.project',string="專案編號")
    prod_set = fields.Many2one('neweb.prodset',string="產品組別")
    cus_name = fields.Many2one('res.partner',string="客戶名稱")
    prod_modeltype = fields.Text(string="機型-機種/料號")
    prod_desc = fields.Text(string="規格說明")
    prod_num = fields.Float(digits=(8,0),string="數量")
    prod_cost_price = fields.Float(digits=(10,0),string="成本總價")
    supplier = fields.Many2one('res.partner',string="報價廠商")
    prod_sale_price = fields.Float(digits=(10,0),string="銷售金額")


class invoiceopendata(models.Model):
    _name = "neweb_invoice.invoicedata"
    _description = "專案-發票開立彙整檔"

    project_no = fields.Many2one('neweb.project',string="專案編號")
    invoice_date = fields.Date(string="開立日期")
    invoice_cdate = fields.Char(string="C開立日期")
    invoice_no = fields.Char(string="發票號碼")
    invoice_untax_amount = fields.Float(digits=(9,0),string="金額")
    application_date = fields.Date(string="申請日期")
    application_cdate = fields.Char(string="C申請日期")
    other_memo = fields.Text(string="備註")


class purinvdata(models.Model):
    _name = "neweb_invoice.purinvdata"
    _description = "專案-廠商請款狀況"

    pitem_origin_no = fields.Char(string="來源單號")
    invoice_date = fields.Date(string="發票日期")
    invoice_cdate = fields.Char(string="C發票日期")
    invoice_no = fields.Char(string="發票號碼")
    inv_paymentterm = fields.Date(string="付款期限")
    inv_cpaymentterm = fields.Char(string="C付款期限")
    invoice_partner = fields.Many2one('res.partner',string="付款對象")
    invoice_sum = fields.Float(string="金額")
    payment_yn = fields.Selection([('1','未請款'),('2','已請款')],string="是否請款")