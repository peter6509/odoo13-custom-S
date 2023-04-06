# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebOpenAccountDay(models.Model):
    _name = "neweb.open_account_day1"
    _description = "付款天數"
    _order = "day_seq"

    name = fields.Char(string="付款天數",required=True)
    day_seq = fields.Integer(string="順序",required=True)
    active = fields.Boolean(string="ACTIVE",default=True)

    @api.model
    def create(self, vals):
        mycount = self.env['neweb.open_account_day1'].search_count([('name','=',vals['name'])])
        if mycount > 0:
            raise UserError("此付款天數已重複!")
        res = super(NewebOpenAccountDay, self).create(vals)
        return res
class ResPartnerOpenAccountDay(models.Model):
    _inherit = "res.partner"

    open_account_day1 = fields.Many2one('neweb.open_account_day1',string="付款天數")


class SaleOrderOpenAccountDay(models.Model):
    _inherit = "sale.order"

    open_account_day1 = fields.Many2one('neweb.open_account_day1', string="付款天數")
    open_account_day2 = fields.Many2one('neweb.open_account_day1', string="本案付款天數")

    @api.onchange('partner_id')
    def onchangepartner(self):
        myrec = self.env['res.partner'].search([('id','=',self.partner_id.id)])
        self.open_account_day1 = myrec.open_account_day1.id
        self.open_account_day2 = myrec.open_account_day1.id

class NewebProjectOpenAccountDay(models.Model):
    _inherit = "neweb.project"

    @api.depends('open_account_day1','open_account_day2')
    def _is_greater(self):
        for rec in self:
            if rec.open_account_day2.day_seq > rec.open_account_day1.day_seq and rec.open_account_day2.id != 9:
                rec.is_greaterday = True
            else:
                rec.is_greaterday = False

    open_account_day1 = fields.Many2one('neweb.open_account_day1', string="付款天數")
    open_account_day2 = fields.Many2one('neweb.open_account_day1', string="本案付款天數")
    greater_day_desc = fields.Char(string="本案付款天數說明")
    is_greaterday = fields.Boolean(string="is_greater",compute=_is_greater)

    def write(self, vals):
        res = super(NewebProjectOpenAccountDay, self).write(vals)
        for rec in self:
            if rec.is_greaterday==True and not rec.greater_day_desc:
                raise UserError("必須輸入本案付款天數說明")
        return res

