# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class py3onewebproject(models.Model):
    _inherit = "neweb.project"


    @api.depends('shipping_type')
    def _get_shipping_type(self):
        for rec in self:
            if rec.shipping_type=='1':
                mycshippingtype = '一次交貨'
            else:
                mycshippingtype = '可分批交貨'
            rec.cshippingtype = mycshippingtype
            return mycshippingtype

    @api.depends('stamp_duty_type')
    def _get_stamp_duty_type(self):
        for rec in self:
            if rec.stamp_duty_type=='1':
                mycstampdutytype='買賣'
            else:
                mycstampdutytype='承攬'
            rec.cstampdutytype = mycstampdutytype
            return mycstampdutytype

    @api.depends('have_contract')
    def _get_have_contract(self):
        for rec in self:
            if rec.have_contract=='Y':
                mychavecontract='有合約'
            else:
                mychavecontract='無合約'
            rec.chavecontract = mychavecontract
            return mychavecontract


    @api.depends('setup_type')
    def _get_setup_type(self):
        for rec in self:
            if rec.setup_type=='1':
                mycsetuptype='是'
            else:
                mycsetuptype='否'
            rec.csetuptype = mycsetuptype
            return mycsetuptype

    @api.depends('eng_assign')
    def _get_eng_assign(self):
        for rec in self:
            if rec.eng_assign=='1':
                mycengassign='需至客戶端裝機'
            elif rec.eng_assign=='2':
                mycengassign='否'
            elif rec.eng_assign=='3':
                mycengassign='其他'
            rec.cengassign = mycengassign
            return mycengassign

    @api.depends('invoice_type')
    def _get_invoice_type(self):
        for rec in self:
            if rec.invoice_type=='1':
                mycinvoicetype = '隨貨開立發票'
            elif rec.invoice_type=='2':
                mycinvoicetype = '待業務通知'
            elif rec.invoice_type=='3':
                mycinvoicetype = '完工後隨工單開立發票'
            elif rec.invoice_type=='4':
                mycinvoicetype = '其他'
            rec.cinvoicetype = mycinvoicetype
            return mycinvoicetype

    @api.depends('state')
    def _get_state(self):
        for rec in self:
            if rec.state=='1':
                mycstate = '新單'
            elif rec.state=='2':
                mycstate = '提交'
            elif rec.state=='3':
                mycstate = '派工'
            elif rec.state=='4':
                mycstate = '完工'
            elif rec.state=='5':
                mycstate = '結案'
            elif rec.state=='6':
                mycstate = '合約'
            rec.cstate = mycstate
            return mycstate

    cshippingtype = fields.Char(string="交貨方式py3o",compute=_get_shipping_type)
    cstampdutytype = fields.Char(string="印花稅別py3o",compute=_get_stamp_duty_type)
    chavecontract = fields.Char(string="是否有合約py3o",compute=_get_have_contract)
    csetuptype = fields.Char(string="工程師內部組裝py3o",compute=_get_setup_type)
    cengassign = fields.Char(string="工程師派工py3o",compute=_get_eng_assign)
    cinvoicetype = fields.Char(string="開立發票說明py3o",compute=_get_invoice_type)
    cstate = fields.Char(string="表單狀態py3o",compute=_get_state)