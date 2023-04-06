# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotproductmoin(models.TransientModel):
    _name = "alldo_gh_iot.prod_moin_wizard"
    _description = "成品進料/委外供料精靈"

    @api.depends('cus_name', 'prod_no')
    def _get_prodnum1(self):  # 最後一次進料數
        self.env.cr.execute("""select getlastprodinnum(%d,%d)""" % (self.cus_name.id, self.prod_no.id))
        myres = self.env.cr.fetchone()[0]
        self.prod_num1 = myres
        return myres

    @api.depends('cus_name', 'prod_no')
    def _get_prodindate(self):  # 最後一次進料日
        self.env.cr.execute("""select getlastprodindate(%d,%d)""" % (self.cus_name.id, self.prod_no.id))
        myres = self.env.cr.fetchone()[0]
        self.prodin_date = myres
        return myres

    @api.depends('partner_id', 'prod_no')
    def _get_outsourcingnum1(self):  # 最後一次供料數
        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
        myprodlocid = mycomploc.prod_loc.id  # 公司成品庫存位置
        self.env.cr.execute("""select getlastoutsourcingnum(%d,%d,%d)""" % (myprodlocid, self.partner_id.prod_loc.id, self.prod_no.id))
        myres = self.env.cr.fetchone()[0]
        self.outsourcing_num1 = myres
        return myres

    @api.depends('partner_id', 'prod_no')
    def _get_prodoutdate(self):  # 最後一次供料
        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
        myprodlocid = mycomploc.prod_loc.id  # 公司成品庫存位置
        self.env.cr.execute("""select getlastoutsourcingdate(%d,%d,%d)""" % (myprodlocid, self.partner_id.prod_loc.id, self.prod_no.id))
        myres = self.env.cr.fetchone()[0]
        self.prodout_date = myres
        return myres


    cus_name = fields.Many2one('res.partner',string=u"客戶")
    prod_no = fields.Many2one('product.product',string="成品料號",required=True)
    prod_num = fields.Float(digits=(10,0),string="成品進料數",default=0.00)
    stockin_owner = fields.Many2one('res.users', string="入帳人員", default=lambda self: self.env.uid)
    prod_onhand = fields.Float(string="成品倉在手數量")
    is_outsourcing = fields.Boolean(string="直接委外供料？",default=False)
    partner_id = fields.Many2one('res.partner', string="委外加工廠商")
    outsourcing_num = fields.Float(digits=(10,0),string="成品供料數",default=0.00)

    prod_num1 = fields.Float(digits=(10, 0), string="最後一次進料數", compute=_get_prodnum1)
    prodin_date = fields.Date(string="最後一次進料日期", compute=_get_prodindate)
    outsourcing_num1 = fields.Float(digits=(10, 0), string="最後一次供料數", compute=_get_outsourcingnum1)
    prodout_date = fields.Date(string="最後一次供料日期", compute=_get_prodoutdate)

    @api.onchange('cus_name')
    def onchangecusname(self):
        self.env.cr.execute("""select getpartnerprod(%d)""" % self.cus_name.id)
        myrec = self.env.cr.fetchall()
        myids = []
        for rec in myrec:
            myids.append(rec[0])
        return {'domain': {'prod_no': [('id', 'in', myids)]}}

    @api.onchange('prod_no')
    def onclientchange(self):
        self.env.cr.execute("""select getprodonhand(%d)""" % self.prod_no.id)
        self.prod_onhand = self.env.cr.fetchone()[0]

    @api.onchange('prod_num')
    def onclientchangenum(self):
        self.outsourcing_num = self.prod_num



    def run_prod_stockin(self):
        if self.is_outsourcing and not self.partner_id:
            raise UserError("未輸入委外供應商！")
        # self.env.cr.execute("""select genblankstockin1(%d,%s,%d)""" % (self.mo_no.id,self.blank_num,self.stockin_owner.id))
        # self.env.cr.execute("""commit""")
        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
        myprodlocid = mycomploc.prod_loc.id  # 公司成品庫存位置
        mypartnerlocid = self.cus_name.property_stock_customer.id  # 客戶位置
        myprod = self.prod_no.id  # 成品料號
        myrec = self.env['stock.picking'].search([])
        if self.prod_num > 0:
            myres = myrec.create({'picking_type_id': 1, 'location_id': mypartnerlocid, 'location_dest_id': myprodlocid, 'move_type': 'direct',
                                  'user_id': self.stockin_owner.id, 'origin': '成品進料成品倉',
                                  'move_line_ids': [
                                      (0, 0, {'product_id': self.prod_no.id, 'company_id': 1, 'location_id': mypartnerlocid,
                                              'location_dest_id': myprodlocid, 'product_uom_id': 1,
                                              'qty_done': self.prod_num})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
        if self.is_outsourcing:
            # mysupplocid = self.partner_id.property_stock_supplier.id  # 委外商倉庫
            mysupplocid = self.partner_id.prod_loc.id  # 委外商倉庫
            myres = myrec.create({'picking_type_id': 5, 'location_id': myprodlocid, 'location_dest_id': mysupplocid,
                                  'move_type': 'direct',
                                  'user_id': self.stockin_owner.id, 'origin': '成品倉委外供料',
                                  'move_line_ids': [
                                      (0, 0,
                                       {'product_id': self.prod_no.id, 'company_id': 1, 'location_id': myprodlocid,
                                        'location_dest_id': mysupplocid, 'product_uom_id': 1,
                                        'qty_done': self.outsourcing_num})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
            mymoveno = myres.name
            mymoveid = myres.id
            self.env.cr.execute("""select genoutpartner(%d,%d,%d,%d,'%s','%s',%d)""" % (
            self.partner_id.id, self.prod_no.id, self.stockin_owner.id, self.outsourcing_num, '委外供料(成品)', ' ', mymoveid))
            self.env.cr.execute("commit")


        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '成品委外輸入完成！'
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
