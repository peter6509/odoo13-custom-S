# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class neweb_projectinherit6(models.Model):
    _inherit = "neweb.projcustom"

    @api.depends('cus_select', 'cus_address')
    def _get_cusaddr1(self):
        for rec in self:
            if rec.cus_select:
                myadd = rec.cus_select.name.replace('\n', '\\n').replace('\r', '') + ' ' + rec.cus_address.replace('\n','\\n').replace('\r', '')
            else:
                myadd = rec.cus_address.replace('\n', '\\n').replace('\r', '')
            rec.update({'cus_address1': myadd})

    cus_select = fields.Many2one('res.partner',string="聯絡資訊",domain=lambda self:['|', ('parent_id', '=', self.cus_id.cus_name.id),('parent_id', '=', self.cus_id.main_cus_name.id)])
    cus_address1 = fields.Char(string="專案客戶地址-印表",default=_get_cusaddr1)




    @api.onchange('cus_type')
    def onchangecusselect1(self):
        res = {}
        res['domain'] = {'cus_select': ['|', ('parent_id', '=', self.cus_id.cus_name.id),('parent_id', '=', self.cus_id.main_cus_name.id)]}
        return res

    @api.onchange('cus_select')
    def onchangecusselect2(self):
        myrec = self.env['res.partner'].search([('id','=',self.cus_select.id)])
        self.cus_address = myrec.street
        self.cus_phone = myrec.phone
        self.cus_fax = myrec.fax
        # self.cus_memo = myrec.comment