# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class cloudrentHouseholdLandlord(models.Model):
    _name = "cloudrent.household_landlord"
    _description = "房東基本資料主檔"
    _order = "landlord_no"

    @api.depends('landlord_ar_line')
    def _get_artotamount(self):
        for rec in self:
            artotamount = 0
            for rec1 in rec.landlord_ar_line:
                artotamount += rec1.tot_amount
            rec.ar_tot_amount = artotamount

    @api.depends('landlord_arpayment_line')
    def _get_artotpayment(self):
        for rec in self:
            artotpayment = 0
            for rec1 in rec.landlord_arpayment_line:
                artotpayment += rec1.payment_tot
            rec.ar_tot_payment = artotpayment

    @api.depends('ar_tot_amount','ar_tot_payment')
    def _get_artotbalance(self):
        for rec in self:
            rec.ar_tot_balance = rec.ar_tot_amount - rec.ar_tot_payment

    @api.depends('landlord_ap_line')
    def _get_aptotamount(self):
        for rec in self:
            aptotamount = 0
            for rec1 in rec.landlord_ap_line:
                aptotamount += rec1.tot_amount
            rec.ap_tot_amount = aptotamount

    @api.depends('landlord_appayment_line')
    def _get_aptotpayment(self):
        for rec in self:
            appayment = 0
            for rec1 in rec.landlord_appayment_line:
                appayment += rec1.pay_ap
            rec.ap_tot_payment = appayment

    @api.depends('ap_tot_amount','ap_tot_payment')
    def _get_aptotbalance(self):
        for rec in self:
            rec.ap_tot_balance = rec.ap_tot_amount - rec.ap_tot_payment

    landlord_no = fields.Char(string="編號", required=True)
    landlord_name = fields.Char(string="住戶姓名", required=True)
    user_id = fields.Many2one('res.users', string="使用者")
    landlord_pid = fields.Char(string="身分證號")
    landlord_email = fields.Char(string="EMAIL")
    landlord_address1 = fields.Char(string="聯絡地址1")
    landlord_address2 = fields.Char(string="聯絡地址2")
    landlord_phone1 = fields.Char(string="聯絡電話1")
    landlord_phone2 = fields.Char(string="聯絡電話2")
    is_management_ar = fields.Boolean(string="是否管理應收帳款?",defaualt=False)
    is_management_ap = fields.Boolean(string="是否管理應付帳款?",default=False)
    ar_tot_amount = fields.Float(digits=(10,0),string="應收總計",compute=_get_artotamount)
    ar_tot_payment = fields.Float(digits=(10,0),string="應收已收",compute=_get_artotpayment)
    ar_tot_balance = fields.Float(digits=(10,0),string="應收未收",compute=_get_artotbalance)
    ap_tot_amount = fields.Float(digits=(10,0),string="應付總計",compute=_get_aptotamount)
    ap_tot_payment = fields.Float(digits=(10, 0), string="應付已付",compute=_get_aptotpayment)
    ap_tot_balance = fields.Float(digits=(10, 0), string="應付未付", compute=_get_aptotbalance)
    income_date = fields.Date(string="簽約日期")
    ap_system_sd = fields.Date(string="使用雲平台起始日期")
    ap_system_ed = fields.Date(string="使用雲平台起始日期")
    landlord_ar_line = fields.One2many('cloudrent.household_landlord_ar_line','landlord_id',copy=False)
    landlord_arpayment_line = fields.One2many('cloudrent.household_landlord_arpayment_line','landlord_id',copy=False)
    landlord_ap_line = fields.One2many('cloudrent.household_landlord_ap_line','landlord_id',copy=False)
    landlord_appayment_line = fields.One2many('cloudrent.household_landlord_appayment_line','landlord_id',copy=False)
    landlord_line_user = fields.One2many('cloudrent.household_landlord_line_user','landlord_id',copy=False)
    landlord_project_ids = fields.Many2many('cloudrent.household_house','cloudrent_landlord_household_house_rel','landlord_id','house_id',string="所有案場")
    landlord_line_message = fields.One2many('cloudrent.household_landlord_line_message','landlord_id',copy=False)
    landlord_user1 = fields.Many2one('res.users', string="房東U1")
    landlord_user2 = fields.Many2one('res.users', string="房東U2")
    manage_user1 = fields.Many2one('res.users', string="代管U1")
    manage_user2 = fields.Many2one('res.users', string="代管U2")
    manage_user3 = fields.Many2one('res.users', string="代管U3")
    month_fee = fields.Integer(string="每月月租(每戶)元？", default=0)
    have_contract_data = fields.Boolean(string="合約管理資料輸入服務?", default=False)
    contract_data_fee = fields.Integer(string="合約管理資料輸入(每筆)元？", default=0)
    have_emeter = fields.Boolean(string="雲端數位電錶租用?", default=False)
    emeter_fee = fields.Integer(string="雲端數位電錶租用(每月)元?", default=0)
    have_account_push = fields.Boolean(string="帳務推送服務?", default=False)
    account_push_fee = fields.Integer(string="帳務推送(每則)元?", default=0)
    have_call_notice = fields.Boolean(string="逾期催繳服務?", default=False)
    call_notice_fee = fields.Integer(string="逾期催繳(每則)元?", default=0)
    have_repair_message = fields.Boolean(string="報修訊息推送服務?", default=False)
    repair_message_fee = fields.Integer(string="報修訊息推送(每則)元？", default=0)


