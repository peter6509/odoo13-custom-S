# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class cloudrentContractCloseWizard(models.TransientModel):
    _name = "cloudrent.contract_close_wizard"
    _description = "CloudRent解約返還押金核銷精靈"

    @api.depends('contract_id')
    def _get_member_deposit(self):
        for rec in self:
            rec.member_deposit = rec.contract_id.contract_close_line.member_deposit

    @api.depends('contract_id')
    def _get_110v_start(self):
        for rec in self:
            rec.member_110v_start = rec.contract_id.contract_close_line.member_110v_start

    @api.depends('contract_id')
    def _get_110v_current_scale(self):
        for rec in self:
            rec.member_110v_end = rec.contract_id.contract_close_line.member_110v_end

    @api.depends('contract_id')
    def _get_220v_start(self):
        for rec in self:
            rec.member_220v_start = rec.contract_id.contract_close_line.member_220v_start

    @api.depends('contract_id')
    def _get_220v_current_scale(self):
        for rec in self:
            rec.member_220v_end = rec.contract_id.contract_close_line.member_220v_end

    @api.depends('contract_id')
    def _get_110v_amount(self):
        for rec in self:
            rec.member_110v_amount = rec.contract_id.contract_close_line.member_110v_amount

    @api.depends('contract_id')
    def _get_220v_amount(self):
        for rec in self:
            rec.member_220v_amount = rec.contract_id.contract_close_line.member_220v_amount

    @api.depends('contract_id')
    def _get_emeter_complete(self):
        for rec in self:
            rec.member_emeter_complete = rec.contract_id.contract_close_line.member_emeter_complete

    @api.depends('contract_id')
    def _get_emeter_noncomplete(self):
        for rec in self:
            rec.member_emeter_noncomplete = rec.contract_id.contract_close_line.member_emeter_noncomplete

    @api.depends('contract_id')
    def _get_landlord_noncomplete(self):
        for rec in self:
            rec.member_landlord_noncomplete = rec.contract_id.contract_close_line.member_landlord_noncomplete

    @api.depends('contract_id')
    def _get_management_fee(self):
        for rec in self:
            rec.member_management_fee = rec.contract_id.contract_close_line.member_management_fee

    @api.depends('member_deposit', 'member_emeter_noncomplete', 'member_landlord_noncomplete', 'member_management_fee','household_clean_fee', 'other_impairment')
    def _get_return_amount(self):
        for rec in self:
            rec.member_return_amount = rec.member_deposit - rec.member_emeter_noncomplete - rec.member_landlord_noncomplete - rec.member_management_fee - rec.household_clean_fee - rec.other_impairment


    member_id = fields.Many2one('cloudrent.household_member',string="租戶",required=True)
    contract_id = fields.Many2one('cloudrent.contract',string="合約")
    member_deposit = fields.Float(digits=(10, 0), string="合約押金", compute=_get_member_deposit)
    member_110v_start = fields.Float(digits=(10, 2), string="110V合約啟始度數", compute=_get_110v_start)
    member_110v_end = fields.Float(digits=(10, 2), string="110V目前度數", compute=_get_110v_current_scale)
    member_220v_start = fields.Float(digits=(10, 2), string="220V合約啟始度數", compute=_get_220v_start)
    member_220v_end = fields.Float(digits=(10, 2), string="220V目前度數", compute=_get_220v_current_scale)
    member_110v_amount = fields.Integer(string="110V用電合計金額", compute=_get_110v_amount)
    member_220v_amount = fields.Integer(string="220V用電合計金額", compute=_get_220v_amount)
    member_emeter_complete = fields.Integer(string="已繳電費總計", compute=_get_emeter_complete)
    member_emeter_noncomplete = fields.Integer(string="應繳電費餘額", compute=_get_emeter_noncomplete)
    member_landlord_noncomplete = fields.Integer(string="應繳租金餘額", compute=_get_landlord_noncomplete)
    member_management_fee = fields.Integer(string="尚欠管理費", compute=_get_management_fee)
    household_clean_fee = fields.Integer(string="房務清潔費")
    other_impairment = fields.Integer(string="其他減損")
    member_return_amount = fields.Integer(string="應退(補)押金合計", compute=_get_return_amount)


    @api.onchange('member_id')
    def onchangecusname(self):
        myrec = self.env['cloudrent.household_member'].search([('id','=',self.member_id.id)])
        myids = []
        for rec in myrec:
            myids.append(rec[0])
        self.contract_id = myrec.contract_id.id
        return {'domain': {'': [('id', 'in', myids)]}}

    def run_contract_close(self):
        if self.member_landlord_noncomplete > 0:
            mylandlord = self.member_landlord_noncomplete
        else:
            mylandlord = 0

        if self.member_emeter_noncomplete > 0:
            myemeter = self.member_emeter_noncomplete
        else:
            myemeter = 0

        if self.member_management_fee > 0 :
            mymanagement = self.member_management_fee
        else:
            mymanagement = 0

        if self.other_impairment > 0:
            myimpairment = self.other_impairment
        else:
            myimpairment = 0
        if self.member_return_amount > 0:
            myreturnamount = self.member_return_amount
        else:
            myreturnamount = 0

        if self.member_return_amount > 0 :
            myrec = self.env['cloudrent.member_payment']
            mypayrec = myrec.create({'member_id':self.member_id.id,'house_id':self.contract_id.house_id1.id})
            # memberid,paymentid,emeter_amount,clean_fee,impairment_fee
            self.env.cr.execute("""select genmembernoncomplete(%d,%d,%d,%d,%d)""" % (self.member_id.id,mypayrec.id,self.member_emeter_noncomplete,self.household_clean_fee,self.other_impairment))
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select genpaymentinfo(%d)""" % mypayrec.id)
            self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='CloudRent租戶解約完成'
        return {
            'name':'Success',
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'sh.message.wizard',
            'views':[(view.id,'form')],
            'view_id':view.id,
            'target':'new',
            'context':context,
            }



