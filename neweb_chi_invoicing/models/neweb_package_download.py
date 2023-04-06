# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebchiinvoicingpackagedownload(models.Model):
    _name = "neweb_chi_invoicing.package_excel_download"
    _description = "整包專案進銷存資料夾"
    _order = "id desc"
    _rec_name = "project_no"


    project_no = fields.Char(string="成本分析")
    xls_file1 = fields.Binary(string="專案下載",attachment=False)
    xls_file_name1 = fields.Char(string="專案檔名")
    xls_file2 = fields.Binary(string="產品料號下載",attachment=False)
    xls_file_name2 = fields.Char(string="產品料號檔名")
    xls_file3 = fields.Binary(string="進貨憑證下載",attachment=False)
    xls_file_name3 = fields.Char(string="進貨憑證檔名")
    xls_file4 = fields.Binary(string="銷貨憑證下載",attachment=False)
    xls_file_name4 = fields.Char(string="銷貨憑證檔名")
    xls_file5 = fields.Binary(string="進貨憑證下載(維護)",attachment=False)
    xls_file_name5 = fields.Char(string="進貨憑證(維護)檔名")
    xls_file6 = fields.Binary(string="退貨下載",attachment=False)
    xls_file_name6 = fields.Char(string="退貨檔名")
    run_desc = fields.Char(string="匯出說明")
    invoicing1_date = fields.Date(string="專案EXCEL匯出日")
    invoicing1_owner = fields.Many2one('hr.employee',string="專案EXCEL匯出人")
    invoicing2_date = fields.Date(string="產品料號EXCEL匯出日")
    invoicing2_owner = fields.Many2one('hr.employee',string="產品料號EXCEL匯出人")
    invoicing3_date = fields.Date(string="進貨憑證EXCEL匯出日")
    invoicing3_owner = fields.Many2one('hr.employee',string="進貨憑證EXCEL匯出人")
    invoicing4_date = fields.Date(string="銷貨憑證EXCEL匯出日")
    invoicing4_owner = fields.Many2one('hr.employee',string="銷貨憑證EXCEL匯出人")
    invoicing5_date = fields.Date(string="銷貨憑證(維護)EXCEL匯出日")
    invoicing5_owner = fields.Many2one('hr.employee', string="銷貨憑證(維護)EXCEL匯出人")
    invoicing6_date = fields.Date(string="退貨變更EXCEL匯出日")
    invoicing6_owner = fields.Many2one('hr.employee', string="退貨變更EXCEL匯出人")




    # @api.multi
    # def unlink(self):
    #     for rec in self:
    #         if rec.xls_file3 or rec.xls_file4 or rec.xls_file5 or rec.xls_file6 :
    #             raise UserError("以產生憑證,無法刪除下載記錄檔")
    #     res = super(newebchiinvoicingpackagedownload, self).unlink()
    #     return res


class newebchiinvoicingpackagepurinvdownload(models.Model):
    _name = "neweb_chi_invoicing.package_purinv_excel_download"
    _description = "整包專案進銷存進項資料夾"
    _order = "id desc"
    _rec_name = "purchase_no"


    purchase_no = fields.Char(string="採購單號")
    xls_file = fields.Binary(string="專案下載",attachment=False)
    xls_file_name = fields.Char(string="專案檔名")
    run_desc = fields.Char(string="匯出說明")
    invoicing_date = fields.Date(string="專案EXCEL匯出日")
    invoicing_owner = fields.Many2one('hr.employee',string="專案EXCEL匯出人")


class newebchiinvoicingpackagesaleinvdownload(models.Model):
    _name = "neweb_chi_invoicing.package_saleinv_excel_download"
    _description = "整包專案進銷存銷項資料夾"
    _order = "id desc"
    _rec_name = "project_no"


    project_no = fields.Char(string="專案編號")
    xls_file = fields.Binary(string="專案下載",attachment=False)
    xls_file_name = fields.Char(string="專案檔名")
    run_desc = fields.Char(string="匯出說明")
    invoicing_date = fields.Date(string="專案EXCEL匯出日")
    invoicing_owner = fields.Many2one('hr.employee',string="專案EXCEL匯出人")