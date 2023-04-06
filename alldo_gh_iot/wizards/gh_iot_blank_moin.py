# -*- coding: utf-8 -*-
# Author : Peter Wu



from odoo import models,fields,api
from odoo.exceptions import UserError


class ghiotblankmoin(models.TransientModel):
    _name = "alldo_gh_iot.blank_moin_wizard"
    _description = "毛胚進料/委外供料精靈"

    @api.depends('cus_name','blank_no')
    def _get_blanknum1(self):    # 最後一次進料數
        self.env.cr.execute("""select getlastblankinnum(%d,%d)""" % (self.cus_name.id,self.blank_no.id))
        myres = self.env.cr.fetchone()[0]
        self.blank_num1 = myres
        return myres

    @api.depends('cus_name', 'blank_no')
    def _get_blankindate(self):  # 最後一次進料日
        self.env.cr.execute("""select getlastblankindate(%d,%d)""" % (self.cus_name.id, self.blank_no.id))
        myres = self.env.cr.fetchone()[0]
        self.blankin_date = myres
        return myres

    @api.depends('partner_id', 'blank_no')
    def _get_outsourcingnum1(self):  # 最後一次供料數
        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
        myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
        self.env.cr.execute("""select getlastoutsourcingnum(%d,%d,%d)""" % (myblanklocid,self.partner_id.blank_loc.id, self.blank_no.id))
        myres = self.env.cr.fetchone()[0]
        self.outsourcing_num1 = myres
        return myres

    @api.depends('partner_id', 'blank_no')
    def _get_outsourcingdate(self):  # 最後一次供料
        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
        myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
        self.env.cr.execute("""select getlastoutsourcingdate(%d,%d,%d)""" % (myblanklocid,self.partner_id.blank_loc.id, self.blank_no.id))
        myres = self.env.cr.fetchone()[0]
        self.blankout_date = myres
        return myres

    cus_name = fields.Many2one('res.partner',string=u"客戶")
    blank_no = fields.Many2one('product.product',string="毛胚料號",required=True)
    blank_num = fields.Float(digits=(10,0),string="毛胚進料數",default=0.00)
    stockin_owner = fields.Many2one('res.users', string="入帳人員", default=lambda self: self.env.uid)
    blank_onhand = fields.Float(string="毛胚倉在手數量")
    is_outsourcing = fields.Boolean(string="直接委外供料？",default=False)
    partner_id = fields.Many2one('res.partner', string="委外加工廠商")
    outsourcing_num = fields.Float(digits=(10,0),string="毛胚供料數",default=0.00)

    blank_num1 = fields.Float(digits=(10,0),string="最後一次進料數",compute=_get_blanknum1)
    blankin_date = fields.Date(string="最後一次進料日期",compute=_get_blankindate)
    outsourcing_num1 = fields.Float(digits=(10,0),string="最後一次供料數",compute=_get_outsourcingnum1)
    blankout_date = fields.Date(string="最後一次供料日期",compute=_get_outsourcingdate)

    @api.onchange('cus_name')
    def onchangecus(self):
        self.env.cr.execute("""select getblankbycus(%d)""" % self.cus_name.id)
        myrec = self.env.cr.fetchall()
        myids = []
        for rec in myrec:
            myids.append(rec[0])
        return {'domain': {'blank_no': [('id', 'in', myids)]}}

    @api.onchange('blank_no')
    def onclientchange(self):
        self.env.cr.execute("""select getblankonhand(%d)""" % self.blank_no.id)
        self.blank_onhand = self.env.cr.fetchone()[0]

    @api.onchange('blank_num')
    def onclientchangenum(self):
        self.outsourcing_num = self.blank_num



    def run_blank_stockin(self):
        if self.is_outsourcing and not self.partner_id:
            raise UserError("未輸入委外供應商！")
        # self.env.cr.execute("""select genblankstockin1(%d,%s,%d)""" % (self.mo_no.id,self.blank_num,self.stockin_owner.id))
        # self.env.cr.execute("""commit""")
        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
        myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
        mypartnerlocid = self.cus_name.property_stock_customer.id  # 客戶位置
        myprod = self.blank_no.id  # 毛胚料號
        myrec = self.env['stock.picking'].search([])
        if self.blank_num > 0:
            myres = myrec.create({'picking_type_id': 1, 'location_id': mypartnerlocid, 'location_dest_id': myblanklocid, 'move_type': 'direct',
                                  'user_id': self.stockin_owner.id, 'origin': '毛胚進料毛胚倉',
                                  'move_line_ids': [
                                      (0, 0, {'product_id': self.blank_no.id, 'company_id': 1, 'location_id': mypartnerlocid,
                                              'location_dest_id': myblanklocid, 'product_uom_id': 1,
                                              'qty_done': self.blank_num})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
        if self.is_outsourcing:

            if not self.partner_id.blank_loc:
                mysupplocid = self.partner_id.property_stock_supplier.id  # 委外商倉庫
            else:
                mysupplocid = self.partner_id.blank_loc.id  # 委外商倉庫
            myres = myrec.create({'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': mysupplocid,
                                  'move_type': 'direct',
                                  'user_id': self.stockin_owner.id, 'origin': '毛胚倉委外供料',
                                  'move_line_ids': [
                                      (0, 0,
                                       {'product_id': self.blank_no.id, 'company_id': 1, 'location_id': myblanklocid,
                                        'location_dest_id': mysupplocid, 'product_uom_id': 1,
                                        'qty_done': self.outsourcing_num})]})

            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
            mymoveno = myres.name
            mymoveid = myres.id
            self.env.cr.execute("""select genoutpartner(%d,%d,%d,%d,'%s','%s',%d)""" % (
            self.partner_id.id, self.blank_no.id, self.stockin_owner.id, self.outsourcing_num, '委外供料', ' ', mymoveid))
            self.env.cr.execute("commit")


        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '毛胚進料輸入完成！'
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
