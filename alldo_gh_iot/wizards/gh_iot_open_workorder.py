# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError


class ghiotopenworkorder(models.TransientModel):
    _name = "alldo_gh_iot.open_workorder_wizard"
    _description = "工單開立精靈"

    prod_id = fields.Many2one('product.product', string="產品料號", required=True)
    blank_no = fields.Many2one('product.product',string="毛胚料號", required=True)
    cus_name = fields.Many2one('res.partner', string="客戶", required=True)
    po_no = fields.Many2one('alldo_gh_iot.po_wkorder',string="客戶訂單")
    po_no1 = fields.Many2many('alldo_gh_iot.po_wkorder','po_wkorder_wizard_rel','wiz_id','po_id',string="客戶訂單")
    so_no = fields.Many2one('sale.order', string="客戶訂單")
    wk_type = fields.Selection([('1','廠內加工'),('2','全委外')],string="工單型態",default='1')
    not_close = fields.Boolean(string="工單不結案", default=False)
    product_num = fields.Float(digits=(10,0),string="訂單數量", required=True, default=0)
    wkorder_num = fields.Float(digits=(10,0),string="工單開立數量",required=True,default=0)
    blank_num = fields.Float(string="毛胚數量",default=0.00)
    blank_type = fields.Selection([('1','開工單且毛胚進料入庫'),('2','僅開工單毛胚不進料入庫')],string="毛胚進料方式",default='1')
    stockin_date = fields.Date(string="進料日")
    shipping_date = fields.Date(string="出貨日")
    in_owner = fields.Many2one('res.users', string="開單人員", default=lambda self: self.env.uid)
    open_shipping = fields.Boolean(string="是否產生出貨草稿？",default=True)
    blank_onhand1 = fields.Float(string="毛胚倉在手數量")
    blank_onhand2 = fields.Float(string="毛胚倉進料後在手數量",compute='_get_onhand2')
    blank_onhand3 = fields.Float(string="委外商毛胚在手數量")
    prod_onhand = fields.Float(string="產品總庫在手數量")
    is_out_blank = fields.Boolean(string="毛胚入庫後是否直接委外供料？", default=False)
    supplier_no = fields.Many2one('res.partner', string="委外加工廠商")
    supplier_num = fields.Float(digits=(10, 2), string="委外供料數量", default=0.00)


    @api.onchange('product_num')
    def onchangeproductnum(self):
        # print("POID:%d" % self.po_no.id)
        self.env.cr.execute("""select getpoprodlocknum(%d)""" % self.po_no.id)
        mybookingnum = self.env.cr.fetchone()[0]
        # print("LOCK NUM:%d" % mybookingnum)
        self.wkorder_num = self.product_num - mybookingnum

    @api.onchange('po_no')
    def onchangepono(self):
        myponoid = self.env.context.get('po_wkorder_id',False)
        if myponoid:
            myrec = self.env['alldo_gh_iot.po_wkorder'].search([('id','=',myponoid)])
            self.prod_id = myrec.product_no.id
            self.cus_name = myrec.cus_name.id
            self.product_num = myrec.po_num
            self.po_no = myponoid
            self.shipping_date = myrec.shipping_date



    # @api.depends('blank_no', 'supplier_no')
    # def _get_onhand3(self):
    #     mysupplierlocid = self.supplier_no.property_stock_customer.id  # 委外位置倉庫
    #     self.env.cr.execute("""select getpartnerbkonhand(%d,%d)""" % (mysupplierlocid,self.blank_no.id))
    #     self.blank_onhand3 = self.env.cr.fetchone()[0]


    @api.onchange('is_out_blank')
    def onchangeisoutblank(self):
        self.supplier_num = self.blank_num
        self.env.cr.execute("""select getprodsupplier(%d)""" % self.blank_no.id)
        myrec = self.env.cr.fetchall()
        if not myrec:
            return {'domain': {'supplier_no': [(1, '=', 1)]}}
        else:
            ids = []
            for rec in myrec:
                ids.append(rec[0])
            return {'domain': {'supplier_no': [('id', '=', ids)]}}

    @api.onchange('supplier_no')
    def onchangesupplierno(self):
        mysupplierlocid = self.supplier_no.property_stock_supplier.id  # 委外位置倉庫
        # print("SupplierID:%d" % mysupplierlocid)
        # print("blanknoID:%d" % self.blank_no.id)
        self.env.cr.execute("""select getpartnerbkonhand(%d,%d)""" % (mysupplierlocid, self.blank_no.id))
        self.blank_onhand3 = self.env.cr.fetchone()[0]

    @api.onchange('blank_no')
    def onclientchange(self):
        self.env.cr.execute("""select getblankonhand(%d)""" % self.blank_no.id)
        self.blank_onhand1 = self.env.cr.fetchone()[0]


    @api.depends('blank_no','blank_num','blank_type','blank_onhand1')
    def _get_onhand2(self):
        if self.blank_type=='1':
            if self.blank_onhand1 != False:
                self.blank_onhand2 = self.blank_onhand1 + self.blank_num
            else:
                self.blank_onhand2 = self.blank_onhand1
        else:
            if self.blank_onhand1 != False:
                self.blank_onhand2 = self.blank_onhand1
            else:
                self.blank_onhand2 = 0


    @api.onchange('cus_name')
    def onchangecusname(self):
        self.env.cr.execute("""select getpartnerprod(%d)""" % self.cus_name.id)
        myrec = self.env.cr.fetchall()
        myids = []
        for rec in myrec:
            myids.append(rec[0])
        return {'domain': {'prod_id': [('id', 'in', myids)]}}

    @api.onchange('prod_id')
    def onchangeprodid(self):
        self.env.cr.execute("""select getprodblank(%d)""" % self.prod_id.id)
        self.blank_no = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getprodonhand(%d)""" % self.prod_id.id)
        self.prod_onhand = self.env.cr.fetchone()[0]
        myponoid = self.env.context.get('po_wkorder_id', False)
        if myponoid != False:
            self.write({'po_no1': [(6, 0, [myponoid])]})
        # self.env.cr.execute("""select getsoprodnum(%d,%d)""" % (self.so_no.id,self.prod_id.id))
        # myres = self.env.cr.fetchone()[0]
        # self.product_num = myres
        # self.blank_num = myres

    # @api.onchange('product_num')
    # def onchangenum(self):
    #     self.blank_num = self.product_num

    def run_open_workorder(self):
        mypowkorderid = self.env.context.get('po_wkorder_id',False)
        if not self.po_no and mypowkorderid != False:
            self.po_no = mypowkorderid
        if self.po_no:
            self.env.cr.execute("""update alldo_gh_iot_po_wkorder set is_open=True where id=%d""" % self.po_no.id)
            self.env.cr.execute("""commit""")
        for line in self.po_no1:
            self.env.cr.execute("""update alldo_gh_iot_po_wkorder set is_open=True where id=%d""" % line.po_id)
            self.env.cr.execute("""commit""")
        self.env.cr.execute("""select getmogpseq()""")
        mymogpid = self.env.cr.fetchone()[0]
        mystockinno=' '
        myshippingno = ' '
        myreportmemo = ' '
        myshippingid = 0
        mystockinid = 0
        myworkorderrec = self.env['alldo_gh_iot.workorder']
        myoutsuborderrec = self.env['alldo_gh_iot.outsuborder']
        myrec = self.env['product.template'].search([('id', '=', self.prod_id.product_tmpl_id.id)])
        isopen=False
        myfirstid = 0
        if not self.prod_id.product_tmpl_id.wkorder_memo:
            mywkordermemo = ' '
        else:
            mywkordermemo = self.prod_id.product_tmpl_id.wkorder_memo
        self.env.cr.execute("""select getprodequip(%d)""" % self.prod_id.id)
        myprodequipid = self.env.cr.fetchone()[0]
        if myprodequipid > 0:
            myequiprec = self.env['maintenance.equipment'].search([('id','=',myprodequipid)])

        if self.wk_type == '2':         # 全委外
            myid = myworkorderrec.create({'product_no': self.prod_id.id,
                                          'blank_no': self.blank_no.id,
                                          'eng_type': '全委外',
                                          'eng_order': '4',
                                          'eng_seq': 1,
                                          'po_no1': self.po_no.id,
                                          'cus_name': self.cus_name.id,
                                          'order_num': self.wkorder_num,
                                          'blank_num': self.blank_num,
                                          'shipping_date': self.shipping_date,
                                          'blank_input_date':self.stockin_date,
                                          'not_close':self.not_close,
                                          'mo_group_id': mymogpid,
                                          'state': '5',
                                          'prodin_line': [(0, 0,
                                                           {'prodin_datetime': fields.datetime.now(),
                                                            'product_no': self.blank_no.id,
                                                            'in_good_num': self.blank_num,
                                                            'in_ng_num': 0.00,
                                                            'in_type': '1',
                                                            'in_loc': self.cus_name.name,
                                                            'in_owner': self.in_owner.id})]})
            isopen= True
            myreportmemo = myid.name
        else:     # 廠內工單
            for rec in myrec.eng_line:
                self.env.cr.execute("""select getprodengorder(%d,'%s')""" % (self.prod_id.id, rec.eng_type))
                myres = self.env.cr.fetchone()[0]
                self.env.cr.execute("""select getprodengseq(%d,'%s')""" % (self.prod_id.id, rec.eng_type))
                myres1 = self.env.cr.fetchone()[0]

                if myres == '1':  # 首工序
                    if rec.is_outsourcing:   # 委外加工
                        myid = myoutsuborderrec.create({'product_no': self.prod_id.id,
                                                        'blank_no': self.blank_no.id,
                                                        'eng_type': rec.eng_type,
                                                        'eng_order': myres,
                                                        'eng_seq': myres1,
                                                        'po_no1': self.po_no.id,
                                                        'so_no': self.so_no.id,
                                                        'cus_name': rec.partner_id.id,
                                                        'shipping_date': self.shipping_date,
                                                        'blank_input_date': self.stockin_date,
                                                        'mo_group_id': mymogpid,
                                                        'prodout_line': [(0, 0,
                                                                           {'prodout_datetime': fields.datetime.now(),
                                                                            'product_no': self.blank_no.id,
                                                                            'out_good_num': 0,
                                                                            'out_ng_num': 0,
                                                                            'out_owner': self.in_owner.id})]})
                    else:
                        #print("pono:%d" % self.po_no.id)
                        myid = myworkorderrec.create({'product_no': self.prod_id.id,
                                                      'blank_no': self.blank_no.id,
                                                      'eng_type': rec.eng_type,
                                                      'eng_order': myres,
                                                      'eng_seq': myres1,
                                                      'po_no1': self.po_no.id,
                                                      'cus_name': self.cus_name.id,
                                                      'order_num': self.wkorder_num,
                                                      'blank_num': self.blank_num,
                                                      'shipping_date': self.shipping_date,
                                                      'blank_input_date': self.stockin_date,
                                                      'mo_group_id': mymogpid,
                                                      'workorder_memo': mywkordermemo,
                                                      'prodin_line': [(0, 0,
                                                                       {'prodin_datetime': fields.datetime.now(),
                                                                        'product_no': self.blank_no.id,
                                                                        'in_good_num': self.blank_num,
                                                                        'in_ng_num': 0.00,
                                                                        'in_type': '1',
                                                                        'in_loc':  self.cus_name.name,
                                                                        'in_owner': self.in_owner.id})]})
                        isopen=True
                        if myprodequipid > 0:
                            myequiprec.write({'schedule_line': [(0, 0, {'schedule_date': fields.datetime.now(),'mo_no':myid.id,'mo_group_id':mymogpid,'product_no':self.prod_id.id,'state':'1','active':True})]})
                    if myreportmemo==' ':
                        myreportmemo = myid.name
                    else:    
                        myreportmemo = myreportmemo + '/' + myid.name
                    self.env.cr.execute("""select genopenpowkorder(%d,%d)""" % (self.id,myid.id))
                    self.env.cr.execute("""commit""")

                elif myres == '2' or myres == '3' :
                    if rec.is_outsourcing:
                        myoutsuborderrec.create({'product_no': self.prod_id.id,
                                                 'blank_no': self.blank_no.id,
                                                 'eng_type': rec.eng_type,
                                                 'eng_order': myres,
                                                 'eng_seq': myres1,
                                                 'po_no1': self.po_no.id,
                                                 'cus_name': rec.partner_id.id,
                                                 'mo_group_id': mymogpid,
                                                 'blank_input_date': self.stockin_date,
                                                 'shipping_date': self.shipping_date})
                    else:
                        myid = myworkorderrec.create({'product_no': self.prod_id.id,
                                               'blank_no': self.blank_no.id,
                                               'eng_type': rec.eng_type,
                                               'eng_order': myres,
                                               'eng_seq': myres1,
                                               'po_no1': self.po_no.id,
                                               'cus_name': self.cus_name.id,
                                               'order_num': self.wkorder_num,
                                               'blank_num': self.blank_num,
                                               'mo_group_id': mymogpid,
                                               'workorder_memo': mywkordermemo,
                                               'blank_input_date': self.stockin_date,
                                               'shipping_date': self.shipping_date})
                        self.env.cr.execute("""select genopenpowkorder(%d,%d)""" % (self.id, myid.id))
                        self.env.cr.execute("""commit""")
                        if myprodequipid > 0:
                            myequiprec.write({'schedule_line': [(0, 0,{'schedule_date': fields.datetime.now(), 'mo_no': myid.id,
                                                              'mo_group_id': mymogpid, 'product_no': self.prod_id.id,
                                                              'state': '1', 'active': True})]})
                elif myres == '4':  # 成品後工序(包裝)
                    myworkorderrec.create({'product_no': self.prod_id.id,
                                           # 'blank_no': self.blank_no.id,
                                           'eng_type': rec.eng_type,
                                           'eng_order': myres,
                                           'eng_seq': myres1,
                                           'po_no1': self.po_no.id,
                                           'cus_name': self.cus_name.id,
                                           'order_num': self.wkorder_num,
                                           # 'blank_num': self.blank_num,
                                           'mo_group_id': mymogpid,
                                           'workorder_memo': mywkordermemo,
                                           # 'blank_input_date': self.stockin_date,
                                           'shipping_date': self.shipping_date})

        if self.blank_type=='1' and self.blank_num > 0 :  # 毛胚進料入毛胚倉 客戶倉庫 => 公司毛胚倉
            mycustomerlocid = self.cus_name.property_stock_customer.id   # 客戶位置倉庫
            mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
            myblanklocid = mycomploc.blank_loc.id
            myrec = self.env['stock.picking'].search([])
            myres = myrec.create({'picking_type_id': 1, 'location_id': mycustomerlocid, 'location_dest_id': myblanklocid, 'move_type': 'direct',
                                  'user_id': self.in_owner.id, 'origin': self.po_no.po_no,'mo_group_id': mymogpid,
                                  'partner_id': self.cus_name.id,'report_memo':myreportmemo,
                                  'move_line_ids': [
                                      (0, 0, {'product_id': self.blank_no.id, 'company_id': 1, 'location_id': mycustomerlocid,
                                              'location_dest_id': myblanklocid, 'product_uom_id': 1,
                                              'qty_done': self.blank_num})]})
            # try:
            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
            mystockinno = myres.name
            mystockinid = myres.id
            # except Exception as inst:
            #     print("No Confirm & action Done")

        ######## 毛胚倉毛胚 => 委外加工廠商
        if self.is_out_blank == True and self.supplier_num > 0:
            mysupplocid = self.supplier_no.property_stock_supplier.id  # 委外商倉庫
            mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
            myprodlocid = mycomploc.prod_loc.id  # 公司產品庫存位置
            myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
            myscraplocid = mycomploc.scrap_loc.id  # 公司NG報廢位置
            mytranslocid = mycomploc.trans_loc.id  # 公司內部轉換位置
            myrec = self.env['stock.picking'].search([])
            ## 委外供料 : 公司毛胚倉 => 委外廠商倉庫位置
            myres = myrec.create(
                {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': mysupplocid,
                 'move_type': 'direct',
                 'user_id': self.in_owner.id, 'origin': '開工單一併供料委外商', 'partner_id': self.supplier_no.id,
                 'move_line_ids': [
                     (0, 0, {'product_id': self.blank_no.id, 'company_id': 1, 'location_id': myblanklocid,
                             'location_dest_id': mysupplocid, 'product_uom_id': 1,
                             'qty_done': self.supplier_num})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
            mymoveno = myres.name
            mymoveid = myres.id
            mymemo = '開工單一併供料委外商'
            myreturndate = fields.datetime.today()
            self.env.cr.execute("""select genoutpartner(%d,%d,%d,%d,'%s','%s','%s',%d)""" % (
            self.supplier_no.id, self.blank_no.id, self.in_owner.id, self.supplier_num, mymemo, mymemo,
            myreturndate, mymoveid))
            self.env.cr.execute("""commit""")
        ########


        if self.product_num > 0:
            ## 直接產生一張出貨單 待辦  ; 公司產品倉 => 客戶位置倉庫
            mycustomerlocid = self.cus_name.property_stock_customer.id
            mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
            myprodlocid = mycomploc.prod_loc.id
            myrec = self.env['stock.picking'].search([])
            # self.env.cr.execute("""select blankgetprod(%d)""" % self.blank_no.id)
            # myprodrec = self.env.cr.fetchall()
            # if len(myprodrec) > 2:
            #     myres = myrec.create(
            #         {'picking_type_id': 2, 'location_id': myprodlocid, 'location_dest_id': mycustomerlocid,
            #          'move_type': 'direct', 'state': 'draft',
            #          'user_id': self.in_owner.id, 'origin': self.po_no, 'state': 'assigned',
            #          'scheduled_date': self.shipping_date,
            #          'partner_id': self.cus_name.id, 'mo_group_id': mymogpid, 'report_memo': myreportmemo,})
            #     for rec in myprodrec:
            #         myres.write({'move_ids_without_package': [(0, 0, {'product_id': rec[0], 'company_id': 1, 'location_id': myprodlocid,
            #                                    'location_dest_id': mycustomerlocid, 'product_uom': 1,'name':self.prod_id.name,
            #                                    'product_uom_qty': 0})],
            #                      'move_line_ids_without_package':[(0,0,{'product_id':rec[0],'location_id': myprodlocid,
            #                                    'location_dest_id': mycustomerlocid,'qty_done':0,'product_uom_id': 1,
            #                                     'company_id': 1})]})
            # else:
            # if not myprodrec:
            #     myprodid = self.prod_id.id
            # else:
            #     myprodid = myprodrec[0]
            myprodid = self.prod_id.id
            myres = myrec.create(
                {'picking_type_id': 2, 'location_id': myprodlocid, 'location_dest_id': mycustomerlocid, 'move_type': 'direct','state':'draft',
                 'user_id': self.in_owner.id, 'origin': self.po_no.po_no, 'state':'assigned','scheduled_date':self.shipping_date,
                 'partner_id':self.cus_name.id,'mo_group_id' : mymogpid,'report_memo':myreportmemo,
                 'move_ids_without_package': [(0, 0, {'product_id': myprodid, 'company_id': 1, 'location_id': myprodlocid,
                                           'location_dest_id': mycustomerlocid, 'product_uom': 1,'name':self.prod_id.name,
                                           'product_uom_qty': self.product_num})],
                 'move_line_ids_without_package':[(0,0,{'product_id':myprodid,'location_id': myprodlocid,
                                           'location_dest_id': mycustomerlocid,'qty_done':0,'product_uom_id': 1,
                                            'company_id': 1})]})

            myres.action_confirm()
            self.env.cr.commit()
            # myres.action_done()
            myshippingno = myres.name
            myshippingid = myres.id


        self.env.cr.execute("""update sale_order_line set is_openwkorder=true where order_id=%d and product_id=%d""" % (self.so_no.id,self.prod_id.id))
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select cksoiswkopen(%d)""" % self.so_no.id)
        self.env.cr.execute("""commit""")
        # if isopen:
        self.env.cr.execute("""select getlastmo(%d)""" % self.cus_name.id)
        myid1 = self.env.cr.fetchone()[0]
        if self.blank_type=='2':
            mystockinno = '無入庫單'
        if not self.open_shipping:
            myshippingno = '無出貨單號'
        mydesc = '內部收貨單:(%s) 內部交貨單:(%s)' % (mystockinno, myshippingno)
        self.env.cr.execute("""select updatemomemo(%d,'%s',%d,%d)""" % (self.cus_name.id,mydesc,mystockinid,myshippingid))
        self.env.cr.execute("""commit""")

        return {'view_name': 'alldoghiotworkorder',
                'name': (u'工單作業'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'alldo_gh_iot.workorder',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'self',
                'res_id': myid1,
                'view_mode': 'form',
                'view_type': 'form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }
