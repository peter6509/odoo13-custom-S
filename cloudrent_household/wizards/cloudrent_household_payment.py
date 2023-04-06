# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class cloudrenthouseholdpayment(models.TransientModel):
    _name = "cloudrent.cloudrent_payment_wizard"

    @api.depends('payment_account','payment_amount','payment_ym')
    def _get_uncomplete(self):
        myhouseno = self.payment_account.house_no
        if self.payment_ym:
            myy = self.payment_ym[0:4]
            mym = self.payment_ym[5:7]
            mynm = int(mym) - 1
            if mynm < 0:
                mym = '12'
                myny = int(myy) - 1
                myy = str(myny)
            else:
                mym = str(mynm).zfill(2)
            myym = myy +'-'+ mym
            self.env.cr.execute("""select getlastuncompletefee(%d,'%s')""" % (self.payment_account.id,self.payment_ym))
            myres = self.env.cr.fetchone()[0]
            # if myrec:
            #     myres = myrec.uncomplete_fee
            # else:
            #     myres = 0

            self.uncomplete_fee = myres
            return myres

    @api.depends('uncomplete_fee','current_fee','other_uncompletefee')
    def _get_currenttotfee(self):
        self.current_total_fee = self.uncomplete_fee + self.current_fee + self.other_uncompletefee


    @api.depends('payment_account','payment_ym')
    def _get_currentfee(self):
        myym = self.payment_ym
        self.env.cr.execute("""select gethashousrental(%d,'%s')""" % (self.payment_account.id,myym))
        myres = self.env.cr.fetchone()[0]
        if myres:
            myhouserentalfee = 0
            myhouserentalfee = 0
            myhousemanagementfee = 0
            myparkingspacerent = 0
            myparkingmanagement = 0
            myloparkingmanagement = 0
            mycurrentemeterfee = 0
        else:

            myhouserentalfee = self.payment_account.house_rental_fee
            myhousemanagementfee = self.payment_account.house_management_fee
            myparkingspacerent = self.payment_account.parking_space_rent
            myparkingmanagement = self.payment_account.parking_management
            myloparkingmanagement = self.payment_account.lo_parking_management
            mycurrentemeterfee = self.payment_account.current_emeter_fee
        myhouseno = self.payment_account.house_no
        self.current_fee = (mycurrentemeterfee + myhouserentalfee + myhousemanagementfee + myparkingspacerent + myparkingmanagement + myloparkingmanagement)

    @api.depends()
    def _get_paymentym(self):
        myrec = self.env['cloudrent.household_config'].search([])
        if myrec:
            myym = myrec.bill_ym
            # if myrec.bill_ym[5:7]=='01':
            #     myy=str(int(myrec.bill_ym[0:4])-1)
            #     mym='12'
            #     myym=myy+'-'+mym
            # else:
            #     myy=myrec.bill_ym[0:5]
            #     mym=str(int(myrec.bill_ym[5:7])-1).zfill(2)
            #     myym = myy+mym
            self.payment_ym = myym
            return myym


    payment_account = fields.Many2one('cloudrent.household_house_line',string="租戶房號",required=True)
    payment_ym = fields.Char(string="年-月", size=7,default=_get_paymentym)
    payment_amount = fields.Float(digits=(10,0),string="匯款金額",default=0)
    other_uncompletefee = fields.Float(digits=(10,0),string="額外未繳金額",default=0)
    uncomplete_fee = fields.Float(digits=(10,0),string="上期未繳餘額",compute=_get_uncomplete,store=True)
    current_fee = fields.Float(digits=(10,0),string="本期費用合計",compute=_get_currentfee,store=True)
    current_total_fee = fields.Float(digits=(10,0),string="應繳總額",compute=_get_currenttotfee,store=True)
    payment_desc = fields.Char(string="匯款說明")
    payment_date = fields.Date(string="匯款日期",required=True)
    emeter_scale = fields.Boolean(string="電費核銷", default=False)
    house_rental = fields.Boolean(string="房屋租金核銷", default=False)
    house_management = fields.Boolean(string="房屋管理費核銷", default=False)
    parking_space_rent = fields.Boolean(string="車位租金核銷", default=False)
    parking_management = fields.Boolean(string="車位管理費核銷", default=False)
    lo_parking_management = fields.Boolean(string="機車位管理費核銷", default=False)

    def run_payment_fee(self):
        myrec = self.env['cloudrent.household_config'].search([])
        if myrec:
            myym = myrec.bill_ym
        if self.payment_ym > myym:
            raise UserError("輸入的年-月 %s 超過目前待結帳年月 %s ,請確認" % (self.payment_ym,myym))
        self.env.cr.execute("""select gencloudrentpayment(%d)""" % self.id)
        self.env.cr.execute("""commit""")
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '房號：%s 繳款核銷成功 OK！' % self.payment_account.house_no
        return {
            'name': '系統通知訊息',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }
