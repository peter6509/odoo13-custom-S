# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaelectronicscale(models.Model):
    _name = "alldo_ipla_iot.electronic_scale"
    _description = "電子秤刷碼數據"
    _order = "scale_datetime desc"

    scale_type = fields.Selection([('1','機台投料'),('2','物料入庫')],string="類別",default='1')
    product_no = fields.Many2one('product.product',string="料號")
    need_lotno = fields.Boolean(string="是否需批次號",default=False)
    lot_no = fields.Many2one('stock.quant',string="批號")
    scale_weight = fields.Float(digits=(10,3),string="重量")
    equipment_no = fields.Many2one('maintenance.equipment', string="設備")
    uom_id = fields.Many2one('uom.uom',string="單位")
    scale_owner = fields.Many2one('res.users',string="作業人員",default=lambda self:self.env.uid)
    picking_no = fields.Many2one('stock.picking',string="調撥單號",readonly=True)
    is_posting = fields.Selection([('1','未過帳'),('2','已過帳'),('3','記錄缺批次號')],string="資料狀態",default='1')
    scale_datetime = fields.Datetime(string="日期時間")

    @api.onchange('product_no')
    def onchangeprodno(self):
        mytracking = self.product_no.tracking
        self.env.cr.execute("""select getfurnace()""")
        myrec1 = self.env.cr.fetchall()
        ids1 = []
        for rec1 in myrec1:
            ids1.append(rec1[0])
        if mytracking == 'lot':
            self.need_lotno = True
        else:
            self.need_lotno = False
        self.env.cr.execute("""select genlotid(%d)""" % self.product_no.id)
        myrec = self.env.cr.fetchall()
        ids = []
        for rec in myrec:
            ids.append(rec[0])
        return {'domain': {'lot_no': [('id', 'in', ids)]}}

    def run_scale_move(self):  ## odoo schedule action  每5分鐘一次
        ## 熔爐混合料號
        myfurnaceprodid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].furnace_prod_id.id
        ## 熔爐位置
        myfurnacelocid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].furnace_loc.id
        ## 原物料位置
        mymateriallocid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].material_loc.id
        mymolocid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].mo_loc.id
        mypickingrec = self.env['stock.picking'].search([])
        myrec = self.env['alldo_ipla_iot.electronic_scale'].search([('picking_no','=',False)])
        for rec in myrec:
            if rec.scale_type=='1':  # 熔爐投料
                if rec.product_no.product_tmpl_id.tracking=='lot' and not rec.lot_no :
                    # print("物料 [%s] 需輸入批次號" % rec.product_no.default_code)
                    self.env.cr.execute("""update alldo_ipla_iot_electronic_scale set is_posting='3' where id=%d""" % rec.id)
                    self.env.cr.execute("""commit""")
                else:                # 無需批次號 or 資料確認無問題可投料
                    if not rec.lot_no:
                        try:
                            ## 原物料倉 -> 生產位置 一般料號
                            myres = mypickingrec.create(
                                {'picking_type_id': 5, 'location_id': mymateriallocid, 'location_dest_id': mymolocid,
                                 'move_type': 'direct','user_id': rec.scale_owner.id,
                                 'move_line_ids': [
                                     (0, 0,{'product_id': rec.product_no.id, 'company_id': 1, 'location_id': mymateriallocid,
                                       'location_dest_id': mymolocid, 'product_uom_id': rec.product_no.product_tmpl_id.uom_id.id,
                                       'qty_done': rec.scale_weight})]})

                            myres.action_confirm()
                            self.env.cr.commit()
                            myres.action_done()
                            self.env.cr.commit()
                            self.env.cr.execute("""update alldo_ipla_iot_electronic_scale set is_posting='2',picking_no=%d where id=%d""" % (myres.id, rec.id))
                            self.env.cr.execute("""commit""")

                            ## 生產位置 -> 熔爐位置 熔爐混合料號
                            myres1 = mypickingrec.create(
                                {'picking_type_id': 5, 'location_id': mymolocid, 'location_dest_id': myfurnacelocid,
                                 'move_type': 'direct', 'user_id': rec.scale_owner.id,
                                 'move_line_ids': [(0, 0,
                                      {'product_id': myfurnaceprodid, 'company_id': 1, 'location_id': mymolocid,
                                       'location_dest_id': myfurnacelocid,
                                       'product_uom_id': rec.product_no.product_tmpl_id.uom_id.id,
                                       'qty_done': rec.scale_weight})]})

                            myres1.action_confirm()
                            self.env.cr.commit()
                            myres1.action_done()
                            self.env.cr.commit()
                        except Exception as inst:
                            A=1

                    else:
                        try:
                            ## 批次號 原物料倉 -> 生產位置 一般產品
                            mylotid = rec.lot_no.lot_id.id
                            myres = mypickingrec.create(
                                {'picking_type_id': 5, 'location_id': mymateriallocid, 'location_dest_id': mymolocid,
                                 'move_type': 'direct','user_id': rec.scale_owner.id, 'origin': '熔爐投料','move_line_ids': [
                                     (0, 0,{'product_id': rec.product_no.id, 'company_id': 1, 'location_id': mymateriallocid,
                                       'lot_id': mylotid,'location_dest_id': mymolocid, 'product_uom_id': rec.product_no.product_tmpl_id.uom_id.id,'qty_done': rec.scale_weight})]})

                            myres.action_confirm()
                            self.env.cr.commit()
                            myres.action_done()
                            self.env.cr.commit()
                            self.env.cr.execute("""update alldo_ipla_iot_electronic_scale set is_posting='2',picking_no=%d where id=%d""" % (myres.id, rec.id))
                            self.env.cr.execute("""commit""")
                            ## 生產位置 -> 熔爐位置 熔爐混合料號
                            myres1 = mypickingrec.create(
                                {'picking_type_id': 5, 'location_id': mymolocid, 'location_dest_id': myfurnacelocid,
                                 'move_type': 'direct', 'user_id': rec.scale_owner.id, 'origin': '熔爐投料', 'move_line_ids': [
                                    (0, 0, {'product_id': myfurnaceprodid, 'company_id': 1, 'location_id': mymolocid,
                                           'location_dest_id': myfurnacelocid,
                                           'product_uom_id': 3,
                                           'qty_done': rec.scale_weight})]})
                            myres1.action_confirm()
                            self.env.cr.commit()
                            myres1.action_done()
                            self.env.cr.commit()
                        except Exception as inst:
                            A=1
            else:   # 回收料入庫
                try:
                   myres = mypickingrec.create({'picking_type_id': 5, 'location_id': mymolocid, 'location_dest_id': mymateriallocid,
                         'move_type': 'direct',
                         'user_id': rec.scale_owner.id, 'origin': '產線回收料入庫',
                         'move_line_ids': [(0, 0, {'product_id': rec.product_no.id, 'company_id': 1, 'location_id': mymolocid,
                                     'location_dest_id': mymateriallocid,
                                     'product_uom_id': rec.product_no.product_tmpl_id.uom_id.id,
                                     'qty_done': rec.scale_weight})]})

                   myres.action_confirm()
                   self.env.cr.commit()
                   myres.action_done()
                   self.env.cr.commit()
                   self.env.cr.execute("""update alldo_ipla_iot_electronic_scale set is_posting='2',picking_no=%d where id=%d""" % (myres.id, rec.id))
                   self.env.cr.execute("""commit""")
                except Exception as inst:
                    A=1
