# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class iplafurnacemove(models.TransientModel):
    _name = "alldo_ipla_iot.furnace_move_wizard"
    _descripton = "原材物料投料熔爐精靈"

    product_no = fields.Many2one('product.template',string="料號",required=True)
    have_lot = fields.Boolean(default=False)
    quant_id = fields.Many2one('stock.quant',string="批次號")
    equipment_no = fields.Many2one('maintenance.equipment',string="熔爐")
    quantity = fields.Float(digits=(10,3),string="數量(KG)")
    move_owner = fields.Many2one('res.users',string="入帳人員",default=lambda self:self.env.uid)

    @api.onchange('product_no')
    def onchangeprodno(self):
        mytracking = self.product_no.tracking
        self.env.cr.execute("""select getfurnace()""")
        myrec1 = self.env.cr.fetchall()
        ids1 =[]
        for rec1 in myrec1:
            ids1.append(rec1[0])
        if mytracking=='lot':
            self.have_lot=True
        else:
            self.have_lot=False
        self.env.cr.execute("""select genlotid(%d)""" % self.product_no.id)
        myrec = self.env.cr.fetchall()
        ids = []
        for rec in myrec:
            ids.append(rec[0])
        return {'domain': {'quant_id': [('id', 'in', ids)],'equipment_no': [('id','in',ids1)]}}

    @api.onchange('quant_id')
    def onchangequantid(self):
        myrec = self.env['stock.quant'].search([('id','=',self.quant_id.id)])
        self.quantity = myrec.quantity


    def run_furnace_move(self):
        if self.have_lot==True and not self.quant_id:
            raise UserError("必須輸入批次號碼")

        # myrec = self.env['stock.quant'].search([('id', '=', self.quant_id.id)])
        # myquantity = myrec.quantity
        # if self.quantity > myquantity:
        #     raise UserError("數量超過一個批號,請分開作業！")
        ## 熔爐混合料號
        myfurnaceprodid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].furnace_prod_id.id
        ## 熔爐位置
        myfurnacelocid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].furnace_loc.id
        ## 生產位置
        mymolocid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].mo_loc.id
        ## 原物料位置
        mymateriallocid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].material_loc.id
        ## 批次號
        mylotid = self.env['stock.quant'].search([('id','=',self.quant_id.id)]).lot_id.id

        mypickingrec = self.env['stock.picking'].search([])
        if not self.equipment_no:
            myequipname = ' '
        else:
            myequipname= self.equipment_no.name
        ## 先將 投料 移動到 furnace_loc 位置
        self.env.cr.execute("""select getproduom(%d)""" % self.product_no.id)
        myuomid = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getproduom(%d)""" % myfurnaceprodid)
        myfurnaceuomid = self.env.cr.fetchone()[0]
        if not self.quant_id:  ## 無批次號狀況
            myres = mypickingrec.create({'picking_type_id': 5, 'location_id': mymateriallocid, 'location_dest_id': mymolocid,
                 'move_type': 'direct',
                 'user_id': self.move_owner.id, 'report_memo': myequipname,
                 'move_line_ids': [
                     (0, 0, {'product_id': self.product_no.id, 'company_id': 1, 'location_id': mymateriallocid,
                             'location_dest_id': mymolocid, 'product_uom_id': myuomid, 'qty_done': self.quantity})]})
            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
            myres1 = mypickingrec.create(
                {'picking_type_id': 5, 'location_id': mymolocid, 'location_dest_id': myfurnacelocid,
                 'move_type': 'direct',
                 'user_id': self.move_owner.id, 'report_memo': myequipname,
                 'move_line_ids': [
                     (0, 0, {'product_id': myfurnaceprodid, 'company_id': 1, 'location_id': mymolocid,
                             'location_dest_id': myfurnacelocid, 'product_uom_id': myfurnaceuomid, 'qty_done': self.quantity})]})
            myres1.action_confirm()
            self.env.cr.commit()
            myres1.action_done()
            self.env.cr.commit()


        else:   ## 有批次號狀況
            ## 將物料 從原物料倉 -> 生產位置 含批次號
            myres = mypickingrec.create({'picking_type_id': 5, 'location_id': mymateriallocid, 'location_dest_id': mymolocid, 'move_type': 'direct',
                  'user_id': self.move_owner.id, 'report_memo': self.equipment_no.name ,
                  'move_line_ids': [
                      (0, 0, {'product_id': self.product_no.id, 'company_id': 1, 'location_id': mymateriallocid,'lot_id':mylotid,
                              'location_dest_id': mymolocid, 'product_uom_id': myuomid , 'qty_done': self.quantity})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
            ## 將物料從 生產位置 -> 熔爐位置 轉換為 鋁液混合料號 沒有批號
            myres1 = mypickingrec.create(
                {'picking_type_id': 5, 'location_id': mymolocid, 'location_dest_id': myfurnacelocid,
                 'move_type': 'direct',
                 'user_id': self.move_owner.id, 'report_memo': self.equipment_no.name,
                 'move_line_ids': [
                     (0, 0, {'product_id': myfurnaceprodid, 'company_id': 1, 'location_id': mymolocid,
                             'location_dest_id': myfurnacelocid, 'product_uom_id': myfurnaceuomid,
                             'qty_done': self.quantity})]})

            myres1.action_confirm()
            self.env.cr.commit()
            myres1.action_done()
            self.env.cr.commit()



        myfurnaceerec = self.env['alldo_ipla_iot.furnace_stock_move']

        if not self.quant_id:
            myfurnaceerec.create({'product_no': self.product_no.id, 'mixprod_no': myfurnaceprodid,
                                  'move_type': '1', 'move_datetime': fields.datetime.now(),
                                  'stock_owner': self.move_owner.id,
                                  'equipment_no': self.equipment_no.id, 'quantity': self.quantity, 'product_uom_id': 3})
        else:
            myfurnaceerec.create({'product_no':self.product_no.id,'mixprod_no':myfurnaceprodid,'lot_id':mylotid,
                                  'move_type':'1','move_datetime':fields.datetime.now(),'stock_owner':self.move_owner.id,
                                  'equipment_no':self.equipment_no.id,'quantity':self.quantity,'product_uom_id':3})


