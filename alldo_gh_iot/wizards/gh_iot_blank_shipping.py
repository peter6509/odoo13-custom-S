# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotblankshippingwizard(models.TransientModel):
    _name = "alldo_gh_iot.blank_shipping_wizard"
    _description = "毛胚入總庫(成品倉)出貨"

    blank_no = fields.Many2one('product.product',string="毛胚料號",required=True)
    shipping_num = fields.Float(digits=(8,0),string="出貨數量")
    partner_id = fields.Many2one('res.partner',string="出貨客戶",required=True)
    shipping_owner = fields.Many2one('res.users', string="入帳人員", default=lambda self: self.env.uid)
    blank_onhand = fields.Float(string="毛胚倉在手數量")

    @api.onchange('blank_no')
    def onclientchange(self):
        self.env.cr.execute("""select getblankonhand(%d)""" % self.blank_no.id)
        self.blank_onhand = self.env.cr.fetchone()[0]

    def run_blank_shipping(self):
        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
        myprodlocid = mycomploc.prod_loc.id  # 公司產品庫存位置
        myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
        mypartnerlocid = self.partner_id.property_stock_customer.id  # 客戶位置
        myprod = self.blank_no.id  # 毛胚料號

        myrec = self.env['stock.picking'].search([])

        ## 毛胚倉入成品倉總庫
        myres = myrec.create(
            {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': myprodlocid,
             'move_type': 'direct',
             'user_id': self.shipping_owner.id, 'origin': '毛胚倉入總庫移動', 'partner_id': self.partner_id.id,
             'move_line_ids': [
                 (0, 0, {'product_id': self.blank_no.id, 'company_id': 1, 'location_id': myblanklocid,
                         'location_dest_id': myprodlocid, 'product_uom_id': 1, 'qty_done': self.shipping_num})]})
        myres.action_confirm()
        self.env.cr.commit()
        myres.action_done()
        self.env.cr.commit()
        ## 毛胚成品倉出貨給客戶
        myres = myrec.create(
            {'picking_type_id': 2, 'location_id': myprodlocid, 'location_dest_id': mypartnerlocid,
             'move_type': 'direct',
             'user_id': self.shipping_owner.id, 'origin': '毛胚從總庫出貨給客戶', 'partner_id': self.partner_id.id,
             'move_line_ids': [
                 (0, 0, {'product_id': self.blank_no.id, 'company_id': 1, 'location_id': myprodlocid,
                         'location_dest_id': mypartnerlocid, 'product_uom_id': 1, 'qty_done': self.shipping_num})]})
        myres.action_confirm()
        self.env.cr.commit()
        myres.action_done()
        self.env.cr.commit()

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '毛胚入總庫並出貨完成！'
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




