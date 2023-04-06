# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class newebrespartnerinherit(models.Model):
    _inherit = ["res.partner"]

    @api.model
    def create(self, vals):
        if 'sno' in vals and vals['sno']:
            mysno = vals['sno']
            if not mysno.isdigit():
                raise UserError(("統編必須是數字"))
            myrec = self.env['res.partner'].search([('sno', '=', mysno)])
            if myrec:
                raise UserError(("統編 " + '%s' + " 複建立了,請確認") % mysno)
        # if 'name' in vals and vals['name']:
        #     myname = vals['name']
        #     myrec = self.env['res.partner'].search(
        #         [('name', '=', myname), ('company_type', '=', 'company'), ('parent_id', '=', False)])
        #     if myrec:
        #         raise UserError(("公司名稱 " + '%s' + " 重複建立了,請確認") % myname)
        if 'comp_sname' in vals and vals['comp_sname']:
            myname = vals['comp_sname']
            myrec = self.env['res.partner'].search(
                [('comp_sname', '=', myname), ('company_type', '=', 'company'), ('parent_id', '=', False)])
            if myrec:
                raise UserError(("公司簡稱 " + '%s' + " 重複建立了,請確認") % myname)
        vals['lang'] = 'zh_TW'
        res = super(newebrespartnerinherit, self).create(vals)
        if 'proj_saleid' in vals and vals['proj_saleid']:
            self.env.cr.execute("select projsaleid(%d)" % res.id)
        return res


    def write(self, vals):
        vals['lang'] = 'zh_TW'
        if 'proj_saleid' in vals and vals['proj_saleid']:
            self.env.cr.execute("select projsaleid(%d)" % self.id)
        return super(newebrespartnerinherit, self).write(vals)
