# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api,_
from odoo import exceptions
import datetime


class newebofficialdoc(models.Model):
    _name = "neweb_sale_analysis.official_doc"
    _description = "公文列印作業"

    name = fields.Char(string="發文字號",default='New')
    send_owner = fields.Many2one('res.users',string="發文者",default=lambda self:self.env.uid)
    send_name = fields.Char(string="聯絡人")
    send_address = fields.Char(string="地址")
    send_phone = fields.Char(string="電話")
    send_phoneext =fields.Char(string="分機")
    send_fax = fields.Char(string="傳真")
    send_email = fields.Char(string="電子信箱")
    receiver_owner = fields.Many2one('res.partner',string="受文者",track_invisibility='onchange')
    receiver_address = fields.Char(string="受文者地址")
    receiver_zip = fields.Char(string="郵遞區號")
    doc_date = fields.Date(string="發文日期")
    doc_date_y = fields.Char(string="年")
    doc_date_m = fields.Char(string="月")
    doc_date_d = fields.Char(string="日")
    doc_urgent = fields.Selection([('1','最速件'),('2','速件'),('3','普通件'),('4','特別件')],string="速別")
    doc_security = fields.Selection([('1','絕對機密'),('2','極機密'),('3','密')],string="文件密等說明")
    doc_attach = fields.Char(string="附件")
    doc_subject = fields.Text(string="主旨")
    doc_memo = fields.Text(string="說明")
    doc_set1 = fields.Char(string="正本")
    doc_set2 = fields.Char(string="副本")

    is_signed = fields.Boolean(string="是否授信",default=False)

    @api.onchange('receiver_owner')
    def onclientowner(self):
        self.doc_set1 = self.receiver_owner.name


    def set_signed(self):
    	for rec in self:
    		rec.update({'is_signed':True})


    def set_reject(self):
        for rec in self:
            rec.update({'is_closed':False , 'is_signed':False})

    is_closed = fields.Boolean(string="是否結案",default=False)


    def set_closed(self):
        for rec in self:
            rec.update({'is_closed':True})

    @api.onchange('send_owner')
    def onclientchangesend(self):
        self.send_name = self.send_owner.employee_ids[0].resource_id.name
        self.send_address = self.send_owner.partner_id.street
        self.send_phone = self.send_owner.partner_id.phone
        self.send_fax = self.send_owner.partner_id.fax
        self.send_email = self.send_owner.partner_id.email

    @api.onchange('receiver_owner')
    def onclientchangereceiver(self):
        self.receiver_address = self.receiver_owner.street


    def _get_year(self):
        self.doc_date_y = str(int(datetime.datetime.now().year) - 1911)



    @api.model
    def create(self,vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('neweb_sale_analysis.official_doc') or _('New')
            myname = vals['name']
            aa = myname[:4]
            bb = myname[4:]
            cc = str(int(aa) - 1911)
            vals['name']= cc+bb
        res=super(newebofficialdoc,self).create(vals)
        self.env.cr.execute("""select getofficialdate(%d)""" % res.id)
        self.env.cr.execute("commit")
        return res


    def write(self,vals):
        if 'doc_date' in vals and vals['doc_date']:
            self.env.cr.execute("""select getofficialdate(%d)""" % self.id)
            self.env.cr.execute("commit")
        res=super(newebofficialdoc,self).write(vals)
        return res
