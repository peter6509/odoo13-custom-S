# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from datetime import datetime,timedelta

class NewebAcceptance(models.Model):
    _name = "neweb.acceptance"
    _description = "專案驗收狀態控管"

    @api.depends('acceptanced_date1','acceptanced_date2')
    def _get_alerttags(self):
        for rec in self:
            if (rec.acceptanced_date2 == False and rec.acceptanced_date1 > datetime.today()) :
                rec.alert_tags = '2'
            elif (rec.acceptanced_date2 > rec.acceptanced_date1 and rec.acceptanced_date1 != False) :
                rec.alert_tags = '2'
            else:
                rec.alert_tags = '1'

    keyin_date = fields.Date(string="填單日")
    purchase_no = fields.Char(string="採購單號")
    purchase_date = fields.Date(string="採購日期")
    proj_date = fields.Date(string="專案成立日")
    stockout_no = fields.Char(string="出貨單號")
    stockout_no1 = fields.Many2one('stock.picking',string="出貨單號")
    project_no = fields.Many2one('neweb.project',string="專案編號")
    project_no1 = fields.Char(string="專案編號C")
    acceptance_status = fields.Selection([('1','未驗收'),('2','已驗收')],string="驗收狀態",default='1')
    proj_sale = fields.Many2one('hr.employee', string="業務")
    cus_name = fields.Many2one('res.partner', string="客戶名稱")
    cus_project = fields.Char(string="客戶專案/標案名稱")
    prod_no = fields.Char(string="產品料號")
    prod_modeltype = fields.Char(string="機種-機型/料號")
    prod_desc = fields.Text(string="規格說明")
    prod_num = fields.Float(digits=(10, 0), string="數量")
    supplier = fields.Char(string="供應商")
    acceptanced_date1 = fields.Date(string="預計驗收日")
    stockin_date = fields.Date(string="收貨日期")
    stockout_date = fields.Date(string="出貨日期")
    acceptanced_date2 = fields.Date(string="結案日")
    projsaleitem_status = fields.Selection([('1', '貨在公司待貨齊'), ('2', '貨在公司待出貨'), ('3', '貨在公司測試安裝中'), ('4', '貨在客戶端待貨齊'), ('5', '貨在客戶端待裝機'),
         ('6', '貨在客戶端裝機中'), ('7', '貨在客戶端待驗收'), ('8', '貨在客戶端驗收中')], string="狀態",default='1')
    memo = fields.Text(string="狀態說明")
    active = fields.Boolean(string="ACTIVE",default=True)
    acceptance_line = fields.One2many('neweb.acceptance_line','acceptance_id',copy=False)
    own_user1 = fields.Many2one('res.users',string="own1")
    own_user2 = fields.Many2one('res.users', string="own2")
    alert_tags = fields.Selection([('1','正常'),('2','異常')],string="驗收狀態",compute=_get_alerttags)

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.stockout_no, myrec.project_no.name)
            result.append((myrec.id, myname))
        return result

    def run_acceptance_child(self):
        myacceptanceid = self.env.context.get('acceptance_id')
        mydomain = []
        mydomain.append(('id', '=', myacceptanceid))
        myviewid = self.env.ref('neweb_acceptance.view_neweb_acceptance_child_form')

        return {'view_name': 'NEWEB ACCEPTANCE CHILD LIST',
                'name': ('NEWEB ACCEPTANCE CHILD LIST'),
                'views': [[False, 'form'],[False, 'tree']],
                'res_model': 'neweb.acceptance',
                # 'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'self',
                'domain':mydomain,
                'view_id':myviewid.id,
                'res_id': myacceptanceid,
                'view_mode': 'form',
                'view_type': 'form',
                # 'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }

    # 每天檢查是否為月初1號
    def run_month_work(self):
        self.env.cr.execute("""select ismonth1day();""")
        myres = self.env.cr.fetchone()[0]  # myres = True 今天為1號
        if myres:
            self.env.cr.execute("""select genprojacceptance()""")
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select gen_purno_supp()""")
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select geninvprojamount()""")
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select genaccsecurity()""")
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select genacceptancedate()""")
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select genacceptanceemail()""")
            self.env.cr.execute("""commit""")

    # 每天檢查例行工作
    def run_day_work(self):
        self.env.cr.execute("""select gennewprojacceptance()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gen_purno_supp()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select genprojinvcomplete()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select genacceptancedate()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select genaccsecurity()""")
        self.env.cr.execute("""commit""")



class NewebAcceptanceLine(models.Model):
    _name = "neweb.acceptance_line"
    _description = "貨品出貨單狀態明細"

    acceptance_id = fields.Many2one('neweb.acceptance',ondelete='cascade')
    keyin_date = fields.Date(string="填單日")
    purchase_no = fields.Char(string="採購單號")
    purchase_date = fields.Date(string="採購日期")
    stockout_no = fields.Many2one('stock.picking', string="出貨單號")
    stockout_no1 = fields.Char(string="出貨單號")
    project_no = fields.Many2one('neweb.project', string="專案編號")
    project_no1 = fields.Char(string="專案編號C")
    acceptance_status = fields.Selection([('1', '未驗收'), ('2', '已驗收')], string="驗收狀態", default='1')
    proj_sale = fields.Many2one('hr.employee', string="業務")
    cus_name = fields.Many2one('res.partner', string="客戶名稱")
    cus_project = fields.Char(string="客戶專案/標案名稱")
    prod_no = fields.Char(string="產品料號")
    prod_modeltype = fields.Char(string="機種-機型/料號")
    prod_desc = fields.Text(string="規格說明")
    prod_num = fields.Float(digits=(10, 0), string="數量")
    supplier = fields.Char(string="供應商")
    acceptanced_date1 = fields.Date(string="預計驗收日")
    stockin_date = fields.Date(string="收貨日期")
    stockout_date = fields.Date(string="出貨日期")
    acceptanced_date2 = fields.Date(string="結案日")
    proj_date = fields.Date(string="專案建立日期")
    projsaleitem_status = fields.Selection([('1', '貨在公司待貨齊'), ('2', '貨在公司待出貨'), ('3', '貨在公司測試安裝中'), ('4', '貨在客戶端待貨齊'), ('5', '貨在客戶端待裝機'),
         ('6', '貨在客戶端裝機中'), ('7', '貨在客戶端待驗收'), ('8', '貨在客戶端驗收中')], string="狀態", default='1')
    memo = fields.Text(string="狀態說明")
    accym = fields.Char(string="年月")
    active = fields.Boolean(string="ACTIVE")
    projsaleitem_id = fields.Integer(string="projsaleitem id")

class NewebAcceptanceemail(models.Model):
    _name = "neweb_acceptance.email"
    _description = "每月貨品出貨狀態回報Email通知"
    _order = "accym desc"

    proj_sale = fields.Many2one('hr.employee', string="業務")
    url_address = fields.Char(string="內部連結")
    url_address1 = fields.Char(string="外部連結")
    send_date = fields.Date(string="預定發送日期")
    send_date1 = fields.Date(string="實際發送日期")
    accym = fields.Char(string="年月")
    email_line = fields.One2many('neweb_acceptance.email_line','line_id',copy=False)
    active = fields.Boolean(string="ACTIVE", default=True)

    def get_acceptance_email(self,projsale):
        myids = self.env['hr.employee'].search([('id', '=', projsale.id)])
        all_mails = []
        for item in myids:
            all_mails.append(item.work_email)
        return ','.join(str(mail) for mail in all_mails)

    def acceptance_sendmail(self):
        '''
        This function opens a window to compose an email, with the edi purchase request template message loaded by default
        '''
        self.env.cr.execute("""select ismonth1day();""")
        myres = self.env.cr.fetchone()[0]  # myres = True 今天為1號
        # if myres:
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_acceptance', 'email_template_neweb_acceptance')[1]
        except ValueError:
            template_id = False
        myrec = self.env['neweb_acceptance.email'].search([('send_date1', '=', False)])
        for rec in myrec:
             self.env['mail.template'].browse(template_id).sudo().send_mail(rec.id)
             rec.update({'active': False,'send_date1': datetime.now()})
             # rec.send_date1 = datetime.now()



class  NewebAcceptanceemailline(models.Model):
    _name = "neweb_acceptance.email_line"
    _description = "每月貨品出貨狀態回報Email通知明細"
    _order = "project_no,stockout_no"

    line_id = fields.Many2one('neweb_acceptance.email',ondelete='cascade')
    project_no = fields.Many2one('neweb.project', string="專案編號")
    stockout_no = fields.Char(string="出貨單號")
    cus_name = fields.Many2one('res.partner', string="客戶名稱")
    acceptanced_date1 = fields.Date(string="預計驗收日")
    stockin_date = fields.Date(string="收貨日期")
    stockout_date = fields.Date(string="出貨日期")
    projsaleitem_status = fields.Selection([('1', '貨在公司待貨齊'), ('2', '貨在公司待出貨'), ('3', '貨在公司測試安裝中'), ('4', '貨在客戶端待貨齊'), ('5', '貨在客戶端待裝機'),
         ('6', '貨在客戶端裝機中'), ('7', '貨在客戶端待驗收'), ('8', '貨在客戶端驗收中')], string="目前狀態")
    last_send_mail = fields.Datetime(string="發信日期")


