# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
# from odoo.addons import decimal_precision as dp

class newebchiexportmainpurchaselog(models.Model):
    _name = "neweb_chi_invoicing.export_main_purchase_log"
    _description = "生成匯出(維護)進項數據記錄"

    @api.depends('chi_purchase_vat')
    def _get_partner(self):
        for rec in self:
            if rec.chi_purchase_vat:
                self.env.cr.execute("""select getvatname('%s')""" % rec.chi_purchase_vat)
                myres = self.env.cr.fetchone()[0]
                if myres > 0:
                    rec.chi_purchase_sup = myres

    chi_purchase_name = fields.Char(string="單據號碼")
    chi_income_date = fields.Date(string="進貨日期")
    chi_income_cdate = fields.Char(string="C進貨日期")
    chi_purchase_vat = fields.Char(string="廠商編號")
    chi_purchase_sup = fields.Many2one('res.partner',string="廠商",compute=_get_partner,store=True)
    chi_currency_type = fields.Char(string="使用幣別")
    chi_wh = fields.Char(string="倉庫")
    chi_project_no = fields.Char(string="所屬專案")
    proj_no = fields.Many2one('neweb.project',string="專案")
    chi_paymentdate = fields.Date(string="付款日期")
    chi_cpaymentdate = fields.Char(string="C付款日期")
    chi_product = fields.Char(string="產品編號")
    chi_purchase_num = fields.Float(digits=(10,0),string="數量")
    chi_purchase_price = fields.Float(digits=(13,2),string="單價")
    chi_origin_id = fields.Integer(string="來源PITEM_ID")
    chi_purchase_no = fields.Many2one('purchase.order',string="採購單號")

    def name_get(self):
        result = []
        for myrec in self:
            mypurchasename = "[%s]%s" % (myrec.chi_purchase_no,myrec.chi_purchase_sup.name)
            result.append((myrec.id, mypurchasename))
        return result



class newebchiexportmainsaleslog(models.Model):
    _name = "neweb_chi_invoicing.export_main_sales_log"
    _description = "生成匯出(維護)銷項數據記錄"

    @api.depends('chi_sales_vat')
    def _get_custom(self):
        for rec in self:
            if rec.chi_sales_vat:
                self.env.cr.execute("""select getvatname('%s')""" % rec.chi_sales_vat)
                myres = self.env.cr.fetchone()[0]
                if myres > 0:
                    rec.chi_sales_cus = myres


    chi_sales_no = fields.Char(string="單據號碼")
    chi_outcome_date = fields.Date(string="銷貨日期")
    chi_outcome_cdate = fields.Char(string="C銷貨日期")
    chi_sales_vat = fields.Char(string="客戶編號")
    chi_sales_cus = fields.Many2one('res.partner',string="客戶",compute=_get_custom,store=True)
    chi_currency_type = fields.Char(string="使用幣別")
    proj_sale = fields.Many2one('hr.employee',string="業務人員")
    proj_sale_name = fields.Char(string="業務人員")
    chi_wh = fields.Char(string="倉庫")
    proj_no = fields.Many2one('neweb.project', string="專案")
    chi_project_no = fields.Char(string="所屬專案")
    chi_cus_order = fields.Char(string="自定欄二")
    chi_paymentdate = fields.Date(string="收款日期")
    chi_cpaymentdate = fields.Char(string="C收款日期")
    chi_product = fields.Char(string="產品編號")
    chi_sales_num = fields.Float(digits=(10,0),string="數量")
    chi_sales_price = fields.Float(digits=(13,2),string="單價")
    chi_origin_id = fields.Integer(string="來源PROJSALE_ITEM_ID")
    chi_sale_memo = fields.Text(string="備註")


    def name_get(self):
        result = []
        for myrec in self:
            mysalesname = "[%s]%s" % (myrec.chi_sales_no, myrec.chi_sales_cus.name)
            result.append((myrec.id, mysalesname))
        return result









