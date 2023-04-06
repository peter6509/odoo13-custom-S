# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api, _
from odoo.exceptions import UserError


class alldoacmeiotoutsuborder(models.Model):
    _name = "alldo_acme_iot.outsuborder"
    _description = "委外加工單"
    _order = "name desc"

    mrp_prod_id = fields.Many2one('mrp.production', string="製造命令", ondeleted='cascade')
    name = fields.Char(string="委外單號", default=lambda self: _('New'),copy=False,required=True,readonly=True)
    product_no = fields.Many2one('product.product',string="產品料號",required=True)
    eng_type = fields.Char(string="途程編號")
    eng_order = fields.Selection([('1','首工序'),('2','中工序'),('3','完工序')],string="工序位置")
    eng_seq = fields.Integer(string="eng seq")
    po_no = fields.Char(string="生產製造單")
    so_pi = fields.Char(string="PI單號")
    purchase_no = fields.Many2one('purchase.order',string="委外採購單")
    so_no = fields.Many2one('sale.order',string="客戶訂單")
    cus_name = fields.Many2one('res.partner',string="委外加工商")
    order_num = fields.Integer(string="訂單數量")
    blank_num = fields.Integer(string="累計毛胚供料")
    last_blank_num = fields.Integer(string="本次數量")
    prod_date = fields.Datetime(string="委外生產時間")
    shipping_date = fields.Date(string="委外交貨日期")
    blank_input_date = fields.Date(string="進貨日")
    qc_line = fields.One2many('alldo_acme_iot.outsuborder_qc','order_id',string="QC明細",copy=False)
    prodout_line = fields.One2many('alldo_acme_iot.outsuborder_prodout','order_id',string="委外給料記錄",copy=False)
    prodin_line = fields.One2many('alldo_acme_iot.outsuborder_prodin','order_id',string="委外入庫記錄",copy=False)
    ngratio_line = fields.One2many('alldo_acme_iot.outsuborder_ngratio', 'order_id', string="委外不良率", copy=False)
    state = fields.Selection([('1','草稿'),('2','已開工'),('3','已完工'),('4','取消')],string='狀態',default='1')
    prod_num = fields.Integer(string="實際生產總數")
    outsuborder_memo = fields.Text(string="註記")
    outsuborder_name = fields.Char(string="工單說明",compute='_get_outsubordername',store=True)
    mo_group_id = fields.Integer(string="GROUP ID")
    blank_good_num = fields.Float(string="總計GOOD數量",compute='_get_blank_good')

    blank_ng_num = fields.Float(string="總計NG數量",compute='_get_blank_ng')
    active = fields.Boolean(string="ARCHIVE", default=True)
    out_plastic_frame1 = fields.Integer(string="隨貨出塑膠框數",default=0)
    out_plastic_frame2 = fields.Integer(string="隨貨出蝴蝶籠數",default=0)
    out_pallet = fields.Integer(string="隨貨出棧板數",default=0)
    in_plastic_frame1 = fields.Integer(string="轉回塑膠框數", default=0)
    in_plastic_frame2 = fields.Integer(string="轉回蝴蝶籠數", default=0)
    in_pallet = fields.Integer(string="轉回棧板數", default=0)

    def run_archive(self):
        for rec in self:
            if rec.state=='3':
                if rec.active==True:
                    self.env.cr.execute("""update alldo_acme_iot_outsuborder set active=False where mo_group_id=%d""" % rec.mo_group_id)
                else:
                    self.env.cr.execute("""update alldo_acme_iot_outsuborder set active=True where mo_group_id=%d""" % rec.mo_group_id)
                self.env.cr.execute("""commit""")

    @api.depends('prodin_line')
    def _get_blank_good(self):
        for line in self:
            goodnum = 0
            for rec in line.prodin_line:
                goodnum = goodnum + rec.in_good_num
            line.blank_good_num = goodnum

    @api.depends('prodin_line')
    def _get_blank_ng(self):
        for line in self:
            ngnum = 0
            for rec in line.prodin_line:
                ngnum = ngnum + rec.in_ng_num
            line.blank_ng_num = ngnum


    def name_get(self):
            res = []
            for rec in self:
                myname = "[%s(%s)]-%s-(PI:%s)" % (rec.name,rec.product_no.default_code,rec.cus_name.name,rec.so_pi)
                res += [(rec.id, myname)]
            return res

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('alldo_acme_iot.outsuborder') or _('New')
        res = super(alldoacmeiotoutsuborder, self).create(vals)
        self.env.cr.execute("""select createpooutsuborder(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

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

    @api.onchange('write_date')
    def onclientchange(self):
        self.env.cr.execute("""select getpurno(%d)""" % self.product_no.id)
        myrec = self.env.cr.fetchall()
        ids=[]
        for rec in myrec:
            ids.append(rec[0])
        return {'domain': {'purchase_no': [('id', 'in', ids)]}}

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
            vals['name'] = self.env['ir.sequence'].next_by_code('alldo_acme_iot.outsuborder') or _('New')
        res = super(alldoacmeiotoutsuborder, self).create(vals)
        self.env.cr.execute("""select createpooutsuborder(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    def _write(self, vals):
        res = super(alldoacmeiotoutsuborder, self)._write(vals)
        for rec in self:
            self.env.cr.execute("""select genpooutsuborderngnum(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select gensubngratio(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res


class alldoacmeiotoutsuborderqc(models.Model):
    _name = "alldo_acme_iot.outsuborder_qc"
    _description = "委外加工加工質檢"
    _order = "order_id,qc_date"

    order_id = fields.Many2one('alldo_acme_iot.outsuborder', ondelete='cascade')
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

class alldoacmeiotoutsuborderprodin(models.Model):
    _name = "alldo_acme_iot.outsuborder_prodin"
    _description = "委外毛胚轉入記錄明細"
    _order = "prodin_datetime desc"

    order_id = fields.Many2one('alldo_acme_iot.outsuborder', ondelete='cascade')
    prodin_datetime = fields.Datetime(string="登錄時間")
    product_no = fields.Many2one('product.product', string="產品")
    in_good_num = fields.Float(digits=(10, 2), string="轉出良品數量", default=0.00)
    in_ng_num = fields.Float(digits=(10, 2), string="轉出NG數量", default=0.00)
    # process_num = fields.Float(digits=(10, 2), string="目前已加工數", default=0.00)
    # in_stock_num = fields.Float(digits=(10,2),string="已入庫數量", default=0.00)
    in_id = fields.Integer(string="來源ID")
    in_loc = fields.Char(string="轉移目的")
    in_owner = fields.Many2one('res.users', string="建檔人員")
    image = fields.Binary('文件夾檔')
    image_filename = fields.Char("Image Filename")

class alldoacmeiotoutsuborderprodout(models.Model):
    _name = "alldo_acme_iot.outsuborder_prodout"
    _description = "委外毛胚轉出記錄明細"
    _order = "prodout_datetime desc"

    order_id = fields.Many2one('alldo_acme_iot.outsuborder', ondelete='cascade')
    prodout_datetime = fields.Datetime(string="登錄時間")
    product_no = fields.Many2one('product.product', string="產品")
    out_good_num = fields.Float(digits=(10, 2), string="轉入良品數量", default=0.00)
    out_ng_num = fields.Float(digits=(10, 2), string="轉入NG數量", default=0.00)
    out_loc = fields.Char(string="轉入來源")
    out_owner = fields.Many2one('res.users', string="建檔人員")
    report_date = fields.Date(string="印表日期")
    last_record = fields.Boolean(string="Last",default=False)
    out_desc = fields.Char(string="備註說明")


class alldoacmeiotoutsuborderngratio(models.Model):
    _name = "alldo_acme_iot.outsuborder_ngratio"

    order_id = fields.Many2one('alldo_acme_iot.outsuborder',ondelete='cascade')
    sub_good_num = fields.Float(digits=(10,0),string="委外良品數")
    sub_ng_num = fields.Float(digits=(10,0),string="委外不良數")
    sub_ratio = fields.Float(digits=(5,1),string="委外不良率")







