# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError
import math,json
from lxml import etree


class CloudRentHouseholdMaintenance(models.Model):
    _name = "cloudrent.household_maintenance"
    _description = "租房修繕主檔"

    @api.depends('quotation_line')
    def _get_quotation_amount(self):
        for rec in self:
            myquoamount = 0
            for rec1 in rec.quotation_line:
                myquoamount = myquoamount + (rec1.quo_amount_tot + rec1.quo_tax)
            rec.quotation_amount = myquoamount

    @api.depends('assign_line')
    def _get_invoice_amount(self):
        myinvamount = 0
        for rec in self:
            for rec1 in rec.assign_line:
                if rec1.assign_status=='3': # 驗收
                   myinvamount = myinvamount + rec1.inv_amount_tot
            rec.invoice_amount = myinvamount

    name = fields.Char(string="修繕單號",default="New")
    house_id = fields.Many2one('cloudrent.household_house_line',string="租房編號",required=True)
    member_id = fields.Many2one('cloudrent.household_member',string="租戶")
    require_date = fields.Date(string="通報日期",required=True)
    maintenance_line = fields.One2many('cloudrent.household_maintenance_line','maintenance_id',string="報修設備")
    visit_line = fields.One2many('cloudrent.household_visit_line','visit_id',string="預約訪視/現場檢查")
    quotation_line = fields.One2many('cloudrent.household_quotation_line','quotation_id',string="修繕廠商報價")
    assign_line = fields.One2many('cloudrent.household_assign_line','assign_id',string="派工修繕")
    quotation_amount = fields.Float(digits=(10,0),string="修繕報價金額",compute=_get_quotation_amount)
    invoice_amount = fields.Float(digits=(10,0),string="發票已認列金額",compute=_get_invoice_amount)
    manage_user1 = fields.Many2one('res.users', string="房東U1")
    manage_user2 = fields.Many2one('res.users', string="代管U1")
    manage_user3 = fields.Many2one('res.users', string="代管U2")
    manage_user4 = fields.Many2one('res.users', string="代管U3")
    flow_owner = fields.Many2one('res.users',string="建檔人員",default=lambda self:self.env.uid)
    flow_man1 = fields.Many2one('cloudrent.household_member',string="指派管理師")
    flow_man2 = fields.Many2one('cloudrent.household_member',string="該案房東")
    flow_man3 = fields.Many2one('cloudrent.household_member',string="該案物業")
    inquiry_date = fields.Date(string="預約訪視日期")
    agent_satisfaction = fields.Selection([('1','不足'),('2','普通'),('3','尚可'),('4','滿意'),('5','非常滿意')],string="管理師滿意度",default='4')
    sup_satisfaction = fields.Selection([('1','不足'),('2','普通'),('3','尚可'),('4','滿意'),('5','非常滿意')],string="廠商工班滿意度",default='4')
    state = fields.Selection([('1','新單'),('2','預約檢查'),('3','房東同意'),('4','廠商報價'),('5','房東確認報價'),('6','修繕派工'),('7','完工'),('8','滿意度調查'),('9','發票核銷')],string="狀態",default='1')
    landlord_sign = fields.Char(string="報價單房東簽名")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('cloudrent.household_maintenance') or _('New')
        res = super(CloudRentHouseholdMaintenance, self).create(vals)
        return res

class CloudRentHouseholdMaintenanceline(models.Model):
    _name = "cloudrent.household_maintenance_line"
    _description = "租房修繕設備明細"

    maintenance_id = fields.Many2one('cloudrent.household_maintenance',ondelete='cascade')
    equip_id = fields.Many2one('cloudrent.equip_list', string="報修設備")
    maintenance_memo = fields.Text(string="狀況說明")
    equip_num = fields.Integer(string="數量",default=1)
    equip_img = fields.Binary(string="照片")
    equip_attach = fields.Many2many('ir.attachment',string="夾檔")

    @api.onchange('maintenance_id')
    def onchangemainid(self):
        myids = []
        myhouseid = self.maintenance_id.house_id.id
        myrec = self.env['cloudrent.equip_list'].search([('equip_id', '=', myhouseid)])
        for rec in myrec:
            myids.append(rec.id)
        return {'domain': {'equip_id': [('id', 'in', myids)],}}


