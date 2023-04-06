# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmeprodout(models.Model):
    _name = "alldo_acme_iot.prodout"
    _order = "prodout_date desc"

    prodout_date = fields.Date(string="委外日期",default=fields.Date.today())
    partner_id = fields.Many2one('res.partner',string="委外廠商")
    prodout_line = fields.One2many('alldo_acme_iot.prodout_line','prodout_id',copy=False)
    prodout_owner = fields.Many2one('res.users',string="建檔人",default=lambda self:self.env.uid)
    tot_plastic_frame1 = fields.Integer(string="隨貨出塑膠框數", default=0,compute='_get_frame1')
    tot_plastic_frame2 = fields.Integer(string="隨貨出蝴蝶籠數", default=0,compute='_get_frame2')
    tot_pallet = fields.Integer(string="隨貨出棧板數", default=0,compute='_get_pallet')
    prodout_memo = fields.Char(string="MEMO")

    @api.depends('prodout_line.out_plastic_frame1')
    def _get_frame1(self):
        for rec in self:
            mytotframe1 = 0
            for rec1 in rec.prodout_line:
                mytotframe1 = mytotframe1 + rec1.out_plastic_frame1
            rec.tot_plastic_frame1 = mytotframe1

    @api.depends('prodout_line.out_plastic_frame2')
    def _get_frame2(self):
        for rec in self:
            mytotframe2 = 0
            for rec1 in rec.prodout_line:
                mytotframe2 = mytotframe2 + rec1.out_plastic_frame2
            rec.tot_plastic_frame2 = mytotframe2

    @api.depends('prodout_line.out_pallet')
    def _get_pallet(self):
        for rec in self:
            mytotpallet = 0
            for rec1 in rec.prodout_line:
                mytotpallet = mytotpallet + rec1.out_pallet
            rec.tot_pallet = mytotpallet

    @api.model
    def create(self, vals):
        res = super(acmeprodout, self).create(vals)
        self.env.cr.execute("""select genprodout(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        myoutowner = self.prodout_owner.id
        ## WH/毛胚倉位置
        myblanklocid = self.env['alldo_acme_iot.company_stockloc'].search([])[0].blank_loc.id
        mypickingrec = self.env['stock.picking']
        mysupplocid = res.partner_id.blank_stock_supplier.id  # 委外商倉庫
        # myrec = self.env['alldo_acme_iot.prodout_line'].search([('prodout_id','=',res.id)])
        for rec in res.prodout_line:
            self.env.cr.execute("""select getproduom(%d)""" % rec.product_no.id)
            myuomid = self.env.cr.fetchone()[0]
            if rec.out_good_num > 0:
                myres = mypickingrec.create(
                    {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': mysupplocid,
                     'move_type': 'direct',
                     'user_id': myoutowner,
                     'move_line_ids': [
                         (0, 0, {'product_id': rec.product_no.id, 'company_id': 1, 'location_id': myblanklocid,
                                 'location_dest_id': mysupplocid, 'product_uom_id': myuomid,
                                 'qty_done': rec.out_good_num})]})
                rec.picking_id = myres.id
                myres.action_confirm()
                myres.env.cr.commit()
                myres.action_done()
                myres.env.cr.commit()
        self.env.cr.execute("""select syncoldprodout(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    def write(self, vals):
        res = super(acmeprodout, self).write(vals)
        myoutowner = self.prodout_owner.id
        ## WH/毛胚倉位置
        myblanklocid = self.env['alldo_acme_iot.company_stockloc'].search([])[0].blank_loc.id
        mypickingrec = self.env['stock.picking'].search([])
        for rec in self:
            mysupplocid = rec.partner_id.blank_stock_supplier.id  # 委外商倉庫
            for rec1 in rec.prodout_line:
                # self.env.cr.execute("""select updateprodoutline(%d)""" % rec1.id)
                # self.env.cr.execute("""commit""")
                # myrec = self.env['alldo_acme_iot.prodout_line'].search([('id', '=', rec1.id)])
                myoutsublrec = self.env['alldo_acme_iot.outsuborder_prodout'].search([('id','=',rec1.outsuborderlineid)])
                myoutsublrec.update({'out_good_num':rec1.out_good_num})
                myoutsubrec = self.env['alldo_acme_iot.outsuborder'].search([('id','=',myoutsublrec.order_id.id)])
                if rec1.out_good_num != rec1.old_good_num:
                    mygoodnum = rec1.out_good_num - rec1.old_good_num
                    myoutsubrec.update({'blank_num': myoutsubrec.blank_num + mygoodnum})
                if rec1.out_plastic_frame1 != rec1.old_plastic_frame1:
                    mypframe1 = rec1.out_plastic_frame1 - rec1.old_plastic_frame1
                    myoutsubrec.update({'out_plastic_frame1': myoutsubrec.out_plastic_frame1 + mypframe1})
                if rec1.out_plastic_frame2 != rec1.old_plastic_frame2:
                    mypframe2 = rec1.out_plastic_frame2 - rec1.old_plastic_frame2
                    myoutsubrec.update({'out_plastic_frame2': myoutsubrec.out_plastic_frame2 + mypframe2})
                if rec1.out_pallet != rec1.old_pallet:
                    mypallet = rec1.out_pallet - rec1.old_pallet
                    myoutsubrec.update({'out_pallet': myoutsubrec.out_pallet + mypallet})
                self.env.cr.execute("""select getproduom(%d)""" % rec1.product_no.id)
                myuomid = self.env.cr.fetchone()[0]
                if rec1.out_good_num > rec1.old_good_num:
                    myres = mypickingrec.create(
                        {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': mysupplocid,
                         'move_type': 'direct',
                         'user_id': myoutowner,
                         'move_line_ids': [
                             (0, 0, {'product_id': rec1.product_no.id, 'company_id': 1, 'location_id': myblanklocid,
                                     'location_dest_id': mysupplocid, 'product_uom_id': myuomid,
                                     'qty_done': (rec1.out_good_num - rec1.old_good_num)})]})
                else:
                    myres = mypickingrec.create(
                        {'picking_type_id': 5, 'location_id': mysupplocid, 'location_dest_id': myblanklocid,
                         'move_type': 'direct',
                         'user_id': myoutowner,
                         'move_line_ids': [
                             (0, 0, {'product_id': rec1.product_no.id, 'company_id': 1, 'location_id': mysupplocid,
                                     'location_dest_id': myblanklocid, 'product_uom_id': myuomid,
                                     'qty_done': (rec1.old_good_num - rec1.out_good_num)})]})
                myres.action_confirm()
                self.env.cr.commit()
                myres.action_done()
                self.env.cr.commit()
            self.env.cr.execute("""select syncoldprodout(%d)""" % rec.id)
            self.env.cr.execute("""commit""")

        return res

    def unlink(self):
        myoutowner = self.prodout_owner.id
        ## WH/毛胚倉位置
        myblanklocid = self.env['alldo_acme_iot.company_stockloc'].search([])[0].blank_loc.id
        mypickingrec = self.env['stock.picking'].search([])
        for rec in self:
            mysupplocid = rec.partner_id.blank_stock_supplier.id  # 委外商倉庫
            for rec1 in rec.prodout_line:
                self.env.cr.execute("""select delprodoutline(%d)""" % rec1.id)
                self.env.cr.execute("""commit""")
                myrec = self.env['alldo_acme_iot.prodout_line'].search([('id', '=', rec1.id)])
                for rec2 in myrec:
                    self.env.cr.execute("""select getproduom(%d)""" % rec2.product_no.id)
                    myuomid = self.env.cr.fetchone()[0]
                    if rec2.out_good_num > 0:
                        myres = mypickingrec.create(
                            {'picking_type_id': 5, 'location_id': mysupplocid, 'location_dest_id': myblanklocid,
                             'move_type': 'direct',
                             'user_id': myoutowner,
                             'move_line_ids': [
                                 (0, 0, {'product_id': rec2.product_no.id, 'company_id': 1, 'location_id': mysupplocid,
                                         'location_dest_id': myblanklocid, 'product_uom_id': myuomid,
                                         'qty_done': rec2.old_good_num})]})
                        myres.action_confirm()
                        self.env.cr.commit()
                        myres.action_done()
                        self.env.cr.commit()
        res = super(acmeprodout, self).unlink()
        return res


class acmeprodoutline(models.Model):
    _name ="alldo_acme_iot.prodout_line"

    prodout_id = fields.Many2one('alldo_acme_iot.prodout',ondelete='cascade')
    product_no = fields.Many2one('product.product', string="產品",required=True)
    eng_type = fields.Char(string="途程編號")
    out_good_num = fields.Float(digits=(10, 0), string="供料數量", default=0.00)
    old_good_num = fields.Float(digits=(10, 0), string="old供料數量", default=0.00)
    out_plastic_frame1 = fields.Integer(string="塑膠框數", default=0)
    old_plastic_frame1 = fields.Integer(string="old塑膠框數", default=0)
    out_plastic_frame2 = fields.Integer(string="蝴蝶籠數", default=0)
    old_plastic_frame2 = fields.Integer(string="old蝴蝶籠數", default=0)
    out_pallet = fields.Integer(string="棧板數", default=0)
    old_pallet = fields.Integer(string="old棧板數", default=0)
    prodout_no = fields.Many2one('alldo_acme_iot.outsuborder',string="委外單號",required=True)
    outsuborderlineid = fields.Integer(string="委外明細ID")
    outpartnerlineid = fields.Integer(string="廠商給料明細ID")
    prodout_desc = fields.Char(string="備註")
    picking_id = fields.Many2one('stock.picking',string="調撥單號")

    @api.onchange('prodout_no')
    def onprodoutnochange(self):
        myrec = self.env['alldo_acme_iot.outsuborder'].search([('id','=',self.prodout_no.id)])
        self.eng_type=myrec.eng_type

    @api.onchange('product_no')
    def onchangeproductno(self):
        mypartnerid = self.prodout_id.partner_id.id
        myproductid = self.product_no.id
        return {'domain': {'prodout_no': [('cus_name', '=', mypartnerid),('product_no','=',myproductid)]}}

    def unlink(self):
        myoutowner = self.prodout_id.prodout_owner.id
        ## WH/毛胚倉位置
        myblanklocid = self.env['alldo_acme_iot.company_stockloc'].search([])[0].blank_loc.id
        mypickingrec = self.env['stock.picking'].search([])
        mysupplocid = self.prodout_id.partner_id.blank_stock_supplier.id  # 委外商倉庫
        for rec in self:
            self.env.cr.execute("""select delprodoutline(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            myrec = self.env['alldo_acme_iot.prodout_line'].search([('id', '=', rec.id)])
            for rec in myrec:
                self.env.cr.execute("""select getproduom(%d)""" % rec.product_no.id)
                myuomid = self.env.cr.fetchone()[0]
                if rec.out_good_num > 0:
                    myres = mypickingrec.create(
                        {'picking_type_id': 5, 'location_id': mysupplocid, 'location_dest_id': myblanklocid,
                         'move_type': 'direct',
                         'user_id': myoutowner,
                         'move_line_ids': [
                             (0, 0, {'product_id': rec.product_no.id, 'company_id': 1, 'location_id': mysupplocid,
                                     'location_dest_id': myblanklocid, 'product_uom_id': myuomid,
                                     'qty_done': rec.old_good_num})]})
                    myres.action_confirm()
                    self.env.cr.commit()
                    myres.action_done()
                    self.env.cr.commit()
        res = super(acmeprodoutline, self).unlink()
        return res

