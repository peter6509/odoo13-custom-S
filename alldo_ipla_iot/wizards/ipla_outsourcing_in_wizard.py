# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class iplaoutsourcinginwizard(models.TransientModel):
    _name = "alldo_ipla_iot.outsourcing_in"
    _description = "委外加工完工回廠記錄"


    suborder_id = fields.Many2one('alldo_ipla_iot.outsuborder',string="委外加工單",required=True)
    partner_id = fields.Many2one('res.partner', string="委外加工廠商")
    product_id = fields.Many2one('product.product',string="產品/料號",required=True)
    in_good_num = fields.Integer(string="完工良品數量",default=0)
    in_ng_num = fields.Integer(string="完工NG數量",default=0)
    in_desc = fields.Char(string="說明")
    in_owner = fields.Many2one('res.users',string="建單人",default=lambda self:self.env.uid)
    is_complete = fields.Boolean(string="是否結案？",default=False)
    in_plastic_frame1 = fields.Integer(string="回收塑膠框數", default=0)
    in_plastic_frame2 = fields.Integer(string="回收蝴蝶籠數", default=0)
    in_pallet = fields.Integer(string="回收棧板數", default=0)

    @api.onchange('product_id')
    def onchangeproductid(self):
        myrec = self.env['alldo_ipla_iot.outsuborder'].search([('product_no','=',self.product_id.id),('state','not in',['4','3'])])
        ids=[]
        for rec in myrec:
            ids.append(rec.id)
        return {'domain': {'suborder_id': [('id', 'in', ids)]}}

    @api.onchange('suborder_id')
    def onchangclient(self):
        self.partner_id = self.suborder_id.cus_name.id


    def run_outsourcing_in(self):
        if not self.product_id and not self.suborder_id:
            raise UserError("委外單號 or 委外廠商 不得同時空值！")
        # if self.in_good_num==0 and self.in_ng_num==0 :
        #     raise UserError("未輸入完工入庫數量！")
        if self.suborder_id:
            if self.in_good_num > 0 or self.in_ng_num > 0 :
                self.env.cr.execute("""select genoutsourcingin(%d,%d,%d,%d,%d)""" % (self.suborder_id.id,0,self.in_owner.id,self.in_good_num,self.in_ng_num))
                self.env.cr.execute("""commit""")
                self.env.cr.execute("""select geninpartner(%d,%d,%d,%d,%d,%d,'%s')""" % (self.partner_id.id,0, self.product_id.id, self.in_owner.id, self.in_good_num, self.in_ng_num, self.in_desc))
                self.env.cr.execute("commit")
        else:
            if self.in_good_num > 0 or self.in_ng_num > 0:
                self.env.cr.execute("""select geninpartner(%d,%d,%d,%d,%d,%d,'%s')""" % (self.partner_id.id,0,self.product_id.id, self.in_owner.id, self.in_good_num, self.in_ng_num,self.in_desc))
                self.env.cr.execute("commit")

        if self.in_plastic_frame1 > 0 or self.in_plastic_frame2 > 0 or self.in_pallet > 0 :
            ## 註記回收籠框/蝴蝶欄/棧板 數量
            self.env.cr.execute("""select updatesuborderframe1(%d,%d,%d,%d)""" % (self.suborder_id.id, self.in_plastic_frame1, self.in_plastic_frame2, self.in_pallet))
            self.env.cr.execute("""commit""")

        ## WH/成品倉位置
        myprodlocid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].prod_loc.id
        ## 報廢倉位置(NG)
        myscraplocid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].scrap_loc.id
        mypickingrec = self.env['stock.picking'].search([])
        mysupplocid = self.partner_id.blank_stock_supplier.id  # 委外商倉庫
        self.env.cr.execute("""select getproduom(%d)""" % self.product_id.id)
        myuomid = self.env.cr.fetchone()[0]
        ## GOOD 加工完工回廠

        if self.in_good_num > 0 :
            myres = mypickingrec.create(
                {'picking_type_id': 5, 'location_id': mysupplocid, 'location_dest_id': myprodlocid,
                 'move_type': 'direct',
                 'user_id': self.in_owner.id, 'report_memo': self.in_desc,
                 'move_line_ids': [
                     (0, 0, {'product_id': self.product_id.id, 'company_id': 1, 'location_id': mysupplocid,
                             'location_dest_id': myprodlocid, 'product_uom_id': myuomid,
                             'qty_done': self.in_good_num})]})
            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()
        if self.in_ng_num > 0 :
            ## NG 加工回廠
            myres1 = mypickingrec.create(
                {'picking_type_id': 5, 'location_id': mysupplocid, 'location_dest_id': myscraplocid,
                 'move_type': 'direct',
                 'user_id': self.in_owner.id, 'report_memo': self.in_desc,
                 'move_line_ids': [
                     (0, 0, {'product_id': self.product_id.id, 'company_id': 1, 'location_id': mysupplocid,
                             'location_dest_id': myscraplocid, 'product_uom_id': myuomid,
                             'qty_done': self.in_ng_num})]})
            myres1.action_confirm()
            self.env.cr.commit()
            myres1.action_done()
            self.env.cr.commit()

        if self.is_complete == True :
           self.env.cr.execute("""update alldo_ipla_iot_outsuborder set state='4' where id=%d""" % self.suborder_id.id)
           self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '委外加工完工入庫輸入完成！'
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