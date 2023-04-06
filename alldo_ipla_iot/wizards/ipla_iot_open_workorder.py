# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError


class iplaiotopenworkorder(models.TransientModel):
    _name = "alldo_ipla_iot.open_workorder_wizard"
    _description = "工單開工精靈"
    # ipla 目前使用製造命令直接開工單

    prod_id = fields.Many2one('product.product', string="產品")
    cus_name = fields.Many2one('res.partner', string="客戶")
    so_no = fields.Many2one('sale.order', string="客戶訂單")
    mo_no = fields.Many2one('mrp.production',string="製造命令",required=True)
    product_num = fields.Float(string="訂單數量", required=True, default=0.00)
    shipping_date = fields.Date(string="截止日期")
    in_owner = fields.Many2one('res.users', string="開單人員", default=lambda self: self.env.uid)
    # open_shipping = fields.Boolean(string="是否產生出貨草稿？",default=True)

    @api.onchange('mo_no')
    def onchangemono(self):
        if self.mo_no:
            myprodid= self.mo_no.product_id.id
            self.env.cr.execute("""select getmodeadline(%d)""" % self.mo_no.id)
            mydeadline = self.env.cr.fetchone()[0]
            self.prod_id = myprodid
            self.shipping_date = mydeadline


    @api.onchange('prod_id')
    def onchangeprodid(self):
        self.env.cr.execute("""select getmoqty(%d)""" % self.mo_no.id)
        myqty = self.env.cr.fetchone()[0]
        self.product_num = myqty
        self.env.cr.execute("""select getmosaleno(%d)""" % self.mo_no.id)
        mysaleno = self.env.cr.fetchone()[0]
        if mysaleno > 0:
            self.so_no = mysaleno

    # @api.onchange('so_no')
    # def onchangesono(self):
    #     myrec = self.env['sale.order'].search([('id', '=', self.so_no.id)])
    #     if myrec:
    #         mycusid = myrec.partner_id.id
    #         self.cus_name = myrec.partner_id.id


    def run_open_workorder(self):
        self.env.cr.execute("""select getmogpseq()""")
        mymogpid = self.env.cr.fetchone()[0]
        myworkorderrec = self.env['alldo_ipla_iot.workorder']
        myoutsuborderrec = self.env['alldo_ipla_iot.outsuborder']
        myrec = self.env['product.template'].search([('id', '=', self.prod_id.product_tmpl_id.id)])
        myfirstid = 0
        myfurnaceprodid=self.env['alldo_ipla_iot.company_stockloc'].search([]).furnace_prod_id.id
        for rec in myrec.eng_line:
            self.env.cr.execute("""select getprodengorder(%d,'%s')""" % (self.prod_id.id, rec.eng_type))
            myres = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select getprodengseq(%d,'%s')""" % (self.prod_id.id, rec.eng_type))
            myres1 = self.env.cr.fetchone()[0]
            if myres == '1':
                if rec.is_outsourcing:
                    myid = myoutsuborderrec.create({
                                                  'mrp_prod_id' : self.mo_no.id,
                                                  'product_no': self.prod_id.id,
                                                  'eng_type': rec.eng_type,
                                                  'eng_order': myres,
                                                  'eng_seq': myres1,
                                                  'po_no': self.mo_no.name,
                                                  'so_no': self.so_no.id,
                                                  'cus_name': rec.partner_id.id,
                                                  'shipping_date': self.shipping_date,
                                                  'mo_group_id': mymogpid,
                                                  'prodout_line': [(0, 0,
                                                                   {'prodout_datetime': fields.datetime.now(),
                                                                    'product_no': self.prod_id.id,
                                                                    'out_good_num': 0,
                                                                    'out_ng_num': 0,
                                                                    'out_owner': self.in_owner.id})]})
                else:
                    myid = myworkorderrec.create({
                                                  'mrp_prod_id': self.mo_no.id,
                                                  'product_no': self.prod_id.id,
                                                  'eng_type': rec.eng_type,
                                                  'eng_order': myres,
                                                  'eng_seq': myres1,
                                                  'po_no': self.mo_no.name,
                                                  'cus_name': self.cus_name.id,
                                                  'order_num': self.product_num,
                                                  'shipping_date': self.shipping_date,
                                                  'mo_group_id': mymogpid,
                                                  'prodin_line': [(0, 0,
                                                                   {'prodin_datetime': fields.datetime.now(),
                                                                    'product_no': myfurnaceprodid,
                                                                    'in_good_num': 0.00,
                                                                    'in_ng_num': 0.00,
                                                                    'in_type': '1',
                                                                    'in_loc': self.mo_no.name,
                                                                    'in_owner': self.in_owner.id})]})
                myfirstid = myid
            else:
                if rec.is_outsourcing:
                    myoutsuborderrec.create({
                                           'mrp_prod_id': self.mo_no.id,
                                           'product_no': self.prod_id.id,
                                           'eng_type': rec.eng_type,
                                           'eng_order': myres,
                                           'eng_seq': myres1,
                                           'po_no': self.mo_no.name,
                                           'cus_name': rec.partner_id.id,
                                           'mo_group_id': mymogpid,
                                           'shipping_date': self.shipping_date})
                else:
                    myworkorderrec.create({
                                           'mrp_prod_id': self.mo_no.id,
                                           'product_no': self.prod_id.id,
                                           'eng_type': rec.eng_type,
                                           'eng_order': myres,
                                           'eng_seq': myres1,
                                           'po_no': self.mo_no.name,
                                           'cus_name': self.cus_name.id,
                                           'order_num': self.product_num,
                                           'mo_group_id': mymogpid ,
                                           'shipping_date': self.shipping_date})
        # if self.open_shipping==True:
        #     if self.product_num > 0:
        #         myrec = self.env['stock.picking'].search([])
        #         myres = myrec.create(
        #             {'picking_type_id': 2, 'location_id': 8, 'location_dest_id': 5, 'move_type': 'direct','state':'draft',
        #              'user_id': self.in_owner.id, 'origin': self.mo_no.name, 'state':'assigned','scheduled_date':self.shipping_date,
        #              'partner_id':self.cus_name.id,'mo_group_id' : mymogpid,
        #              'move_ids_without_package': [(0, 0, {'product_id': self.prod_id.id, 'company_id': 1, 'location_id': 8,
        #                                        'location_dest_id': 5, 'product_uom': 1,'name':self.prod_id.name,
        #                                        'product_uom_qty': self.product_num})]})
        #         try:
        #             myres.action_confirm()
        #             # myres.action_done()
        #         except Exception as inst:
        #             print("No Confirm & action Done")

        self.env.cr.execute("""update sale_order_line set is_openwkorder=true where order_id=%d and product_id=%d""" % (self.so_no.id,self.prod_id.id))
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select cksoiswkopen(%d)""" % self.so_no.id)
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""update mrp_production set state='planned',mo_group_id=%d where id=%d""" % (mymogpid,self.mo_no.id))
        self.env.cr.execute("""commit""")

        if myfirstid != 0:
            myid1 = self.env['alldo_ipla_iot.workorder'].search([('id', '=', myfirstid.id)])
            return {'view_name': 'alldoiplaiotworkorder',
                    'name': (u'工單作業'),
                    'views': [[False, 'form'], [False, 'tree']],
                    'res_model': 'alldo_ipla_iot.workorder',
                    'context': self._context,
                    'type': 'ir.actions.act_window',
                    'target': 'self',
                    'res_id': myid1.id,
                    'view_mode': 'form',
                    'view_type': 'form',
                    'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                    }
