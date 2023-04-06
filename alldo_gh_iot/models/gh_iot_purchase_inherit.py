# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotpurchaseinherit(models.Model):
    _inherit = "purchase.order"

    po_wkorder_ids = fields.Many2many('alldo_gh_iot.po_wkorder','po_wkorder_purchase_order_rel','po_id','powk_id',string="訂單")
    change_ids = fields.Boolean(string="Change IDS",default=False)
    change_prodloc = fields.Boolean(string="進貨入成品倉",default=False)
    stockin_state = fields.Selection([('1','未收貨'),('2','已收貨'),('3','已結案')],string="收貨狀態",default='1')
    active = fields.Boolean(string="ACTIVE",default=True)

    @api.onchange('po_wkorder_ids')
    def onchangepowkids(self):
        self.change_ids=True


    def write(self, vals):

        res = super(ghiotpurchaseinherit, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select genpowkorderdata(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res

    def run_check_purchase(self):
        self.env.cr.execute("""select genpurchasedata();""")
        self.env.cr.execute("""commit""")

    def run_purchase_archive(self):
        self.env.cr.execute("""update purchase_order set active=FALSE where id=%d""" % self.id)
        self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='採購單 收貨已結案 歸檔完成'
        return {
            'name':'Success',
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'sh.message.wizard',
            'views':[(view.id,'form')],
            'view_id':view.id,
            'target':'new',
            'context':context,
            }





