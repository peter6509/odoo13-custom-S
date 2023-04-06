# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api, _
from odoo.exceptions import UserError


class newebrepairinherit(models.Model):
    _inherit = "neweb_repair.repair"


    # @api.model
    # def create(self, vals):
    #     if 'repair_type' in vals and not vals['repair_type']:
    x_wkf_state = fields.Selection([('43','草稿'),('44','待料中'),('45','待工程師處理'),('46','待主管簽核'),('47','完成'),('48','結案'),('49','作廢')],string="x_wkf_state")
    completed_care_call = fields.Boolean(string="完成 care call",default=False)
    ae_dept = fields.Char(string="工程師部門")


    def write(self, vals):

        res = super(newebrepairinherit,self).write(vals)
        # for rec in self:
        #     if rec.state == 'repair_done':
        #         self.env.cr.execute("""select checkrepairparts(%d)""" % rec.id)
        #         myres = self.env.cr.fetchone()
        #         if not myres[0] :
        #             raise UserError("有領料零件料號未輸入,無法結案,請確認")
        return res