# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmeaccountmoveinherit(models.Model):
    _inherit = "account.move"

    taiwan_receipt = fields.Char(string="發票號碼")
    report_no = fields.Char(string="對帳單號")
    receive_check = fields.Boolean(string="支票(一)收付？")
    check_duedate = fields.Date(string="支票(一)到期日")
    check_num = fields.Float(digits=(10,0),string="支票(一)金額")
    receive2_check = fields.Boolean(string="支票(二)收付？")
    check2_duedate = fields.Date(string="支票(二)到期日")
    check2_num = fields.Float(digits=(10, 0), string="支票(二)金額")

class acmeaccountmoveseq(models.Model):
    _name = "alldo_acme_iot.account_seq"

    seq_type = fields.Char(string="單號類型")
    seq_date = fields.Date(string="日期")
    seq_num = fields.Integer(string="流水號")



class acmeaccountmoveselectitem(models.Model):
    _name = "alldo_acme_iot.accountmove_selectitem"
    _description = "對帳選單主檔"

    report_date = fields.Date(string="列印日期")
    report_date1 = fields.Char(string="列印日期1")
    startenddate = fields.Char(string="日期區間")
    partner_id = fields.Many2one('res.partner',string="客戶名稱")
    name = fields.Char(string="應收帳款對帳單號")
    taiwan_receipt = fields.Char(string="發票號碼")
    contract_man = fields.Many2one('res.partner',string="聯絡人")
    contract_tel = fields.Char(string="聯絡電話")
    start_date = fields.Date(string="啟始日期")
    end_date = fields.Date(string="截止日期")
    amount_untax_total = fields.Float(digits=(13,2),string="合計金額(未稅)",compute='_get_amountuntax')
    amount_tax = fields.Float(digits=(10,2),string="稅金",compute='_get_tax')
    amount_tax_total = fields.Float(digits=(13,2),string="合計金額(含稅)",compute='_get_amounttotal')
    amount_balance = fields.Float(digits=(13,2),string="前期餘額",compute='_get_residual')
    total_real_amount = fields.Float(digits=(13,2),string="本期應收總計",compute='_get_real_tot')
    selectyn = fields.Boolean(string="勾選",default=False)
    account_move_line = fields.One2many('alldo_acme_iot.accountmove_selectitem_line','move_id',string="對帳明細")

    def _write(self, vals):

        res = super(acmeaccountmoveselectitem, self)._write(vals)
        for rec in self:
            self.env.cr.execute("""select updatetaiwanreceipt(%d)""" % rec.id)
            self.env.cr.execute("""commit""")

        return res

    @api.depends('partner_id')
    def _get_residual(self):
        for rec in self:
            # print(rec.partner_id.id)
            self.env.cr.execute("""select getpartnerresidual(%d)""" % rec.partner_id.id)
            myres = self.env.cr.fetchone()[0]
            rec.update({'amount_balance':myres - rec.amount_tax_total})

    @api.depends('amount_balance','amount_tax_total')
    def _get_real_tot(self):
        for rec in self:
            rec.total_real_amount = rec.amount_tax_total + rec.amount_balance

    @api.depends('account_move_line.amount_untax_num','account_move_line.selectyn')
    def _get_amountuntax(self):
        for rec1 in self:
            myamountuntaxtot = 0
            for rec in rec1.account_move_line:
                if rec.selectyn:
                    myamountuntaxtot = myamountuntaxtot + rec.amount_untax_num
            rec1.update({'amount_untax_total':myamountuntaxtot})

    @api.depends('account_move_line.amount_untax_num','account_move_line.amount_tax_num', 'account_move_line.selectyn')
    def _get_tax(self):
        for rec1 in self:
            mytaxtot = 0
            for rec in rec1.account_move_line:
                if rec.selectyn:
                    mytaxtot = mytaxtot + (rec.amount_tax_num - rec.amount_untax_num)
            rec1.update({'amount_tax': mytaxtot})

    @api.depends('account_move_line.amount_tax_num', 'account_move_line.selectyn')
    def _get_amounttotal(self):
        for rec1 in self:
            myamounttot = 0
            for rec in rec1.account_move_line:
                if rec.selectyn:
                    myamounttot = myamounttot + rec.amount_tax_num
            rec1.update({'amount_tax_total': myamounttot})


    def run_accountmove_line(self):
        if not self.name:
            self.env.cr.execute("""select getaccountseq('AR')""")
            myres = self.env.cr.fetchone()[0]
            self.name = myres
        if self.name:
            self.env.cr.execute("""select genaccountarno('%s')""" % myres)
            self.env.cr.execute("""commit""")



class acmeaccountmoveselectitemline(models.Model):
    _name = "alldo_acme_iot.accountmove_selectitem_line"
    _description = "對帳選單明細檔"

    move_id = fields.Many2one('alldo_acme_iot.accountmove_selectitem',ondelete='cascade')
    account_date = fields.Date(string="銷貨日期")
    sales_no = fields.Char(string="銷單號碼")
    ref = fields.Char(string="帳單號碼")
    prod_no = fields.Many2one('product.product',string="產品編號")
    prod_desc = fields.Char(string="品名規格")
    prod_num = fields.Float(digits=(10,2),string="數量")
    uom_id = fields.Many2one('uom.uom',string="單位")
    prod_price = fields.Float(digits=(10,2),string="單價")
    tax_type = fields.Many2one('account.tax',string="税別")
    amount_untax_num = fields.Float(digits=(11,2),string="金額(未稅)")
    amount_tax_num = fields.Float(digits=(11, 2), string="金額(含稅)")
    selectyn = fields.Boolean(string="勾選", default=False)
    account_move_line_id = fields.Integer(string="account move line id")

    def run_selectyn(self):
        for rec in self:
            if rec.selectyn==False:
                rec.update({'selectyn':True})
            else:
                rec.update({'selectyn':False})


