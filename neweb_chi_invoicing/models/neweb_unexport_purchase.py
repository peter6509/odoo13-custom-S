# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
# from odoo.addons import decimal_precision as dp



class newebincomeoutcomeseq(models.Model):
    _name = "neweb_chi_invoicing.incomeoutcome_seq"
    _description = u"進銷存進項/銷項單據流水號檔"


    chi_year = fields.Char(string=u"年度")
    chi_month = fields.Char(string=u"月")
    chi_day = fields.Char(string=u"日")
    chi_sname = fields.Char(string=u"簡碼")
    chi_seq = fields.Integer(string=u"流水號",default=1)



class newebunexportpitemlist(models.Model):
    _inherit = "neweb.pitem_list"


    chi_purchase_no = fields.Char(string=u"正航採購單號")



class newebunexportprojsaleitemlist(models.Model):
    _inherit = "neweb.projsaleitem"

    chi_sales_no = fields.Char(string=u"正航出貨單號")



class newebchiexportpurchaselog(models.Model):
    _name = "neweb_chi_invoicing.export_purchase_log"
    _description = u"生成匯出進項數據記錄"
    _order = "chi_purchase_no,purchase_seq,pitem_id"

    @api.depends('chi_purchase_vat')
    def _get_partner(self):
        for rec in self:
            if rec.chi_purchase_vat:
                self.env.cr.execute("""select getvatname('%s')""" % rec.chi_purchase_vat)
                myres = self.env.cr.fetchone()[0]
                if myres > 0:
                    rec.chi_purchase_sup = myres


    chi_purchase_name = fields.Char(string=u"單據號碼")
    chi_income_date = fields.Date(string=u"進貨日期")
    chi_income_cdate = fields.Char(string=u"C進貨日期")
    chi_purchase_vat = fields.Char(string=u"廠商編號")
    chi_purchase_sup = fields.Many2one('res.partner',string=u"廠商",compute=_get_partner,store=True)
    chi_currency_type = fields.Char(string=u"使用幣別")
    chi_wh = fields.Char(string=u"倉庫")
    chi_project_no = fields.Char(string=u"所屬專案")
    proj_no = fields.Many2one('neweb.project',string=u"專案")
    chi_paymentdate = fields.Date(string=u"付款日期")
    chi_cpaymentdate = fields.Char(string=u"C付款日期")
    chi_product = fields.Char(string=u"產品編號")
    chi_purchase_num = fields.Float(digits=(10,0),string=u"數量")
    chi_purchase_price = fields.Float(digits=(13,2),string=u"單價")
    chi_origin_id = fields.Integer(string=u"來源PITEM_ID")
    chi_purchase_no = fields.Many2one('purchase.order',string=u"採購單號")
    purchase_seq = fields.Integer(string=u"採購SEQ")
    pitem_id = fields.Integer(string=u"PITEM ID")




    # @api.multi
    def name_get(self):
        result = []
        for myrec in self:
            mypurchasename = u"[%s]%s" % (myrec.chi_purchase_no,myrec.chi_purchase_sup.name)
            result.append((myrec.id, mypurchasename))
        return result



class newebchiexportsaleslog(models.Model):
    _name = "neweb_chi_invoicing.export_sales_log"
    _description = u"生成匯出銷項數據記錄"

    @api.depends('chi_sales_vat')
    def _get_custom(self):
        for rec in self:
            if rec.chi_sales_vat:
                self.env.cr.execute("""select getvatname('%s')""" % rec.chi_sales_vat)
                myres = self.env.cr.fetchone()[0]
                if myres > 0:
                    rec.chi_sales_cus = myres

    chi_sales_no = fields.Char(string=u"單據號碼")
    chi_outcome_date = fields.Date(string=u"銷貨日期")
    chi_outcome_cdate = fields.Char(string=u"C銷貨日期")
    chi_sales_vat = fields.Char(string=u"客戶編號")
    chi_sales_cus = fields.Many2one('res.partner',string=u"客戶",compute=_get_custom,store=True)
    chi_currency_type = fields.Char(string=u"使用幣別")
    proj_sale = fields.Many2one('hr.employee',string=u"業務人員")
    proj_sale_name = fields.Char(string=u"業務人員")
    chi_wh = fields.Char(string=u"倉庫")
    proj_no = fields.Many2one('neweb.project', string=u"專案")
    chi_project_no = fields.Char(string=u"所屬專案")
    chi_cus_order = fields.Char(string=u"自定欄二")
    chi_paymentdate = fields.Date(string=u"收款日期")
    chi_cpaymentdate = fields.Char(string=u"C收款日期")
    chi_product = fields.Char(string=u"產品編號")
    chi_sales_num = fields.Float(digits=(10,0),string=u"數量")
    chi_sales_price = fields.Float(digits=(13,2),string=u"單價")
    chi_origin_id = fields.Integer(string=u"來源PROJSALE_ITEM_ID")
    chi_sale_memo = fields.Text(string=u"備註")
    chi_sale_spec = fields.Char(string=u"品名規格")
    saleitem_seq = fields.Integer(string=u"PROJ SEQ")


    def name_get(self):
        result = []
        for myrec in self:
            mysalesname = u"[%s]%s" % (myrec.chi_sales_no, myrec.chi_sales_cus.name)
            result.append((myrec.id, mysalesname))
        return result








