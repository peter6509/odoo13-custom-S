# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class acmematerialtoprodwizard(models.TransientModel):
    _name = "alldo_acme_iot.materialtoprod_wizard"
    _description = "原物料倉TO產品倉移動精靈"


    product_id = fields.Many2one('product.product',string="產品/料號",required=True)
    move_num = fields.Integer(string="移轉數量",default=0.00)
    move_owner = fields.Many2one('res.users',string="建單人",default=lambda self:self.env.uid)
    move_note = fields.Char(string="備註",default=' ')


    def run_move_material(self):
        ## WH/原物料位置
        mymateriallocid = self.env['alldo_acme_iot.company_stockloc'].search([])[0].material_loc.id
        ## WH/產品倉位置
        myprodlocid = self.env['alldo_acme_iot.company_stockloc'].search([])[0].prod_loc.id
        mypickingrec = self.env['stock.picking'].search([])
        self.env.cr.execute("""select getproduom(%d)""" % self.product_id.id)
        myuomid = self.env.cr.fetchone()[0]

        myres = mypickingrec.create(
            {'picking_type_id': 5, 'location_id': mymateriallocid, 'location_dest_id': myprodlocid,
             'move_type': 'direct',
             'user_id': self.move_owner.id, 'report_memo': self.move_note,
             'move_line_ids': [
                 (0, 0, {'product_id': self.product_id.id, 'company_id': 1, 'location_id': mymateriallocid,
                         'location_dest_id': myprodlocid, 'product_uom_id': myuomid,
                         'qty_done': self.move_num})]})
        myres.action_confirm()
        self.env.cr.commit()
        myres.action_done()
        self.env.cr.commit()


        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '原材物料移動至產品倉資料輸入完成！'
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