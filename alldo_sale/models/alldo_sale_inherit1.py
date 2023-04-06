# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
# import odoo.addons.decimal_precision as dp


class alldosaleinherit1(models.Model):
    _inherit = "sale.order"

    @api.depends('partner_id')
    def _get_partnername(self):
        for rec in self:
            mypartnername =' '
            if rec.partner_id:
                mypartnername = rec.partner_id.name
            rec.partnername = mypartnername
            return mypartnername

    @api.depends('contact_id')
    def _get_contactname(self):
        for rec in self:
            mycontactname = ' '
            if rec.contact_id:
                mycontactname = rec.contact_id.name
            rec.contactname = mycontactname
            return mycontactname

    @api.depends('contact_id')
    def _get_contactphone(self):
        for rec in self:
            mycontactphone = ' '
            if rec.contact_id:
                mycontactphone = rec.contact_id.phone
            rec.contactphone = mycontactphone
            return mycontactphone

    @api.depends('contact_id')
    def _get_contactemail(self):
        for rec in self:
            mycontactemail = ' '
            if rec.contact_id:
                mycontactemail = rec.contact_id.email
            rec.contactemail = mycontactemail
            return mycontactemail

    @api.depends('partner_id')
    def _get_partnerstreet(self):
        for rec in self:
            mypartnerstreet = ' '
            if rec.partner_id:
                mypartnerstreet = rec.partner_id.street
            rec.partnerstreet = mypartnerstreet
            return mypartnerstreet

    @api.depends('user_id.employee_id')
    def _get_username(self):
        for rec in self:
            myusername = ' '
            if rec.user_id.employee_id:
                myusername = rec.user_id.employee_id.name
            rec.username = myusername
            return myusername

    @api.depends('user_id.employee_id')
    def _get_userphone(self):
        for rec in self:
            myuserphone = ' '
            if rec.user_id.employee_id:
                myuserphone = rec.user_id.employee_id.work_phone
            rec.userphone = myuserphone
            return myuserphone

    @api.depends('user_id.employee_id')
    def _get_usermobile(self):
        for rec in self:
            myusermobile = ' '
            if rec.user_id.employee_id:
                myusermobile = rec.user_id.employee_id.mobile_phone
            rec.usermobile = myusermobile
            return myusermobile

    date_order = fields.Datetime(string="報價日期")
    date_order1 = fields.Date(string="bf報價日期")
    partnername = fields.Char(string="客戶名稱",compute=_get_partnername)
    contactname = fields.Char(string="客戶聯絡人",compute=_get_contactname)
    contactphone = fields.Char(string="客戶聯絡電話", compute=_get_contactphone)
    contactemail = fields.Char(string="客戶聯絡EMAIL", compute=_get_contactemail)
    partnerstreet = fields.Char(string="客戶地址",compute=_get_partnerstreet)
    username = fields.Char(string="業務聯絡人",compute=_get_username)
    userphone = fields.Char(string="聯絡人電話",compute=_get_userphone)
    usermobile = fields.Char(string="聯絡人行動",compute=_get_usermobile)