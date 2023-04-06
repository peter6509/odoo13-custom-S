# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebpurchaseinherit4(models.Model):
    _name = "neweb_purchase.costtype"


    name = fields.Char(string="成本分攤類別名稱")


    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError("成本分攤類別名稱不能空值！")
        if 'name' in vals and vals['name']:
            myname = vals['name']
            mynum = self.env['neweb_purchase.costtype'].search_count([('name','=',myname)])
            if mynum > 0 :
                raise UserError("成本分攤名稱重複了！")
        res = super(newebpurchaseinherit4, self).create(vals)
        return res


    def write(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError("成本分攤類別名稱不能空值！")
        if 'name' in vals and vals['name']:
            myname = vals['name']
            mynum = self.env['neweb_purchase.costtype'].search_count([('name','=',myname)])
            if mynum > 1 :
                raise UserError("成本分攤名稱重複了！")
        res = super(newebpurchaseinherit4, self).write(vals)

        return res



class newebpurchaseinherit41(models.Model):
    _inherit = "purchase.order"

    @api.depends('date_order')
    def _get_date_order(self):
        for rec in self:
            rec.date_order1 = rec.date_order

    cost_type = fields.Many2one('neweb_purchase.costtype',string="成本分攤類別")
    foreign_purchase = fields.Boolean(string="國外採購單?(請款品名產生)",default=False)
    date_order1 = fields.Date(string="詢價日期",compute=_get_date_order)
    dest_address_id = fields.Many2one('res.partner',string="直運地址",default=1)
    stockinno_line = fields.One2many('neweb.stockinno_line', 'in_id', string="進貨單號", copy=False)
    main_stockinno = fields.Many2one('stock.picking', string="主進貨單")


class NewebStockInNoLine(models.Model):
    _name = "neweb.stockinno_line"
    _description = "採購進貨單明細"

    in_id = fields.Many2one('purchase.order', ondelete='cascade')
    name = fields.Many2one('stock.picking', string="進貨單號")
