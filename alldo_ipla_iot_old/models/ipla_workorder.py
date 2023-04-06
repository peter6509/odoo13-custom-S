# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning


class alldoiplaiotworkorder(models.Model):
    _name = "alldo_ipla_iot.workorder"
    _description = "工單主檔"
    _order = "name desc"

    mrp_prod_id = fields.Many2one('mrp.production',string="製造命令",required=True,ondeleted='cascade')
    name = fields.Char(string="工單號碼", default=lambda self: _('New'), copy=False, required=True, readonly=True)
    product_no = fields.Many2one('product.product', string="產品料號", required=True)
    eng_type = fields.Char(string="途程編號")
    eng_order = fields.Selection([('1', '首工序'), ('2', '中工序'), ('3', '完工序'),('4','單工序')], string="工序位置")
    eng_seq = fields.Integer(string="eng seq")
    po_no = fields.Char(string="生產製造單")
    so_no = fields.Many2one('sale.order', string="客戶訂單")
    so_pi = fields.Char(string="PI單號")
    cus_name = fields.Many2one('res.partner', string="客戶")
    order_num = fields.Integer(string="訂單數量", required=True, default=0)
    blank_num = fields.Integer(string="累計毛胚進料數", required=True, default=0)
    prod_date = fields.Datetime(string="開工生產時間")
    prodin_num = fields.Integer(string="成品累計入庫量")
    shipping_date = fields.Date(string="出貨日期",default=0)
    shipping_num = fields.Integer(string="成品累計出貨量")
    blank_input_date = fields.Date(string="進貨日")
    qc_line = fields.One2many('alldo_ipla_iot.workorder_qc', 'order_id', string="QC明細", copy=False)
    iot_line = fields.One2many('alldo_ipla_iot.workorder_iot_data', 'order_id', string="IOT BOX資料明細", copy=False)
    status_line = fields.One2many('alldo_ipla_iot.node_change_status', 'order_id', string="NODE 變更狀態記錄", copy=False)
    prodin_line = fields.One2many('alldo_ipla_iot.wkorder_prodin', 'order_id', string="工單來料記錄", copy=False)
    prodout_line = fields.One2many('alldo_ipla_iot.wkorder_prodout', 'order_id', string="加工後轉出記錄", copy=False)
    replace_line = fields.One2many('alldo_ipla_iot.wkorder_replaceline','order_id',string="架機換線記錄",copy=False)
    material_line = fields.One2many('alldo_ipla_iot.wkorder_materialline','order_id',string="工單投料表",copy=False)
    state = fields.Selection([('1', '草稿'), ('2', '印表'), ('3', '已開工'), ('4', '已完工'), ('5', '取消')], string='狀態',
                             default='1')
    active = fields.Boolean(string="ARCHIVE", default=True)
    prod_num = fields.Integer(string="實際生產總數")
    good_num = fields.Integer(string="完成良品數", compute='_get_qc_total_num')
    prod_duration = fields.Float(digits=(10, 1), string="總工時(分鐘)", default=0.0)
    start_duration = fields.Float(digits=(10, 1), string="今日開工總工時(分鐘)", default=0.0)
    stop_duration = fields.Float(digits=(10, 1), string="今日暫停總工時(分鐘)", default=0.0)
    workorder_memo = fields.Text(string="註記")
    workorder_name = fields.Char(string="工單說明", compute='_get_workordername', store=True)
    mo_group_id = fields.Integer(string="GROUP ID")
    have_mold = fields.Boolean(string="有模具?",default=False)
    mold_no = fields.Many2one('alldo_ipla_iot.ipla_mold',string="模具")
    # blankin_picking = fields.Many2one('stock.picking', string="進料調撥單")
    prodout_picking = fields.Many2one('stock.picking', string="開立出貨單")
    uncomplete_shipping = fields.Boolean(string='出貨未完成', compute='_get_uncomplete_ship', store=True)
    complete_shipping = fields.Boolean(string="已出貨完成", default=False)
    mo_production_num = fields.Integer(string="生產良品總數", default=0)

    # def run_complete(self):
    #     for rec in self:
    #         self.env.cr.execute("""update alldo_ipla_iot_workorder set state='4""")


    def run_archive(self):
        for rec in self:
            if rec.state=='4':
                if rec.active==True:
                    self.env.cr.execute("""update alldo_ipla_iot_workorder set active=False where mo_group_id=%d""" % rec.mo_group_id)
                else:
                    self.env.cr.execute("""update alldo_ipla_iot_workorder set active=True where mo_group_id=%d""" % rec.mo_group_id)
                self.env.cr.execute("""commit""")


    def name_get(self):
        res = []
        for rec in self:
            myname = "[%s-(PI:%s)]-%s-%s(%s)" % (
            rec.name, rec.so_pi, rec.cus_name.name, rec.product_no.default_code, rec.order_num)
            res += [(rec.id, myname)]
        return res

    def complete_workorder(self):
        myworkorderid = self.env.context.get('workorder_id')
        self.env.cr.execute("""select setworkordercomplete(%d)""" % myworkorderid)
        self.env.cr.execute("""commit""")

    @api.depends('name', 'product_no', 'cus_name', 'shipping_date', 'order_num', 'eng_type')
    def _get_workordername(self):
        for rec in self:
            myname = "[%s]-[%s-%s]-%s-%s-%s" % (
            rec.name, rec.product_no.name, rec.eng_type, rec.cus_name.name, rec.order_num, rec.shipping_date)
            rec.update({'workorder_name': myname})

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
            vals['name'] = self.env['ir.sequence'].next_by_code('alldo_ipla_iot.workorder') or _('New')
        res = super(alldoiplaiotworkorder, self).create(vals)
        self.env.cr.execute("""select createpowkorder(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    def _write(self, vals):

        res = super(alldoiplaiotworkorder, self)._write(vals)
        for rec in self:
            self.env.cr.execute("""select genpowkorderngnum(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res

    def unlink(self):
        for rec in self:
            self.env.cr.execute("""select candelwkorder(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            if not myres:
                raise UserError("工單已啟動,無法刪除了！")
        res = super(alldoiplaiotworkorder, self).unlink()
        return res


class alldoiplaiotworkorderiotdata(models.Model):
    _name = "alldo_ipla_iot.workorder_iot_data"
    _description = "工單IOT生產數據資料"
    _order = "order_id,iot_date desc"

    order_id = fields.Many2one('alldo_ipla_iot.workorder', ondelete='cascade')
    iot_date = fields.Datetime(string="IOT時間")
    iot_node = fields.Many2one('maintenance.equipment', string="機台")
    iot_owner = fields.Many2one('hr.employee', string="擔當者1")
    iot_owner1 = fields.Many2one('hr.employee',string="擔當者2")
    iot_num = fields.Float(digits=(13, 2), string="數量")
    iot_duration = fields.Float(digits=(5, 1), string="單件工時")
    std_duration = fields.Float(digits=(6, 0), string="標準工時(秒)")
    iot_serial = fields.Char(string="IOT 流水號")
    is_posting = fields.Boolean(string="過帳",default=False)
    is_select = fields.Boolean(string="計算勾選",default=False)


class alldoiplaiotworkorderqc(models.Model):
    _name = "alldo_ipla_iot.workorder_qc"
    _description = "工單產品加工質檢"
    _order = "order_id,iot_node,qc_date desc"

    order_id = fields.Many2one('alldo_ipla_iot.workorder', ondelete='cascade')
    qc_date = fields.Date(string="承製日期")
    iot_node = fields.Many2one('maintenance.equipment', string="機台")
    qc_good_num = fields.Float(digits=(13, 2), string="IOT完成數量", default=0)
    material_ng_num = fields.Float(digits=(13, 2), string="材料不良數量", default=0)
    processing_ng_num = fields.Float(digits=(13, 2), string="生產不良數量", default=0)
    total_amount_num = fields.Float(digits=(13, 2), string="GOOD數量", compute='_get_total_amount')
    complete_date = fields.Date(string="完成日期")
    iot_owner = fields.Many2one('hr.employee', string="責任者")
    line_memo = fields.Char(string="說明")
    report_date = fields.Date(string="製表日期")
    report_no = fields.Char(string="NG退料單號")
    product_no = fields.Many2one('product.product',string="PRODUCT",store=True,compute='_get_prod')
    cus_name = fields.Many2one('res.partner',string="CUSTOMER",store=True,compute='_get_cus')

    @api.depends('order_id')
    def _get_cus(self):
        for rec in self:
            rec.cus_name = rec.order_id.cus_name.id

    @api.depends('order_id')
    def _get_prod(self):
        for rec in self:
            rec.product_no=rec.order_id.product_no.id


    @api.depends('qc_good_num', 'material_ng_num', 'processing_ng_num')
    def _get_total_amount(self):
        for rec in self:
            rec.total_amount_num = rec.qc_good_num - rec.material_ng_num - rec.processing_ng_num


class alldoiplaiotnodechangestatus(models.Model):
    _name = "alldo_ipla_iot.node_change_status"
    _description = "IOT裝置狀態變化記錄檔"

    order_id = fields.Many2one('alldo_ipla_iot.workorder', ondelete='cascade')
    node_status = fields.Selection([('1', '開工'), ('2', '暫停'), ('3', '停工')], string="變化模式")
    iot_node = fields.Many2one('maintenance.equipment', string="機台")
    node_datetime = fields.Datetime(string="發生時間")


class alldoiplaiotworkordermeasuretool(models.Model):
    _name = "alldo_ipla_iot.measure_tool"
    _description = "加工產品檢驗工具"
    _order = "sequence,id"

    sequence = fields.Integer(string="SEQ", default=10)
    inspect_code = fields.Char(string="代號", required=True)
    name = fields.Char(string="量測工具", required=True)


class alldoiplaiotlastwork(models.Model):
    _name = "alldo_ipla_iot.workorder_lastwork"
    _description = "工件最後生產時間記錄"

    work_datetime = fields.Datetime(string="最後件生產時間")
    equipment_id = fields.Many2one('maintenance.equipment', string="機台")
    workorder_id = fields.Many2one('alldo_ipla_iot.workorder', string="工單")
    iot_owner = fields.Many2one('hr.employee', string="擔當者1")
    iot_owner1 = fields.Many2one('hr.employee', string="擔當者2")


class alldoiplaiotwkorderprodin(models.Model):
    _name = "alldo_ipla_iot.wkorder_prodin"
    _description = "工單來料記錄明細"

    order_id = fields.Many2one('alldo_ipla_iot.workorder', ondelete='cascade')
    prodin_datetime = fields.Datetime(string="時間")
    product_no = fields.Many2one('product.product', string="產品")
    in_type = fields.Selection([('1', '庫存'), ('2', '前工序')], string="來料類別")
    in_good_num = fields.Float(digits=(10, 2), string="良品數量", default=0.00)
    in_ng_num = fields.Float(digits=(10, 2), string="NG數量", default=0.00)
    process_num = fields.Float(digits=(10, 2), string="目前已耗用量", default=0.00)
    in_loc = fields.Char(string="來源對象")
    in_id = fields.Integer(string="來源ID")
    in_owner = fields.Many2one('res.users', string="建檔人員")


class alldoiplaiotwkorderprodout(models.Model):
    _name = "alldo_ipla_iot.wkorder_prodout"
    _description = "工單加工完轉出記錄明細"
    _order = "prodout_datetime desc"

    order_id = fields.Many2one('alldo_ipla_iot.workorder', ondelete='cascade')
    prodout_datetime = fields.Datetime(string="時間")
    product_no = fields.Many2one('product.product', string="產品")
    is_cutting = fields.Boolean(string="切割")
    out_type = fields.Selection([('1', '客戶'), ('2', '後工序')], string="轉出類別")
    out_good_num = fields.Float(digits=(10, 2), string="切割良品數量", default=0.00)
    out_ng_num = fields.Float(digits=(10, 2), string="切割NG數量", default=0.00)
    out_memo = fields.Char(string="NOTE")
    out_stock_num = fields.Float(digits=(10, 2), string="已入庫數", default=0.00)
    out_loc = fields.Char(string="轉出對象")
    out_owner = fields.Many2one('res.users', string="建檔人員")


class alldoiplaiotwkorderreplaceline(models.Model):
    _name = "alldo_ipla_iot.wkorder_replaceline"
    _description = "架機換線記錄明細"
    _order = "replace_start_datetime desc"

    order_id = fields.Many2one('alldo_ipla_iot.workorder', ondelete='cascade')
    replace_owner = fields.Many2one('hr.employee', string="工程師")
    equipment_id = fields.Many2one('maintenance.equipment', string="機台")
    replace_type = fields.Selection([('P','備模'),('L','架模'),('B','烘模')],string="類別")
    replace_start_datetime = fields.Datetime(string="啟始時間")
    replace_end_datetime = fields.Datetime(string="截止時間")
    replace_duration = fields.Float(digits=(6,1),string="時間(分)")


class alldoiplamaterialline(models.Model):
    _name = "alldo_ipla_iot.wkorder_materialline"
    _description = "工單耗料清單"

    order_id = fields.Many2one('alldo_ipla_iot.workorder',ondelete='cascade')
    product_id = fields.Many2one('product.product',string="料號")
    product_uom = fields.Many2one('product.uom',string="單位")
    qty_done = fields.Float(string="耗料數量")
    on_hand_qty = fields.Float(string="在手數量")
    prodin_datetime = fields.Datetime(string="投料時間")
    prodin_complete = fields.Boolean(string="已完成扣料?",default=False)

class alldoiplaiotwkordermogroupid(models.Model):
    _name = "alldo_ipla_iot.mo_group_seq"

    seqnum = fields.Integer(string="GROUP流水號",default=0)


