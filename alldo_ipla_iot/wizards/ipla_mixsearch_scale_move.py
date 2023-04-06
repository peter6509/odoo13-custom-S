# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iplamixsearchscalemove(models.TransientModel):
    _name = "alldo_ipla_iot.mixsearch_scalemove"

    start_date = fields.Date(string="啟始時間",required=True)
    end_date = fields.Date(string="截止時間",required=True)
    scale_type = fields.Selection([('1', '熔爐投料'), ('2', '回收料入庫')], string="類別")
    product_no = fields.Many2one('product.product',string="料號")

    @api.onchange('start_date')
    def onchangestartdate(self):
        self.env.cr.execute("""select getmaterialno()""")
        myrec = self.env.cr.fetchall()
        ids = []
        for rec in myrec:
            ids.append(rec[0])
        return {'domain': {'product_no': [('id', 'in', ids)]}}

    def run_mixsearch_scalemove(self):
        if not self.product_no:
            myprodid = 0
        else:
            myprodid = self.product_no.id
        if not self.scale_type:
            myscaletype='0'
        else:
            myscaletype=self.scale_type
        self.env.cr.execute("""select genscalemovemixsearch('%s','%s',%d,'%s')""" % (self.start_date,self.end_date,myprodid,myscaletype))
        self.env.cr.execute("""commit""")

        myviewid = self.env.ref('alldo_ipla_iot.ipla_mixsearch_scalemovelist_tree')
        return {
            'view_name': 'ipla_mixsearch_scalemove',
            'name': (u'磅秤投料入庫複合查詢'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_ipla_iot.mixsearch_scalemovelist',
            'view_id': myviewid.id,
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'current'}

