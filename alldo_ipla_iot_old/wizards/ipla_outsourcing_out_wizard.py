# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class iplaoutsourcingoutwizard(models.TransientModel):
    _name = "alldo_ipla_iot.outsourcing_out"
    _description = "委外加工供料作業"


    suborder_id = fields.Many2one('alldo_ipla_iot.outsuborder',string="委外加工單")
    partner_id = fields.Many2one('res.partner',string="委外加工廠商")
    product_id = fields.Many2one('product.product',string="料號",required=True)
    out_num = fields.Integer(string="供料數量",default=0)
    out_owner = fields.Many2one('res.users',string="建單人",default=lambda self:self.env.uid)
    out_desc = fields.Char(string="加工說明")
    out_memo = fields.Text(string="備註")
    out_return_date = fields.Date(string="委外交期")
    report_date = fields.Date(string="製表日期")
    partner_blank_onhand1 = fields.Float(string="委外毛胚倉數量",default=0.00)
    partner_blank_onhand2 = fields.Float(string="供料後委外倉毛胚數",compute='_get_partner_bkonhand2')
    wh_blank_onhand1 = fields.Float(string="公司毛胚倉數量")
    wh_blank_onhand2 = fields.Float(string="供料後公司毛胚倉數量",compute='_get_wh_bkonhand2')

    @api.onchange('partner_id','product_id')
    def onchangeclient1(self):
        self.env.cr.execute("""select getpartnerbkonhand(%d,%d)""" % (self.partner_id.property_stock_supplier.id,self.product_id.id))
        self.partner_blank_onhand1 = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getwhbkonhand(%d)""" % self.product_id.id)
        self.wh_blank_onhand1 = self.env.cr.fetchone()[0]

    @api.depends('partner_blank_onhand1','out_num')
    def _get_partner_bkonhand2(self):
        if self.partner_blank_onhand1 != False:
           self.partner_blank_onhand2 = self.partner_blank_onhand1 + self.out_num
        else:
           self.partner_blank_onhand2 = 0.00

    @api.depends('wh_blank_onhand1', 'out_num')
    def _get_wh_bkonhand2(self):

        self.wh_blank_onhand2 = self.wh_blank_onhand1 - self.out_num



    @api.onchange('suborder_id')
    def onchangclient(self):
        myrec = self.env['alldo_ipla_iot.outsuborder'].search([('id','=',self.suborder_id.id)])
        return {'domain': {'product_id': [('id', '=', myrec.product_no.id)]}}


    def run_outsourcing_out(self):
        mymoveno = '無調撥單'
        if not self.out_return_date:
            raise UserError("需要設定委外交期")
        if not self.product_id and not self.suborder_id:
            raise UserError("委外單號 or 委外廠商 不得同時無值！")
        if self.out_num==0:
            raise UserError("未輸入委外供料數量！")
        if not self.partner_id:
            self.env.cr.execute("""select genoutsourcingout(%d,%d,%d)""" % (self.suborder_id.id,self.out_owner.id,self.out_num))
            self.env.cr.execute("""commit""")
        elif not self.suborder_id:
            if self.out_num > 0:
                mysupplocid = self.partner_id.property_stock_supplier.id  # 委外商倉庫
                mycomploc = self.env['alldo_ipla_iot.company_stockloc'].search([])
                myprodlocid = mycomploc.prod_loc.id  # 公司產品庫存位置
                myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
                myscraplocid = mycomploc.scrap_loc.id  # 公司NG報廢位置
                mytranslocid = mycomploc.trans_loc.id  # 公司內部轉換位置
                myrec = self.env['stock.picking'].search([])
                ## 委外供料 : 公司毛胚倉 => 委外廠商倉庫位置
                if not self.suborder_id:
                    myres = myrec.create(
                        {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': mysupplocid, 'move_type': 'direct',
                         'user_id': self.out_owner.id, 'origin': self.out_desc, 'partner_id': self.partner_id.id,
                         'move_line_ids': [
                             (0, 0, {'product_id': self.product_id.id, 'company_id': 1, 'location_id': myblanklocid,
                                     'location_dest_id': mysupplocid, 'product_uom_id': 1, 'qty_done': self.out_num})]})
                else:
                    mymogpid = self.suborder_id.mo_group_id
                    myres = myrec.create(
                        {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': mysupplocid,
                         'move_type': 'direct','mo_group_id':mymogpid,
                         'user_id': self.out_owner.id, 'origin': self.out_desc, 'partner_id': self.partner_id.id,
                         'move_line_ids': [
                             (0, 0, {'product_id': self.product_id.id, 'company_id': 1, 'location_id': myblanklocid,
                                     'location_dest_id': mysupplocid, 'product_uom_id': 1, 'qty_done': self.out_num})]})
                myres.action_confirm()
                self.env.cr.commit()
                myres.action_done()
                self.env.cr.commit()
                mymoveno = myres.name
                mymoveid = myres.id
                self.env.cr.execute("""select genoutpartner(%d,%d,%d,%d,'%s','%s','%s',%d)""" % (self.partner_id.id,self.product_id.id,self.out_owner.id,self.out_num,self.out_desc,self.out_memo,self.out_return_date,mymoveid))
        self.env.cr.execute("commit")
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '委外加工供料輸入完成！ 調撥單：%s' % mymoveno
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