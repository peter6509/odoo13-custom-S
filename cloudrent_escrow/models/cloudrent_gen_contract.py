# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class CloudRentGenContract(models.Model):
    _name = "cloudrent.gen_contract"
    _description = "合約範本自動產生"

    # 每 5 分鐘run 一次
    def contract_auto_run(self):
        myrec = self.env['crm.lead'].sudo().search([('gen_new_contract','=',True)])
        for rec in myrec:
            rec.sudo().run_docx_replace()
            rec.write({'gen_new_contract': False})