class cloudrentHouseholdLandlordARLine(models.Model):
    _name = "cloudrent.household_landlord_ar_line"
    _description = "房東案場應收帳款明細"
    _order = "landlord_ar_ym desc,project_no,house_id"

    @api.depends('house_rental_fee','house_management_fee','parking_space_rent','parking_management','water_fee','emeter_fee','lo_parking_management')
    def _get_tot_amount(self):
        for rec in self:
            rec.tot_amount = rec.house_rental_fee + rec.house_management_fee + rec.parking_space_rent + rec.parking_management + rec.lo_parking_management + rec.water_fee + rec.emeter_fee

    landlord_id = fields.Many2one('cloudrent.household_landlord',ondelete='cascade')
    landlord_ar_ym = fields.Char(string="年月")
    project_no = fields.Many2one('cloudrent.household_house',string="租屋案場")
    house_id = fields.Many2one('cloudrent.household_house_line',string="房號")
    member_id = fields.Many2one('cloudrent.household_member',string="房客")
    house_rental_fee = fields.Float(digits=(10, 0), string="房屋租金")
    house_management_fee = fields.Float(digits=(10, 0), string="房屋管理費")
    parking_space_rent = fields.Float(digits=(10, 0), string="車位租金")
    parking_management = fields.Float(digits=(10, 0), string="車位管理費")
    lo_parking_management = fields.Float(digits=(10, 0), string="機車位管理費")
    emeter_fee = fields.Float(digits=(10,0),string='電費')
    water_fee = fields.Float(digits=(10, 0), string="水費")
    tot_amount = fields.Float(digits=(10,0),string="合計金額",compute=_get_tot_amount)



class cloudrentHouseholdLandlordARPaymentLine(models.Model):
    _name = "cloudrent.household_landlord_arpayment_line"
    _description ="房客已繳記錄"
    _order = "landlord_arpayment_ym desc,house_id"


    @api.depends('house_rental_pay', 'house_management_pay', 'parking_space_pay', 'parking_management_pay','lopark_management_pay', 'water_pay','emeter_pay')
    def _get_payment_tot(self):
        mytot = 0
        for rec in self:
            mytot = rec.house_rental_pay + rec.house_management_pay + rec.parking_space_pay + rec.parking_management_pay + rec.lopark_management_pay + rec.water_pay + rec.emeter_pay
            rec.payment_tot = mytot
        return mytot

    landlord_id = fields.Many2one('cloudrent.household_landlord',ondelete='cascade')
    landlord_arpayment_ym = fields.Char(string="年月")
    landlord_arpayment_date = fields.Date(string="入帳日")
    project_no = fields.Many2one('cloudrent.household_house', string="租屋案場")
    house_id = fields.Many2one('cloudrent.household_house_line', string="房號")
    member_id = fields.Many2one('cloudrent.household_member', string="房客")
    house_rental_pay = fields.Float(digits=(10, 0), string="已繳房屋租金")
    house_management_pay = fields.Float(digits=(10, 0), string="已繳房屋管理費")
    parking_space_pay = fields.Float(digits=(10, 0), string="已繳車位租金")
    parking_management_pay = fields.Float(digits=(10, 0), string="已繳車位管理費")
    lopark_management_pay = fields.Float(digits=(10, 0), string="已繳機車位管理費")
    water_pay = fields.Float(digits=(10, 0), string="已繳水費")
    emeter_pay = fields.Float(digits=(10,0),string="已繳電費")
    payment_tot = fields.Float(digits=(10, 0), string="已繳金額小計",compute=_get_payment_tot)
    member_payment_ids = fields.Many2many('cloudrent.member_payment','cloudrent_landlord_ar_payment_rel','landlord_payment_line_id','payment_id',string="核銷單號")



