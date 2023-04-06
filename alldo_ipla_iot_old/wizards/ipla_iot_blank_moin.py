# -*- coding: utf-8 -*-
# Author : Peter Wu



from odoo import models,fields,api
from odoo.exceptions import UserError


class iplaiotblankmoin(models.TransientModel):
    _name = "alldo_ipla_iot.blank_moin_wizard"
    _description = "毛胚進料(毛胚倉)精靈"



    cus_name = fields.Many2one('res.partner',string=u"客戶",required=True)
    blank_no = fields.Many2one('product.product',string="毛胚料號",required=True)
    blank_num = fields.Float(digits=(10,2),string="毛胚進料數",default=0.00,required=True)
    stockin_owner = fields.Many2one('res.users', string="入帳人員", default=lambda self: self.env.uid)
    blank_onhand = fields.Float(string="毛胚倉在手數量")

    @api.onchange('blank_no')
    def onclientchange(self):
        self.env.cr.execute("""select getblankonhand(%d)""" % self.blank_no.id)
        self.blank_onhand = self.env.cr.fetchone()[0]



    def run_blank_stockin(self):
        # self.env.cr.execute("""select genblankstockin1(%d,%s,%d)""" % (self.mo_no.id,self.blank_num,self.stockin_owner.id))
        # self.env.cr.execute("""commit""")
        mycomploc = self.env['alldo_ipla_iot.company_stockloc'].search([])
        myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
        mypartnerlocid = self.cus_name.property_stock_customer.id  # 客戶位置
        myprod = self.blank_no.id  # 毛胚料號
        if self.blank_num > 0:
            myrec = self.env['stock.picking'].search([])
            myres = myrec.create({'picking_type_id': 1, 'location_id': mypartnerlocid, 'location_dest_id': myblanklocid, 'move_type': 'direct',
                                  'user_id': self.stockin_owner.id, 'origin': '毛胚進料毛胚倉',
                                  'move_line_ids': [
                                      (0, 0, {'product_id': self.blank_no.id, 'company_id': 1, 'location_id': mypartnerlocid,
                                              'location_dest_id': myblanklocid, 'product_uom_id': 1,
                                              'qty_done': self.blank_num})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()



        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '毛胚進料輸入完成！'
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
