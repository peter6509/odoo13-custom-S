# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class alldoacmepowkorder(models.Model):
    _name = "alldo_acme_iot.po_wkorder"
    _description = "訂單-工單記錄"


    po_no = fields.Char(string="客戶訂單")
    so_no = fields.Many2one('sale.order',string="客戶訂單")
    cus_name = fields.Many2one('res.partner', string="客戶")
    product_no = fields.Many2one('product.product', string="產品", required=True)
    po_line = fields.One2many('alldo_acme_iot.po_wkorder_line','po_id',copy=False)
    sub_line = fields.One2many('alldo_acme_iot.po_suborder_line','po_id',copy=False)
    shipping_date = fields.Date(string="出貨日期")
    po_num = fields.Float(digits=(10,2),string="訂單數量")
    blank_num = fields.Float(digits=(10,2),string="累計毛胚數量")
    stock_num = fields.Float(digits=(10,2),string="累計入庫數量")
    shipping_num = fields.Float(digits=(10,2),string="累計出貨數量")
    is_closed = fields.Boolean(string="完成",default=False)
    state = fields.Selection([('1', '草稿'), ('2', '已開工'), ('3', '已完工'), ('4', '取消')], string='狀態', default='1')


    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s-%s" % (myrec.so_no.name,myrec.cus_name.name,myrec.product_no.name)
            result.append((myrec.id, myname))
        return result

    def complete_powkorder(self):
        myworkorderid = self.env.context.get('powkorder_id')
        self.env.cr.execute("""select setpowkordercomplete(%d)""" % myworkorderid)
        self.env.cr.execute("""commit""")



class alldoacmepowkorderline(models.Model):
    _name = "alldo_acme_iot.po_wkorder_line"
    _description = "訂單-工單明細記錄"

    po_id = fields.Many2one('alldo_acme_iot.po_wkorder',ondelete='cascade')
    wkorder_id = fields.Many2one('alldo_acme_iot.workorder',string="工單")
    eng_type = fields.Char(string="工程別")
    eng_seq = fields.Integer(string="工序seq")
    eng_order = fields.Selection([('1','首工序'),('2','中工序'),('3','完工序')],string="工序位置")
    complete_num = fields.Float(digits=(10,2),string="完成數量")
    ng_num = fields.Float(digits=(10,2),string="NG數量")


class alldoacmeposuborderline(models.Model):
    _name = "alldo_acme_iot.po_suborder_line"
    _description = "訂單-委外加工明細記錄"

    po_id = fields.Many2one('alldo_acme_iot.po_wkorder',ondelete='cascade')
    outsourcing_id = fields.Many2one('alldo_acme_iot.outsuborder',string="委外加工單")
    eng_type = fields.Char(string="工程別")
    eng_seq = fields.Integer(string="工序seq")
    eng_order = fields.Selection([('1','首工序'),('2','中工序'),('3','完工序')],string="工序位置")
    complete_num = fields.Float(digits=(10,2),string="完成數量")
    ng_num = fields.Float(digits=(10,2),string="NG數量")