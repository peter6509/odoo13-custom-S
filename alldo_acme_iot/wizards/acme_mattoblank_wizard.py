# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmemattoblankwizard(models.TransientModel):
    _name = "alldo_acme_iot.mattoblank_wizard"

    product_id = fields.Many2one('product.product',string="料號",required=True)
    prod_num = fields.Float(digits=(10,0),string="移動數量",default=0)
    move_owner = fields.Many2one('res.users',string="轉移人員",default=lambda self:self.env.uid)

    def run_mattoblank(self):
        ## 原材物料倉
        mymatlocid = self.env['alldo_acme_iot.company_stockloc'].search([])[0].material_loc.id
        ## 毛胚倉
        myblanklocid = self.env['alldo_acme_iot.company_stockloc'].search([])[0].blank_loc.id
        if self.prod_num > 0 :
            myrec = self.env['stock.picking'].search([])
            myres = myrec.create(
                {'picking_type_id': 5, 'location_id': mymatlocid, 'location_dest_id': myblanklocid,
                 'move_type': 'direct',
                 'user_id': self.move_owner.id, 'origin': '原物料移轉至毛胚倉',
                 'move_line_ids': [
                     (0, 0, {'product_id': self.product_id.id, 'company_id': 1, 'location_id': mymatlocid,
                             'location_dest_id': myblanklocid,
                             'product_uom_id': self.product_id.product_tmpl_id.uom_id.id, 'qty_done': self.prod_num})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '原物料倉移動至毛胚倉輸入完成！'
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
