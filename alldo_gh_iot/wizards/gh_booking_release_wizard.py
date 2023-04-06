# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghbookingreleasewizard(models.TransientModel):
    _name = "alldo_gh_iot.booking_release_wizard"

    release_owner = fields.Many2one('res.users',string="解除人員",default=lambda self:self.env.uid)
    booking_id = fields.Many2one('alldo_gh_iot.prod_booking',string="鎖定記錄")
    po_id = fields.Many2one('alldo_gh_iot.po_wkorder', string="訂單")
    release_custom = fields.Many2one('res.partner', string="預留設定客戶")
    booking_prod = fields.Many2one('product.product', string="預留產品")
    booking_blank = fields.Many2one('product.product',string="預留毛坯")
    booking_num = fields.Float(digits=(10, 0), string="鎖定數量")
    release_num = fields.Float(digits=(10, 0), string="解除數量", default=0)
    booking_p_picking = fields.Many2one('stock.picking', string="產品預留調撥單號")
    booking_b_picking = fields.Many2one('stock.picking', string="毛胚預留調撥單號")
    release_desc = fields.Char(string="解除說明",default=' ')


    @api.onchange('release_owner')
    def onclientchangeowner(self):
        mywkorderid = self.env.context.get('powkorder_id')
        if mywkorderid:
            myrec = self.env['alldo_gh_iot.prod_booking'].search([('po_id','=',mywkorderid)])
            myid = myrec.id
        else:
            myid = self.env.context.get('booking_id')
        if myid:
            print('booking_id => %d' % myid)
            self.booking_id = myid

            myrec = self.env['alldo_gh_iot.prod_booking'].search([('id', '=',myid)])
            mybookingprodid = myrec.booking_prod.id
            mybookingblankid = myrec.booking_blank.id
            self.po_id = myrec.po_id.id
            self.booking_prod = mybookingprodid
            self.booking_blank = mybookingblankid
            self.booking_p_picking = myrec.booking_p_picking.id
            self.booking_b_picking = myrec.booking_b_picking.id
            # print(myrec.booking_num)
            # print(myrec.release_prod_num)
            # print(myrec.release_blank_num)


    @api.onchange('po_id')
    def onchangepoid(self):
        print("POID:%d" % self.po_id.id)
        self.env.cr.execute("""select getpounreleasenum(%d)""" % self.po_id.id)
        self.booking_num = self.env.cr.fetchone()[0]

    def run_booking_release(self):
        if self.release_num == 0 :
            raise UserError("未輸入解除數量")
        if self.release_num > 0 and self.release_num > self.booking_num :
            raise UserError("無法解除超過產品預留鎖定數量")
        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
        myblankloc = mycomploc.blank_loc.id  # 公司毛胚庫存位置
        myprodloc = mycomploc.prod_loc.id  # 公司成品庫存位置
        mypbookingloc = mycomploc.pbooking_loc.id  # 公司成品預留鎖定位置
        mybbookingloc = mycomploc.bbooking_loc.id  # 公司毛胚預留鎖定位置
        myppicking = self.booking_p_picking.id
        mybpicking = self.booking_b_picking.id
        mybookingtype = self.booking_id.booking_type
        mypoid = self.po_id.id
        print("POID:%d" % mypoid)
        mybookingprodnum = self.booking_id.booking_prod_num - self.booking_id.release_prod_num
        mybookingblanknum = self.booking_id.booking_blank_num - self.booking_id.release_blank_num
        myrec = self.env['stock.picking']

        myres = myrec.create(
            {'picking_type_id': 5, 'location_id': mypbookingloc, 'location_dest_id': myprodloc,
             'move_type': 'direct',
             'user_id': self.release_owner.id, 'origin': '客戶預留鎖定解除',
             'move_line_ids': [
                 (0, 0,
                  {'product_id': self.booking_prod.id, 'company_id': 1, 'location_id': mypbookingloc,
                   'location_dest_id': myprodloc, 'product_uom_id': 1,
                   'qty_done': self.release_num})]})

        myres.action_confirm()
        self.env.cr.commit()
        myres.action_done()
        self.env.cr.commit()
        self.env.cr.execute("""insert into alldo_gh_iot_prod_booking_release(po_id,release_num,release_owner,release_desc,release_p_picking,release_date) values (%d,%s,%d,'%s',%d,current_date)""" % (mypoid, self.release_num, self.release_owner.id, self.release_desc, myres.id))
        self.env.cr.execute("""commit""")
        if self.release_num == self.booking_num :
            self.env.cr.execute("""update alldo_gh_iot_prod_booking set release_prod_num=coalesce(release_prod_num,0) + %s ,booking_type='2',booking_release=current_date where id=%d""" % (self.release_num, self.booking_id.id))
        else:
            self.env.cr.execute("""update alldo_gh_iot_prod_booking set release_prod_num=coalesce(release_prod_num,0) + %s ,booking_release=current_date where id=%d""" % (self.release_num, self.booking_id.id))
        self.env.cr.execute("""commit""")

        #
        #
        #
        # if mybookingprodnum > 0 and self.release_num <= mybookingprodnum : # 只要解鎖產品
        #     myres = myrec.create(
        #         {'picking_type_id': 5, 'location_id': mypbookingloc, 'location_dest_id': myprodloc,
        #          'move_type': 'direct',
        #          'user_id': self.release_owner.id, 'origin': '客戶預留鎖定解除',
        #          'move_line_ids': [
        #              (0, 0,
        #               {'product_id': self.booking_prod.id, 'company_id': 1, 'location_id': mypbookingloc,
        #                'location_dest_id': myprodloc, 'product_uom_id': 1,
        #                'qty_done': self.release_num})]})
        #
        #     myres.action_confirm()
        #     self.env.cr.commit()
        #     myres.action_done()
        #     self.env.cr.commit()
        #     self.env.cr.execute("""insert into alldo_gh_iot_prod_booking_release(po_id,release_num,release_owner,release_desc,release_p_picking,release_date) values (%d,%s,%d,'%s',%d,current_date)""" % (mypoid,self.release_num,self.release_owner.id,self.release_desc,myres.id))
        #     self.env.cr.execute("""commit""")
        #     if self.release_num == (mybookingprodnum + mybookingblanknum) :
        #         self.env.cr.execute("""update alldo_gh_iot_prod_booking set release_prod_num=coalesce(release_prod_num,0) + %s ,booking_type='2',booking_release=current_date where id=%d""" % (self.release_num,self.booking_id.id))
        #     else:
        #         self.env.cr.execute("""update alldo_gh_iot_prod_booking set release_prod_num=coalesce(release_prod_num,0) + %s ,booking_release=current_date where id=%d""" % (self.release_num,self.booking_id.id))
        #     self.env.cr.execute("""commit""")
        # elif mybookingprodnum > 0 and self.release_num > mybookingprodnum and self.release_num <= (mybookingprodnum + mybookingblanknum) : # 解兩種
        #     myres = myrec.create(
        #         {'picking_type_id': 5, 'location_id': mypbookingloc, 'location_dest_id': myprodloc,
        #          'move_type': 'direct',
        #          'user_id': self.release_owner.id, 'origin': '客戶預留鎖定解除',
        #          'move_line_ids': [
        #              (0, 0,
        #               {'product_id': self.booking_prod.id, 'company_id': 1, 'location_id': mypbookingloc,
        #                'location_dest_id': myprodloc, 'product_uom_id': 1,
        #                'qty_done': mybookingprodnum})]})
        #
        #     myres.action_confirm()
        #     self.env.cr.commit()
        #     myres.action_done()
        #     self.env.cr.commit()
        #
        #     self.env.cr.execute("""update alldo_gh_iot_prod_booking set release_prod_num=coalesce(release_prod_num,0) + %s ,booking_release=current_date where id=%d""" % (mybookingprodnum, self.booking_id.id))
        #     self.env.cr.execute("""commit""")
        #
        #     myres1 = myrec.create(
        #         {'picking_type_id': 5, 'location_id': mybbookingloc, 'location_dest_id': myblankloc,
        #          'move_type': 'direct',
        #          'user_id': self.release_owner.id, 'origin': '客戶預留鎖定解除',
        #          'move_line_ids': [
        #              (0, 0,
        #               {'product_id': self.booking_blank.id, 'company_id': 1, 'location_id': mybbookingloc,
        #                'location_dest_id': myblankloc, 'product_uom_id': 1,
        #                'qty_done': (self.release_num - mybookingprodnum) })]})
        #
        #     myres1.action_confirm()
        #     self.env.cr.commit()
        #     myres1.action_done()
        #     self.env.cr.commit()
        #     self.env.cr.execute("""insert into alldo_gh_iot_prod_booking_release(po_id,release_num,release_owner,release_desc,release_p_picking,release_b_picking,release_date) values (%d,%s,%d,'%s',%d,%d,current_date)""" % (mypoid, self.release_num, self.release_owner.id, self.release_desc, myres.id,myres1.id))
        #     self.env.cr.execute("""commit""")
        #     if self.release_num == (mybookingprodnum + mybookingblanknum) :
        #         self.env.cr.execute("""update alldo_gh_iot_prod_booking set release_blank_num=coalesce(release_blank_num,0) + %s ,booking_type='2',booking_release=current_date where id=%d""" % ((self.release_num - mybookingprodnum),self.booking_id.id))
        #     else:
        #         self.env.cr.execute("""update alldo_gh_iot_prod_booking set release_blank_num=coalesce(release_blank_num,0) + %s ,booking_release=current_date where id=%d""" % ((self.release_num - mybookingprodnum), self.booking_id.id))
        #     self.env.cr.execute("""commit""")
        # elif mybookingprodnum == 0 and self.release_num <= mybookingblanknum : # 要解鎖毛胚
        #     myres = myrec.create(
        #         {'picking_type_id': 5, 'location_id': mybbookingloc, 'location_dest_id': myblankloc,
        #          'move_type': 'direct',
        #          'user_id': self.release_owner.id, 'origin': '客戶預留鎖定解除',
        #          'move_line_ids': [
        #              (0, 0,
        #               {'product_id': self.booking_blank.id, 'company_id': 1, 'location_id': mybbookingloc,
        #                'location_dest_id': myblankloc, 'product_uom_id': 1,
        #                'qty_done': self.release_num})]})
        #
        #     myres.action_confirm()
        #     self.env.cr.commit()
        #     myres.action_done()
        #     self.env.cr.commit()
        #     self.env.cr.execute("""insert into alldo_gh_iot_prod_booking_release(po_id,release_num,release_owner,release_desc,release_b_picking,release_date) values (%d,%s,%d,'%s',%d,current_date)""" % (mypoid, self.release_num, self.release_owner.id, self.release_desc, myres.id))
        #     self.env.cr.execute("""commit""")
        #     if self.release_num == mybookingblanknum :
        #         self.env.cr.execute("""update alldo_gh_iot_prod_booking set release_blank_num=coalesce(release_blank_num,0) + %s ,booking_type='2',booking_release=current_date where id=%d""" % (self.release_num, self.booking_id.id))
        #     else:
        #         self.env.cr.execute("""update alldo_gh_iot_prod_booking set release_blank_num=coalesce(release_blank_num,0) + %s ,booking_release=current_date where id=%d""" % (self.release_num, self.booking_id.id))
        #     self.env.cr.execute("""commit""")
        # else:
        #     raise UserError("解除數量大於預留數量！")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '產品解鎖完成！'
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