class cloudrentHouseholdLandlordAPLine(models.Model):
    _name = "cloudrent.household_landlord_ap_line"
    _description = "房東案場應付帳款明細"
    _order = "landlord_ap_ym desc,project_no"

    @api.depends('management_fee','line_month_fee')
    def _get_tot_amount(self):
        for rec in self:
            rec.tot_amount = rec.management_fee + rec.line_month_fee

    landlord_id = fields.Many2one('cloudrent.household_landlord', ondelete='cascade')
    landlord_ap_ym = fields.Char(string="年月")
    project_no = fields.Many2one('cloudrent.household_house', string="租屋案場")
    management_num = fields.Integer(string="戶數")
    management_fee = fields.Float(digits=(10,0),string="雲平台租戶管理費")
    line_month_record = fields.Integer(string="LINE訊息本月筆數")
    line_month_fee = fields.Float(digits=(10,0),string="LINE通訊費")
    tot_amount = fields.Float(digits=(10, 0), string="合計金額", compute=_get_tot_amount)
    active = fields.Boolean(string="生效")


class cloudrentHouseholdLandlordLineUser(models.Model):
    _name = "cloudrent.household_landlord_line_user"
    _description = "房東人員 LINE APP綁定紀錄"

    landlord_id = fields.Many2one('cloudrent.household_landlord',ondelete='cascade')
    line_user_id = fields.Char(string='Line User ID')
    line_rich_menu_id = fields.Char(string='Line Rich menu ID')
    landlord_pid = fields.Char(string="身份字號")
    landlord_name = fields.Char(string="姓名")
    send_acc_bill = fields.Boolean(string="發送催繳帳單?",default=True)
    send_announcement = fields.Boolean(string="發送公告訊息?",default=True)
    send_bus_adv = fields.Boolean(string="發送廣告訊息?",default=False)
    active = fields.Boolean(string="生效")

class cloudrentHouseholdLandlordLineMessage(models.Model):
    _name = "cloudrent.household_landlord_line_message"
    _description = "LINE Message 通訊記錄"
    _order = "send_date desc,project_no,house_id,member_id"

    landlord_id = fields.Many2one('cloudrent.household_landlord',ondelete='cascade')
    project_no = fields.Many2one('cloudrent.household_house', string="租屋案場")
    house_id = fields.Many2one('cloudrent.household_house_line', string="房號")
    member_id = fields.Many2one('cloudrent.member_line_user', string="LINE對象")
    line_type = fields.Selection([('1','帳單催繳通知'),('2','公告通知'),('3','修膳訊息')],string="訊息類型")
    send_date = fields.Date(string="發送日期")


class cloudrentHouseholdLandlordappaymentline(models.Model):
    _name = "cloudrent.household_landlord_appayment_line"
    _description = "房東平台管理費用核銷明細檔"
    _order = "name desc"

    landlord_id = fields.Many2one('cloudrent.household_landlord',ondelete='cascade')
    name = fields.Char(string="核銷單號",default='New',copy=False)
    pay_status = fields.Selection([('1','草稿'),('2','入帳')],string="狀態",default='1',change_default=True)
    pay_active = fields.Boolean(string="勾選",track_visibility="always",change_default=True)
    pay_name = fields.Char(string="付費說明")
    pay_year = fields.Char(string="年份")
    pay_month = fields.Many2many('cloudrent.payment_month','cloudrent_month_landlord_appayment_rel','landlord_appayment_id','month_id',string="核銷月份",track_visibility="always")
    pay_ap = fields.Float(digits=(10,0),string="實付金額")
    pay_confirm = fields.Many2one('res.users',string="過帳人員")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('cloudrent.payment') or _('New')
        res = super(cloudrentHouseholdLandlordappaymentline, self).create(vals)
        return res

    def gen_payment_confirm(self):       # 入帳
        if self.pay_status == '1':
            self.pay_status = '2'

    def gen_payment_retconfirm(self):    # 入帳返回
        if self.pay_status == '2':
            self.pay_status = '1'


