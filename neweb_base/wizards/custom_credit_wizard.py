# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class CustomCreditWizard(models.TransientModel):
    _name = "base.custom_credit_wizard"

    custom_id = fields.Many2one('res.partner',string="客戶",required=True)
    payment_days = fields.Integer(string="付款天數")
    # open_account_day1 = fields.Many2one('neweb.open_account_day1',string="付款天數",required=True)
    credit_limit = fields.Integer(string="信用額度")

    @api.onchange('custom_id')
    def onchangecustom(self):
        myrec = self.env['res.partner'].search([('id','=',self.custom_id.id)])
        if myrec:
            self.payment_days = myrec.payment_days
            self.credit_limit = myrec.credit_limit

    def change_credit_limit(self):
        myrec = self.env['res.partner'].search([('id', '=', self.custom_id.id)])
        if myrec:
            myrec.write({'payment_days':self.payment_days,'credit_limit':self.credit_limit})

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='客戶信用額度＆付款天數變更OK'
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
