# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api,_
from odoo import exceptions
import datetime


class newebpithdoc(models.Model):
    _name = "neweb_sale_analysis.pith_doc"
    _description = "用印申請單"

    name = fields.Char(string="表單單號",default="New")
    customer = fields.Many2one('res.partner',string="對象名稱")
    project_num = fields.Char(string="專案編號")
    project = fields.Char(string="專案名稱")
    app_work = fields.Many2one('res.users', string="申請部門")
    app_human = fields.Many2one('res.users', string="申請人")
    categ = fields.Selection([('1', '用印申請'), ('2', '印鑑借出申請'), ('3', '用印及印鑑借出申請')], string="申請類別")
    doc_date = fields.Date(string="日期")
    doc_date_y = fields.Char(string="年")
    doc_date_m = fields.Char(string="月")
    doc_date_d = fields.Char(string="日")
    reason = fields.Text(string="申請原因")
    director = fields.Text(string="主管意見")
    doc_name = fields.Char(string="用印文件名稱")
    doc_num = fields.Integer(string="用印份數")
    doc_date2 = fields.Date(string="借出日期")
    doc_date2_y = fields.Char(string="年")
    doc_date2_m = fields.Char(string="月")
    doc_date2_d = fields.Char(string="日")
    doc_date3 = fields.Date(string="預計歸還")
    doc_date3_y = fields.Char(string="年")
    doc_date3_m = fields.Char(string="月")
    doc_date3_d = fields.Char(string="日")
    doc_date4 = fields.Date(string="實際歸還")
    doc_date4_y = fields.Char(string="年")
    doc_date4_m = fields.Char(string="月")
    doc_date4_d = fields.Char(string="日")
    b_stamp = fields.Boolean(string="經濟部大小章",default=False)
    s_stamp = fields.Boolean(string="銀行專用章",default=False)
    i_stamp = fields.Boolean(string="發票章",default=False)
    o_stamp = fields.Boolean(string="橢圓章",default=False)
    c_stamp = fields.Boolean(string="合約專用章", default=False)
    s_cstmp = fields.Selection([('1','1號'),('2','2號'),('3','3號'),('4','4號')],string="合約專用章別")


