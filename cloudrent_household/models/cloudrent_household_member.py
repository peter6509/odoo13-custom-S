# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError
import base64
from io import BytesIO
import string
import secrets
from datetime import datetime
import json,logging,re
from lxml import etree
import contextlib

try:
    import qrcode
except ImportError:
    raise ImportError(
        '此模組必須要安裝 qrcode 才能運作，請配合安裝，謝謝!!(sudo pip3 install qrcode)')

class alldocloudrenthousehold(models.Model):
    _name = "cloudrent.household_member"
    _description = "cloudrent住戶資料"
    _order = "member_no"
    _rec_name = "member_name"

    @api.depends('member_rent_line')
    def _get_member_balance(self):
        for rec in self:
            mybalance = 0
            for rec1 in rec.member_rent_line:
                mybalance = mybalance + (rec1.account_tot - rec1.payment_tot)
            rec.member_account_balance = mybalance
            return mybalance

    @api.depends('member_payment_line')
    def _get_member_paymenttot(self):
        for rec in self:
            mypaymenttot = 0
            for rec1 in rec.member_payment_line:
                if rec1.has_confirm:
                    mypaymenttot = mypaymenttot + (rec1.payment_ap_now)
            rec.member_payment_tot = mypaymenttot
            return mypaymenttot

    @api.depends('member_income_emeter','member_emeter_payline')
    def _get_account_emeter(self):
        myartot=0
        myaptot=0
        mybalancetot =0
        for rec in self.member_income_emeter:
            myartot = myartot + rec.tot_ar_fee
        for rec1 in self.member_emeter_payline:
            myaptot = myaptot + rec1.account_amount
        mybalancetot = myartot - myaptot
        self.member_account_emeter=mybalancetot
        return mybalancetot

    @api.depends('member_rent_line')
    def _get_hasrentline(self):
        nnum =0
        for rec in self.member_rent_line:
            nnum = nnum + 1
        if nnum > 0 :
            myres = True
        else:
            myres = False
        self.has_rent_line=myres
        return myres

    @api.depends('member_breach_contract')
    def _get_breach_contract(self):
        myamount = 0
        for rec in self.member_breach_contract:
            if rec.breach_07_amount:
                my07amount = rec.breach_07_amount
            else:
                my07amount = 0
            if rec.breach_08_amount:
                my08amount = rec.breach_08_amount
            else:
                my08amount = 0
            if rec.breach_09_amount:
                my09amount = rec.breach_09_amount
            else:
                my09amount = 0
            myamount = myamount + (my07amount + my08amount + my09amount)
        self.member_breach_amount = myamount
        return myamount

    @api.depends('member_deposit_line')
    def _get_member_deposit(self):
        mydeposit=0
        for rec in self.member_deposit_line:
            if rec.deposit_status=='1':
               mydeposit = mydeposit + rec.deposit_amount
        self.member_deposit1 = mydeposit
        return mydeposit

    @api.depends('house_id')
    def _get_casecode(self):
        for rec in self:
            rec.case_code = rec.house_id.house_id.case_code

    @api.depends('member_type')
    def _get_member_position(self):
        for rec in self:
            rec.member_position = rec.member_type

    member_no = fields.Char(string="編號")
    member_name = fields.Char(string="住戶姓名",required=True)
    user_id = fields.Many2one('res.users',string="使用者")
    member_pid = fields.Char(string="身分證號",required=True)
    member_email = fields.Char(string="EMAIL")
    income_date = fields.Date(string="入住日期")
    start_rental = fields.Date(string="起租日期")
    end_rental = fields.Date(string="退租日期")
    house_rental_fee = fields.Float(digits=(10,0),string="房屋租金")
    house_rental_desc = fields.Char(string="房屋租金說明")
    house_management_fee = fields.Float(digits=(10, 0), string="房屋管理費")
    house_management_desc = fields.Char(string="房屋管理費說明")
    parking_space_rent = fields.Float(digits=(10,0),string="車位租金")
    parking_rent_desc = fields.Char(string="車位租金說明")
    parking_management = fields.Float(digits=(10,0),string="車位管理費")
    parking_management_desc = fields.Char(string="車位管理費說明")
    lo_parking_management = fields.Float(digits=(10,0),string="機車位管理費")
    lo_parking_desc = fields.Char(string="機車位管理費說明")
    water_fee = fields.Float(digits=(10,0),string="水費",deault=0)
    member_sex = fields.Selection([('F','女'),('M','男'),('O','其他')],string="性別")
    member_age = fields.Selection([('1','11 - 20'),('2','21 - 30'),('3','31 - 40'),('4','41 - 50'),('5','51 - 60'),('6','61 - 70'),('7','71 - 80'),('8','81 - 90'),('9','90 以上')],string="年齡")
    member_amount = fields.Integer(string="住戶人數")
    member_address1 = fields.Char(string="聯絡地址1")
    member_address2 = fields.Char(string="聯絡地址2")
    member_phone1 = fields.Char(string="聯絡電話1")
    member_phone2 = fields.Char(string="聯絡電話2")
    member_phone3 = fields.Char(string="聯絡電話3")
    member_phone4 = fields.Char(string="聯絡電話4")
    member_desc = fields.Text(string="備註")
    qr_image = fields.Binary(string='QR Code', attachment=True, store=True)
    state_code = fields.Char(string='Line Notify state code', readonly=True)
    line_access_token = fields.Char(string='Line Access Token', readonly=True)
    member_rent_line = fields.One2many('cloudrent.member_account','member_id',string="合約房租帳本",track_visibility="onchange")
    member_payment_line = fields.One2many('cloudrent.member_payment','member_id',string="房租繳款記錄",track_visibility="onchange")
    member_income_emeter = fields.One2many('cloudrent.member_income_emeter','member_id',string="入住電錶啟始度數",track_visibility="onchange")
    member_emeter_payline = fields.One2many('cloudrent.member_emeter','account_id',string="租戶電費核銷記錄",track_visibility="onchange")
    member_breach_contract = fields.One2many('cloudrent.member_breach_contract','account_id',string="租戶違約金記錄",track_visibility="onchange")
    member_deposit_line = fields.One2many('cloudrent.member_deposit','account_id',string="租戶繳交押金記錄",track_visibility="onchange")
    member_account_balance = fields.Float(digits=(10,0),string="租戶總應繳總額",compute=_get_member_balance)
    member_payment_tot = fields.Float(digits=(10,0),string="租戶總已繳總額",compute=_get_member_paymenttot)
    member_account_emeter = fields.Float(digits=(10,0),string="電費應繳餘額",compute=_get_account_emeter)
    member_breach_amount = fields.Float(digits=(10,0),string="租戶違約金",compute=_get_breach_contract)
    member_deposit1 = fields.Float(digits=(10,0),string="租戶押金",compute=_get_member_deposit)
    has_rent_line = fields.Boolean(string="是否有帳本",compute=_get_hasrentline)
    member_deposit = fields.Float(digits=(10,0),string="租戶押金",default=0)
    active = fields.Boolean(string="ACTIVE",default=True)
    house_id = fields.Many2one('cloudrent.household_house_line',string="入住房間")
    member_type = fields.Selection([('1','物業'),('2','房東'), ('3','房客'), ('4','供應商/工班'),('5','管理師')], string="人員屬性",default='3')
    case_code = fields.Char(string="案場代號",compute=_get_casecode)
    member_position = fields.Char(string="MEMBER型態",compute=_get_member_position)


    landlord_user1 = fields.Many2one('res.users', string="房東U1")
    landlord_user2 = fields.Many2one('res.users', string="房東U2")
    manage_user1 = fields.Many2one('res.users', string="代管U1")
    manage_user2 = fields.Many2one('res.users', string="代管U2")
    manage_user3 = fields.Many2one('res.users', string="代管U3")

    line_user_ids = fields.One2many('cloudrent.member_line_user', 'member_id', copy=False)
    contract_id = fields.Many2one('cloudrent.contract', string="合約編號")
    rent_convention = fields.Binary(related="house_id.house_id.rent_convention", string="租戶公約")

    match_no = fields.Char(string='媒合編號')
    landlord_no = fields.Char(string="房東物件編號")
    tenant_no = fields.Char(string="房客編號")
    loc = fields.Char(string='地區')
    community = fields.Char(string="社區")
    writ_addr = fields.Char(string="權狀地址")
    owner = fields.Char(string="所有權人")
    owner_phone = fields.Char(string="電話")
    lessee = fields.Char(string="承租人")
    lessee_phone = fields.Char(string="電話")
    contact = fields.Char(string="聯絡人")
    type = fields.Char(string="型態")
    pattern = fields.Char(string="格局")
    member_subsidy_level = fields.Selection([('1','ㄧ類戶'),('2','二類戶'),('3','一般戶')],string="客戶類別")
    normal_rent = fields.Float(digits=(10,0),string="一般戶租金",default=0)

    # @api.model
    # def fields_view_get(self,view_id=None, view_type='form', toolbar=False, submenu=False,context=None):
    #     if context is None:
    #         context = {}
    #     res = super(alldocloudrenthousehold, self)._fields_view_get(view_id=view_id, view_type=view_type,toolbar=toolbar, submenu=submenu)
    #     doc = etree.XML(res['arch'])
    #     if view_type == 'form':
    #         for node in doc.xpath("//field[@name='match_no']"):
    #             if self.member_type in ('1','2','4','5') :
    #                 node.set('invisible','1')
    #             else:
    #                 node.set('invisible','0')
    #         for node in doc.xpath("//field[@name='landlord_no']"):
    #             if self.member_type in ('1', '2', '4', '5'):
    #                 node.set('invisible', '1')
    #             else:
    #                 node.set('invisible', '0')
    #         for node in doc.xpath("//field[@name='loc']"):
    #             if self.member_type in ['1', '2', '4', '5']:
    #                 node.set('invisible', '1')
    #             else:
    #                 node.set('invisible', '0')
    #         for node in doc.xpath("//field[@name='community']"):
    #             if self.member_type in ['1', '2', '4', '5']:
    #                 node.set('invisible', '1')
    #             else:
    #                 node.set('invisible', '0')
    #         for node in doc.xpath("//field[@name='writ_addr']"):
    #             if self.member_type in ['1', '2', '4', '5']:
    #                 node.set('invisible', '1')
    #             else:
    #                 node.set('invisible', '0')
    #         for node in doc.xpath("//field[@name='owner']"):
    #             if self.member_type in ['1', '2', '4', '5']:
    #                 node.set('invisible', '1')
    #             else:
    #                 node.set('invisible', '0')
    #         for node in doc.xpath("//field[@name='owner_phone']"):
    #             if self.member_type in ['1', '2', '4', '5']:
    #                 node.set('invisible', '1')
    #             else:
    #                 node.set('invisible', '0')
    #         for node in doc.xpath("//field[@name='lessee']"):
    #             if self.member_type in ['1', '2', '4', '5']:
    #                 node.set('invisible', '1')
    #             else:
    #                 node.set('invisible', '0')
    #         for node in doc.xpath("//field[@name='lessee_phone']"):
    #             if self.member_type in ['1', '2', '4', '5']:
    #                 node.set('invisible', '1')
    #             else:
    #                 node.set('invisible', '0')
    #
    #     res['arch'] = etree.tostring(doc, encoding='unicode')
    #     return res

    @api.depends('normal_rent')
    def _get_level1(self):
        for rec in self:
            if rec.normal_rent * 0.225 >= 4545 :
                rec.level1_rent = rec.normal_rent - 4545
            else:
                rec.level1_rent = round(rec.normal_rent * 0.775)

    @api.depends('normal_rent')
    def _get_level2(self):
        for rec in self:
            if rec.normal_rent * 0.445 >= 7200 :
                rec.level2_rent = rec.normal_rent - 7200
            else:
                rec.level2_rent = round(rec.normal_rent * 0.555)

    @api.depends('member_subsidy_level','normal_rent','level1_rent','level2_rent')
    def _get_subsidy(self):
        for rec in self:
            if rec.member_subsidy_level=='1':   # 一類戶
                rec.subsidy = rec.normal_rent - rec.level1_rent
            elif rec.member_subsidy_level=='2': # 二類戶
                rec.subsidy = rec.normal_rent - rec.level2_rent
            else:                      # 一般戶
                rec.subsidy = 0

    level1_rent = fields.Float(digits=(10,0),string="ㄧ類戶",compute=_get_level1)
    level2_rent = fields.Float(digits=(10,0),string="二類戶",compute=_get_level2)
    subsidy = fields.Integer(string="補助款",compute=_get_subsidy)

    @api.depends('parking_space_rent','normal_rent','subsidy','house_management_fee')
    def _get_rent_amount(self):
        for rec in self:
            rec.rent_amount = rec.normal_rent - rec.subsidy + rec.house_management_fee + rec.parking_space_rent

    rent_amount = fields.Integer(string="房客(月)應繳金額",compute=_get_rent_amount)
    household_reg = fields.Char(string="入戶籍")
    memo = fields.Text(string="備註")

    def run_account_payment(self):   # 租戶開帳應繳數據
        self.env.cr.execute("""select run_account_payment(%d)""" % self.id)
        self.env.cr.execute("""commit""")

    def recall_account_payment(self):  # 已存在,更新相關數據正
        self.env.cr.execute("""select recall_account_payment(%d)""" % self.id)
        self.env.cr.execute("""commit""")

    def del_member_account(self):
        self.env.cr.execute("""select delmembcloudrentccount(%d)""" % self.id)
        self.env.cr.execute("""commit""")

    @api.model
    def create(self,vals):
        if 'member_no' in vals and not vals['member_no']:
            raise UserError("未輸入租戶編號")
        if 'member_name' in vals and not vals['member_name']:
            raise UserError("未輸入租戶姓名")
        if 'member_pid' in vals and not vals['member_pid']:
            raise UserError("未輸入租戶身分字號")
        res = super(alldocloudrenthousehold, self).create(vals)
        self.env.cr.execute("""select chkuser('%s')""" % res.member_pid)
        myres = self.env.cr.fetchone()[0]
        if myres:
            self.env.cr.execute("""select max(id) from res_users where login='%s'""" % res.member_pid)
            mymaxid1 = self.env.cr.fetchone()[0]
            self.env.cr.execute("""update res_users set active=True where id=%d""" % mymaxid1)
            self.env.cr.execute("""commit""")
        else:
            self.env.cr.execute("""select max(id) from res_users where active=True""")
            mymaxid = self.env.cr.fetchone()[0]
            max_user = self.env['res.users'].search([('id', '=', mymaxid)])  # max_user
            maxuser = max_user.sudo().copy()  # copy New user
            self.env.cr.commit()
            self.env.cr.execute("""select max(id) from res_users""")
            mymaxid1 = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select genmemberemeter(%d)""" % res.id)
        # self.env.cr.execute("""commit""")
        self.env.cr.execute("""select chnewuser(%d,'%s','%s')""" % (mymaxid1,res.member_pid,res.member_pid))
        self.env.cr.execute("""commit""")
        return res

    def write(self,vals):

        res = super(alldocloudrenthousehold, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select chkuser('%s')""" % rec.member_no)
            myres = self.env.cr.fetchone()[0]
            if myres:
                self.env.cr.execute("""select max(id) from res_users where login='%s'""" % rec.member_no)
                mymaxid1 = self.env.cr.fetchone()[0]
                self.env.cr.execute("""update res_users set active=True where id=%d""" % mymaxid1)
                self.env.cr.execute("""commit""")
            else:
                self.env.cr.execute("""select max(id) from res_users where active=True""")
                mymaxid = self.env.cr.fetchone()[0]
                max_user = self.env['res.users'].search([('id', '=', mymaxid)])  # max_user
                maxuser = max_user.sudo().copy()  # copy New user
                self.env.cr.commit()
                self.env.cr.execute("""select max(id) from res_users""")
                mymaxid1 = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select genmemberemeter(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select chnewuser(%d,'%s','%s')""" % (mymaxid1, rec.member_no, rec.member_pid))
            self.env.cr.execute("""commit""")
        return res

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.member_no, myrec.member_name)
            result.append((myrec.id, myname))
        return result

    def gencloudrentte_secrets_code(self):
        self.ensure_one()
        # code_list = self.search([('state_code', 'not in', False)])
        if not self.state_code:
            state_code = ''.join(secrets.choice(string.ascii_letters) for _ in range(48))
            # state_check = code_list.filtered(lambda x: x.state_code not in state_code)
            # if not state_check:
            self.state_code = state_code
            self.gencloudrentte_qr_code()
            # else:
            #     self.gencloudrentte_secrets_code()
        else:
            self.gencloudrentte_qr_code()

    def gencloudrentte_qr_code(self):
        # 定義 QRcode的 參數，可調整，詳細請參閱python qrcode 規範
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        # 取Line Notify Configure 參數值做為 qrcode value
        line_configure = self.env['cloudrent.line_notify_configure'].search([('active', '=', True), ('test_mode', '=', False)])
        # 目前只取第一筆有效的服務通知，後續在思考如何變化它。
        URL = line_configure.notify_url + 'response_type=code' + '&client_id=' + line_configure.client_id + '&redirect_uri=' + line_configure.redirect_url + '&scope=notify' + '&state=' + self.state_code
        print(URL)
        qr.add_data(URL)
        qr.make(fit=True)
        img = qr.make_image()
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_image = base64.b64encode(temp.getvalue())
        self.qr_image = qr_image

    def gencloudrentte_unlink(self):
        self.ensure_one()
        if self.line_access_token:
            self.line_access_token = ''
            self.qr_image = ''
            
class cloudrentMemberLineUser(models.Model):
    _name = "cloudrent.member_line_user"
    _description = "LINE APP綁定記錄"

    member_id = fields.Many2one('cloudrent.household_member',ondelete='cascade')
    line_user_id = fields.Char(string='Line User ID')
    line_rich_menu_id = fields.Char(string='Line Rich menu ID')
    member_pid = fields.Char(string="身份字號")
    member_name = fields.Char(string="姓名")
    send_acc_bill = fields.Boolean(string="發送帳單?",default=True)
    send_announcement = fields.Boolean(string="發送公告訊息?",default=True)
    send_bus_adv = fields.Boolean(string="發送廣告訊息?",default=False)
    active = fields.Boolean(string="生效",default=True)

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.member_pid, myrec.member_name)
            result.append((myrec.id, myname))
        return result


class cloudrentbreachcontract(models.Model):
    _name = "cloudrent.member_breach_contract"
    _description = "租戶違約繳交記錄"

    account_id = fields.Many2one('cloudrent.household_member',ondelete='cascade')
    account_ym = fields.Char(string="年月")
    account_date = fields.Date(string="入帳日")
    breach_07_amount = fields.Float(digits=(10,0),string="一般違約金")
    breach_08_amount = fields.Float(digits=(10,0),string="損壞違約金")
    breach_09_amount = fields.Float(digits=(10,0),string="提前解約違約金")
    user_id = fields.Many2one('res.users',string="入帳人員")
    member_payment_id = fields.Many2one('cloudrent.member_payment', string="核銷單號")

    def button_action(self):
        try:
            form_view_id = self.env.ref("cloudrent_household.cloudrent_member_payment_form").id
        except Exception as e:
            form_view_id = False
        return {
            'type': 'ir.actions.act_window',
            'name': 'My Action Name',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'cloudrent.member_payment',
            'views': [(form_view_id, 'form')],
            'res_id': self.member_payment_id.id,
            # 'domain': [('id', '=', self.member_payment_id.id)],
            'target': 'current',
        }

class cloudrentmemberdeposit(models.Model):
    _name = "cloudrent.member_deposit"
    _description = "租戶押金繳交記錄"

    account_id = fields.Many2one('cloudrent.household_member',ondelete='cascade')
    # account_ym = fields.Char(string="年月")
    account_date = fields.Date(string="入帳日期")
    deposit_amount = fields.Float(digits=(10,0),string="押金金額")
    deposit_status = fields.Selection([('1','有效'),('2','無效')],string="狀態",default='1')
    user_id = fields.Many2one('res.users',string="入帳人員")
    member_payment_id = fields.Many2one('cloudrent.member_payment', string="核銷單號")

    def button_action(self):
        try:
            form_view_id = self.env.ref("cloudrent_household.cloudrent_member_payment_form").id
        except Exception as e:
            form_view_id = False
        return {
            'type': 'ir.actions.act_window',
            'name': 'My Action Name',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'cloudrent.member_payment',
            'views': [(form_view_id, 'form')],
            'res_id': self.member_payment_id.id,
            'target': 'current',
        }


class cloudrentmemberemeter(models.Model):
    _name = "cloudrent.member_emeter"
    _description = "租戶電費核銷記錄"

    account_id = fields.Many2one('cloudrent.household_member',ondelete='cascade')
    account_ym = fields.Char(string="年月")
    account_date = fields.Date(string="入帳日期")
    account_amount = fields.Float(digits=(10,0),string="繳納金額")
    user_id = fields.Many2one('res.users',string="入帳人員")
    member_payment_id = fields.Many2one('cloudrent.member_payment', string="核銷單號")


    def button_action(self):
        try:
            form_view_id = self.env.ref("cloudrent_household.cloudrent_member_payment_form").id
        except Exception as e:
            form_view_id = False
        return {
            'type': 'ir.actions.act_window',
            'name': 'My Action Name',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'cloudrent.member_payment',
            'views': [(form_view_id, 'form')],
            'res_id': self.member_payment_id.id,
            # 'domain': [('id', '=', self.member_payment_id.id)],
            'target': 'current',
        }


class cloudrentmembcloudrentccount(models.Model):
    _name = "cloudrent.member_account"
    _description ="月固定應繳費用/已繳記錄"

    @api.depends('house_rental_fee','house_management_fee','parking_space_rent','account_active')
    def _get_account_tot(self):
        mytot = 0
        for rec in self:
            if rec.account_active:
               mytot = rec.house_rental_fee + rec.house_management_fee + rec.parking_space_rent
            else:
               mytot = 0
            rec.account_tot = mytot
            return mytot

    @api.depends('house_rental_pay', 'house_management_pay', 'parking_space_pay')
    def _get_payment_tot(self):
        mytot = 0
        for rec in self:
            mytot = rec.house_rental_pay + rec.house_management_pay + rec.parking_space_pay
            rec.payment_tot = mytot
            return mytot


    member_id = fields.Many2one('cloudrent.household_member',ondelete='cascade')
    account_ym = fields.Char(string="年月")
    house_rental_fee = fields.Float(digits=(10, 0), string="房屋租金")
    house_management_fee = fields.Float(digits=(10, 0), string="房屋管理費")
    parking_space_rent = fields.Float(digits=(10, 0), string="車位租金")
    house_rental_pay = fields.Float(digits=(10, 0), string="已繳房屋租金")
    house_management_pay = fields.Float(digits=(10, 0), string="已繳房屋管理費")
    parking_space_pay = fields.Float(digits=(10, 0), string="已繳車位租金")
    account_active = fields.Boolean(string="生效", default=False)
    account_tot = fields.Float(digits=(10, 0), string="生效金額小計", compute=_get_account_tot)
    payment_tot = fields.Float(digits=(10, 0), string="已繳金額小計", compute=_get_payment_tot)
    member_payment_ids = fields.Many2many('cloudrent.member_payment', 'cloudrent_member_account_payment_rel', 'acc_id',
                                          'payment_id', string="核銷單號")


    ## 雲房不用
    parking_management = fields.Float(digits=(10, 0), string="車位管理費")
    lo_parking_management = fields.Float(digits=(10, 0), string="機車位管理費")
    water_fee = fields.Float(digits=(10, 0), string="水費")
    parking_management_pay = fields.Float(digits=(10, 0), string="已繳車位管理費")
    lopark_management_pay = fields.Float(digits=(10, 0), string="已繳機車位管理費")
    water_pay = fields.Float(digits=(10, 0), string="已繳水費")
    member_payment_id = fields.Many2one('cloudrent.member_payment',string="核銷單號")


    def button_action(self):
        if self.payment_tot==0:
            raise UserError("無核銷入帳記錄!")
        try:
            form_view_id = self.env.ref("cloudrent_household.cloudrent_member_payment_form").id
        except Exception as e:
            form_view_id = False
        return {
            'type': 'ir.actions.act_window',
            'name': 'My Action Name',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'cloudrent.member_payment',
            'views': [(form_view_id, 'form')],
              'res_id': self.member_payment_id.id,
            # 'domain': [('id', '=', self.member_payment_id.id)],
            'target': 'current',
        }


class cloudrentmemberincomeemeter(models.Model):
    _name = "cloudrent.member_income_emeter"
    _description = "租戶合約電錶起始度數"
    _order = "emeter_id"

    @api.depends('member_id')
    def _get_emeter_unit(self):
        myunit=0
        for rec in self:
            for rec1 in rec.member_id:
                myhouseid = self.env['cloudrent.household_house_line'].search([('member_id','=',rec1.id)],limit=1)
                myunit = myhouseid.price_unit
            rec.emeter_unit=myunit
            return myunit

    @api.depends('start_scale','current_scale','emeter_unit')
    def _get_totfee(self):
        mytot = 0
        for rec in self:
            if rec.start_scale == False:
                mystartscale = 0
            else:
                mystartscale = rec.start_scale
            if rec.current_scale == False:
                mycurrentscale = 0
            else:
                mycurrentscale = rec.current_scale
            mytot = (mycurrentscale - mystartscale) * rec.emeter_unit
            rec.tot_ar_fee = mytot
            return mytot

    member_id = fields.Many2one('cloudrent.household_member',string="租戶",ondelete='cascade')
    emeter_id = fields.Many2one('cloudrent.household_electric_meter',string="電錶")
    start_date = fields.Date(string="入住日期")
    end_date = fields.Date(string="退租日期")
    start_scale = fields.Float(digits=(10,2),string="合約電錶啟始度數",default=0)
    current_scale = fields.Float(digits=(10,2),string="目前電錶度數")
    emeter_unit = fields.Float(digits=(5,1),string="度單價",compute=_get_emeter_unit)
    tot_ar_fee = fields.Float(digits=(10,0),string="總電費",compute=_get_totfee)
    in_used = fields.Boolean(string="有作用",default=True)


class cloudrentmemberpayment(models.Model):
    _name = "cloudrent.member_payment"
    _description = "租戶核銷主檔"
    _order = "payment_date desc"

    @api.depends('member_id')
    def _get_ar_tot(self):
        for rec in self:
            myrec = self.env['cloudrent.household_member'].search([('id','=',rec.member_id.id)])
            myar = 0
            for rec1 in myrec.member_rent_line:
                myar = myar + rec1.account_tot
            rec.payment_ar = myar
            return myar


    @api.depends('member_id')
    def _get_ap_tot(self):
        for rec in self:
            myrec = self.env['cloudrent.household_member'].search([('id', '=', rec.member_id.id)])
            myap = 0
            for rec1 in myrec.member_rent_line:
                myap = myap + rec1.payment_tot
            rec.payment_ap = myap
            return myap

    @api.depends('payment_ar','payment_ap')
    def _get_tot_balance(self):
        mybalance = 0
        for rec in self:
            mybalance = rec.payment_ar - rec.payment_ap
            rec.payment_balance = mybalance
            return mybalance

    @api.depends('payment_line')
    def _get_haspayline(self):
        for rec in self:
            nitem = 0
            mypayline=False
            for rec1 in rec.payment_line:
                nitem = nitem + 1
            if nitem > 0:
                mypayline=True
            else:
                mypayline=False
            rec.has_payline = mypayline
            return mypayline

    @api.depends('payment_line')
    def _get_ap_nowtot(self):
        for rec in self:
            mypayap = 0
            for rec1 in rec.payment_line:
                mypayap = mypayap + rec1.pay_ap
            rec.payment_ap_now = mypayap
            return mypayap

    # @api.depends('payment_date')
    # def _get_paymentym(self):
    #     for rec in self:
    #         self.env.cr.execute("""select getpaymentym()""")
    #         myres = self.env.cr.fetchone()[0]
    #         rec.payment_year = myres
    #         return myres



    name = fields.Char(string="核銷單號",default='New',copy=False)
    member_id = fields.Many2one('cloudrent.household_member',ondelete='cascade',string="租戶名稱")
    house_id = fields.Many2one('cloudrent.household_house_line',string="房號")
    payment_line = fields.One2many('cloudrent.member_payment_line','payment_id',copy=False,track_visibility='onchange')
    user_id = fields.Many2one('res.users',string="登錄者",default=lambda self:self.env.user)
    payment_date = fields.Date(string="登錄日期",default=fields.Date.today())
    payment_year = fields.Char(string="入帳西元年",store=True,default=datetime.now().year,required=True)
    payment_ar = fields.Float(digits=(10,0),string="租戶應付總金額",compute=_get_ar_tot,track_visibility="onchange")
    payment_ap = fields.Float(digits=(10,0),string="租戶實付總金額",compute=_get_ap_tot,track_visibility="onchange")
    payment_ap_now = fields.Float(digits=(10, 0), string="租戶本次實付總金額",compute=_get_ap_nowtot, track_visibility="onchange")
    payment_balance = fields.Float(digits=(10,0),string="不足餘額",compute=_get_tot_balance,track_visibility="onchange")
    has_payline = fields.Boolean(string="Has Payline",compute=_get_haspayline)
    has_confirm = fields.Boolean(string="入帳否?",default=False)
    tt_date = fields.Date(string="匯款日期")
    account_date = fields.Date(string="入帳日期")
    payment_memo = fields.Text(string="核銷備註")

    def button_action(self):
        if self.payment_ap_now==0:
            raise UserError("查無核銷記錄")
        try:
            form_view_id = self.env.ref("cloudrent_household.cloudrent_member_payment_form").id
        except Exception as e:
            form_view_id = False
        return {
            'type': 'ir.actions.act_window',
            'name': 'My Action Name',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'cloudrent.member_payment',
            'views': [(form_view_id, 'form')],
              'res_id': self.id,
            # 'domain': [('id', '=', self.member_payment_id.id)],
            'target': 'current',
        }

    @api.onchange('member_id')
    def onchange_memberid(self):
        if self.member_id:
            myrec = self.env['cloudrent.household_house_line'].search([('member_id', '=', self.member_id.id)])
            # if myrec:
            #    self.house_id = myrec.id

            ids = []
            for item in myrec:
                ids.append(item.id)
            res = {}

            # print "%s" % ids
            res['domain'] = {'house_id': [('id', 'in', ids)]}
            return res

    def gen_payitem(self):
        self.env.cr.execute("""select genpayitem(%d)""" % self.id)
        self.env.cr.execute("""commit""")

    def gen_confirm(self):
        self.env.cr.execute("""select genpaymentinfo(%d)""" % self.id)
        self.env.cr.execute("""commit""")

    def cancel_confirm(self):
        self.env.cr.execute("""select delpaymentinfo(%d)""" % self.id)
        self.env.cr.execute("""commit""")

    def unlink(self):
        for rec in self:
            if rec.has_confirm==True:
                raise UserError("核銷記錄已入帳,無法刪除！")
        res = super(cloudrentmemberpayment, self).unlink()
        return res

    def write(self, vals):

        res = super(cloudrentmemberpayment, self).write(vals)
        for rec in self:
            if rec.has_confirm==True:
                raise UserError("核銷記錄已入帳,無法修改！")
            self.env.cr.execute("""select checkselmonth(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            if not myres:
                raise UserError("核銷記錄有重複狀況,請確認！")
        return res

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('cloudrent.payment') or _('New')
        res = super(cloudrentmemberpayment, self).create(vals)
        return res





class cloudrentmemberpaymentline(models.Model):
    _name = "cloudrent.member_payment_line"
    _description = "租戶核銷明細檔"

    @api.depends('payment_id','pay_code','pay_month','pay_active')
    def _get_payar(self):
        nitem=0
        for rec in self.pay_month:
            nitem = nitem + 1
        for rec in self:
            mymember = rec.payment_id.member_id
            mytotar = 0
            if rec.pay_code=='01' and rec.pay_active :    # 房租
                mytotar = mymember.house_rental_fee * nitem
            elif rec.pay_code=='02' and rec.pay_active :  # 房屋管理費
                mytotar = mymember.house_management_fee * nitem
            elif rec.pay_code=='03' and rec.pay_active :  # 汽車管理費
                mytotar = (mymember.parking_space_rent + mymember.parking_management) * nitem
            elif rec.pay_code=='04' and rec.pay_active :  # 機車管理費
                mytotar = mymember.lo_parking_management * nitem
            elif rec.pay_code=='05' and rec.pay_active :  # 電費
                mytotar = mymember.member_account_emeter
            elif rec.pay_code=='06' and rec.pay_active :  # 水費
                mytotar = mymember.water_fee * nitem
            elif rec.pay_code=='10' and rec.pay_active:   # 押金
                mytotar = mymember.member_deposit
            else:
                mytotar = 0
            rec.pay_ar = mytotar
            return mytotar

    @api.depends('payment_id', 'pay_code', 'pay_month', 'pay_active')
    def _get_payarunit(self):
        for rec in self:
            mymember = rec.payment_id.member_id
            mytotar = 0
            if rec.pay_code == '01' and rec.pay_active:  # 房租
                mytotar = mymember.house_rental_fee
            elif rec.pay_code == '02' and rec.pay_active:  # 房屋管理費
                mytotar = mymember.house_management_fee
            elif rec.pay_code == '03' and rec.pay_active:  # 汽車管理費
                mytotar = (mymember.parking_space_rent + mymember.parking_management)
            elif rec.pay_code == '04' and rec.pay_active:  # 機車管理費
                mytotar = mymember.lo_parking_management
            elif rec.pay_code == '05' and rec.pay_active:  # 電費
                mytotar = mymember.member_account_emeter
            elif rec.pay_code == '06' and rec.pay_active:  # 水費
                mytotar = mymember.water_fee
            elif rec.pay_code == '10' and rec.pay_active:  # 押金
                mytotar = mymember.member_deposit
            else:
                mytotar = 0
            rec.pay_ar = mytotar
            return mytotar
            # self.env.cr.execute("""select getpayar(%d)""" % rec.id)
            # rec.pay_ar = self.env.cr.fetchone()[0]



    @api.onchange('pay_ar')
    def onchangeap(self):
        self.pay_active=True
        self.pay_ap = self.pay_ar

    def active_tag(self):
        for rec in self:
            if rec.pay_active==True:
                rec.write({'pay_active':False})
            else:
                rec.write({'pay_active':True})
                # self.env.cr.execute(
                #     """select selmonth(%d,'%s','%s')""" % (self.payment_id.member_id.id, self.pay_code, self.pay_year))
                # myres = self.env.cr.fetchall()
                # res = {}
                # ids = []
                # for item in myres:
                #     ids.append(item[0])
                # res['domain'] = {'pay_month': [('id', 'in', ids)]}
                # return res

    @api.depends('pay_month')
    def _get_month_num(self):
        for rec in self:
            nnum=0
            for rec1 in rec.pay_month:
                nnum = nnum + 1
            rec.month_num = nnum
            return nnum

    # @api.depends()
    # def _get_nowyear(self):
    #     dt = datetime.date.today()
    #     return str(dt.year)

    @api.onchange('pay_status')
    def onchangepayactive(self):
        if self.pay_status=='1':
           self.pay_active=False
        else:
           self.pay_active=True
        self.env.cr.execute("""select selmonth(%d,'%s','%s')""" % (self.payment_id.member_id.id,self.pay_code,self.pay_year))
        myres = self.env.cr.fetchall()
        res = {}
        ids=[]
        for item in myres:
            ids.append(item[0])
        res['domain'] = {'pay_month': [('id', 'in', ids)]}
        return res




    payment_id = fields.Many2one('cloudrent.member_payment',ondelete='cascade')
    pay_status = fields.Selection([('1','未選'),('2','已選')],string="選擇",default='1',change_default=True)
    pay_active = fields.Boolean(string="勾選",track_visibility="always",change_default=True)
    pay_name = fields.Char(string="項目")
    pay_code = fields.Char(string="代碼")
    pay_year = fields.Char(string="年份")
    pay_month = fields.Many2many('cloudrent.payment_month','cloudrent_month_payline_rel','payment_id','month_id',string="核銷月份",track_visibility="always")
    month_num = fields.Integer(string="月數",store=True,compute=_get_month_num)
    pay_ar = fields.Float(digits=(10,0),string="應付金額",store=True,compute=_get_payar)
    pay_ar_unit = fields.Float(digits=(10,0),string="應付單位費用",store=True,conpute=_get_payarunit)
    pay_ap = fields.Float(digits=(10,0),string="實付金額",onchange_default=True)



class cloudrentpaymentmonth(models.Model):
    _name = "cloudrent.payment_month"
    _description = "月份選單主檔資料"

    name = fields.Char(string="月份")
    value = fields.Char(string="值")

class cloudrentpaymentitem(models.Model):
    _name = "cloudrent.payment_item"
    _description = "核銷項目主檔資料"
    _order = "pay_code"

    name = fields.Char(string="核銷項目")
    pay_code = fields.Char(string="代碼")

