# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api, _
from odoo.exceptions import UserError


class alldoghiotoutsuborder(models.Model):
    _name = "alldo_gh_iot.outsuborder"
    _description = "委外加工單"
    _order = "name"

    name = fields.Char(string="委外單號", default=lambda self: _('New'),copy=False,required=True,readonly=True)
    product_no = fields.Many2one('product.product',string="料號",required=True)
    eng_type = fields.Char(string="工程別")
    eng_order = fields.Selection([('1','首工序'),('2','中工序'),('3','完工序')],string="工序位置")
    eng_seq = fields.Integer(string="eng seq")
    po_no = fields.Char(string="客戶訂單")
    so_no = fields.Many2one('sale.order',string="客戶訂單")
    cus_name = fields.Many2one('res.partner',string="委外加工商")
    order_num = fields.Integer(string="累計加工數量")
    blank_num = fields.Integer(string="累計毛胚數")
    prod_date = fields.Datetime(string="開工生產時間")
    shipping_date = fields.Date(string="出貨日期")
    blank_input_date = fields.Date(string="進貨日")
    qc_line = fields.One2many('alldo_gh_iot.outsuborder_qc','order_id',string="QC明細",copy=False)
    prodout_line = fields.One2many('alldo_gh_iot.outsuborder_prodout','order_id',string="委外給料記錄",copy=False)
    prodin_line = fields.One2many('alldo_gh_iot.outsuborder_prodin','order_id',string="委外入庫記錄",copy=False)
    state = fields.Selection([('1','草稿'),('2','已開工'),('3','已完工'),('4','取消')],string='狀態',default='1')
    prod_num = fields.Integer(string="實際生產總數")
    outsuborder_memo = fields.Text(string="註記")
    outsuborder_name = fields.Char(string="工單說明",compute='_get_outsubordername',store=True)
    mo_group_id = fields.Integer(string="GROUP ID")

    def name_get(self):
        res = []
        for rec in self:
            myname = "[%s(%s)]-%s" % (rec.name,rec.product_no.name,rec.cus_name.name)
            res += [(rec.id, myname)]
        return res

    # @api.model
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         vals['name'] = self.env['ir.sequence'].next_by_code('alldo_gh_iot.outsuborder') or _('New')
    #     res = super(alldoghiotoutsuborder, self).create(vals)
    #     self.env.cr.execute("""select createpooutsuborder(%d)""" % res.id)
    #     self.env.cr.execute("""commit""")
    #     return res

    def complete_outsuborder(self):
        myworkorderid = self.env.context.get('outsuborder_id')
        self.env.cr.execute("""select setoutsubordercomplete(%d)""" % myworkorderid)
        self.env.cr.execute("""commit""")

    @api.depends('name', 'product_no', 'cus_name', 'shipping_date', 'order_num', 'eng_type')
    def _get_outsubordername(self):
        for rec in self:
            myname = "[%s]-[%s-%s]-%s-%s-%s" % (
            rec.name, rec.product_no.name, rec.eng_type, rec.cus_name.name, rec.order_num, rec.shipping_date)
            rec.update({'outsuborder_name': myname})

    @api.depends('qc_line')
    def _get_qc_total_num(self):
        for rec in self:
            myamount = 0.0
            for rec1 in rec.qc_line:
                myamount = myamount + rec1.total_amount_num
            rec.good_num = myamount

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('alldo_gh_iot.outsuborder') or _('New')
        res = super(alldoghiotoutsuborder, self).create(vals)
        self.env.cr.execute("""select createpooutsuborder(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    def _write(self, vals):
        res = super(alldoghiotoutsuborder, self)._write(vals)
        for rec in self:
            self.env.cr.execute("""select genpooutsuborderngnum(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res


class alldoghiotoutsuborderqc(models.Model):
    _name = "alldo_gh_iot.outsuborder_qc"
    _description = "委外加工加工質檢"
    _order = "order_id,qc_date"

    order_id = fields.Many2one('alldo_gh_iot.outsuborder', ondelete='cascade')
    qc_date = fields.Date(string="承製日期")
    iot_node = fields.Many2one('maintenance.equipment', string="機台")
    qc_good_num = fields.Float(digits=(13, 2), string="完成數量", default=0)
    material_ng_num = fields.Float(digits=(13, 2), string="材料不良數量", default=0)
    processing_ng_num = fields.Float(digits=(13, 2), string="加工不良數量", default=0)
    total_amount_num = fields.Float(digits=(13, 2), string="合計承交數", compute='_get_total_amount')
    complete_date = fields.Date(string="完成日期")
    iot_owner = fields.Many2one('hr.employee', string="品檢員")

    @api.depends('qc_good_num', 'material_ng_num', 'processing_ng_num')
    def _get_total_amount(self):
        for rec in self:
            rec.total_amount_num = rec.qc_good_num - rec.material_ng_num - rec.processing_ng_num

class alldoghiotoutsuborderprodin(models.Model):
    _name = "alldo_gh_iot.outsuborder_prodin"
    _description = "委外入庫記錄明細"

    order_id = fields.Many2one('alldo_gh_iot.outsuborder', ondelete='cascade')
    prodin_datetime = fields.Datetime(string="時間")
    product_no = fields.Many2one('product.product', string="產品")
    in_good_num = fields.Float(digits=(10, 2), string="良品數量", default=0.00)
    in_ng_num = fields.Float(digits=(10, 2), string="NG數量", default=0.00)
    loss_num = fields.Float(digits=(10, 2), string="毛胚短少數量", default=0.00)
    process_num = fields.Float(digits=(10, 2), string="目前已加工數", default=0.00)
    in_stock_num = fields.Float(digits=(10,2),string="已入庫數量", default=0.00)
    in_id = fields.Integer(string="來源ID")
    in_owner = fields.Many2one('res.users', string="建檔人員")

class alldoghiotoutsuborderprodout(models.Model):
    _name = "alldo_gh_iot.outsuborder_prodout"
    _description = "委外加工給料記錄明細"

    order_id = fields.Many2one('alldo_gh_iot.outsuborder', ondelete='cascade')
    prodout_datetime = fields.Datetime(string="時間")
    product_no = fields.Many2one('product.product', string="產品")
    out_good_num = fields.Float(digits=(10, 2), string="給料數量", default=0.00)
    out_ng_num = fields.Float(digits=(10, 2), string="給料NG數量", default=0.00)
    out_loc = fields.Char(string="轉出來源")
    out_owner = fields.Many2one('res.users', string="建檔人員")