class CloudRentHouseholdVisitLine(models.Model):
    _name = "cloudrent.household_visit_line"
    _description = "現場勘驗檢查明細"

    visit_id = fields.Many2one('cloudrent.household_maintenance',ondelete='cascade')
    visit_date = fields.Date(string="現場勘驗日期",required=True)
    visit_man = fields.Many2one('cloudrent.household_member',string="管理師",domain=lambda self:[('member_type','=','5')])
    visit_desc = fields.Text(string="勘驗說明")
    visit_img = fields.Binary(string="現場照片")
    visit_attach = fields.Many2many('ir.attachment',string="文件夾檔",attachment=False)

class CloudRentHouseholdQuotationLine(models.Model):
    _name = "cloudrent.household_quotation_line"
    _description = "修繕廠商報價"

    @api.depends('quo_qty','quo_price')
    def _get_untaxamount(self):
        for rec in self:
            rec.quo_untax_amount = rec.quo_rty * rec.quo_price


    @api.depends('quo_untax_amount')
    def _get_quotax(self):
        for rec in self:
            rec.quo_tax = math.ceil(rec.quo_untax_amount * 0.05)

    # @api.depends('quo_untax_amount','quo_tax')
    # def _get_amounttot1(self):
    #     myamounttot = 0
    #     for rec in self:
    #         rec.quo_amount_tot = myamounttot
    #         return myamounttot

    quotation_id = fields.Many2one('cloudrent.household_maintenance',ondelete='cascade')
    quo_item = fields.Char(string="項次")
    quo_partner = fields.Many2one('cloudrent.household_member',string="廠商/工班",domain=lambda self:[('member_type','=','4')])
    quo_desc = fields.Char(string="規格說明")
    quo_qty = fields.Integer(string="數量")
    quo_price = fields.Float(digits=(10,0),string="單價")
    quo_untax_amount = fields.Float(digits=(7,0),string="小計", compute=_get_untaxamount)
    quo_tax = fields = fields.Float(digits=(5,0),string="稅金", compute=_get_quotax)


class CloudRentAssignLine(models.Model):
    _name = "cloudrent.household_assign_line"
    _description = "派工修繕及發票資訊明細"
    _order = "assign_item"

    assign_id = fields.Many2one('cloudrent.household_maintenance',ondelete='cascade')
    assign_item = fields.Char(string="項次")
    assign_date = fields.Date(string="派工日期")
    assign_desc = fields.Char(string="派工說明")
    assign_partner = fields.Many2one('cloudrent.household_member',string="廠商/工班",domain=lambda self:[('member_type','=','4')])
    equip_id = fields.Many2one('cloudrent.equip_list',string="設備")
    assign_bpic = fields.Binary(string="修繕前照片")
    assign_ppic = fields.Binary(string="修繕中照片")
    assign_cpic = fields.Binary(string="修繕完成後照片")
    assign_attachment = fields.Many2many('ir.attachment',string='夾檔')
    assign_status = fields.Selection([('1','派工'),('2','完工'),('3','驗收')],string="派工狀況")
    invoice_no = fields.Char(string='發票編號')
    inv_untax_amount = fields.Float(digits=(7, 0), string="發票未稅合計")
    inv_tax = fields = fields.Float(digits=(5, 0), string="發票稅金")
    # inv_amount_tot = fields.Float(digits=(10, 0), string="發票金額合計")

    @api.onchange('assign_partner')
    def onchangepartner(self):
        myrec = self.env['cloudrent.household_quotation_line'].search([('quotation_id','=',self.assign_id),('quo_partner','=',self.assign_partner.id)])
        if myrec:
            myuntaxamount = 0
            mytax = 0
            myamounttot = 0
            for rec in myrec:
                myuntaxamount = myuntaxamount + rec.quo_untax_amount
                mytax = mytax + rec.quo_tax
                myamounttot = myamounttot + rec.quo_amount_tot
            self.inv_untax_amount = myuntaxamount
            self.inv_tax = mytax
            self.inv_amount_tot = myamounttot
        else:
            self.inv_untax_amount = 0
            self.inv_tax = 0
            self.inv_amount_tot = 0







