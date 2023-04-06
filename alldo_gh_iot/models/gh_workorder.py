# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import api, fields, models, _
from odoo.exceptions import UserError


class alldoghiotworkorder(models.Model):
    _name = "alldo_gh_iot.workorder"
    _description = "工單主檔"
    _order = "mo_group_id desc ,id"

    # @api.depends()
    # def _get_pono(self):
    #     for rec in self:
    #         self.env.cr.execute("""select getwkorderpono(%d)""" % rec.id)
    #         rec.po_no = self.env.cr.fetchone()[0]

    @api.depends('order_num','shipping_num')
    def _get_canachive(self):
        for rec in self:
            if rec.order_num <= rec.shipping_num:
                rec.can_achive = True
            else:
                rec.can_achive = False

    name = fields.Char(string="工單號碼", default=lambda self: _('New'), copy=False, required=True, readonly=True)
    product_no = fields.Many2one('product.product', string="產品料號", required=True)
    blank_no = fields.Many2one('product.product',string="毛胚料號")
    eng_type = fields.Char(string="工程別")
    eng_order = fields.Selection([('1', '首工序'), ('2', '中工序'), ('3', '完工序'),('4','雜項工序')], string="工序位置")
    eng_seq = fields.Integer(string="eng seq")
    po_no = fields.Char(string="客戶訂單")
    po_no1 = fields.Many2one('alldo_gh_iot.po_wkorder', string="客戶訂單")
    so_no = fields.Many2one('sale.order', string="客戶訂單")
    cus_name = fields.Many2one('res.partner', string="客戶")
    order_num = fields.Integer(string="累計訂單數量", required=True, default=0)
    blank_num = fields.Integer(string="累計毛胚數量", required=True, default=0)
    prod_date = fields.Datetime(string="開工生產時間")
    prodin_num = fields.Integer(string="成品累計入庫量")
    shipping_date = fields.Date(string="出貨日期",default=0)
    shipping_num = fields.Integer(string="成品累計出貨量")
    blank_input_date = fields.Date(string="進貨日")
    qc_line = fields.One2many('alldo_gh_iot.workorder_qc', 'order_id', string="QC明細", copy=False)
    iot_line = fields.One2many('alldo_gh_iot.workorder_iot_data', 'order_id', string="IOT BOX資料明細", copy=False)
    status_line = fields.One2many('alldo_gh_iot.node_change_status', 'order_id', string="NODE 變更狀態記錄", copy=False)
    prodin_line = fields.One2many('alldo_gh_iot.wkorder_prodin', 'order_id', string="工單來料記錄", copy=False)
    prodout_line = fields.One2many('alldo_gh_iot.wkorder_prodout', 'order_id', string="加工後轉出記錄", copy=False)
    replace_line = fields.One2many('alldo_gh_iot.wkorder_replaceline','order_id',string="架機換線記錄",copy=False)
    ngratio_line = fields.One2many('alldo_gh_iot.wkorder_ngratio', 'order_id', string="工單不良率", copy=False)
    state = fields.Selection([('1', '草稿'), ('2', '印表'), ('3', '已開工'), ('4', '已完工'), ('5', '全委外')], string='狀態',
                             default='1')
    active = fields.Boolean(string="ARCHIVE",default=True)
    prod_num = fields.Integer(string="實際生產總數")
    good_num = fields.Integer(string="完成良品數", compute='_get_qc_total_num')
    prod_duration = fields.Float(digits=(10, 1), string="總工時(分鐘)", default=0.0)
    start_duration = fields.Float(digits=(10, 1), string="今日開工總工時(分鐘)", default=0.0)
    stop_duration = fields.Float(digits=(10, 1), string="今日暫停總工時(分鐘)", default=0.0)
    workorder_memo = fields.Text(string="註記")
    workorder_name = fields.Char(string="工單說明", compute='_get_workordername',store=True)
    mo_group_id = fields.Integer(string="GROUP ID")
    blankin_picking = fields.Many2one('stock.picking',string="進料調撥單")
    prodout_picking = fields.Many2one('stock.picking',string="開立出貨單")
    uncomplete_shipping = fields.Boolean(string='出貨未完成',compute='_get_uncomplete_ship',store=True)
    complete_shipping = fields.Boolean(string="已出貨完成",default=False)
    mo_production_num = fields.Integer(string="生產良品總數", default=0)
    not_close = fields.Boolean(string="工單不結案",default=False)
    process_ng_num = fields.Float(digits=(13, 2), string="已扣帳NG數量", default=0)
    new_ng_num = fields.Float(digits=(13, 2), string="當前NG數量", default=0)
    ng_complete = fields.Boolean(string="已扣帳？", default=True)
    can_achive = fields.Boolean(string="工單可歸檔?",compute=_get_canachive)

    # def complete_workorder(self):
    #     self.env.cr.execute("""update alldo_gh_iot_workorder set state='4' where id=%d""" % self.id)
    #     self.env.cr.execute("""commit""")



    def open_shipping_report(self):
        myrec1 = self.env['alldo_gh_iot.workorder'].search([('id','=',self.id)])
        mymogpid = myrec1.mo_group_id
        mycustomerlocid = myrec1.cus_name.property_stock_customer.id
        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
        myprodlocid = mycomploc.prod_loc.id
        myrec = self.env['stock.picking'].search([])

        myprodid = myrec1.product_no.id
        myres = myrec.create(
            {'picking_type_id': 2, 'location_id': myprodlocid, 'location_dest_id': mycustomerlocid,
             'move_type': 'direct', 'state': 'draft',
             'user_id': myrec1.create_uid.id, 'origin': myrec1.po_no1.po_no, 'state': 'assigned',
             'scheduled_date': myrec1.shipping_date,
             'partner_id': myrec1.cus_name.id, 'mo_group_id': mymogpid, 'report_memo': ' ',
             'move_ids_without_package': [(0, 0, {'product_id': myprodid, 'company_id': 1, 'location_id': myprodlocid,
                                                  'location_dest_id': mycustomerlocid, 'product_uom': 1,
                                                  'name': myrec1.product_no.name,
                                                  'product_uom_qty': myrec1.order_num})],
             'move_line_ids_without_package': [(0, 0, {'product_id': myprodid, 'location_id': myprodlocid,
                                                       'location_dest_id': mycustomerlocid, 'qty_done': 0,
                                                       'product_uom_id': 1,
                                                       'company_id': 1})]})

        myres.action_confirm()
        self.env.cr.commit()
        # myres.action_done()
        myshippingno = myres.name
        myshippingid = myres.id
        self.env.cr.execute("""update alldo_gh_iot_workorder set prodout_picking=%d where mo_group_id=%d""" % (myshippingid,mymogpid))
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""update stock_picking set mo_group_id=%d where id=%d""" % (mymogpid,myshippingid))
        self.env.cr.execute("""commit""")

    def run_archive(self):
        for rec in self:
            if rec.state=='4' or rec.state=='5':
                if rec.active==True:
                    if rec.mo_group_id > 0:
                        self.env.cr.execute("""update alldo_gh_iot_workorder set active=False where mo_group_id=%d""" % rec.mo_group_id)
                        self.env.cr.execute("""commit""")
                        self.env.cr.execute("""update alldo_gh_iot_schedule_line set active=False where mo_group_id=%d""" % rec.mo_group_id)
                        self.env.cr.execute("""commit""")
                    else:
                        self.env.cr.execute("""update alldo_gh_iot_workorder set active=False where id=%d""" % rec.id)
                        self.env.cr.execute("""commit""")

                else:
                    if rec.mo_group_id > 0 :
                        self.env.cr.execute("""update alldo_gh_iot_workorder set active=False where mo_group_id=%d""" % rec.mo_group_id)
                        self.env.cr.execute("""commit""")
                        self.env.cr.execute("""update alldo_gh_iot_schedule_line set active=False where mo_group_id=%d""" % rec.mo_group_id)
                        self.env.cr.execute("""commit""")
                    else:
                        self.env.cr.execute("""update alldo_gh_iot_workorder set active=False where id=%d""" % rec.id)
                        self.env.cr.execute("""commit""")

    @api.depends('shipping_num','order_num')
    def _get_uncomplete_ship(self):
        for rec in self:
            if rec.order_num > rec.shipping_num :
                rec.update({'uncomplete_shipping':True})
            else:
                rec.update({'uncomplete_shipping':False})

    def name_get(self):
        res = []
        for rec in self:
            myname = "[%s-(%s)]-%s-%s(%s)" % (
            rec.name, rec.eng_type, rec.cus_name.name, rec.product_no.name, rec.order_num)
            res += [(rec.id, myname)]
        return res

    def complete_workorder(self):
        myworkorderid = self.env.context.get('workorder_id')
        # self.env.cr.execute("""select setworkordercomplete(%d)""" % self.id)
        self.env.cr.execute("""select setallmoclose(%d)""" % self.id)
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
            vals['name'] = self.env['ir.sequence'].next_by_code('alldo_gh_iot.workorder') or _('New')
        if 'blank_no' in vals and not vals['blank_no']:
            vals['blank_no']=vals['product_no']
        res = super(alldoghiotworkorder, self).create(vals)
        self.env.cr.execute("""select createpowkorder(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    def _write(self, vals):
        res = super(alldoghiotworkorder, self)._write(vals)
        for rec in self:
            self.env.cr.execute("""select genpowkorderngnum(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select processwkorderng(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select getmogoodnum(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select genwkngratio(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            print("NEWNG:%s" % rec.new_ng_num)
            print("PRONG:%s" % rec.process_ng_num)
            if not rec.ng_complete and rec.new_ng_num != rec.process_ng_num :
                myrec = self.env['stock.picking']
                mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
                myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
                myscraplocid = mycomploc.scrap_loc.id  # 公司報廢位置
                ## 毛胚扣料 => NG倉
                if not rec.blank_no:
                    myblankno = rec.product_no.id
                else:
                    myblankno = rec.blank_no.id
                if (rec.new_ng_num - rec.process_ng_num) > 0:
                    myres = myrec.create(
                        {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': myscraplocid,
                         'move_type': 'direct',
                         'user_id': self.env.uid, 'origin': rec.name + ' NG扣帳', 'mo_group_id': rec.mo_group_id,
                         'move_line_ids': [
                             (0, 0, {'product_id': myblankno, 'company_id': 1, 'location_id': myblanklocid,
                                     'location_dest_id': myscraplocid, 'product_uom_id': 1, 'qty_done': (rec.new_ng_num - rec.process_ng_num)})]})

                    myres.action_confirm()
                    self.env.cr.commit()
                    myres.action_done()
                    self.env.cr.commit()
                else:
                    myres = myrec.create(
                        {'picking_type_id': 5, 'location_id': myscraplocid, 'location_dest_id': myblanklocid,
                         'move_type': 'direct',
                         'user_id': self.env.uid, 'origin': rec.name + ' NG扣帳返回', 'mo_group_id': rec.mo_group_id,
                         'move_line_ids': [
                             (0, 0, {'product_id': myblankno, 'company_id': 1, 'location_id': myscraplocid,
                                     'location_dest_id': myblanklocid, 'product_uom_id': 1,
                                     'qty_done': (rec.process_ng_num - rec.new_ng_num)})]})

                    myres.action_confirm()
                    self.env.cr.commit()
                    myres.action_done()
                    self.env.cr.commit()
            self.env.cr.execute("""update alldo_gh_iot_workorder set ng_complete=True,process_ng_num=%s where id=%d""" % (rec.new_ng_num,rec.id))
            self.env.cr.execute("""commit""")
        return res

    def unlink(self):
        for rec in self:
            self.env.cr.execute("""select candelwkorder(%d)""" % rec.id)
            mygpid = self.env.cr.fetchone()[0]
            if mygpid == 0 :
                raise UserError("工單已啟動,無法刪除了！")
            else:
                ################################################
                try:
                    mygprec = self.env['alldo_gh_iot.workorder'].search([('mo_group_id','=',mygpid)])[0]
                    if mygprec.blank_num > 0 : # 毛胚有進料
                        myblankno = mygprec.blank_no.id
                        myblanknum = mygprec.blank_num
                        mycusname = mygprec.cus_name.id
                        mycustomerlocid = self.cus_name.property_stock_customer.id  # 客戶位置倉庫
                        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
                        myblanklocid = mycomploc.blank_loc.id
                        myrec = self.env['stock.picking'].search([])
                        if myblankno > 0:
                            myres = myrec.create(
                                {'picking_type_id': 2, 'location_id': myblanklocid, 'location_dest_id': mycustomerlocid,
                                 'move_type': 'direct',
                                 'user_id': self.env.uid, 'origin': '工單刪除退毛胚', 'mo_group_id': mygpid,
                                 'partner_id': mycusname, 'report_memo': ' ',
                                 'move_line_ids': [
                                     (0, 0, {'product_id': myblankno, 'company_id': 1, 'location_id': myblanklocid,
                                             'location_dest_id': mycustomerlocid, 'product_uom_id': 1,
                                             'qty_done': myblanknum})]})
                            myres.action_confirm()
                            self.env.cr.commit()
                            myres.action_done()
                            self.env.cr.commit()
                except Exception as inst:
                    print('已刪除')
                try:
                    self.env.cr.execute("""delete from alldo_gh_iot_workorder where mo_group_id=%d""" % mygpid)
                    self.env.cr.execute("""commit""")
                except Exception as inst:
                    print('已刪除')

        res = super(alldoghiotworkorder, self).unlink()
        return res


class alldoghiotworkorderiotdata(models.Model):
    _name = "alldo_gh_iot.workorder_iot_data"
    _description = "工單IOT生產數據資料"
    _order = "order_id,iot_date desc"

    order_id = fields.Many2one('alldo_gh_iot.workorder', ondelete='cascade')
    iot_date = fields.Datetime(string="IOT時間")
    iot_node = fields.Many2one('maintenance.equipment', string="機台")
    iot_owner = fields.Many2one('hr.employee', string="擔當者")
    iot_num = fields.Float(digits=(13, 2), string="數量")
    iot_duration = fields.Float(digits=(6,0), string="單件工時(秒)")
    iot_duration1 = fields.Float(digits=(6,0),string="組合工時(秒)")
    std_duration = fields.Float(digits=(6,0), string="標準工時(秒)")
    iot_serial = fields.Char(string="IOT 流水號")
    iot_seq = fields.Integer(string="生產順序")
    cal_process = fields.Boolean(string="計算否",default=False)



class alldoghiotworkorderqc(models.Model):
    _name = "alldo_gh_iot.workorder_qc"
    _description = "工單產品加工質檢"
    _order = "qc_date desc"

    order_id = fields.Many2one('alldo_gh_iot.workorder', ondelete='cascade')
    qc_date = fields.Date(string="承製日期")
    iot_node = fields.Many2one('maintenance.equipment', string="機台")
    qc_good_num = fields.Float(digits=(13, 2), string="良品數量", default=0,compute='_get_good_num')
    material_ng_num = fields.Float(digits=(13, 2), string="材料不良數量", default=0)
    processing_ng_num = fields.Float(digits=(13, 2), string="加工不良數量", default=0)
    loss_num = fields.Float(digits=(13, 2), string="毛胚短少數量", default=0)
    total_amount_num = fields.Float(digits=(13, 2), string="合計承交數")
    complete_date = fields.Date(string="完成日期")
    iot_owner = fields.Many2one('res.users', string="責任者")
    iot_owner1 = fields.Many2one('hr.employee',string="擔當者")
    line_memo = fields.Char(string="說明",default=' ')
    report_date = fields.Date(string="製表日期")
    report_no = fields.Char(string="NG退料單號")
    product_no = fields.Many2one('product.product',string="PRODUCT",store=True,compute='_get_prod')
    cus_name = fields.Many2one('res.partner',string="CUSTOMER",store=True,compute='_get_cus')
    is_return_custom = fields.Boolean(string="NG是否已退回客戶端",default=False)


    @api.depends('order_id')
    def _get_cus(self):
        for rec in self:
            rec.cus_name = rec.order_id.cus_name.id

    @api.depends('order_id')
    def _get_prod(self):
        for rec in self:
            rec.product_no=rec.order_id.product_no.id


    # @api.depends('qc_good_num', 'material_ng_num', 'processing_ng_num')
    # def _get_total_amount(self):
    #     for rec in self:
    #         rec.total_amount_num = rec.qc_good_num - rec.material_ng_num - rec.processing_ng_num

    @api.depends('total_amount_num','loss_num', 'material_ng_num', 'processing_ng_num')
    def _get_good_num(self):
        for rec in self:
            rec.qc_good_num = rec.total_amount_num - rec.loss_num - rec.material_ng_num - rec.processing_ng_num


class alldoghiotnodechangestatus(models.Model):
    _name = "alldo_gh_iot.node_change_status"
    _description = "IOT裝置狀態變化記錄檔"

    order_id = fields.Many2one('alldo_gh_iot.workorder', ondelete='cascade')
    node_status = fields.Selection([('1', '開工'), ('2', '暫停'), ('3', '停工')], string="變化模式")
    iot_node = fields.Many2one('maintenance.equipment', string="機台")
    node_datetime = fields.Datetime(string="發生時間")


class alldoghiotworkordermeasuretool(models.Model):
    _name = "alldo_gh_iot.measure_tool"
    _description = "加工產品檢驗工具"
    _order = "sequence,id"

    sequence = fields.Integer(string="SEQ", default=10)
    inspect_code = fields.Char(string="代號", required=True)
    name = fields.Char(string="量測工具", required=True)
    inspect_line = fields.One2many('alldo_gh_iot.tool_inspect','inspect_id',copy=False)


class alldoghiotlastwork(models.Model):
    _name = "alldo_gh_iot.workorder_lastwork"
    _description = "工件最後生產時間記錄"

    work_datetime = fields.Datetime(string="最後件生產時間")
    equipment_id = fields.Many2one('maintenance.equipment', string="機台")
    workorder_id = fields.Many2one('alldo_gh_iot.workorder', string="工單")


class alldoghiotwkorderprodin(models.Model):
    _name = "alldo_gh_iot.wkorder_prodin"
    _description = "工單來料記錄明細"

    order_id = fields.Many2one('alldo_gh_iot.workorder', ondelete='cascade')
    prodin_datetime = fields.Datetime(string="時間")
    product_no = fields.Many2one('product.product', string="料號")
    in_type = fields.Selection([('1', '客戶'), ('2', '前工序')], string="來料類別")
    in_good_num = fields.Float(digits=(10, 2), string="良品數量", default=0.00)
    in_ng_num = fields.Float(digits=(10, 2), string="NG數量", default=0.00)
    process_num = fields.Float(digits=(10, 2), string="目前已加工數", default=0.00)
    in_loc = fields.Char(string="來源對象")
    in_id = fields.Integer(string="來源ID")
    in_owner = fields.Many2one('res.users', string="建檔人員")


class alldoghiotwkorderprodout(models.Model):
    _name = "alldo_gh_iot.wkorder_prodout"
    _description = "工單加工完轉出記錄明細"

    order_id = fields.Many2one('alldo_gh_iot.workorder', ondelete='cascade')
    prodout_datetime = fields.Datetime(string="時間")
    product_no = fields.Many2one('product.product', string="料號")
    out_type = fields.Selection([('1', '客戶'), ('2', '後工序')], string="轉出類別")
    out_good_num = fields.Float(digits=(10, 2), string="轉出良品數量", default=0.00)
    out_ng_num = fields.Float(digits=(10, 2), string="轉出NG數量", default=0.00)
    out_stock_num = fields.Float(digits=(10, 2), string="已入庫數", default=0.00)
    out_loc = fields.Char(string="轉出對象")
    out_owner = fields.Many2one('res.users', string="建檔人員")


class alldoghiotwkorderreplaceline(models.Model):
    _name = "alldo_gh_iot.wkorder_replaceline"
    _description = "架機換線記錄明細"

    order_id = fields.Many2one('alldo_gh_iot.workorder', ondelete='cascade')
    replace_owner = fields.Many2one('hr.employee', string="工程師")
    equipment_id = fields.Many2one('maintenance.equipment', string="機台")
    replace_start_datetime = fields.Datetime(string="啟始時間")
    replace_end_datetime = fields.Datetime(string="截止時間")
    replace_duration = fields.Float(digits=(6,1),string="時間(分)")
    replace_std = fields.Integer(string="標準時間(H)")
    replace_performance = fields.Float(digits=(5,2),string="達成率%")


class alldoghiotwkordermogroupid(models.Model):
    _name = "alldo_gh_iot.mo_group_seq"

    seqnum = fields.Integer(string="GROUP流水號",default=0)


class alldoacmeiotwkorderngratio(models.Model):
    _name = "alldo_gh_iot.wkorder_ngratio"

    order_id = fields.Many2one('alldo_gh_iot.workorder',ondelete='cascade')
    wk_good_num = fields.Float(digits=(10,0),string="生產良品數")
    wk_ng_num = fields.Float(digits=(10,0),string="加工不良數")
    material_ng_num = fields.Float(digits=(10,0),string="材料不良數")
    wk_loss_num = fields.Float(digits=(10,0),string="來料短少數")
    ng_ratio = fields.Float(digits=(5,1),string="不良率")

class AlldoGhIotToolInspect(models.Model):
    _name = "alldo_gh_iot.tool_inspect"
    _description = "量測工具校驗記錄"

    inspect_id = fields.Many2one('alldo_gh_iot.measure_tool',ondelete='cascade')
    inspect_date = fields.Date(string="日期")
    inspect_method = fields.Char(string="校正方式")
    inspect_man = fields.Char(string="人員")
    inspect_sup = fields.Char(string="廠商")
    inspect_fname = fields.Char(string="檔名")
    inspect_attach = fields.Binary(string="夾檔")


