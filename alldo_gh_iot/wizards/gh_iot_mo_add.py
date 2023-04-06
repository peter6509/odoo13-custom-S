# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class ghiotmoadd(models.TransientModel):
    _name = "alldo_gh_iot.mo_add_wizard"
    _description = "工單訂單數量追加"

    mo_no = fields.Many2one('alldo_gh_iot.workorder', string="追加工單")
    product_no = fields.Many2one('product.product',string="產品",required=True)
    prod_origin_num = fields.Float(digits=(10,2),string="原工單數量")
    prod_num = fields.Float(digits=(10,2),string="客戶追加數",default=0.00,required=True)
    is_outsourcing = fields.Boolean(string="直接委外供料？",default=False)
    partner_id = fields.Many2one('res.partner',string="委外加工商")
    addin_owner = fields.Many2one('res.users',string="入帳人員",default=lambda self:self.env.uid)

    @api.onchange('mo_no')
    def onclientchangepo(self):
        # self.env.cr.execute("""select getmoprod(%d)""" % self.mo_no.id)
        # myprodid = self.env.cr.fetchone()[0]
        # self.product_no =myprodid
        # return {'domain': {'product_no': [('id', '=', myprodid)]}}
        self.env.cr.execute("""select getmooriginnum(%d)""" % self.mo_no.id)
        self.prod_origin_num = self.env.cr.fetchone()[0]

    @api.onchange('product_no')
    def onclientchangeoriginnum(self):
        self.env.cr.execute("""select getprodmo(%d)""" % self.product_no.id)
        myrec = self.env.cr.fetchall()
        ids1 = []
        for rec in myrec:
            ids1.append(rec[0])
        return {'domain': {'mo_no': [('id', '=', ids1)]}}


    def run_mo_add(self):
        if self.is_outsourcing and not self.partner_id:
            raise UserError("必須輸入委外廠商資訊")

        if self.prod_num > 0:
            self.env.cr.execute("""select runmoadd(%d,%f)""" % (self.mo_no.id,self.prod_num))
            self.env.cr.execute("""commit""")
        else:
            raise UserError("沒有輸入追加數量 ！")

        mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
        mycustomerlocid = self.mo_no.cus_name.property_stock_customer.id  # 客戶位置倉庫
        myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
        mysupplocid = self.partner_id.property_stock_supplier.id  # 委外商倉庫
        # myprod = self.blank_no.id  # 毛胚料號
        mymogpid = self.mo_no.mo_group_id
        myrec = self.env['stock.picking'].search([])
        ## 額外執行毛胚追加進 毛胚倉
        # if self.prod_num > 0 :
        #     myres = myrec.create({'picking_type_id': 1, 'location_id': mycustomerlocid, 'location_dest_id': myblanklocid,
        #                           'move_type': 'direct',
        #                           'user_id': self.addin_owner.id, 'origin': '工單追加毛胚', 'mo_group_id': mymogpid,
        #                           'partner_id': self.mo_no.cus_name.id,
        #                           'move_line_ids': [
        #                               (0, 0,
        #                                {'product_id': self.product_no.id, 'company_id': 1, 'location_id': mycustomerlocid,
        #                                 'location_dest_id': myblanklocid, 'product_uom_id': 1,
        #                                 'qty_done': self.prod_num})]})
        #
        #     myres.action_confirm()
        #     self.env.cr.commit()
        #     myres.action_done()
        #     self.env.cr.commit()
        ##   額外直接委外供料
        # if self.is_outsourcing:
        #     if self.prod_num > 0:
        #         myres = myrec.create(
        #             {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': mysupplocid,
        #              'move_type': 'direct',
        #              'user_id': self.addin_owner.id, 'origin': '毛胚追加後直接委外供料', 'mo_group_id': mymogpid,
        #              'move_line_ids': [
        #                  (0, 0, {'product_id': self.blank_no.id, 'company_id': 1, 'location_id':myblanklocid,
        #                          'location_dest_id': mysupplocid, 'product_uom_id': 1,
        #                          'qty_done': self.prod_num})]})
        #
        #         myres.action_confirm()
        #         self.env.cr.commit()
        #         myres.action_done()
        #         self.env.cr.commit()


        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '工單產品追加輸入完成！'
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
