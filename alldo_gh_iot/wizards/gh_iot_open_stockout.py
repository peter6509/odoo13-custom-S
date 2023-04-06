# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError


class ghiotopenstockout(models.TransientModel):
    _name = "alldo_gh_iot.open_stockout_wizard"
    _description = "工單重置出貨單精靈"

    cus_name = fields.Many2one('res.partner', string="客戶", required=True)
    prod_id = fields.Many2one('product.product', string="產品料號", required=True)
    wkorder_id = fields.Many2one('alldo_gh_iot.workorder',string="工單號碼",required=True)
    product_num = fields.Float(digits=(10,0),string="訂單數量", required=True, default=0)
    shipping_date = fields.Date(string="出貨日")
    ship_num = fields.Float(digits=(10,0),string="已出貨數量",required=True,default=0)
    in_owner = fields.Many2one('res.users',string="登錄人員",default=lambda self:self.env.uid)


    @api.onchange('cus_name')
    def onchangecusname(self):
        self.env.cr.execute("""select getpartnerprod(%d)""" % self.cus_name.id)
        myrec = self.env.cr.fetchall()
        myids = []
        for rec in myrec:
            myids.append(rec[0])
        return {'domain': {'prod_id': [('id', 'in', myids)]}}

    @api.onchange('prod_id')
    def onchangeprodid(self):
        myrec = self.env['alldo_gh_iot.workorder'].search([('product_no','=',self.prod_id.id)],order="name desc")
        ids=[]
        for line in myrec:
            ids.append(line.id)
        return {'domain': {'wkorder_id': [('id', 'in', ids)]}}

    def run_open_stockout(self):
        if self.product_num > 0:
            ## 直接產生一張出貨單 待辦  ; 公司產品倉 => 客戶位置倉庫
            mymogpid = self.wkorder_id.mo_group_id
            myreportmemo = self.wkorder_id.name
            mycustomerlocid = self.cus_name.property_stock_customer.id
            mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
            myprodlocid = mycomploc.prod_loc.id
            myrec = self.env['stock.picking'].search([])

            myprodid = self.prod_id.id
            myres = myrec.create(
                {'picking_type_id': 2, 'location_id': myprodlocid, 'location_dest_id': mycustomerlocid, 'move_type': 'direct','state':'draft',
                 'user_id': self.in_owner.id, 'origin': ' ', 'state':'assigned','scheduled_date':self.shipping_date,
                 'partner_id':self.cus_name.id,'mo_group_id' : mymogpid,'report_memo':myreportmemo,
                 'move_ids_without_package': [(0, 0, {'product_id': myprodid, 'company_id': 1, 'location_id': myprodlocid,
                                           'location_dest_id': mycustomerlocid, 'product_uom': 1,'name':self.prod_id.name,
                                           'product_uom_qty': self.product_num,'quantity_done':self.ship_num})],})

            myres.action_confirm()
            self.env.cr.commit()
            # myres.action_done()
            myshippingno = myres.name
            myshippingid = myres.id


            mystockinid = self.wkorder_id.blankin_picking.id
            mystockinno = self.wkorder_id.blankin_picking.name
            mydesc = '內部收貨單:(%s) 內部交貨單:(%s)' % (mystockinno, myshippingno)
            self.env.cr.execute("""select updatemomemo(%d,'%s',%d,%d)""" % (self.cus_name.id,mydesc,mystockinid,myshippingid))
            self.env.cr.execute("""commit""")

            return {'view_name': 'alldoghiotworkorder',
                    'name': (u'工單作業'),
                    'views': [[False, 'form'], [False, 'tree']],
                    'res_model': 'alldo_gh_iot.workorder',
                    'context': self._context,
                    'type': 'ir.actions.act_window',
                    'target': 'self',
                    'res_id': self.wkorder_id.id,
                    'view_mode': 'form',
                    'view_type': 'form',
                    'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                    }
        else:
            A=1
