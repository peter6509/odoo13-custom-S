# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotstockmovemixsearch(models.TransientModel):
    _name ="alldo_gh_iot.stockmove_mixsearch"

    start_date = fields.Date(string="啟始日期")
    end_date = fields.Date(string="截止日前")
    partner_id = fields.Many2one('res.partner',string="客戶")
    product_id = fields.Many2one('product.product',string="產品料號")


    def run_stockmove_mixsearch(self):
        if not self.partner_id and not self.product_id:
            raise UserError("客戶 & 料號不能全數空值！")
        if not self.partner_id:
            mypartnerid = 0
        else:
            mypartnerid = self.partner_id.id
        if not self.product_id:
            myprodid = 0
        else:
            myprodid = self.product_id.id

        if not self.start_date:
            self.env.cr.execute("""select genstockmovemixsearch1(%d,%d)""" % (mypartnerid,myprodid))
            self.env.cr.execute("""commit""")
        else:
            self.env.cr.execute("""select genstockmovemixsearch('%s','%s',%d,%d)""" % (self.start_date,self.end_date,mypartnerid,myprodid))
            self.env.cr.execute("""commit""")


        myviewid = self.env.ref('alldo_gh_iot.ghiot_stockmove_tree')
        return {
            'view_name': 'ghiot_stockmove_tree',
            'name': (u'產品出貨複合數據'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_gh_iot.stock_move_list',
            'view_id': myviewid.id,
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'list'}
