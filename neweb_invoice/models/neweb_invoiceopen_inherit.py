# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class newebinvoiceopeninherit(models.Model):
    _inherit = "neweb_invoice.invoiceopen"
    _order = "projectno desc"

    @api.depends('invoice_open_lines')
    def _get_cfuntaxamount(self):
        cfuntaxamount = 0
        for rec in self.invoice_open_lines:
            cfuntaxamount = cfuntaxamount + round(rec.invoice_untax_amount)
        self.cf_untax_amount = cfuntaxamount

    @api.depends('invoice_open_lines')
    def _get_cftaxamount(self):
        cftaxamount = 0
        for rec in self.invoice_open_lines:
            cftaxamount = cftaxamount + round(rec.invoice_tax)
        self.cf_tax_amount = cftaxamount

    @api.depends('invoice_open_lines')
    def _get_cftotalamount(self):
        cftotalamount = 0
        for rec in self.invoice_open_lines:
            cftotalamount = cftotalamount + round(rec.invoice_tax_amount)
        self.cf_total_amount = cftotalamount

    @api.depends('cus_order')
    def _get_cusorder(self):
        for rec in self:
            rec.purchase_no = rec.cus_order

    invoice_list_ids = fields.One2many('neweb_invoice.invopen_list','inv_id',copy=True,string="已開立記錄")
    invoice_contact1 = fields.Many2one('res.partner',string="收件人",domain=lambda self:self._gen_contact1)
    purchase_no = fields.Char(string="採購單號",compute=_get_cusorder)
    cus_order = fields.Char(string="客戶訂單")

    invoice_paymentdate = fields.Date(string="客戶付款日期")
    cf_untax_amount = fields.Float(digits=(11,0),string="未稅合計",store=False,compute=_get_cfuntaxamount)
    cf_tax_amount = fields.Float(digites=(8,0),string="稅金合計",store=False,compute=_get_cftaxamount)
    cf_total_amount = fields.Float(digits=(13,0),string="含稅合計",store=False,compute=_get_cftotalamount)



    @api.onchange('invoice_contact1')
    def onchange_contact(self):
        myrec = self.env['res.partner'].search([('id', '=', self.invoice_contact1.id)])
        self.invoice_phone = myrec.phone
        self.invoice_address = myrec.street


    @api.onchange('invoice_title')
    def onchange_invoicetitle(self):
        mytitle = self.invoice_title
        myrec = self.env['res.partner'].search([('name','like',mytitle)])
        myrec1 = self.env['res.partner'].search([('parent_id','in',[x.id for x in myrec])])
        ids = []
        for item in myrec1:
            ids.append(item.id)
        res = {}
        res['domain'] = {'invoice_contact1': [('id', 'in', ids)]}
        return res

    def _gen_contact1(self):
        mytitle = self.invoice_title
        myrec = self.env['res.partner'].search([('name', 'like', mytitle)])
        myrec1 = self.env['res.partner'].search([('parent_id', 'in', [x.id for x in myrec])])
        ids = []
        for item in myrec1:
            ids.append(item.id)
        res = [('id', 'in', ids)]
        return res
        # res = {}
        # res['domain'] = {'invoice_contact1': [('id', 'in', ids)]}
        # return res

    @api.onchange('project_no')
    def onchange_projno(self):
        myrec = self.env['neweb.project'].search([('id','=',self.project_no.id)])
        mycusnameid = myrec.cus_name.id
        mymaincusname = myrec.main_cus_name.id
        res={}
        res['domain'] = {'invoice_contact1':['|',('parent_id','=',mycusnameid),('parent_id','=',mymaincusname)]}
        return res


    def write(self,vals):
        for rec in self:
            myrec = self.env['neweb.project'].search([('id','=',rec.project_no.id)])
            vals['purchase_no']=myrec.cus_order
            myrec1 = self.env['sale.order'].search([('name','=',myrec.sale_no)])
            # print("%s" % myrec1.sitem_amounttot)
            # vals['project_amount_total']= round(myrec1.sitem_amounttot)
        res=super(newebinvoiceopeninherit,self).write(vals)
        # for rec1 in self:
        self.env.cr.execute("""select check_invoiceamounttot(%d)""" % self.id)
        myresult = self.env.cr.fetchone()
        # if not myresult[0] :
        #     raise UserError("開立金額已大於專案總金額，請確認！！")
        self.env.cr.execute("""select check_start_date(%d)""" % self.id)
        self.env.cr.execute("""select updatecusorder(%d)""" % self.id)

        return res


class newebinvoiceopenlist(models.Model):
    _name = "neweb_invoice.invopen_list"
    _sql_constraints = [('invitem_uniq', 'unique(inv_item)', 'Invoice Item must be unique!!')]
    _order = "inv_item asc"
    # _order = "sequence,id"
    _description = '發票開立/已開立記錄明細'

    inv_id = fields.Many2one('neweb_invoice.invoiceopen',ondelete='cascade',required=True)
    inv_item = fields.Integer(string="次",required=True)
    inv_date = fields.Date(string="開立日期",required=True)
    inv_cdate = fields.Char(string="C開立日期")
    inv_no = fields.Char(string="發票號碼",required=True)
    inv_open = fields.Selection([('1','生效'),('2','未生效')],string="狀態",default='2')
    inv_amount = fields.Float(digits=(10,0),string="本次開立金額")
    inv_totalamount = fields.Float(digits=(10,0),string="專案總金額",readonly=True)
    inv_memo = fields.Text(string="說明")

    @api.model
    def create(self, vals):
        self.env.cr.execute("select get_max_invitem(%d)" % vals['inv_id'])
        mymaxinvitem = self.env.cr.fetchone()
        vals['inv_item']=mymaxinvitem[0]
        res = super(newebinvoiceopenlist,self).create(vals)
        return res
