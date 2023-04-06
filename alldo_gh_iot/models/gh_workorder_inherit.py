# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghworkorderinherit(models.Model):
    _inherit = "alldo_gh_iot.workorder"

    @api.depends('product_no')
    def _get_pono2(self):
        myrec = self.env['alldo_gh_iot.po_wkorder'].search([('product_no', '=', self.product_no.id)])
        ids = []
        for rec in myrec:
            print("po_no2:%d" % rec.id)
            ids.append(rec.id)
        if myrec:
            return {'domain': {'po_no2': [('id', 'in', ids)]}}
        else:
            return

    @api.depends('cus_name')
    def _get_engmode(self):
        for rec in self:
            if rec.cus_name.id == 35: #龍澤
                rec.is_engmode=True
            else:
                rec.is_engmode=False

    po_no2 = fields.Many2many('alldo_gh_iot.po_wkorder','powkorder_iotwkorder_rel','wk_id','po_id',string="訂單",default=_get_pono2)
    is_proofing = fields.Boolean(string="打樣",default=False)
    proofing_num = fields.Integer(string="打樣數量")
    eng_mode = fields.Selection([('1','粗車'),('2','精車'),('3','銑床')],string="工序模式")
    is_engmode = fields.Boolean(string="判斷是否為龍澤工單",compute=_get_engmode)

    @api.onchange('product_no')
    def onchangeprodno(self):
        myrec = self.env['alldo_gh_iot.po_wkorder'].search([('product_no','=',self.product_no.id)])
        ids=[]
        for rec in myrec:
            print("po_no2:%d" % rec.id)
            ids.append(rec.id)
        if myrec:
            return {'domain': {'po_no2': [('id', 'in', ids)]}}
        else:
            return

    def write(self, vals):

        res = super(ghworkorderinherit, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select genwkorderpodata(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res

    def run_geniotseq(self):
        self.env.cr.execute("""select geniotseq()""")
        self.env.cr.execute("""commit""")
