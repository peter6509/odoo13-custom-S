# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class alldoghpowkorder(models.Model):
    _name = "alldo_gh_iot.po_wkorder"
    _description = "訂單-工單記錄"
    _order = "shipping_date"


    po_no = fields.Char(string="客戶訂單編號")
    so_no = fields.Many2one('sale.order',string="客戶訂單")
    cus_name = fields.Many2one('res.partner', string="客戶")
    product_no = fields.Many2one('product.product', string="產品", required=True)
    po_line = fields.One2many('alldo_gh_iot.po_wkorder_line','po_id',copy=False)
    sub_line = fields.One2many('alldo_gh_iot.po_suborder_line','po_id',copy=False)
    picking_line = fields.One2many('alldo_gh_iot.picking_line','po_id',copy=False)
    stock_line = fields.One2many('alldo_gh_iot.stock_line', 'po_id', copy=False)
    order_date = fields.Date(string="下單日期")
    po_location = fields.Char(string="庫版")
    po_memo = fields.Text(string="內部備註")
    order_memo = fields.Text(string="訂單備註")
    po_lock = fields.Boolean(string="倉庫產品數量鎖定?",default=True)
    shipping_date = fields.Date(string="出貨日期")
    po_num = fields.Float(digits=(10,0),string="訂單數")
    blank_num = fields.Float(digits=(10,0),string="累計毛胚數量")
    stock_num = fields.Float(digits=(10,0),string="累計完工入庫數量",compute='_get_stock_num')
    shipping_num = fields.Float(digits=(10,0),string="出貨數",compute='_get_shipping_num')
    is_closed = fields.Boolean(string="完成",default=False)
    is_open = fields.Boolean(string="已開工單",default=False)
    state = fields.Selection([('1', '草稿'), ('2', '已開工'), ('3', '已完工'), ('4', '取消')], string='狀態', default='1')
    booking_line = fields.One2many('alldo_gh_iot.prod_booking','po_id',string="產品鎖定記錄",copy=False)
    release_line = fields.One2many('alldo_gh_iot.prod_booking_release','po_id', string="產品解除記錄", copy=False)
    active = fields.Boolean(string="ARCHIVE", default=True)
    custom_system = fields.Boolean(string="平台", default=False)
    response_shipping_date = fields.Date(string="回覆交期1")
    change_shipping_date = fields.Char(string="改交期")
    response_shipping_date1 = fields.Char(string="狀態")
    booking_num = fields.Float(digits=(10,0),string="訂單已鎖定數量",compute='_get_bookingnum')
    release_num = fields.Float(digits=(10,0),string="訂單已解除數量",compute='_get_releasenum')
    open_wkorder = fields.Boolean(string="工",default=False)
    open_wkorder1 = fields.Boolean(string="代",default=False)
    after_wkorder = fields.Boolean(string="後",default=False)
    after_wkorder1 = fields.Boolean(string="完",default=False)
    wk_id = fields.Many2one('alldo_gh_iot.workorder',string="工單號碼")
    booking_blank = fields.Boolean(string="訂",default=False)
    booking_blank1 = fields.Boolean(string="訂1", default=False)
    booking_blank_num = fields.Float(digits=(10,0),string="已訂料數量")
    po_id = fields.Many2one('purchase.order',string="採購單號")
    stockin_blank = fields.Boolean(string="進",default=False)
    stockin_blank1 = fields.Boolean(string="進1", default=False)
    stockin_blank_num = fields.Float(digits=(10,0),string="已進料數量")

    @api.model
    def create(self, vals):
        if 'po_no' in vals and vals['po_no'] and vals['po_no'] != ' ':
            mycount = self.env['alldo_gh_iot.po_wkorder'].search_count([('po_no','=',vals['po_no'])])
            if mycount > 0:
                raise UserError("訂單號碼:%s 已重複" % vals['po_no'])
        res = super(alldoghpowkorder, self).create(vals)
        return res

    def write(self, vals):
        if 'po_no' in vals and vals['po_no'] and vals['po_no'] != ' ':
            mycount = self.env['alldo_gh_iot.po_wkorder'].search_count([('po_no', '=', vals['po_no'])])
            if mycount > 0:
                raise UserError("""訂單號已重複,請確認！""")
        res = super(alldoghpowkorder, self).write(vals)
        return res

    def copy(self, default=None):
        default = dict(default or {})
        default.update({'po_no': ''})
        res = super(alldoghpowkorder, self).copy(default)
        return res



    @api.depends('booking_line')
    def _get_bookingnum(self):
        amounttot = 0
        for rec in self.booking_line:
            amounttot = amounttot + rec.booking_num
        self.booking_num = amounttot

    @api.depends('release_line')
    def _get_releasenum(self):
        amounttot = 0
        for rec in self.release_line:
            amounttot = amounttot + rec.release_num
        self.release_num = amounttot


    def unlink(self):
        mycount = 0
        for rec in self.po_line:
            if rec.wkorder_id.id > 0:
               mycount = mycount + 1
        if mycount > 0 :
            raise UserError("訂單已開工了,訂單已不能刪除了;請先手動刪除工單！")


        myid = self.id
        myrec = self.env['alldo_gh_iot.prod_booking'].search([('po_id','=',myid)])
        if myrec:
            myrec.run_booking_release()
        res = super(alldoghpowkorder, self).unlink()
        return res


    @api.depends('picking_line')
    def _get_shipping_num(self):
        for rec in self:
            tot_amount = 0
            for rec1 in rec.picking_line:
                tot_amount = tot_amount + rec1.picking_num
            rec.shipping_num = tot_amount

    @api.depends('stock_line')
    def _get_stock_num(self):
        for rec in self:
            tot_amount = 0
            for rec1 in rec.stock_line:
                tot_amount = tot_amount + rec1.picking_num
            rec.stock_num = tot_amount


    def run_archive(self):
        self.active=False


    def booking_unlock(self):
        myid = self.env.context.get('powkorder_id')
        for rec in self.booking_line:
            myrec = self.env['alldo_gh_iot.prod_booking'].search([('id','=',rec.id)])
            myrec.run_booking_release()
            myrec.write({'booking_release':fields.Date.today(),'booking_type':'2'})
        self.po_lock=False



    @api.onchange('product_no')
    def onchangeproductno(self):
        self.po_memo = self.product_no.product_tmpl_id.description

    def name_get(self):
        result = []
        for myrec in self:
            myname = "(%s)%s-%s" % (myrec.po_no,myrec.product_no.default_code,myrec.po_num)
            result.append((myrec.id, myname))
        return result

    def complete_powkorder(self):
        myworkorderid = self.env.context.get('powkorder_id')
        self.env.cr.execute("""select setpowkordercomplete(%d)""" % myworkorderid)
        self.env.cr.execute("""commit""")


