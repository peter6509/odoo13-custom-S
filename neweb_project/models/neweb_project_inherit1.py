# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class newebprojectinherit1(models.Model):
    _inherit = "neweb.project"

    self_receive_type = fields.Selection([('1','現金'),('2','支票')],string="親領項目",default='2')
    prodset_lines = fields.One2many('neweb.projprodset','prodset_id',string="產品分類統計")
    open_account_day = fields.Selection([('1', '30天'), ('2', '45天'), ('3', '60天'), ('4', '90天'), ('5', '120天')],
                                        string="付款天數")
    proj_info_desc = fields.Text(string="說明")
    proj_info_memo = fields.Text(string="授信額度")
    proj_import_status = fields.Boolean(string="匯入狀態",default=False)

    # @api.depends('cus_name')
    # def _get_paymentday(self):
    #     myres = False
    #     myrec = self.env['res.partner'].search([('id','=',self.cus_name.id)])
    #     try:
    #         myopenaccountday= int(myrec.pay_term)
    #     except Exception as inst:
    #         myopenaccountday = 0
    #     if myopenaccountday == 0:
    #         self.open_account_day = False
    #     elif myopenaccountday <= 30 and myopenaccountday > 0 :
    #         myres = '1'
    #         self.open_account_day = '1'
    #     elif myopenaccountday <= 45 and myopenaccountday > 30 :
    #         myres = '2'
    #         self.open_account_day = '2'
    #     elif myopenaccountday <= 60 and myopenaccountday > 45 :
    #         myres = '3'
    #         self.open_account_day = '3'
    #     elif myopenaccountday <= 90 and myopenaccountday > 60:
    #         myres = '4'
    #         self.open_account_day = '4'
    #     else:
    #         self.open_account_day = '5'
    #         myres = '5'
    #     return myres





class projsaleiteminherit(models.Model):
    _inherit = "neweb.projsaleitem"
    _order = "line_item,id"

    saleitem_item = fields.Char(string="項次")

class saleorderinherit(models.Model):
    _inherit = "neweb.sitem_list"
    _order = "id"

    sitem_item = fields.Char(string="項次")
    sitem_item1 = fields.Float(digits=(5,1),string="項次")
    sitem_serial = fields.Char(string="序號")


class newebprojprodset(models.Model):
    _name = "neweb.projprodset"
    _description = '成本分析產品組別成本/收入金額'

    prodset_id = fields.Many2one('neweb.project',required=True,copy=False, ondelete='cascade')
    prod_set = fields.Many2one('neweb.prodset',string="產品組別")
    prod_price_tot = fields.Float(digits=(10,0),string="總成本金額")
    prod_revenue_tot = fields.Float(digits=(10,0),string="總收入金額")



