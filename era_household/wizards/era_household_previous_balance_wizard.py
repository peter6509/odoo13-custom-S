# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class erahouseholduncompletewizard(models.TransientModel):
    _name = "era.previous_balance_wizard"

    @api.depends()
    def _get_paymentym(self):
        myrec = self.env['era.household_config'].search([])
        if myrec:
            myym = myrec.bill_ym
            # if myrec.bill_ym[5:7] == '01':
            #     myy = str(int(myrec.bill_ym[0:4]) - 1)
            #     mym = '12'
            #     myym = myy + '-' + mym
            # else:
            #     myy = myrec.bill_ym[0:5]
            #     mym = str(int(myrec.bill_ym[5:7]) - 1).zfill(2)
            #     myym = myy + mym
            self.payment_ym = myym
            return myym

    @api.depends('payment_account', 'payment_ym')
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
            myym = myy + '-' + mym
            myrec = self.env['era.household_payment_line'].search(
                [('payment_id', '=', self.payment_account.id), ('payment_ym', '=', myym)])
            if myrec:
                myres = myrec.uncomplete_fee
            else:
                myres = 0

            self.uncomplete_fee = myres
            return myres


    @api.depends('payment_account', 'payment_ym')
    def _get_renew_uncomplete(self):
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
            myym = myy + '-' + mym
            myrec = self.env['era.household_payment_line'].search(
                [('payment_id', '=', self.payment_account.id), ('payment_ym', '=', myym)])
            if myrec:
                myres = myrec.uncomplete_fee
            else:
                myres = 0

            self.renew_uncomplete = myres
            return myres

    @api.onchange('uncomplete_fee')
    def onchangeuncom(self):
        self.renew_uncomplete = self.uncomplete_fee

    payment_account = fields.Many2one('era.household_house_line', string="租戶房號", required=True)
    payment_ym = fields.Char(string="對帳年月", size=7, default=_get_paymentym)
    uncomplete_fee = fields.Float(digits=(10, 0), string="上期未繳餘額", compute=_get_uncomplete, store=True)
    renew_uncomplete = fields.Float(digits=(10,0),string="重新設定上期未繳金額")

    def previous_balance_setting(self):
        myaccount = self.payment_account.id
        if self.payment_ym:
            myy = self.payment_ym[0:4]
            mym = self.payment_ym[5:7]
            mynm = int(mym) - 1
            if mynm <= 0:
                mym = '12'
                myny = int(myy) - 1
                myy = str(myny)
            else:
                mym = str(mynm).zfill(2)
            myym = myy + '-' + mym
        if self.renew_uncomplete > 0 :
            self.env.cr.execute("""select genpreviousbalance(%d,'%s',%s)""" % (myaccount,myym,self.renew_uncomplete))
            self.env.cr.execute("""commit""")

            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = '房號：%s 期初未結清金額設定完成 OK！' % self.payment_account.house_no
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



