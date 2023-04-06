# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotbooking(models.Model):
    _name = "alldo_gh_iot.prod_booking"
    _description = "客戶預留設定記錄"
    _order = "booking_date desc"

    po_id = fields.Many2one('alldo_gh_iot.po_wkorder',string="訂單",ondelete='cascade')
    booking_custom = fields.Many2one('res.partner',string="預留設定客戶",required=True)
    booking_prod = fields.Many2one('product.product',string="預留產品",required=True)
    prod_onhand = fields.Float(digits=(10,0),string="產品在手數量")
    booking_blank = fields.Many2one('product.product',string="預留毛胚",required=True)
    blank_onhand = fields.Float(digits=(10,0),string="毛胚在手數量")
    booking_num = fields.Float(digits=(10,0),string="預留數量")
    booking_prod_num = fields.Float(digits=(10,0),string="預留產品數量")
    booking_blank_num = fields.Float(digits=(10,0),string="預留毛胚數量")
    release_prod_num = fields.Float(digits=(10,0),string="解除產品數量")
    release_blank_num = fields.Float(digits=(10,0),string="解除毛胚數量")
    booking_owner = fields.Many2one('res.users',string="預留設定人員",default=lambda self:self.env.uid)
    booking_date = fields.Date(string="設定日期",default=fields.Date.today())
    booking_release = fields.Date(string="解除日期")
    booking_desc = fields.Char(string="預留說明")
    booking_type = fields.Selection([('1','預留鎖定'),('2','預留解除')],string="預留設定狀態",default='1')
    booking_p_picking = fields.Many2one('stock.picking',string="產品預留調撥單號")
    booking_b_picking = fields.Many2one('stock.picking',string="毛胚預留調撥單號")

    def run_booking_release(self):
        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
        myblankloc = mycomploc.blank_loc.id  # 公司毛胚庫存位置
        myprodloc = mycomploc.prod_loc.id  # 公司成品庫存位置
        mypbookingloc = mycomploc.pbooking_loc.id  # 公司成品預留鎖定位置
        mybbookingloc = mycomploc.bbooking_loc.id  # 公司毛胚預留鎖定位置
        myppicking = self.booking_p_picking.id
        mybpicking = self.booking_b_picking.id
        mybookingtype = self.booking_type


        if self.booking_p_picking != False:
            self.env.cr.execute("""select getbookingnum(%d)""" % self.booking_p_picking.id)
            mynum = self.env.cr.fetchone()[0]
            if mynum > 0 :
                myrec = self.env['stock.picking']
                myres = myrec.create(
                    {'picking_type_id': 5, 'location_id': mypbookingloc, 'location_dest_id': myprodloc,
                     'move_type': 'direct',
                     'user_id': self.booking_owner.id, 'origin': '客戶預留鎖定解除',
                     'move_line_ids': [
                         (0, 0,
                          {'product_id': self.booking_prod.id, 'company_id': 1, 'location_id': mypbookingloc,
                           'location_dest_id': myprodloc, 'product_uom_id': 1,
                           'qty_done': mynum})]})

                myres.action_confirm()
                self.env.cr.commit()
                myres.action_done()
                self.env.cr.commit()
                self.env.cr.execute("""update alldo_gh_iot_prod_booking set booking_p_picking=null,booking_type='2',booking_release=current_date where id=%d""" % self.id)
                self.env.cr.execute("""commit""")
        if self.booking_b_picking != False:
            self.env.cr.execute("""select getbookingnum(%d)""" % self.booking_b_picking.id)
            mynum = self.env.cr.fetchone()[0]
            if mynum > 0 :
                myrec = self.env['stock.picking']
                myres = myrec.create(
                    {'picking_type_id': 5, 'location_id': mybbookingloc, 'location_dest_id': myblankloc,
                     'move_type': 'direct',
                     'user_id': self.booking_owner.id, 'origin': '客戶預留鎖定解除',
                     'move_line_ids': [
                         (0, 0,
                          {'product_id': self.booking_blank.id, 'company_id': 1, 'location_id': mybbookingloc,
                           'location_dest_id': myblankloc, 'product_uom_id': 1,
                           'qty_done': mynum})]})

                myres.action_confirm()
                self.env.cr.commit()
                myres.action_done()
                self.env.cr.commit()
                self.env.cr.execute("""update alldo_gh_iot_prod_booking set booking_b_picking=null,booking_type='2',booking_release=current_date where id=%d""" % self.id)
                self.env.cr.execute("""commit""")


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

    def name_get(self):
        res = []
        for rec in self:
            myname = "[%s-(%s)]-(預留鎖定 %s pcs)" % (rec.booking_custom.name, rec.booking_prod.default_code, rec.booking_num)
            res += [(rec.id, myname)]
        return res

    # @api.model
    # def create(self, vals):
    #
    #
    #      res = super(ghiotbooking, self).create(vals)
    #      return res

    def write(self, vals):
        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
        myblankloc = mycomploc.blank_loc.id  # 公司毛胚庫存位置
        myprodloc = mycomploc.prod_loc.id  # 公司成品庫存位置
        mypbookingloc = mycomploc.pbooking_loc.id  # 公司成品預留鎖定位置
        mybbookingloc = mycomploc.bbooking_loc.id  # 公司毛胚預留鎖定位置
        if 'booking_num' in vals :
            raise UserError('不能變動預留數量,可以解除 or 額外增加一筆')
        if 'booking_custom' in vals :
            raise UserError('不能變動預留客戶,可以解除 or 額外增加一筆')
        if 'booking_prod' in vals or 'booking_blank' in vals :
            raise UserError('不能變動預留產品,可以解除 or 額外增加一筆')
        res = super(ghiotbooking, self).write(vals)
        for rec in self:
            if rec.booking_type == '2' and rec.booking_p_picking != False:
                self.env.cr.execute("""select getbookingnum(%d)""" % rec.booking_p_picking.id)
                mynum = self.env.cr.fetchone()[0]
                myrec = self.env['stock.picking']
                myres = myrec.create(
                    {'picking_type_id': 5, 'location_id': mypbookingloc, 'location_dest_id': myprodloc,
                     'move_type': 'direct',
                     'user_id': self.booking_owner.id, 'origin': '客戶預留鎖定解除',
                     'move_line_ids': [
                         (0, 0,
                          {'product_id': self.booking_prod.id, 'company_id': 1, 'location_id': mypbookingloc,
                           'location_dest_id': myprodloc, 'product_uom_id': self.booking_prod.uom_id.id,
                           'qty_done': mynum})]})

                myres.action_confirm()
                self.env.cr.commit()
                myres.action_done()
                self.env.cr.commit()
                self.env.cr.execute("""update alldo_gh_iot_prod_booking set booking_p_picking=null where id=%d""" % rec.id)
                self.env.cr.execute("""commit""")
            if rec.booking_type == '2' and rec.booking_b_picking != False:
                self.env.cr.execute("""select getbookingnum(%d)""" % rec.booking_b_picking.id)
                mynum = self.env.cr.fetchone()[0]
                myrec = self.env['stock.picking']
                myres = myrec.create(
                    {'picking_type_id': 5, 'location_id': mybbookingloc, 'location_dest_id': myblankloc,
                     'move_type': 'direct',
                     'user_id': self.booking_owner.id, 'origin': '客戶預留鎖定解除',
                     'move_line_ids': [
                         (0, 0,
                          {'product_id': self.booking_prod.id, 'company_id': 1, 'location_id': mybbookingloc,
                           'location_dest_id': myblankloc, 'product_uom_id': self.booking_blank.uom_id.id,
                           'qty_done': mynum})]})

                myres.action_confirm()
                self.env.cr.commit()
                myres.action_done()
                self.env.cr.commit()
                self.env.cr.execute("""update alldo_gh_iot_prod_booking set booking_b_picking=null where id=%d""" % rec.id)
                self.env.cr.execute("""commit""")
        return res

    @api.onchange('booking_prod')
    def onchangebookingprod(self):
        self.env.cr.execute("""select getprodblank(%d)""" % self.booking_prod.id)
        self.booking_blank = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getprodonhand(%d)""" % self.booking_prod.id)
        self.prod_onhand = self.env.cr.fetchone()[0]