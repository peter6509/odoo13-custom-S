# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotpurchaseinherit1(models.Model):
    _inherit = "purchase.order.line"

    @api.onchange('product_id')
    def onchangeprod(self):
        mytmplid = self.env['product.product'].search([('id','=',self.product_id.id)]).product_tmpl_id.id
        myrec1 = self.env['product.template'].search([('id','=',mytmplid)])
        self.prod_material = myrec1.prod_material
        self.prod_spec = myrec1.prod_spec
        self.prod_deliver = myrec1.prod_deliver
        self.env.cr.execute("""select getpurchaseprice(%d)""" % self.product_id.id)
        self.price_unit = self.env.cr.fetchone()[0]
        myrec = self.env['alldo_gh_iot.po_wkorder'].search([('product_no','=',self.product_id.id),('active','=',True)])
        ids=[]
        for rec in myrec:
            ids.append(rec.id)
        return {'domain': {'po_wkorder_id': [('id', 'in', ids)]}}

    # @api.depends('product_id')
    # def _get_powkorder(self):
    #     myrec = self.env['alldo_gh_iot.po_wkorder'].search([('product_no', '=', self.product_id.id), ('active', '=', True)])
    #     for rec in myrec:
    #         mypoid = rec.id
    #     return mypoid

    po_wkorder_id = fields.Many2one('alldo_gh_iot.po_wkorder',string="客戶訂單")
    prod_material = fields.Char(string="材質")
    prod_spec = fields.Char(string="規格")
    prod_deliver = fields.Char(string="指送")
    prod_desc = fields.Char(string="說明")
    po_wkorder_ids1 = fields.Many2many('alldo_gh_iot.po_wkorder', 'po_wkorder_purchase_order_rel1', 'po_line_id', 'powk_id',string="訂單")
    memo = fields.Char(string="備註")
