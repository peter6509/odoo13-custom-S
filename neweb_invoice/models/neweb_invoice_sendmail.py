# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from datetime import datetime,timedelta

class NewebInvoiceSendmail(models.Model):
    _name = "neweb_invoice.invoice_sendmail"
    _description = "傳送給客戶Email清單主檔"
    _order = "invoice_no"

    @api.depends('sendmail_line')
    def _get_untaxamount(self):
        for rec1 in self:
            myamount = 0
            for rec in rec1.sendmail_line:
                myamount += rec.invoice_num * rec.invoice_unit_price
            rec1.invoice_untax_amount = myamount


    @api.depends('sendmail_line')
    def _get_taxamount(self):
        for rec1 in self:
            mytaxamount = 0
            for rec in rec1.sendmail_line:
                mytaxamount += (rec.invoice_num * rec.invoice_unit_price1)
            rec1.invoice_tax_amount = round(mytaxamount)

    @api.depends('invoice_tax_amount')
    def _get_taxamount1(self):
        for rec in self:
            rec.invoice_tax_amount1 = "NT$ " + '{0:,.0f}'.format(rec.invoice_tax_amount)

    @api.depends()
    def _get_saleassist(self):
        myrec=self.env['neweb_acceptance.assist'].search([])
        myassist=''
        for line in myrec:
            if myassist=='':
                myassist = line.sale_assist
            else:
                myassist = myassist + ' /' + line.sale_assist
        for rec in self:
            rec.sale_assist = myassist

    @api.depends('invoice_no')
    def _get_paymentdate(self):
        for rec in self:
            myrec = self.env['neweb_invoice.invoiceopen_line'].search([('invoice_no', '=', rec.invoice_no)], limit=1)
            rec.invoice_paymentdate = myrec.receive_date

    @api.depends('project_no','contract_no')
    def _get_project_contract(self):
        for rec in self:
            pc = ''
            if rec.contract_no:
                pc = rec.project_no.name + ' /' + rec.contract_no.name
            else:
                pc = rec.project_no.name
            rec.project_contract = pc

    @api.depends('project_no')
    def _get_pi_projectname(self):
        for rec in self:
            pp = ''
            if rec.project_no.cus_order:
                if pp == '':
                    pp = rec.project_no.cus_order
            if rec.project_no.cus_project:
                if pp == '':
                    pp = rec.project_no.cus_project
                else:
                    pp = pp + ' /' + rec.project_no.cus_project
            rec.pi_projectname = pp


    invoice_date = fields.Date(string="開立日期")
    send_date = fields.Date(string="預計發送日期")
    send_date1 = fields.Date(string="實際發送日期")
    partner_id = fields.Many2one('res.partner',string="客戶名稱")
    invoice_contact1 = fields.Many2one('res.partner',string="收件人")
    project_no = fields.Many2one('neweb.project',string="專案編號")
    contract_no = fields.Many2one('neweb_contract.contract', string="合約編號")
    invoice_untax_amount = fields.Float(digits=(13, 2), store=False, string="未稅合計", compute=_get_untaxamount)
    invoice_tax_amount = fields.Integer(store=False, string="含稅合計", compute=_get_taxamount)
    invoice_tax_amount1 = fields.Char(string="含稅合計",compute=_get_taxamount1)
    invoice_taxtype = fields.Many2one('account.tax', string='稅')
    invoice_no = fields.Char(size=10, string="發票號碼")
    is_send = fields.Boolean(string="已發送？",default=False)
    cando = fields.Boolean(string="執行否？",default=False)
    invoice_paymentdate = fields.Date(string="客戶付款日期",compute=_get_paymentdate)
    # invoice_paymentdate1 = fields.Char(string="客戶付款日期", compute=_get_paymentdate1)
    sale_assist = fields.Char(string="業助",compute=_get_saleassist)
    sendmail_type = fields.Selection([('1','開立後7天發信'),('2','預計收款日前7日'),('3','收款逾期發信')],string="發信類別")
    sendmail_line = fields.One2many('neweb_invoice.invoice_sendmail_line','sendmail_id',copy=False)
    own_user1 = fields.Many2one('res.users', string="own1")
    own_user2 = fields.Many2one('res.users', string="own2")
    project_contract = fields.Char(string="專案/合約",compute=_get_project_contract)
    pi_projectname = fields.Char(string="PI/案號",compute=_get_pi_projectname)

    def thousand_sep(num):
        return ("{:,}".format(num))

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.partner_id.comp_sname, myrec.invoice_no)
            result.append((myrec.id, myname))
        return result

    def get_paymentdate_email(self,contact1):
        all_mails = []
        sale_email = self.project_no.proj_sale.work_email
        if sale_email:
            all_mails.append(sale_email)  # 專案業務
        all_mails.append('irene.cheng@newebinfo.com.tw')
        all_mails.append('annie.lee@newebinfo.com.tw')
        cus_email = self.invoice_contact1.email
        if cus_email:
            all_mails.append(cus_email)  # 客戶收件人
        return ','.join(str(mail) for mail in all_mails)

    # def get_paymentdate_email(self,contact1):
    #     myids = self.env['res.partner'].search([('id', '=', contact1)])
    #     all_mails = []
    #     for item in myids:
    #         all_mails.append(item.email)  # 客戶聯絡人
    #     sale_email = self.project_no.proj_sale.work_email
    #     if sale_email:
    #         all_mails.append(sale_email)  # 專案業務
    #     return ','.join(str(mail) for mail in all_mails)

    # cron job 每日執行一次 (更新 invoice sendmail new)
    def run_update_sendmail_new(self):
        myrec = self.env['neweb_invoice.invoice_sendmail'].sudo().search([('is_send', '=', False), ('cando', '=', True), ('sendmail_type', '=', '1'), ('partner_id', '!=', False)])
        for rec in myrec:
            self.env.cr.execute("""select updatesendmailnew(%d)""" % rec.id)
            self.env.cr.execute("""commit""")


    # cron job 每日執行一次 (開立發票後7天 通知客戶＆業務)
    def run_invoice_sendmail(self):
        '''This function opens a window to compose an email, with the edi purchase request template message loaded by default'''
        # self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_invoice', 'mail_neweb_invoice_paymentdate')[1]
        except ValueError:
            template_id = False
        self.env.cr.execute("""select gencandoinvmail()""")
        self.env.cr.execute("""commit""")
        myrec = self.env['neweb_invoice.invoice_sendmail'].sudo().search([('is_send','=',False),('cando','=',True),('sendmail_type','=','1'),('partner_id','!=',False),('send_date1','=',False)])
        for rec in myrec:
            self.env['mail.template'].browse(template_id).sudo().send_mail(rec.id)
            rec.update({'is_send':True, 'send_date1': datetime.now()})



