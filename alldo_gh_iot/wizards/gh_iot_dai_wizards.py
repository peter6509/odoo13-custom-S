# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotdaiwizards(models.TransientModel):
    _name = "alldo_gh_iot.dai_shipping_wizards"

    partner_id = fields.Many2one('res.partner',string="出貨客戶",default=40)
    stock_picking_no = fields.Char(string="內部調撥單號")

    def run_partner_shipping(self):
        if not self.stock_picking_no:
            mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
            myprodlocid = mycomploc.prod_loc.id  # 公司產品庫存位置
            myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
            mypartnerlocid = self.partner_id.property_stock_customer.id  # 客戶位置
            myrec = self.env['stock.picking']
            myres = myrec.create({'partner_id':self.partner_id.id,'picking_type_id': 2, 'location_id': myprodlocid, 'location_dest_id': mypartnerlocid,
                                  'move_type': 'direct',
                                  'user_id': self.env.uid, 'origin': '%s手動開立出貨單' % self.env.user.name})
            myres.update({'state':'confirmed'})
        else:
            myres = self.env['stock.picking'].search([('name','=',self.stock_picking_no)])

        myviewid = self.env.ref('stock.view_picking_form')

        return {
            'view_name': 'view_picking_form',
            'name': (u'產品庫存查詢'),
            'type': 'ir.actions.act_window',
            'res_model': 'stock.picking',
            'view_id': myviewid.id,
            'res_id': myres.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current'}
