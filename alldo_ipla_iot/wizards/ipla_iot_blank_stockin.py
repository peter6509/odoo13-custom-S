# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class iplaiotblankstockin(models.TransientModel):
    _name = "alldo_ipla_iot.blank_stockin_wizard"
    _description = "回收料入庫精靈"

    product_no = fields.Many2one('product.template',string="回收料號",required=True)
    blank_num = fields.Float(digits=(10,3),string="數量(KG)",default=0.00,required=True)
    stockin_owner = fields.Many2one('res.users',string="入帳人員",default=lambda self:self.env.uid)



    def run_blank_stockin(self):

        # self.env.cr.execute("""select genblankstockin1(%d,%s,%d)""" % (self.mo_no.id,self.blank_num,self.stockin_owner.id))
        # self.env.cr.execute("""commit""")
        myprodid = self.env['product.product'].search([('product_tmpl_id','=',self.product_no.id)]).id
        if self.blank_num > 0:
            ## 生產位置
            mymolocid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].mo_loc.id
            ## 原物料倉庫
            mymateriallocid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].material_loc.id
            myrec = self.env['stock.picking'].search([])
            myres = myrec.create(
                {'picking_type_id': 5, 'location_id': mymolocid, 'location_dest_id': mymateriallocid,
                 'move_type': 'direct',
                 'user_id': self.stockin_owner.id, 'origin': '產線回收料入庫',
                 'move_line_ids': [
                     (0, 0, {'product_id': myprodid , 'company_id': 1, 'location_id': mymolocid,
                             'location_dest_id': mymateriallocid, 'product_uom_id': self.product_no.uom_id.id, 'qty_done': self.blank_num})]})
            try:
                myres.action_confirm()
                myres.action_done()
            except Exception as inst:
                print("No Confirm & action Done")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '回收料入庫輸入完成！'
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
