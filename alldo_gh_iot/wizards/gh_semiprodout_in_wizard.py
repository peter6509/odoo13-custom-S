# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class ghsemiprodoutsourcinginwizard(models.TransientModel):
    _name = "alldo_gh_iot.semiprodoutsourcing_in"
    _description = "半成品委外加工完工回廠"


    suborder_id = fields.Many2one('alldo_gh_iot.outsuborder',string="委外加工單")
    partner_id = fields.Many2one('res.partner', string="委外加工廠商")
    product_id = fields.Many2one('product.product',string="原始料號",required=True)
    product_id1 = fields.Many2one('product.product', string="變更料號", required=True)
    in_good_num = fields.Integer(string="完工良品數量",default=0)
    in_ng_num = fields.Integer(string="完工NG數量",default=0)
    # loss_num = fields.Integer(string="短少數量",default=0)
    in_desc = fields.Char(string="說明",default=' ')
    in_owner = fields.Many2one('res.users',string="建單人",default=lambda self:self.env.uid)
    partner_semiprod_onhand1 = fields.Float(string="委外半成品倉數量", default=0.00)
    wh_semiprod_onhand1 = fields.Float(string="公司半成品倉數量")
    # is_complete_stockin = fields.Boolean(string="是否工單完工入庫？",default=False)
    product_no = fields.Many2one('product.product', string="工單料號")
    product_no1 = fields.Many2one('product.product', string="轉變料號")
    # mo_no = fields.Many2one('alldo_gh_iot.workorder', string="入庫工單")
    prod_num = fields.Float(digits=(10, 2), string="良品入庫數", default=0.00)
    ng_num = fields.Float(digits=(10, 2), string="NG數量", default=0.00)
    # loss_num1 = fields.Float(digits=(10, 2), string="短少數量", default=0.00)
    # is_close = fields.Boolean(string="是否已完工結案？", default=False)
    in_loc = fields.Selection([('1','WH/總庫(成品倉)'),('2','WH/毛胚倉'),('3','WH/半成品倉')],string="入庫倉別",default='3')

    @api.onchange('product_id1')
    def onclientchangeprodno1(self):
        if self.product_id != self.product_id1 :
            self.in_loc='3'
        else:
            self.in_loc='3'

    @api.onchange('product_id')
    def onclientchangeprodno(self):
        self.product_id1 = self.product_id.id

    @api.onchange('in_good_num')
    def onclientchangegoodnum(self):
        self.prod_num = self.in_good_num

    @api.onchange('in_ng_num')
    def onclientchangengnum(self):
        self.ng_num = self.in_ng_num

    @api.onchange('partner_id', 'product_id')
    def onchangeclient1(self):
        self.env.cr.execute("""select getpartnersemiprodonhand(%d,%d)""" % (self.partner_id.semi_loc.id, self.product_id.id))
        self.partner_semiprod_onhand1 = self.env.cr.fetchone()[0]


    @api.onchange('product_id1')
    def onchangeclient2(self):
        self.env.cr.execute("""select getwhsemiprodonhand(%d)""" % self.product_id1.id)
        self.wh_semiprod_onhand1 = self.env.cr.fetchone()[0]

    @api.depends('partner_prod_onhand1', 'in_good_num','in_ng_num')
    def _get_partner_prodonhand2(self):
        if self.partner_prod_onhand1 != False:
            self.partner_prod_onhand2 = self.partner_prod_onhand1 - self.in_good_num - self.in_ng_num
        else:
            self.partner_prod_onhand2 = 0.00

    @api.depends('wh_prod_onhand1', 'in_good_num')
    def _get_wh_prodonhand2(self):

        self.wh_prod_onhand2 = self.wh_prod_onhand1 + self.in_good_num

    def run_prodout_in(self):
        mymoveno = ' '
        mymoveid = 0
        if not self.product_id and not self.suborder_id:
            raise UserError("委外單號 or 委外廠商 不得同時無值！")
        if self.in_good_num==0 and self.in_ng_num==0 :
            raise UserError("未輸入完工入庫數量！")
        if not self.partner_id:
            self.env.cr.execute("""select genoutsourcingin(%d,%d,%d,%d,%d)""" % (self.suborder_id.id,self.in_owner.id,self.in_good_num,self.in_ng_num,self.loss_num))
            self.env.cr.execute("commit")
        elif not self.suborder_id:
            myrec = self.env['stock.picking'].search([])
            if self.in_good_num > 0 or self.in_ng_num > 0:
                # mysupplocid = self.partner_id.property_stock_supplier.id  # 委外商倉庫
                mysupplocid = self.partner_id.semi_loc.id  # 委外商半成品倉庫
                mycomploc = self.env['alldo_gh_iot.company_stockloc'].search([])
                myprodlocid = mycomploc.prod_loc.id  # 公司產品庫存位置
                mysemiprodloc = mycomploc.semi_prod_loc.id  # 公司半成品庫存位置
                myblanklocid = mycomploc.blank_loc.id  # 公司毛胚庫存位置
                myscraplocid = mycomploc.scrap_loc.id  # 公司NG報廢位置
                mytranslocid = mycomploc.trans_loc.id  # 公司內部轉換位置
                mymovenum = self.in_good_num + self.in_ng_num
                if self.product_id != self.product_id1:
                    ## 有發生換料事件 委外商倉庫位置 => 內部轉換位置 將原始料轉移到 internal trans
                    myres = myrec.create(
                        {'picking_type_id': 5, 'location_id': mysupplocid, 'location_dest_id': mytranslocid, 'move_type': 'direct',
                         'user_id': self.in_owner.id, 'origin': self.in_desc, 'partner_id': self.partner_id.id,
                         'move_line_ids': [
                             (0, 0, {'product_id': self.product_id.id, 'company_id': 1, 'location_id': mysupplocid,
                                     'location_dest_id': mytranslocid, 'product_uom_id': 1, 'qty_done': mymovenum})]})
                    myres.action_confirm()
                    self.env.cr.commit()
                    myres.action_done()
                    self.env.cr.commit()
                    if self.in_good_num > 0:
                        ## 有發生換料事件 內部轉換位置 => 公司毛胚倉 將轉換料號 轉移到毛胚倉
                        if self.in_loc == '1': # 成品倉
                            myres1 = myrec.create(
                                {'picking_type_id': 5, 'location_id': mytranslocid, 'location_dest_id': myprodlocid,
                                 'move_type': 'direct',
                                 'user_id': self.in_owner.id, 'origin': self.in_desc, 'partner_id': self.partner_id.id,
                                 'move_line_ids': [
                                     (0, 0,
                                      {'product_id': self.product_id1.id, 'company_id': 1, 'location_id': mytranslocid,
                                       'location_dest_id': myprodlocid, 'product_uom_id': 1,
                                       'qty_done': self.in_good_num})]})
                        elif self.in_loc == '2':    # 毛胚倉
                            myres1 = myrec.create(
                                {'picking_type_id': 5, 'location_id': mytranslocid, 'location_dest_id': myblanklocid, 'move_type': 'direct',
                                 'user_id': self.in_owner.id, 'origin': self.in_desc, 'partner_id': self.partner_id.id,
                                 'move_line_ids': [
                                     (0, 0, {'product_id': self.product_id1.id, 'company_id': 1, 'location_id': mytranslocid,
                                             'location_dest_id': myblanklocid, 'product_uom_id': 1,
                                             'qty_done': self.in_good_num})]})
                        elif self.in_loc == '3':    # 半成品倉
                            myres1 = myrec.create(
                                {'picking_type_id': 5, 'location_id': mytranslocid, 'location_dest_id': mysemiprodloc, 'move_type': 'direct',
                                 'user_id': self.in_owner.id, 'origin': self.in_desc, 'partner_id': self.partner_id.id,
                                 'move_line_ids': [
                                     (0, 0, {'product_id': self.product_id1.id, 'company_id': 1, 'location_id': mytranslocid,
                                             'location_dest_id': mysemiprodloc, 'product_uom_id': 1,
                                             'qty_done': self.in_good_num})]})

                        myres1.action_confirm()
                        self.env.cr.commit()
                        myres1.action_done()
                        self.env.cr.commit()
                        mymoveno = myres1.name
                        mymoveid = myres1.id
                    if self.in_ng_num > 0 :
                        ## NG件 從 內部轉換位置 => 公司NG倉

                        myres2 = myrec.create(
                            {'picking_type_id': 5, 'location_id': mytranslocid, 'location_dest_id': myscraplocid, 'move_type': 'direct',
                             'user_id': self.in_owner.id, 'origin': self.in_desc, 'partner_id': self.partner_id.id,
                             'move_line_ids': [
                                 (0, 0, {'product_id': self.product_id1.id, 'company_id': 1, 'location_id': mytranslocid,
                                         'location_dest_id': myscraplocid, 'product_uom_id': 1,
                                         'qty_done': self.in_ng_num})]})

                        myres2.action_confirm()
                        self.env.cr.commit()
                        myres2.action_done()
                        self.env.cr.commit()

                else:
                    if self.in_good_num > 0 :
                        ## GOOD 數量 由 委外商位置 => 公司毛胚倉
                        if self.in_loc == '1': # 成品倉
                            myres1 = myrec.create(
                                {'picking_type_id': 5, 'location_id': mysupplocid, 'location_dest_id': myprodlocid,
                                 'move_type': 'direct',
                                 'user_id': self.in_owner.id, 'origin': self.in_desc, 'partner_id': self.partner_id.id,
                                 'move_line_ids': [
                                     (0, 0,
                                      {'product_id': self.product_id1.id, 'company_id': 1, 'location_id': mysupplocid,
                                       'location_dest_id': myprodlocid, 'product_uom_id': 1,
                                       'qty_done': self.in_good_num})]})
                        elif self.in_loc == '2':      # 毛胚倉
                            myres1 = myrec.create(
                                {'picking_type_id': 5, 'location_id': mysupplocid, 'location_dest_id': myblanklocid, 'move_type': 'direct',
                                 'user_id': self.in_owner.id, 'origin': self.in_desc, 'partner_id': self.partner_id.id,
                                 'move_line_ids': [
                                     (0, 0, {'product_id': self.product_id1.id, 'company_id': 1, 'location_id': mysupplocid,
                                             'location_dest_id': myblanklocid, 'product_uom_id': 1,
                                             'qty_done': self.in_good_num})]})
                        elif self.in_loc == '3':      # 半成品倉
                            myres1 = myrec.create(
                                {'picking_type_id': 5, 'location_id': mysupplocid, 'location_dest_id': mysemiprodloc, 'move_type': 'direct',
                                 'user_id': self.in_owner.id, 'origin': self.in_desc, 'partner_id': self.partner_id.id,
                                 'move_line_ids': [
                                     (0, 0, {'product_id': self.product_id1.id, 'company_id': 1, 'location_id': mysupplocid,
                                             'location_dest_id': mysemiprodloc, 'product_uom_id': 1,
                                             'qty_done': self.in_good_num})]})

                        myres1.action_confirm()
                        self.env.cr.commit()
                        myres1.action_done()
                        self.env.cr.commit()
                        mymoveno = myres1.name
                        mymoveid = myres1.id
                    if self.in_ng_num > 0 :
                        ## NG 數量 由 委外商位置 => 公司NG倉

                        myres2 = myrec.create(
                            {'picking_type_id': 5, 'location_id': mysupplocid, 'location_dest_id': myscraplocid, 'move_type': 'direct',
                             'user_id': self.in_owner.id, 'origin': self.in_desc, 'partner_id': self.partner_id.id,
                             'move_line_ids': [
                                 (0, 0, {'product_id': self.product_id1.id, 'company_id': 1, 'location_id': mysupplocid,
                                         'location_dest_id': myscraplocid, 'product_uom_id': 1,
                                         'qty_done': self.in_ng_num})]})

                        myres2.action_confirm()
                        self.env.cr.commit()
                        myres2.action_done()
                        self.env.cr.commit()

                    # if self.loss_num > 0:
                    #     ## 毛胚短少數量 由 委外商位置 => 轉移位置
                    #
                    #     myres2 = myrec.create(
                    #         {'picking_type_id': 5, 'location_id': mysupplocid, 'location_dest_id': mytranslocid,
                    #          'move_type': 'direct',
                    #          'user_id': self.in_owner.id, 'origin': self.in_desc, 'partner_id': self.partner_id.id,
                    #          'move_line_ids': [
                    #              (0, 0,
                    #               {'product_id': self.product_id1.id, 'company_id': 1, 'location_id': mysupplocid,
                    #                'location_dest_id': mytranslocid, 'product_uom_id': 1,
                    #                'qty_done': self.loss_num})]})
                    #
                    #     myres2.action_confirm()
                    #     self.env.cr.commit()
                    #     myres2.action_done()
                    #     self.env.cr.commit()
                    #
                    # if self.is_complete_stockin == True :
                    #
                    #     self.env.cr.execute("""select updatemoprodin(%d,%d)""" % (self.mo_no.id, int(self.prod_num)))
                    #     self.env.cr.execute("""commit""")
                    #     ## 全委外工單產生質檢記錄
                    #     self.env.cr.execute("""select alloutsourcingstockin(%d,%s,%s,%s)""" % (self.mo_no.id,self.prod_num, self.ng_num, self.loss_num1))
                    #     self.env.cr.execute("""commit""")
                    #
                    # if self.is_close == True:
                    #     self.env.cr.execute("""select setallmoclose(%d)""" % self.mo_no.id)
                    #     self.env.cr.execute("""commit""")

            self.env.cr.execute("""select geninpartner(%d,%d,%d,%d,%d,'%s',%d,%d)""" % (self.partner_id.id,self.product_id1.id, self.in_owner.id, self.in_good_num, self.in_ng_num,self.in_desc,mymoveid,0))
            self.env.cr.execute("commit")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '產品委外加工完工入庫輸入完成！ 調撥單:%s' % mymoveno
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