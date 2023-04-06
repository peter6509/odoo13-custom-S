# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from datetime import datetime,timedelta

class NewebInvoiceReminder_alert(models.Model):
    _name = "neweb_invoice.reminder_alert"
    _description = "reminder_alert清單主檔"
    _order = "partner_id"


    @api.depends('ra_line')
    def _get_ra_num(self):
        for rec in self:
            mynum = 0
            for rec1 in rec.ra_line:
                mynum += 1
            rec.reminder_alert_num = mynum

    @api.depends()
    def _get_saleassist(self):
        self.env.cr.execute("""select getsaleassist()""")
        myassist=self.env.cr.fetchone()[0]
        for rec in self:
            rec.sale_assist = myassist


    send_date = fields.Date(string="預定發送日期")
    send_date1 = fields.Date(string="實際發送日期")
    partner_id = fields.Many2one('res.partner',string="客戶名稱")
    invoice_contact1 = fields.Many2one('res.partner',string="收件人")
    is_send = fields.Boolean(string="已發送？",default=False)
    cando = fields.Boolean(string="執行否？",default=False)
    sale_assist = fields.Char(string="業助",compute=_get_saleassist)
    sendmail_type = fields.Selection([('1','開立後7天發信'),('2','收款前7日提醒'),('3','收款逾期警示')],string="發信類別")
    ra_line = fields.One2many('neweb_invoice.reminder_alert_line','ra_id',copy=False)
    inv_year = fields.Char(string="對帳年")
    inv_month = fields.Char(string="對帳月")
    reminder_alert_num = fields.Integer(string="應收帳比數",compute=_get_ra_num)
    active = fields.Boolean(string="ACTIVE")
    own_user1 = fields.Many2one('res.users', string="own1")
    own_user2 = fields.Many2one('res.users', string="own2")


    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s-%s" % (myrec.partner_id.comp_sname, myrec.inv_year,myrec.inv_month)
            result.append((myrec.id, myname))
        return result

    # 每日查檢是否為1日產生 reminder_alert data
    def run_month_reminder_alert(self):
        # 確認今日是否為週1
        # self.env.cr.execute("""select ismonth1day()""")
        # self.env.cr.execute("""select isweek1day()""")
        # myres = self.env.cr.fetchone()[0]
        # if myres:
        self.env.cr.execute("""select gen_month_reminder()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gen_month_alert()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gen_reminder_alert_security()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gencandoremindermail()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gencandoalertmail()""")
        self.env.cr.execute("""commit""")

    # 測試環境版的 get_reminder_email
    def get_reminder_email(self,contact1):
        all_mails = []
        for rec in self.ra_line:
            all_mails.append(rec.project_no.proj_sale.work_email)
        sale_email = self.project_no.proj_sale.work_email
        if sale_email:
            all_mails.append(sale_email)         # 專案業務
        all_mails.append('irene.cheng@newebinfo.com.tw')
        all_mails.append('annie.lee@newebinfo.com.tw')
        myass_rec = self.env['neweb_acceptance.assist']
        for rec1 in myass_rec:
            all_mails.append(rec1.assist_email)   # 業助email
        if self.invoice_contact1.email != False:
           all_mails.append(self.invoice_contact1.email)     # 客戶聯絡人
        return ','.join(str(mail) for mail in all_mails)

    # 正式環境版本的 get_reminder_email
    # def get_reminder_email(self,contact1):
    #     myids = self.env['res.partner'].search([('id', '=', contact1)])
    #     all_mails = []
    #     for item in myids:
    #         all_mails.append(item.email)         # 客戶聯絡人
    #     sale_email = self.project_no.proj_sale.work_email
    #     if sale_email:
    #         all_mails.append(sale_email)         # 專案業務
    #     myass_rec = self.env['neweb_acceptance.assist']
    #     for rec1 in myass_rec:
    #         all_mails.append(rec1.assist_email)   # 業助email
    #     return ','.join(str(mail) for mail in all_mails)

    # 測試環境版的 get_alert_email
    def get_alert_email(self,contact1):
        all_mails = []
        all_mails.append('irene.cheng@newebinfo.com.tw')
        all_mails.append('annie.lee@newebinfo.com.tw')
        for rec in self.ra_line:
            all_mails.append(rec.project_no.proj_sale.work_email)
        myass_rec = self.env['neweb_acceptance.assist']
        for rec1 in myass_rec:
            all_mails.append(rec1.assist_email)   # 業助email
        return ','.join(str(mail) for mail in all_mails)

    # 正式環境版本的 get_alert_email
    # def get_alert_email(self,contact1):
    #     myids = self.env['res.partner'].search([('id', '=', contact1)])
    #     all_mails = []
    #     for item in myids:
    #         all_mails.append(item.email)         # 客戶聯絡人
    #     sale_email = self.project_no.proj_sale.work_email
    #     if sale_email:
    #         all_mails.append(sale_email)         # 專案業務
    #     myass_rec = self.env['neweb_acceptance.assist']
    #     for rec1 in myass_rec:
    #         all_mails.append(rec1.assist_email)   # 業助email
    #     return ','.join(str(mail) for mail in all_mails)

    # cron job 每日執行一次 (付款日前7天 通知客戶＆業務＆業助)
    def run_invoice_reminder(self):
        '''This function opens a window to compose an email, with the edi purchase request template message loaded by default'''
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_invoice', 'mail_neweb_invoice_reminder')[1]
        except ValueError:
            template_id = False
        self.env.cr.execute("""select gencandoremindermail()""")
        self.env.cr.execute("""commit""")
        myrec = self.env['neweb_invoice.reminder_alert'].search([('is_send', '=', False), ('cando', '=', True), ('sendmail_type', '=', '2')])
        for rec in myrec:
            self.env['mail.template'].browse(template_id).sudo().send_mail(rec.id)
            rec.is_send = True
            rec.send_date1 = datetime.now()

    # cron job 每日執行一次 (付款日超過7天未付 警示客戶＆業務＆業助)
    def run_invoice_alert(self):
        '''This function opens a window to compose an email, with the edi purchase request template message loaded by default'''
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_invoice', 'mail_neweb_invoice_alert')[1]
        except ValueError:
            template_id = False
        self.env.cr.execute("""select gencandoalertmail()""")
        self.env.cr.execute("""commit""")
        myrec = self.env['neweb_invoice.reminder_alert'].search([('is_send', '=', False), ('cando', '=', True), ('sendmail_type', '=', '3')])
        for rec in myrec:
            self.env['mail.template'].browse(template_id).sudo().send_mail(rec.id)
            rec.is_send = True
            rec.send_date1 = datetime.now()

