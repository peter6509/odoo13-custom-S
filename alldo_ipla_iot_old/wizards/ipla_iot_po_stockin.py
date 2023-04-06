# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class iplaiotpostockin(models.TransientModel):
    _name = "alldo_ipla_iot.po_stockin_wizard"
    _description = "工單完工入庫"


    po_id = fields.Many2one('alldo_ipla_iot.po_wkorder',string="客戶訂單")
    product_no = fields.Many2one('product.product', string="工單料號", required=True)
    product_no1 = fields.Many2one('product.product', string="轉變料號",required=True)
    mo_no = fields.Many2one('alldo_ipla_iot.workorder', string="入庫工單",required=True)
    prod_num = fields.Float(digits=(10,2),string="良品入庫數",default=0.00,required=True)
    ng_num = fields.Float(digits=(10,2),string="NG數量",default=0.00)
    loss_num = fields.Float(digits=(10,2),string="毛胚短少數量",default=0.00)
    is_close = fields.Boolean(string="是否已完工結案？",default=False)
    stockin_owner = fields.Many2one('res.users',string="入帳人員",default=lambda self:self.env.uid)
    blank_onhand1 = fields.Float(string="工單料號毛胚倉在手量")
    blank_onhand2 = fields.Float(string="入庫後原始料在手數",compute='_get_blank_onhand2')
    prod_onhand1 = fields.Float(string="轉變料號成品倉在手量")
    prod_onhand2 = fields.Float(string="入庫後變更料在手數", compute='_get_prod_onhand2')

    @api.onchange('product_no')
    def onclientchange(self):
        self.blank_onhand1 = 0
        self.blank_onhand2 = 0
        self.prod_onhand1 = 0
        self.prod_onhand2 = 0
        self.env.cr.execute("""select getpdbkonhand(%d)""" % self.product_no.id)
        self.blank_onhand1 = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getpdonhand(%d)""" % self.product_no1.id)
        self.prod_onhand1 = self.env.cr.fetchone()[0]

        self.env.cr.execute("""select getprodmo(%d)""" % self.product_no.id)
        myrec = self.env.cr.fetchall()
        ids1 = []
        for rec in myrec:
            ids1.append(rec[0])
        # return {'domain': {'mo_no': [('id', '=', ids1)]}}

        self.env.cr.execute("""select blankgetprod(%d)""" % self.product_no.id)
        # self.env.cr.execute("""select getprodblank(%d)""" % self.product_no.id)
        myrec = self.env.cr.fetchall()
        if not myrec:
            self.product_no1 = self.product_no.id
            return {'domain': {'product_no1': [(1, '=', 1)],'mo_no': [('id', '=', ids1)]}}
        else:
            ids = []
            for rec in myrec:
                ids.append(rec[0])
            return {'domain': {'product_no1': [('id', 'in', ids)],'mo_no': [('id', '=', ids1)]}}



    @api.depends('prod_num','ng_num','loss_num', 'blank_onhand1')
    def _get_blank_onhand2(self):
        if self.blank_onhand1 != False:
            self.blank_onhand2 = self.blank_onhand1 - self.prod_num - self.ng_num - self.loss_num
        else:
            self.blank_onhand2 = self.blank_onhand1

    @api.depends('prod_num', 'prod_onhand1')
    def _get_prod_onhand2(self):
        self.prod_onhand2 = self.prod_onhand1 + self.prod_num



    # @api.onchange('product_no')
    # def onclientchangepd(self):
    #     self.env.cr.execute("""select getprodmo(%d)""" % self.product_no.id)
    #     myrec = self.env.cr.fetchall()
    #     ids=[]
    #     for rec in myrec:
    #         ids.append(rec[0])
    #     return {'domain': {'mo_no': [('id', '=', ids)]}}

    @api.onchange('mo_no')
    def onclientchangepo(self):
        self.env.cr.execute("""select getmogoodnum(%d)""" % self.mo_no.id)
        mygoodnum = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getmongnum(%d)""" % self.mo_no.id)
        myngnum = self.env.cr.fetchone()[0]
        self.prod_num = mygoodnum
        self.ng_num = myngnum
        self.env.cr.execute("""select getmolossnum(%d)""" % self.mo_no.id)
        mylossnum = self.env.cr.fetchone()[0]
        self.loss_num = mylossnum
        # self.env.cr.execute("""select blankgetprod(%d)""" % self.mo_no.product_no.id)
        # myrec = self.env.cr.fetchall()
        # if not myrec:
        #     self.product_no=self.mo_no.product_no.id
        #     return {'domain': {'product_no': [(1, '=', 1)]}}
        # else:
        #     ids = []
        #     for rec in myrec:
        #         ids.append(rec[0])
        #     return {'domain': {'product_no': [('id', 'in', ids)]}}


    def run_po_stockin(self):
        mymogpid = self.mo_no.mo_group_id
        if self.loss_num > 0 :
            self.env.cr.execute("""select genworkorderqcloss(%d,%s,%d)""" % (self.mo_no.id,self.loss_num,self.stockin_owner.id))
            self.env.cr.execute("""commit""")
        if self.prod_num > 0 :
            ##  扣毛胚庫存數量 => 生產
            # mycustomerrec = self.env['res.partner'].search([('id', '=', self.cus_name.id)])
            # mycustomerlocid = mycustomerrec.property_stock_customer.id  # 客戶倉庫位置

            mycomploc = self.env['alldo_ipla_iot.company_stockloc'].search([])
            myprodlocid = mycomploc.prod_loc.id     # 公司產品庫存位置
            myblanklocid = mycomploc.blank_loc.id   # 公司毛胚庫存位置
            mymolocid = mycomploc.mo_loc.id         # 公司生產移轉位置
            myprod = self.mo_no.product_no.id       # 工單的毛胚料號

            myrec1=self.env['alldo_ipla_iot.workorder'].search([('id','=',self.mo_no.id)])
            ## 工單毛胚料號
            if not myrec1.blank_no:
                myprod = myrec1.product_no.id
            else:
                myprod = myrec1.blank_no.id
            myrec = self.env['stock.picking'].search([])

            ## 產品料號 move from blankloc to prodloc (新模式)
            # myres = myrec.create({'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': myprodlocid,
            #                       'move_type': 'direct','user_id': self.stockin_owner.id, 'origin': self.mo_no.name, 'mo_group_id': mymogpid,
            #                       'move_line_ids': [(0, 0, {'product_id': self.product_no1.id, 'company_id': 1, 'location_id': myblanklocid,
            #                       'location_dest_id': myprodlocid, 'product_uom_id': 1,'qty_done': self.prod_num})]})



            # 毛胚生產投耗料 (舊模式)  扣毛胚倉毛胚數量投入轉換
            # myrunnum = self.prod_num + self.ng_num
            myres = myrec.create({'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': mymolocid, 'move_type': 'direct',
                                  'user_id': self.stockin_owner.id, 'origin': self.mo_no.name,'mo_group_id':mymogpid,
                                  'move_line_ids': [
                                      (0, 0, {'product_id': myprod, 'company_id': 1, 'location_id': myblanklocid,
                                              'location_dest_id': mymolocid, 'product_uom_id': 1,
                                              'qty_done': self.prod_num})]})
            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()

            ## 生產完成 產品入庫 product_no1 轉換料號入成品倉
            myres = myrec.create({'picking_type_id': 5,'location_id':mymolocid,'location_dest_id':myprodlocid,'move_type':'direct',
                                  'user_id':self.stockin_owner.id,'origin':self.mo_no.name,'mo_group_id':mymogpid,
                                  'move_line_ids':[(0,0,{'product_id':self.product_no1.id,'company_id':1,'location_id':mymolocid,
                                                 'location_dest_id':myprodlocid,'product_uom_id':1,'qty_done':self.prod_num})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
            self.env.cr.execute("""select updatemoprodin(%d,%d)""" % (self.mo_no.id, int(self.prod_num)))
            self.env.cr.execute("""commit""")

        if self.is_close==True:
            self.env.cr.execute("""select setallmoclose(%d)""" % self.mo_no.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select getmongnum(%d)""" % self.mo_no.id)
            mynum = self.env.cr.fetchone()[0]
            mycomploc = self.env['alldo_ipla_iot.company_stockloc'].search([])
            myprodlocid = mycomploc.prod_loc.id  # 公司產品庫存位置
            myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
            mymolocid = mycomploc.mo_loc.id  # 公司生產移轉位置
            myscraplocid = mycomploc.scrap_loc.id  # 公司報廢位置
            ## 毛胚扣料 => NG倉
            myres = myrec.create({'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': myscraplocid, 'move_type': 'direct',
                          'user_id': self.stockin_owner.id, 'origin': self.mo_no.name,'mo_group_id':mymogpid,
                          'move_line_ids': [
                              (0, 0, {'product_id': myprod, 'company_id': 1, 'location_id': myblanklocid,
                                      'location_dest_id': myscraplocid, 'product_uom_id': 1, 'qty_done': mynum})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()

        self.env.cr.execute("""select alloutsourcingstockin(%d,%s,%s,%s)""" % (self.mo_no.id,self.prod_num,self.ng_num,self.loss_num))
        self.env.cr.execute("""commit""")
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '工單產品入庫完成輸入完成！'
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
