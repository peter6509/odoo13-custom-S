# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api,_
from odoo import exceptions


class newebpurinvoice(models.Model):
    _name = "neweb_purinv.invoice"
    _description = "請款申請作業"
    _order = "name desc"

    @api.depends('invoice_line')
    def _get_invoicetot(self):
        mysum = 0
        for rec in self.invoice_line:
            mysum += rec.invoice_sum
        self.invoice_total = mysum

    @api.depends('invoice_line.currency_id')
    def _get_purcurrency(self):
        myres = False
        for rec in self.invoice_line:
            myres = rec.currency_id.id
            self.currency_id = rec.currency_id.id
        return myres

    name = fields.Char(string="請款單號",default='New',copy=False)
    invoice_total = fields.Float(digits=(10,0),string="請款總金額(含税)",compute=_get_invoicetot,store=True)
    invoice_memo = fields.Text(string="補充說明")
    invoice_line = fields.One2many('neweb_purinv.invoiceline','invline_id',string="請款明細",copy=True,track_visibility="onchange")
    currency_id = fields.Many2one('res.currency', compute=_get_purcurrency,store=False)
    is_signed = fields.Boolean(string="是否授權",default=False)
    report_date = fields.Date(string="製表日期")
    purinv_type = fields.Selection([('1','進貨請款'),('2','維護請款'),('3','其他費用請款')],string="請款項目",default='1')


    def copy(self, default=None):
        default = dict(default or {})
        myname = self.env['ir.sequence'].next_by_code('neweb_purinv.purinvoice')
        default.update({'name':myname,})
        return super(newebpurinvoice, self).copy(default)


    is_closed = fields.Boolean(string="是否結案",default=False)


    def set_closed(self):
        for rec in self:
            rec.update({'is_closed':True})


    def set_reject(self):
        for rec in self:
            rec.update({'is_closed':False , 'is_signed':False})




    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('neweb_purinv.purinvoice') or _('New')
        if 'invoice_total' in vals and vals['invoice_total'] <= 0 :
            raise exceptions.UserError("請款總金額必須大於0")
        res = super(newebpurinvoice,self).create(vals)
        self.env.cr.execute("""select invlineitem(%d)""" % res.id)
        # for rec in res.invoice_line:
        #     self.env.cr.execute("""select get_invoicedate(%d)""" % rec.id)
        return res


    def write(self, vals):
        res = super(newebpurinvoice, self).write(vals)
        for rec1 in self:
            self.env.cr.execute("""select invlineitem(%d)""" % rec1.id)
            self.env.cr.execute("""commit""")
        for rec in self.invoice_line:
            self.env.cr.execute("""select get_invoicedate(%d)""" % rec.id)
            self.env.cr.execute("""commit""")

        return res

    def re_index_item(self):
        self.env.cr.execute("""select invlineitem(%d)""" % self.id)
        self.env.cr.execute("""commit""")

    def regen_invdate(self):
        for rec in self.invoice_line:
            self.env.cr.execute("""select get_invoicedate(%d)""" % rec.id)
            self.env.cr.execute("""commit""")






class newebpurinvoiceline(models.Model):
    _name = "neweb_purinv.invoiceline"
    _description = "請款申請明細"
    _order = "invline_item"

    # @api.depends('invoice_date')
    # def _get_paymentterm(self):
    #     for rec in self:
    #         self.env.cr.execute("""select get_invoicedate1(%s)""" % rec.id)
    #         rec.inv_paymentterm = self.env.cr.fetchone()[0]

    invline_id = fields.Many2one('neweb_purinv.invoice',required=True,ondelete="cascade")
    inv_prodspec = fields.Char(string="品名")
    cus_partner = fields.Char(string="客戶簡稱")
    purchase_no = fields.Many2one('purchase.order',string="採購單號")
    pitem_origin_no = fields.Char(string="來源單號")
    inv_paymentterm = fields.Date(string="付款期限")
    currency_id = fields.Many2one('res.currency',string="幣別")
    invoice_sum = fields.Float(digits=(10,0),string="付款金額(含税)")
    invoice_partner = fields.Many2one('res.partner',string="付款對象")
    taxes_id = fields.Many2one('account.tax',string="税別")
    invoice_date = fields.Date(string="發票日期")
    invoice_no = fields.Char(string="發票號碼")
    payment_yn = fields.Selection([('1','N'),('2','Y')],string="是否請款",default='1')
    sequence = fields.Integer(string="sequence",default=10)
    invline_memo = fields.Text(string="備註")
    invline_item = fields.Float(digits=(4,1),string="項次")
    purinvtype = fields.Selection([('1','進貨請款'),('2','維護請款'),('3','其他費用請款')],string="請款項目",related="invline_id.purinv_type")

    @api.onchange('invoice_date')
    def onchangeinvdate(self):
        try:
            self.env.cr.execute("""select get_invoicedate1(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            if not self.inv_paymentterm:
               self.inv_paymentterm = myres
        except:
            A=1


    def run_select_puritem(self):
        mypurid = self.purchase_no.id
        self.env.cr.execute("""select genselectpuritem(%d)""" % mypurid)
        self.env.cr.execute("""commit""")



    # def write(self,vals):
    #     res = super(newebpurinvoiceline,self).write(vals)
        # myinvid = self.id
        # self.env.cr.execute("""select get_invoicedate(%s)""" % (myinvid))
        # return res


    def unlink(self):
        for rec in self:
            myid = rec.purchase_no.id
            # mypitemlist = self.env['neweb.pitem_list'].search([('pitem_id','=',myid)])
            # if mypitemlist:
            if myid:
               self.env.cr.execute("""select updateapselect(%s,%s)""" % (myid, False))
            # self.env.cr.execute("commit")
               mypurchaserec = self.env['purchase.order'].search([('id', '=', myid)])
               self.env.cr.execute("""select checkpurapselect(%d)""" % mypurchaserec.id)
            #self.env.cr.execute("commit")


        res = super(newebpurinvoiceline,self).unlink()
        return res


class newebinvoicepurchase(models.Model):
    _inherit = ["purchase.order"]

    invoice_mark = fields.Boolean(string="已請款?",default=False)
    invoice_complete = fields.Boolean(string="已請款完成",default=False)
    invoice_openamount = fields.Float(digits=(10,0),store=True,string="已請金額",default=0)
    invoice_time = fields.Integer(string="第幾次請款?",default=1)


