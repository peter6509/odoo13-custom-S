# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class CloudRentApplyforGrantFee(models.Model):
    _name = "cloudrent.applyfor_grantfee"
    _description = "補助費用申請書"
    _order = "applyfor_year desc,applyfor_month desc,applyfor_period desc"

    name = fields.Char(string="申請書單號",default="New",copy=False)
    escrow_no = fields.Many2one('cloudrent.escrow',string="代管業者")
    applyfor_year = fields.Char(string="民國年")
    applyfor_month = fields.Char(string="月")
    applyfor_period = fields.Char(string="期")
    applyfor_total = fields.Integer(string="總計")
    notarial_fee = fields.Integer(string="公證費")
    develop_fee = fields.Integer(string="開發費")
    guarantee_fee = fields.Integer(string="包管費")
    match_fee = fields.Integer(string="媒合費")
    escrow_fee = fields.Integer(string="代管費")
    vat = fields.Char(string="統編號碼")
    bus_boss = fields.Char(string="負責人")
    bus_addr = fields.Char(string="地址")
    grantfee_sdate = fields.Date(string="申請起始日")
    grantfee_edate = fields.Date(string="申請截止日")

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s年%s月%s期" % (myrec.escrow_no.bus_name, myrec.applyfor_year,myrec.applyfor_month,myrec.applyfor_period)
            result.append((myrec.id, myname))
        return result

    def refresh_data(self):
        self.env.cr.execute("""select gen_grantfee(%d)""" % self.id)
        self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='本申請書數據已重整'
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

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            self.env.cr.execute("""select get_cloudrent_seqno(%d,'%s')""" % (vals['escrow_no'], 'A1'))
            vals['name'] = self.env.cr.fetchone()[0]
        res = super(CloudRentApplyforGrantFee, self).create(vals)
        return res

