# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class ghbookingwizard(models.TransientModel):
    _name = "alldo_gh_iot.booking_wizard"


    booking_custom = fields.Many2one('res.partner', string="預留設定客戶", required=True)
    booking_prod = fields.Many2one('product.product', string="預留產品", required=True)
    prod_onhand = fields.Float(digits=(10, 0), string="產品在手數量")
    booking_blank = fields.Many2one('product.product', string="預留毛胚", required=True)
    blank_onhand = fields.Float(digits=(10, 0), string="毛胚在手數量")
    booking_num = fields.Float(digits=(10, 0), string="預留數量",default=0)
    booking_owner = fields.Many2one('res.users', string="預留設定人員", default=lambda self: self.env.uid)
    booking_date = fields.Date(string="設定日期", default=fields.Date.today())
    booking_desc = fields.Char(string="預留說明",default=' ')

    @api.onchange('booking_blank')
    def onclientchange(self):
        self.env.cr.execute("""select getblankonhand(%d)""" % self.booking_blank.id)
        self.blank_onhand = self.env.cr.fetchone()[0]

    @api.onchange('booking_custom')
    def onchangecusname(self):
        self.env.cr.execute("""select getpartnerprod(%d)""" % self.booking_custom.id)
        myrec = self.env.cr.fetchall()
        myids = []
        for rec in myrec:
            myids.append(rec[0])
        return {'domain': {'booking_prod': [('id', 'in', myids)]}}

    @api.onchange('booking_prod')
    def onchangebookingprod(self):
        self.env.cr.execute("""select getprodblank(%d)""" % self.booking_prod.id)
        self.booking_blank = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getprodonhand(%d)""" % self.booking_prod.id)
        self.prod_onhand = self.env.cr.fetchone()[0]

    def run_booking_proc(self):
        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
        myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
        myprodloc = mycomploc.prod_loc.id  # 公司成品庫存位置
        mypbookingloc = mycomploc.pbooking_loc.id  # 公司成品預留鎖定位置
        mybbookingloc = mycomploc.bbooking_loc.id  # 公司毛胚預留鎖定位置
        myrec = self.env['stock.picking'].search([])
        myprodonhand = self.prod_onhand
        myblankonhand = self.blank_onhand
        mybookingnum = self.booking_num
        if myprodonhand >= mybookingnum:
            myres = myrec.create(
                {'picking_type_id': 5, 'location_id': myprodloc, 'location_dest_id': mypbookingloc,
                 'move_type': 'direct',
                 'user_id': self.booking_owner.id, 'origin': '客戶預留鎖定需求',
                 'move_line_ids': [
                     (0, 0,
                      {'product_id': self.booking_prod.id, 'company_id': 1, 'location_id': myprodloc,
                       'location_dest_id': mypbookingloc, 'product_uom_id': 1,
                       'qty_done': self.booking_num})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
            self.env.cr.execute("""insert into alldo_gh_iot_prod_booking(booking_custom,booking_prod,booking_blank,booking_num,booking_owner,booking_date,booking_desc,booking_p_picking,booking_type,booking_blank_num,booking_prod_num) values (%d,%d,%d,%s,%d,'%s','%s',%d,'1',0,%s)""" %
                                (self.booking_custom.id,self.booking_prod.id,self.booking_blank.id,self.booking_num,self.booking_owner.id,self.booking_date,self.booking_desc,myres.id,self.booking_num))
            self.env.cr.execute("""commit""")

        elif self.prod_onhand > 0 and self.prod_onhand < self.booking_num:
            myres = myrec.create(
                {'picking_type_id': 5, 'location_id': myprodloc, 'location_dest_id': mypbookingloc,
                 'move_type': 'direct',
                 'user_id': self.booking_owner.id, 'origin': '客戶預留鎖定需求',
                 'move_line_ids': [
                     (0, 0,
                      {'product_id': self.booking_prod.id, 'company_id': 1, 'location_id': myprodloc,
                       'location_dest_id': mypbookingloc, 'product_uom_id': 1,
                       'qty_done': self.prod_onhand})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()


            myres1 = myrec.create(
                {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': mybbookingloc,
                 'move_type': 'direct',
                 'user_id': self.booking_owner.id, 'origin': '客戶預留鎖定需求',
                 'move_line_ids': [
                     (0, 0,
                      {'product_id': self.booking_prod.id, 'company_id': 1, 'location_id': myblanklocid,
                       'location_dest_id': mybbookingloc, 'product_uom_id': 1,
                       'qty_done': (self.booking_num - self.prod_onhand)})]})

            myres1.action_confirm()
            self.env.cr.commit()
            myres1.action_done()
            self.env.cr.commit()
            self.env.cr.execute("""insert into alldo_gh_iot_prod_booking(booking_custom,booking_prod,booking_blank,booking_num,booking_owner,booking_date,booking_desc,booking_p_picking,booking_b_picking,booking_type,booking_blank_num,booking_prod_num) values (%d,%d,%d,%s,%d,'%s','%s',%d,%d,'1',%s,%d)""" %
                (self.booking_custom.id, self.booking_prod.id, self.booking_blank.id, self.booking_num,self.booking_owner.id, self.booking_date,self.booking_desc, myres.id,myres1.id,(self.booking_num - self.prod_onhand,self.prod_onhand)))
            self.env.cr.execute("""commit""")
        elif self.prod_onhand == 0:
            myres = myrec.create(
                {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': mybbookingloc,
                 'move_type': 'direct',
                 'user_id': self.booking_owner.id, 'origin': '客戶預留鎖定需求',
                 'move_line_ids': [
                     (0, 0,
                      {'product_id': self.booking_prod.id, 'company_id': 1, 'location_id': myblanklocid,
                       'location_dest_id': mybbookingloc, 'product_uom_id': 1,
                       'qty_done': self.booking_num})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
            self.env.cr.execute("""insert into alldo_gh_iot_prod_booking(booking_custom,booking_prod,booking_blank,booking_num,booking_owner,booking_date,booking_desc,booking_b_picking,booking_type,booking_blank_num,booking_prod_num) values (%d,%d,%d,%s,%d,'%s','%s',%d,'1',%s,0)""" %
                (self.booking_custom.id, self.booking_prod.id, self.booking_blank.id, self.booking_num,self.booking_owner.id, self.booking_date, self.booking_desc, myres.id,self.booking_num))
            self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '產品鎖定完成！'
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
