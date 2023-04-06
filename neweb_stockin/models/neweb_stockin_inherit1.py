# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class newebstockininherit1(models.Model):
    _inherit = "stock.picking"

    stockout_customer = fields.Char(string="聯絡人")
    stockout_customer1 = fields.Many2one('res.partner',string="連絡人")
    neweb_user_id = fields.Many2one('res.users',string="NEWEB聯絡人",default=lambda self:self.env.uid)
    neweb_phone = fields.Char(string="NEWEB聯絡人電話")
    neweb_email = fields.Char(string="NEWEB聯絡人EMAIL")
    neweb_address = fields.Char(string="NEWEB聯絡人地址")
    neweb_fax = fields.Char(string="NEWEB聯絡人傳真")




    # @api.depends('partner_id')
    # def _stockoutcus(self):
    #     self.stockout_customer = self.partner_id.name

    # @api.onchange('partner_id')
    # def onchangepartner(self):
    #     myparentid = self.partner_id.id

        
    # @api.onchange('stockout_proj_no')
    # def onpartnerchange(self):
    #     myopid = self.env.context.get('stockopid')
    #     mystockrec = self.env['stock.picking'].search([('id', '=', myopid)])
    #     myrec1=self.env['res.partner'].search([('parent_id','=',mystockrec.partner_id.id)])
    #     mypartner1=[]
    #     if myrec1:
    #         for rec in myrec1:
    #             mypartner1.append(rec.id)
    #     return {'domain':{'stockout_customer1':[('id','in',mypartner1)]}}

    def get_sale_info(self):
        myopid = self.env.context.get('stockopid')
        mystockrec = self.env['stock.picking'].search([('id','=',myopid)])
        mysaleno = mystockrec.origin
        if mystockrec.stockout_type=='1':
            myproj = self.env['neweb.project'].search([('sale_no','=',mysaleno)])
            myname=myproj.name
        elif mystockrec.stockout_type=='3':
            myname = self.env['ir.sequence'].next_by_code('neweb_stockin.outb')
        else:
            myname = self.env['ir.sequence'].next_by_code('neweb_stockin.outo')
        self.stockout_proj_no = myname


    @api.onchange('stockout_customer1')
    def onchangeclient(self):
        myrec = self.env['res.partner'].search([('id','=',self.stockout_customer1.id)])
        if myrec:
            self.stockout_custel = myrec.phone
            self.stockout_shipaddr = myrec.street
        myuserid = self.neweb_user_id
        self.neweb_phone = myuserid.employee_ids.work_phone
        self.neweb_email = myuserid.employee_ids.work_email


    @api.onchange('neweb_user_id')
    def onchangeclient1(self):
        if self.neweb_user_id :
            # myphone = self.neweb_user_id.employee_ids[0].work_phone.replace('(','').replace(')','').replace('-','')[0:2]
            myphone='02'
            if myphone == '07':
                newebaddress = '高雄市前鎮區中山二路260號21樓A1'
                newebfax = u'(07)-334-5639'
            elif myphone == '03':
                newebaddress = '新竹市東區慈雲路118號12樓之5'
                newebfax = u'(03)-577-7380'
            elif myphone == '04' :
                newebaddress = '台中市南區工學一街197巷32號'
                newebfax = u' '
            else:
                newebaddress = '114台北市內湖區行忠路42號2樓'
                newebfax = u'(02)-2795-5510'
            self.neweb_phone =  self.neweb_user_id.employee_ids[0].work_phone
            self.neweb_email =  self.neweb_user_id.employee_ids[0].work_email
            self.neweb_address = newebaddress
            self.neweb_fax = newebfax
            # self.update({'neweb_phone':self.neweb_user_id.employee_ids[0].work_phone,
            #             'neweb_email':self.neweb_user_id.employee_ids[0].work_email,
            #             'neweb_address':newebaddress,
            #             'neweb_fax':newebfax})

