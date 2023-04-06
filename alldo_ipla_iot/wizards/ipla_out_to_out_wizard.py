
# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class outtooutwizard(models.TransientModel):
    _name = "aldo_ipla_iot.out_to_out_wizard"
    _description = "委外->委外加工物料移轉"

    outsourcing_no = fields.Many2one('alldo_ipla_iot.outsuborder',string="Form 委外工單")
    sup_no = fields.Many2one('res.partner',string="From 委外商")
    outsourcing_no1 = fields.Many2one('alldo_ipla_iot.outsuborder',string="To 委外工單")
    sup_no1 = fields.Many2one('res.partner', string="To 委外商")
    product_no = fields.Many2one('product.product',string="產品料號",required=True)
    prod_num = fields.Float(digits=(10,2),string="GOOD 數量",default=0.0)
    ng_num = fields.Float(digits=(10,2),string="NG 數量",default=0.0)
    move_owner = fields.Many2one('res.users',string="入帳人員",default=lambda self:self.env.uid)
    t_plastic_frame1 = fields.Integer(string="移轉塑膠框數", default=0)
    t_plastic_frame2 = fields.Integer(string="移轉蝴蝶籠數", default=0)
    t_pallet = fields.Integer(string="移轉棧板數", default=0)

    @api.onchange('product_no')
    def onchangeproductno(self):
        myrec = self.env['alldo_ipla_iot.outsuborder'].search([('product_no','=',self.product_no.id),('state','not in',['3','4'])])
        ids=[]
        for rec in myrec:
            ids.append(rec.id)
        return {'domain': {'outsourcing_no': [('id', 'in', ids)]}}

    @api.onchange('outsourcing_no')
    def onchangeoutsourcing(self):
        myoutrec = self.env['alldo_ipla_iot.outsuborder'].search([('id','=',self.outsourcing_no.id)])
        self.sup_no = myoutrec.cus_name.id
        # self.prod_num = myoutrec.blank_num - myoutrec.order_num
        myoutrec1 = self.env['alldo_ipla_iot.outsuborder'].search([('mrp_prod_id','=',myoutrec.mrp_prod_id.id)])
        ids=[]
        for rec in myoutrec1:
            if rec.id != myoutrec.id:
                ids.append(rec.id)
        return {'domain': {'outsourcing_no1': [('id', 'in', ids)]}}

    @api.onchange('outsourcing_no1')
    def onchangeoutsourcing1(self):
        myoutrec1 = self.env['alldo_ipla_iot.outsuborder'].search([('id', '=', self.outsourcing_no1.id)])
        self.sup_no1 = myoutrec1.cus_name.id
        # self.product_no = myoutrec1.product_no.id
        # return {'domain': {'product_no': [('id', '=', myoutrec1.product_no.id)]}}


    def run_outtooutmove(self):
        print(self.product_no.id)
        print(self.product_no.default_code)
        if not self.outsourcing_no and not self.sup_no:
            raise UserError("委外單號 or 委外廠商 不得同時空值！")
        if not self.outsourcing_no1 and not self.sup_no1:
            raise UserError("委外單號 or 委外廠商 不得同時空值！")
        # if self.prod_num==0 and self.ng_num==0 :
        #     raise UserError("未輸入移轉數量！")
        if self.outsourcing_no and self.outsourcing_no1 :
            if self.prod_num > 0 or self. ng_num > 0 :
                self.env.cr.execute("""select genoutsourcingin(%d,%d,%d,%d,%d)""" % (self.outsourcing_no.id,self.outsourcing_no1.id,self.move_owner.id,self.prod_num,self.ng_num))
                self.env.cr.execute("""commit""")
                self.env.cr.execute("""select geninpartner(%d,%d,%d,%d,%d,%d,'%s')""" % (self.sup_no.id,self.sup_no1.id, self.product_no.id, self.move_owner.id, self.prod_num, self.ng_num, ' '))
                self.env.cr.execute("commit")
                self.env.cr.execute("""select genoutsourcingout(%d,%d,%d,%d)""" % (self.outsourcing_no.id,self.outsourcing_no1.id, self.move_owner.id, self.prod_num))
                self.env.cr.execute("commit")
                self.env.cr.execute("""select genoutpartner(%d,%d,%d,%d,%d,'%s','%s','%s')""" % (self.sup_no.id ,self.sup_no1.id, self.product_no.id, self.move_owner.id, self.prod_num, ' ', ' ', fields.datetime.today()))
                self.env.cr.execute("commit")
        else:
            if self.prod_num > 0 or self.ng_num > 0:
                self.env.cr.execute("""select geninpartner(%d,%d,%d,%d,%d,%d,'%s')""" % (self.sup_no.id, self.sup_no1.id, self.product_no.id, self.move_owner.id, self.prod_num, self.ng_num, ' '))
                self.env.cr.execute("commit")
                self.env.cr.execute("""select genoutpartner(%d,%d,%d,%d,%d,'%s','%s','%s')""" % (self.sup_no.id, self.sup_no1.id, self.product_no.id, self.move_owner.id, self.prod_num, ' ', ' ',fields.datetime.today()))
                self.env.cr.execute("commit")

        ## 註記移轉 籠框/蝴蝶欄/棧板 數量
        if self.t_plastic_frame1 > 0 or self.t_plastic_frame2 > 0 or self.t_pallet > 0:
            self.env.cr.execute("""select updatesuborderframe2(%d,%d,%d,%d,%d)""" % (self.outsourcing_no.id,self.outsourcing_no1.id, self.t_plastic_frame1, self.t_plastic_frame2, self.t_pallet))
            self.env.cr.execute("""commit""")


        mypickingrec = self.env['stock.picking'].search([])
        mysupplocid = self.sup_no.blank_stock_supplier.id  # 委外商倉庫 from
        mysupplocid1 = self.sup_no1.blank_stock_supplier.id  # 委外商倉庫1 to
        self.env.cr.execute("""select getproduom(%d)""" % self.product_no.id)
        myuomid = self.env.cr.fetchone()[0]
        ## 報廢倉位置(NG)
        myscraplocid = self.env['alldo_ipla_iot.company_stockloc'].search([])[0].scrap_loc.id
        ## GOOD 加工完工回廠
        if self.prod_num > 0 :
            myres = mypickingrec.create(
                {'picking_type_id': 5, 'location_id': mysupplocid, 'location_dest_id': mysupplocid1,
                 'move_type': 'direct',
                 'user_id': self.move_owner.id, 'report_memo': '委外物料移動',
                 'move_line_ids': [
                     (0, 0, {'product_id': self.product_no.id, 'company_id': 1, 'location_id': mysupplocid,
                             'location_dest_id': mysupplocid1, 'product_uom_id': myuomid,
                             'qty_done': self.prod_num})]})
            myres.action_confirm()
            self.env.cr.commit()
            myres.action_done()
            self.env.cr.commit()

        if self.ng_num > 0 :
            ## NG 加工回廠報廢倉
            myres1 = mypickingrec.create(
                {'picking_type_id': 5, 'location_id': mysupplocid, 'location_dest_id': myscraplocid,
                 'move_type': 'direct',
                 'user_id': self.move_owner.id, 'report_memo': '委外NG',
                 'move_line_ids': [
                     (0, 0, {'product_id': self.product_no.id, 'company_id': 1, 'location_id': mysupplocid,
                             'location_dest_id': myscraplocid, 'product_uom_id': myuomid,
                             'qty_done': self.ng_num})]})
            myres1.action_confirm()
            self.env.cr.commit()
            myres1.action_done()
            self.env.cr.commit()

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '委外加工廠商直接移轉記錄輸入完成！'
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

