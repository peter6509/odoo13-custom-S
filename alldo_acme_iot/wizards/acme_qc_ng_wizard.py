# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmeqcngwizard(models.TransientModel):
    _name = "alldo_acme_iot.qcng_wizard"

    product_id = fields.Many2one('product.product',string="產品料號",required=True)
    ng_type = fields.Selection([('1','廠內工單'),('2','委外加工單')],string="類別",default='2')
    wkorder_id = fields.Many2one('alldo_acme_iot.workorder',string="工單號碼")
    suborder_id = fields.Many2one('alldo_acme_iot.outsuborder',string="委外加工單")
    in_owner = fields.Many2one('res.users',string="建單人",default=lambda self:self.env.uid)
    ng_num = fields.Float(digits=(5,0),string="追加NG數量",default=0)
    ng_memo = fields.Char(string="NG說明")

    @api.onchange('product_id')
    def onchangeproductid(self):
        return {'domain': {'wkorder_id': [('product_no', '=', self.product_id.id),('active','=',True)],'suborder_id':[('product_no','=',self.product_id.id),('active','=',True)]}}


    def run_qcngmarkup(self):
        if not self.wkorder_id and self.ng_type=='1':
            raise UserError("未輸入工單號碼！")
        if not self.suborder_id and self.ng_type=='2':
            raise UserError("未輸入委外加工單號碼！")

        if self.ng_type=='1':
            mynoid = self.wkorder_id.id
        else:
            mynoid = self.suborder_id.id
        if not self.ng_memo:
            mymemo = ' '
        else:
            mymemo = self.ng_memo
        self.env.cr.execute("""select genqcngnum('%s',%d,'%s','%s',%d)""" % (self.ng_type,mynoid,self.ng_num,mymemo,self.in_owner.id))
        self.env.cr.execute("""commit""")
        ## 產線線邊倉
        myuncompletelocid = self.env['alldo_acme_iot.company_stockloc'].search([])[0].uncomplete_loc.id
        ## 毛胚倉
        myblanklocid = self.env['alldo_acme_iot.company_stockloc'].search([])[0].blank_loc.id
        ## 產線成品倉
        myprodlocid = self.env['alldo_acme_iot.company_stockloc'].search([])[0].prod_loc.id
        if self.ng_type=='1':
            if self.ng_num > 0:
                myrec = self.env['stock.picking'].search([])
                myres = myrec.create(
                    {'picking_type_id': 5, 'location_id': myblanklocid, 'location_dest_id': myuncompletelocid ,
                     'move_type': 'direct',
                     'user_id': self.env.uid, 'origin': self.ng_memo,
                     'move_line_ids': [
                         (0, 0, {'product_id': self.product_id.id, 'company_id': 1, 'location_id': myblanklocid,
                                 'location_dest_id': myuncompletelocid,
                                 'product_uom_id': self.product_id.product_tmpl_id.uom_id.id,
                                 'qty_done': self.ng_num})]})

                myres.action_confirm()
                self.env.cr.commit()
                myres.action_done()
                self.env.cr.commit()
        else:
            self.env.cr.execute("""select gensubngratio(%d)""" % self.suborder_id.id)
            self.env.cr.execute("""commit""")
            if self.ng_num > 0:
                myrec = self.env['stock.picking'].search([])
                myres = myrec.create(
                    {'picking_type_id': 5, 'location_id':myprodlocid, 'location_dest_id': myuncompletelocid,
                     'move_type': 'direct',
                     'user_id': self.env.uid, 'origin': 'QC NG追加',
                     'move_line_ids': [
                         (0, 0, {'product_id': self.product_id.id, 'company_id': 1, 'location_id': myprodlocid,
                                 'location_dest_id': myuncompletelocid,
                                 'product_uom_id': self.product_id.product_tmpl_id.uom_id.id,
                                 'qty_done': self.ng_num})]})

                myres.action_confirm()
                self.env.cr.commit()
                myres.action_done()
                self.env.cr.commit()

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = 'QC NG追加輸入完成！'
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