class NewebInvoiceReminderAlertLine(models.Model):
    _name = "neweb_invoice.reminder_alert_line"
    _description = "reminder_alert清單明細檔"

    @api.depends('project_no', 'contract_no')
    def _get_project_contract(self):
        for rec in self:
            pc = ' '
            if rec.contract_no:
                pc = rec.project_no.name + ' /' + rec.contract_no.name
            else:
                pc = rec.project_no.name
            rec.project_contract = pc

    @api.depends('project_no')
    def _get_pi_projectname(self):
        for rec in self:
            pp = ' '
            if rec.project_no.cus_order:
                if pp == ' ':
                    pp = rec.project_no.cus_order
            if rec.project_no.cus_project:
                if pp == ' ':
                    pp = rec.project_no.cus_project
                else:
                    pp = pp + ' /' + rec.project_no.cus_project
            rec.pi_projectname = pp

    @api.depends('invoice_no')
    def _get_paymentdate(self):
        myrec = self.env['neweb_invoice.invoiceopen_line'].search([('invoice_no', '=', self.invoice_no)], limit=1)
        for rec in self:
            rec.invoice_paymentdate = myrec.receive_date

    @api.depends('project_no')
    def _get_projsale(self):
        for rec in self:
            rec.proj_sale = rec.project_no.proj_sale.name

    ra_id = fields.Many2one('neweb_invoice.reminder_alert',ondelete='cascade')
    invoice_date = fields.Date(string="開立日期")
    project_no = fields.Many2one('neweb.project', string="專案編號")
    contract_no = fields.Many2one('neweb_contract.contract', string="合約編號")
    invoice_no = fields.Char(size=10, string="發票號碼")
    invoice_tax_amount = fields.Float(digits=(13, 0), string="含稅合計")
    invoice_paymentdate = fields.Date(string="客戶付款日期")
    project_contract = fields.Char(string="專案/合約", compute=_get_project_contract)
    pi_projectname = fields.Char(string="PI/案號", compute=_get_pi_projectname)
    proj_sale = fields.Char(string="業務",compute=_get_projsale)
