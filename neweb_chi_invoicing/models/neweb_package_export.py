# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebpackageexportproj(models.Model):
    _name = "neweb_chi_invoicing.package_project"
    _description = "整批匯出專案暫存檔"


    project_no = fields.Char(string="成本分析編號")
    project_desc = fields.Char(string="成本分析說明")
    project_memo = fields.Text(string="成本分析備註")



class newebpackageexportprod(models.Model):
    _name = "neweb_chi_invoicing.package_product"
    _description = "整批匯出產品料號暫存擋"


    prod_set = fields.Char(string="產品類別")
    prod_no = fields.Char(string="產品料號")
    prod_spec = fields.Char(string="品名規格")
    prod_currency = fields.Char(string="使用幣別")
    prod_memo = fields.Char(string="自定欄一")
    proj_no = fields.Char(string="成本分析編號")


class newebpackagepurchase(models.Model):
    _name = "neweb_chi_invoicing.package_purchase"
    _description = "整批進項憑證資料暫存檔"

    purchase_no = fields.Char(string="單據號碼")
    purchase_no1 = fields.Char(string="進項單號")
    purchase_indate = fields.Date(string="進貨日")
    purchase_cindate = fields.Char(string="C進貨日")
    purchase_suppvat = fields.Char(string="廠商編號")
    purchase_currency = fields.Char(string="使用幣別")
    purchase_wh = fields.Char(string="倉庫編號")
    purchase_projno = fields.Char(string="所屬專案")
    purchase_payment = fields.Date(string="付款日期")
    purchase_cpayment = fields.Char(string="C付款日期")
    purchase_prod = fields.Char(string="產品編號")
    purchase_num = fields.Float(digits=(6,1),string="數量")
    purchase_price = fields.Float(digits=(11,2),string="單價")
    proj_no = fields.Char(string="成本分析編號")


class newebpackagesales(models.Model):
    _name = "neweb_chi_invoicing.package_sales"
    _description = "整批銷項憑證資料暫存檔"

    sales_no = fields.Char(string="單據號碼")
    sales_outdate = fields.Date(string="銷貨日期")
    sales_coutdate = fields.Char(string="C銷貨日期")
    sales_cusvat = fields.Char(string="客戶編號")
    sales_currency = fields.Char(string="使用幣別")
    sales_man = fields.Char(string="業務人員")
    sales_wh = fields.Char(string="倉庫編號")
    sales_proj_no = fields.Char(string="所屬專案")
    sales_cus_order = fields.Char(string="自定欄位二")
    sales_paymentdate = fields.Date(string="收款日期")
    sales_cpaymentdate = fields.Char(string="C收款日期")
    sales_prod = fields.Char(string="產品編號")
    sales_num = fields.Float(digits=(6,1),string="數量")
    sales_price = fields.Float(digits=(11,2),string="單價")
    proj_no = fields.Char(string="成本分析編號")
    sales_memo = fields.Text(string="備註")
    sale_spec = fields.Char(string="品名規格")
    saleitem_seq = fields.Integer(string="SALEITEM SEQ")