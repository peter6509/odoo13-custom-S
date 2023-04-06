# -*- coding: utf-8 -*-
# Author : Peter Wu



from odoo import models,fields,api
from odoo.exceptions import UserError


class iplaiotblankstockin(models.TransientModel):
    _name = "alldo_ipla_iot.blank_stockin_wizard"
    _description = "毛胚追加精靈"


    po_id = fields.Many2one('alldo_ipla_iot.po_wkorder',string="客戶單號")
    po_desc = fields.Char(string="客戶單號說明",default=' ')
    cus_name = fields.Many2one('res.partner',string=u"客戶")
    product_no = fields.Many2one('product.product', string="料號", required=True)
    mo_no = fields.Many2one('alldo_ipla_iot.workorder',string=u"工單號",required=True)
    stockin_num = fields.Float(string="目前累計數量",compute='_get_complete_stockin')
    blank_num = fields.Float(digits=(10,2),string="毛胚追加數量",default=0.00,required=True)
    is_out_blank = fields.Boolean(string="毛胚入庫後是否直接委外供料？", default=False)
    supplier_no = fields.Many2one('res.partner', string="委外加工廠商")
    supplier_num = fields.Float(digits=(10, 2), string="委外追加數量", default=0.00)
    stockin_owner = fields.Many2one('res.users',string="入帳人員",default=lambda self:self.env.uid)
    blank_onhand1 = fields.Float(string="總庫毛胚倉在手數量")
    blank_onhand2 = fields.Float(string="毛胚倉進料後在手數量", compute='_get_onhand2')
    blank_onhand3 = fields.Float(string="委外商毛胚在手數量")

    @api.onchange('supplier_no')
    def onchangesupplierno(self):
        mysupplierlocid = self.supplier_no.property_stock_supplier.id  # 委外位置倉庫
        # print("SupplierID:%d" % mysupplierlocid)
        # print("blanknoID:%d" % self.blank_no.id)
        self.env.cr.execute("""select getpartnerbkonhand(%d,%d)""" % (mysupplierlocid, self.product_no.id))
        self.blank_onhand3 = self.env.cr.fetchone()[0]

    @api.onchange('is_out_blank')
    def onchangeisoutblank(self):
        self.env.cr.execute("""select getprodsupplier(%d)""" % self.product_no.id)
        myrec = self.env.cr.fetchall()
        if not myrec:
            return {'domain': {'supplier_no': [(1, '=', 1)]}}
        else:
            ids=[]
            for rec in myrec:
                ids.append(rec[0])
            return {'domain': {'supplier_no': [('id', '=', ids)]}}

    @api.onchange('blank_num')
    def onchangeblanknum(self):
        self.supplier_num = self.blank_num


    @api.onchange('product_no')
    def onclientchange(self):
        self.env.cr.execute("""select getblankonhand(%d)""" % self.product_no.id)
        self.blank_onhand1 = self.env.cr.fetchone()[0]

    @api.depends('product_no', 'blank_num', 'blank_onhand1')
    def _get_onhand2(self):
        if self.blank_onhand1 != False:
            self.blank_onhand2 = self.blank_onhand1 + self.blank_num
        else:
            self.blank_onhand2 = self.blank_onhand1


    @api.depends('mo_no')
    def _get_complete_stockin(self):
        myrec = self.env['alldo_ipla_iot.workorder'].search([('id','=',self.mo_no.id)])
        if not myrec.blank_no:
            self.product_no = myrec.product_no.id
        else:
            self.product_no = myrec.blank_no.id
        self.stockin_num = myrec.blank_num


    @api.onchange('cus_name')
    def onchageclient1(self):
        self.env.cr.execute("""select getcusmoprod(%d)""" % self.cus_name.id)
        ids=[]
        myids = self.env.cr.fetchall()
        for rec in myids:
            ids.append(rec[0])
        return {'domain': {'product_no': [('id', '=', ids)]}}


    @api.onchange('product_no')
    def onchageclient2(self):
        self.env.cr.execute("""select getcusmo(%d,%d)""" % (self.cus_name.id,self.product_no.id))
        ids=[]
        myids = self.env.cr.fetchall()
        for rec in myids:
            ids.append(rec[0])
        return {'domain': {'mo_no': [('id', '=', ids)]}}


    @api.onchange('mo_no')
    def onclientchangepo(self):
        self.env.cr.execute("""select getmoprod(%d)""" % self.mo_no.id)
        myprodid = self.env.cr.fetchone()[0]
        return {'domain': {'product_no': [('id', '=', myprodid)]}}


    def run_blank_stockin(self):
        if self.is_out_blank==True and not self.supplier_no:
            raise UserError("選擇立即委外追加毛胚給委外廠商,委外廠商欄位不得空值")
        if self.supplier_no and self.supplier_num <= 0 :
            raise UserError("未輸入委外供料追加數量")
        mymogpid = self.mo_no.mo_group_id
        self.env.cr.execute("""select genblankstockin1(%d,%s,%d)""" % (self.mo_no.id,self.blank_num,self.stockin_owner.id))
        self.env.cr.execute("""commit""")
        mycomploc = self.env['alldo_ipla_iot.company_stockloc'].search([])
        myblanklocid = mycomploc.blank_loc.id
        mycuslocid = self.cus_name.property_stock_customer.id
        if self.blank_num > 0:
            myrec = self.env['stock.picking'].search([])
            myres = myrec.create({'picking_type_id': 1, 'location_id': mycuslocid, 'location_dest_id': myblanklocid, 'move_type': 'direct',
                                  'user_id': self.stockin_owner.id, 'origin': self.po_desc,'partner_id':self.cus_name.id,'mo_group_id':mymogpid,
                                  'move_line_ids': [
                                      (0, 0, {'product_id': self.product_no.id, 'company_id': 1, 'location_id': mycuslocid,
                                              'location_dest_id':  myblanklocid, 'product_uom_id': 1, 'qty_done': self.blank_num})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
        ######## 毛胚追加供料 => 委外加工廠商
        if self.is_out_blank==True and self.supplier_num > 0:
            mysupplocid = self.supplier_no.property_stock_supplier.id  # 委外商倉庫
            mycomploc = self.env['alldo_ipla_iot.company_stockloc'].search([])
            myprodlocid = mycomploc.prod_loc.id  # 公司產品庫存位置
            myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
            myscraplocid = mycomploc.scrap_loc.id  # 公司NG報廢位置
            mytranslocid = mycomploc.trans_loc.id  # 公司內部轉換位置
            myrec = self.env['stock.picking'].search([])
            ## 委外供料 : 公司毛胚倉 => 委外廠商倉庫位置
            myres = myrec.create(
                {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': mysupplocid,
                 'move_type': 'direct',
                 'user_id': self.stockin_owner.id, 'origin': '毛胚額外追加', 'partner_id': self.supplier_no.id,
                 'move_line_ids': [
                     (0, 0, {'product_id': self.product_no.id, 'company_id': 1, 'location_id': myblanklocid,
                             'location_dest_id': mysupplocid, 'product_uom_id': 1, 'qty_done': self.supplier_num})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
            mymoveno = myres.name
            mymoveid = myres.id
            mymemo= self.mo_no.name + '毛胚額外追加'
            myreturndate = fields.datetime.today()
            self.env.cr.execute("""select genoutpartner(%d,%d,%d,%d,'%s','%s','%s',%d)""" % (self.supplier_no.id, self.product_no.id, self.stockin_owner.id, self.supplier_num,mymemo,mymemo,myreturndate, mymoveid))
            self.env.cr.execute("""commit""")
        ########
        mysupplierlocid = self.supplier_no.property_stock_supplier.id  # 委外位置倉庫
        self.env.cr.execute("""select updatenotclosemo(%d,%d)""" % (self.mo_no.id,mysupplierlocid))
        self.env.cr.execute("""commit""")
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '毛胚進料入庫輸入完成！ 入庫單號：%s' % myres.name
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
