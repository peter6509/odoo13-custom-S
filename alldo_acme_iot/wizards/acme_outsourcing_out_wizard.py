# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class acmeoutsourcingoutwizard(models.TransientModel):
    _name = "alldo_acme_iot.outsourcing_out"
    _description = "委外加工給料精靈"


    suborder_id = fields.Many2one('alldo_acme_iot.outsuborder',string="委外加工單")
    partner_id = fields.Many2one('res.partner',string="委外加工廠商")
    product_id = fields.Many2one('product.product',string="產品/料號",required=True)
    out_num = fields.Integer(string="供料數量",default=0)
    out_owner = fields.Many2one('res.users',string="建單人",default=lambda self:self.env.uid)
    out_desc = fields.Char(string="說明",default=' ')
    out_memo = fields.Text(string="備註",default=' ')
    out_return_date = fields.Date(string="委外交期",required=True)
    report_date = fields.Date(string="製表日期")
    out_plastic_frame1 = fields.Integer(string="出塑膠框數", default=0)
    out_plastic_frame2 = fields.Integer(string="出蝴蝶籠數", default=0)
    out_pallet = fields.Integer(string="出棧板數", default=0)




    @api.onchange('product_id')
    def onchangeproductid(self):
        myrec = self.env['alldo_acme_iot.outsuborder'].search([('product_no', '=', self.product_id.id),('state','in',['1','2'])])
        ids = []
        for rec in myrec:
            ids.append(rec.id)
        return {'domain': {'suborder_id': [('id', 'in', ids)]}}

    @api.onchange('suborder_id')
    def onchangclient(self):
        self.partner_id = self.suborder_id.cus_name.id

        # myrec = self.env['alldo_acme_iot.outsuborder'].search([('id','=',self.suborder_id.id)])
        # return {'domain': {'product_id': [('id', '=', myrec.product_no.id)]}}


    def run_outsourcing_out(self):
        if not self.product_id and not self.suborder_id:
            raise UserError("委外單號 or 委外廠商 不得同時空值！")
        # if self.out_num==0:
        #     raise UserError("未輸入委外供料數量！")
        if self.suborder_id:  # 有委外加工單
            if self.out_num > 0 :
                self.env.cr.execute("""select genoutsourcingout(%d,%d,%d,%d)""" % (0,self.suborder_id.id,self.out_owner.id,self.out_num))
                self.env.cr.execute("commit")
                self.env.cr.execute("""select genoutpartner(%d,%d,%d,%d,%d,'%s','%s','%s')""" % (0,self.partner_id.id, self.product_id.id, self.out_owner.id, self.out_num, self.out_desc, self.out_memo,self.out_return_date))
                self.env.cr.execute("commit")
        else:                 # 無委外加工單,有委外商
            if self.out_num > 0 :
                self.env.cr.execute("""select genoutpartner(%d,%d,%d,%d,%d,'%s','%s','%s')""" % (0,self.partner_id.id,self.product_id.id,self.out_owner.id,self.out_num,self.out_desc,self.out_memo,self.out_return_date))
                self.env.cr.execute("commit")

        if self.out_plastic_frame1 > 0 or self.out_plastic_frame2 > 0 or self.out_pallet > 0 :
            ## 註記出籠框/蝴蝶欄/棧板 數量
            self.env.cr.execute("""select updatesuborderframe(%d,%d,%d,%d)""" % (self.suborder_id.id,self.out_plastic_frame1,self.out_plastic_frame2,self.out_pallet))
            self.env.cr.execute("""commit""")

        ## WH/毛胚倉位置
        myblanklocid = self.env['alldo_acme_iot.company_stockloc'].search([])[0].blank_loc.id

        mypickingrec = self.env['stock.picking'].search([])
        mysupplocid = self.partner_id.blank_stock_supplier.id  # 委外商倉庫
        self.env.cr.execute("""select getproduom(%d)""" % self.product_id.id)
        myuomid = self.env.cr.fetchone()[0]

        if self.out_num > 0 :
            myres = mypickingrec.create(
                {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': mysupplocid,
                 'move_type': 'direct',
                 'user_id': self.out_owner.id, 'report_memo': self.out_memo,
                 'move_line_ids': [
                     (0, 0, {'product_id': self.product_id.id, 'company_id': 1, 'location_id': myblanklocid,
                             'location_dest_id': mysupplocid, 'product_uom_id': myuomid,
                             'qty_done': self.out_num})]})
            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()


        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '委外加工供料輸入完成！'
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