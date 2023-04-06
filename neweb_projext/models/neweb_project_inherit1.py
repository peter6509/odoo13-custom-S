# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebprojectextinherit1(models.Model):
    _inherit = ["res.partner"]


    credit_rulelist = fields.Text(string="信用條件")
    payment_days = fields.Integer(string="Payment Days")

    @api.model
    def create(self, vals):
        if 'vat' in vals and vals['vat']:
            myvat = vals['vat']
            myres = self.env['res.partner'].search_count([('vat','like',myvat)])
            if myres > 0 :
                raise UserError("統一編號已重複！")
        res = super(newebprojectextinherit1, self).create(vals)
        return res