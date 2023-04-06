# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class iplamrpproductioninherit(models.Model):
    _inherit = "mrp.production"
    _order = "create_date desc,name asc"

    ipla_wk_line = fields.One2many('alldo_ipla_iot.workorder','mrp_prod_id',string="製造命令工單")
    ipla_sub_line = fields.One2many('alldo_ipla_iot.outsuborder','mrp_prod_id',string="製造命令工單-委外")
    ipla_material_line = fields.One2many('alldo_ipla_iot.materialline','mrp_prod_id',string="製造命令耗料檢核表")
    mo_group_id = fields.Integer(string="WK GROUP ID")
    wo_isrunning = fields.Boolean(string="工單還未結案",default=True)
    so_pi = fields.Char(string="PI單號")
    prodin_num = fields.Integer(string="成品累計入庫量")
    shipping_num = fields.Integer(string="成品累計出貨量")
    active = fields.Boolean(string="ARCHIVE",default=True)

    def run_archive(self):
        for rec in self:
            if rec.state=='done':
                if rec.active==True:
                    self.env.cr.execute("""update mrp_production set active=False where id=%d""" % rec.id)
                else:
                    self.env.cr.execute("""update mrp_production set active=True where id=%d""" % rec.id)
                self.env.cr.execute("""commit""")

    def name_get(self):
        result = []
        for record in self:
            result.append(
                (record.id, '%s-(%s)[PI:%s](QTY:%s)' % (record.name, record.product_id.default_code,record.so_pi, record.product_qty)))
        return result

    def action_assign(self):
        super(iplamrpproductioninherit, self).action_assign()
        self.env.cr.execute("""select gen_mrp_materialline(%d)""" % self.id)
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select resetproductionnum(%d)""" % self.id)
        self.env.cr.execute("""commit""")


    def action_confirm(self):
        super(iplamrpproductioninherit, self).action_confirm()
        self.env.cr.execute("""select mrpproductionupdate('%s')""" % self.name)
        self.env.cr.execute("""commit""")


    def open_produce_product(self):
        ##################### 開立工單作業
        for rec in self:
            self.env.cr.execute("""select getmogpseq()""")
            mymogpid = self.env.cr.fetchone()[0]
            myworkorderrec = self.env['alldo_ipla_iot.workorder']
            myoutsuborderrec = self.env['alldo_ipla_iot.outsuborder']
            myrec = self.env['product.template'].search([('id', '=', rec.product_id.product_tmpl_id.id)])
            myfirstid = 0
            mysaleorderid=False
            mycusid=False
            if rec.origin:
                self.env.cr.execute("""select getmocusid('%s')""" % rec.origin)
                mycusid = self.env.cr.fetchone()[0]
                self.env.cr.execute("""select getmosaleorderid('%s')""" % rec.origin)
                mysaleorderid = self.env.cr.fetchone()[0]
            myfurnaceprodid = self.env['alldo_ipla_iot.company_stockloc'].search([]).furnace_prod_id.id
            for rec1 in myrec.eng_line:
                self.env.cr.execute("""select getprodengorder(%d,'%s')""" % (rec.product_id.id, rec1.eng_type))
                myres = self.env.cr.fetchone()[0]
                self.env.cr.execute("""select getprodengseq(%d,'%s')""" % (rec.product_id.id, rec1.eng_type))
                myres1 = self.env.cr.fetchone()[0]
                if myres == '1':
                    if rec1.is_outsourcing:
                        myid = myoutsuborderrec.create({
                            'mrp_prod_id': rec.id,
                            'product_no': rec.product_id.id,
                            'eng_type': rec1.eng_type + '-' + rec1.eng_desc,
                            'eng_order': myres,
                            'eng_seq': myres1,
                            'po_no': rec.name,
                            'so_pi':rec.so_pi,
                            'order_num':rec.product_qty,
                            'so_no': mysaleorderid if mysaleorderid else False,
                            'cus_name': rec1.partner_id.id if rec1.partner_id else False,
                            'shipping_date': rec.date_deadline,
                            'mo_group_id': mymogpid,
                            'prodout_line': [(0, 0,
                                              {'prodout_datetime': fields.datetime.now(),
                                               'product_no': rec.product_id.id,
                                               'out_good_num': 0,
                                               'out_ng_num': 0,
                                               'out_owner': self.env.uid})]})
                    else:
                        myid = myworkorderrec.create({
                            'mrp_prod_id': rec.id,
                            'product_no': rec.product_id.id,
                            'eng_type': rec1.eng_type + '-' + rec1.eng_desc,
                            'eng_order': myres,
                            'eng_seq': myres1,
                            'po_no': rec.name,
                            'so_pi': rec.so_pi,
                            'so_no': mysaleorderid if mysaleorderid else False,
                            'cus_name': mycusid if mycusid else False,
                            'order_num': rec.product_qty,
                            'shipping_date': rec.date_deadline,
                            'mo_group_id': mymogpid,
                            'prodin_line': [(0, 0,
                                             {'prodin_datetime': fields.datetime.now(),
                                              'product_no': myfurnaceprodid,
                                              'in_good_num': 0.00,
                                              'in_ng_num': 0.00,
                                              'in_type': '1',
                                              'in_loc': rec.name,
                                              'in_owner': self.env.uid})]})
                    myfirstid = myid
                else:
                    if rec1.is_outsourcing:
                        myoutsuborderrec.create({
                            'mrp_prod_id': rec.id,
                            'product_no': rec.product_id.id,
                            'eng_type': rec1.eng_type + '-' + rec1.eng_desc,
                            'eng_order': myres,
                            'eng_seq': myres1,
                            'po_no': rec.name,
                            'so_pi': rec.so_pi,
                            'order_num': rec.product_qty,
                            'so_no': mysaleorderid if mysaleorderid else False,
                            'cus_name': rec1.partner_id.id if rec1.partner_id else False,
                            'mo_group_id': mymogpid,
                            'shipping_date': rec.date_deadline})
                    else:
                        myworkorderrec.create({
                            'mrp_prod_id': rec.id,
                            'product_no': rec.product_id.id,
                            'eng_type': rec1.eng_type + '-' + rec1.eng_desc,
                            'eng_order': myres,
                            'eng_seq': myres1,
                            'po_no': rec.name,
                            'so_pi': rec.so_pi,
                            'so_no': mysaleorderid if mysaleorderid else False,
                            'cus_name': mycusid if mycusid else False,
                            'order_num': rec.product_qty,
                            'mo_group_id': mymogpid,
                            'shipping_date': rec.date_deadline})


        #####################

        self.ensure_one()
        if self.bom_id.type == 'phantom':
            raise UserError(_('You cannot produce a MO with a bom kit product.'))
        action = self.env.ref('mrp.act_mrp_product_produce').read()[0]
        return action

    def button_mark_done(self):
        self.ensure_one()
        self._check_company()
        # if self.wo_isrunning==True:
        #     raise UserError("工單正在執行中...,還不能結束！")
        for wo in self.workorder_ids:
            if wo.time_ids.filtered(lambda x: (not x.date_end) and (x.loss_type in ('productive', 'performance'))):
                raise UserError(_('Work order %s is still running') % wo.name)
        self._check_lots()

        self.post_inventory()
        # Moves without quantity done are not posted => set them as done instead of canceling. In
        # case the user edits the MO later on and sets some consumed quantity on those, we do not
        # want the move lines to be canceled.
        (self.move_raw_ids | self.move_finished_ids).filtered(lambda x: x.state not in ('done', 'cancel')).write({
            'state': 'done',
            'product_uom_qty': 0.0,
        })
        self.env.cr.execute("""select setmrpprodloc(%d,%s)""" % (self.product_id.id,self.product_qty))
        self.env.cr.execute("""commit""")
        return self.write({'date_finished': fields.Datetime.now()})