class alldoghpowkorderline(models.Model):
    _name = "alldo_gh_iot.po_wkorder_line"
    _description = "訂單-工單明細記錄"

    po_id = fields.Many2one('alldo_gh_iot.po_wkorder',ondelete='cascade')
    wkorder_id = fields.Many2one('alldo_gh_iot.workorder',string="工單")
    eng_type = fields.Char(string="工程別")
    eng_seq = fields.Integer(string="工序seq")
    eng_order = fields.Selection([('1','首工序'),('2','中工序'),('3','完工序'),('4','成品後工序')],string="工序位置")
    complete_num = fields.Float(digits=(10,2),string="完成良品數量")
    ng_num = fields.Float(digits=(10,2),string="NG數量")


class alldoghposuborderline(models.Model):
    _name = "alldo_gh_iot.po_suborder_line"
    _description = "訂單-委外加工明細記錄"

    po_id = fields.Many2one('alldo_gh_iot.po_wkorder',ondelete='cascade')
    outsourcing_id = fields.Many2one('alldo_gh_iot.outsuborder',string="委外加工單")
    eng_type = fields.Char(string="工程別")
    eng_seq = fields.Integer(string="工序seq")
    eng_order = fields.Selection([('1','首工序'),('2','中工序'),('3','完工序')],string="工序位置")
    complete_num = fields.Float(digits=(10,2),string="完成數量")
    ng_num = fields.Float(digits=(10,2),string="NG數量")


class alldopickingline(models.Model):
    _name = "alldo_gh_iot.picking_line"
    _description = "訂單-調撥明細記錄"

    po_id = fields.Many2one('alldo_gh_iot.po_wkorder',ondelete='cascade')
    picking_id = fields.Many2one('stock.picking',string="調撥單")
    picking_num = fields.Float(digits=(10,0),string="數量")
    picking_type_id = fields.Many2one('stock.picking.type',string="型態")
    picking_date = fields.Date(string="調撥日期")
    origin = fields.Char(string="來源")


class alldostockline(models.Model):
    _name = "alldo_gh_iot.stock_line"
    _description = "訂單-完工入庫明細記錄"

    po_id = fields.Many2one('alldo_gh_iot.po_wkorder',ondelete='cascade')
    picking_id = fields.Many2one('stock.picking',string="入庫單")
    location_id = fields.Many2one('stock.location',string="來源位置")
    dest_location_id = fields.Many2one('stock.location',string="目的位置")
    picking_num = fields.Float(digits=(10,0),string="數量")
    picking_type_id = fields.Many2one('stock.picking.type',string="型態")
    picking_date = fields.Date(string="入庫日期")