class NewebInvoiceSendmailLine(models.Model):
    _name = "neweb_invoice.invoice_sendmail_line"
    _description = "傳送給客戶Email清單明細檔"

    @api.depends('invoice_num', 'invoice_unit_price', 'invoice_unit_price1')
    def _get_untaxamount(self):
        for rec in self:
            rec.invoice_untax_amount = rec.invoice_num * rec.invoice_unit_price

    @api.depends('invoice_num', 'invoice_unit_price1')
    def _get_taxamount(self):
        for rec in self:
            # mytaxamount = round((rec.invoice_num * rec.invoice_unit_price) * 1.05 ,0)
            mytaxamount = (rec.invoice_num * rec.invoice_unit_price1)
            rec.update({'invoice_tax_amount': mytaxamount})
            return mytaxamount

    sendmail_id = fields.Many2one('neweb_invoice.invoice_sendmail',ondelete='cascade')
    invoice_spec = fields.Text(string="品名")
    invoice_num = fields.Integer(size=5, string="數量", default=1)
    invoice_unit_price = fields.Float(digits=(11, 2), string="單價", default=0)
    invoice_untax_amount = fields.Float(digits=(13, 2), store=False, string="未稅合計", compute=_get_untaxamount)
    invoice_unit_price1 = fields.Float(digits=(11, 2), string="含稅價", default=0)
    invoice_tax_amount = fields.Float(digits=(13, 2), store=False, string="含稅合計", compute=_get_taxamount)
    invoice_taxtype = fields.Many2one('account.tax', string='稅')
    inv_sequence_id = fields.Integer(string="INV ID")
