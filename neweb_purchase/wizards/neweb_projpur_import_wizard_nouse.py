# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebprojpurimportwizard(models.TransientModel):
    _name = "neweb.projimport_wizard"

    proj_no = fields.Many2one('neweb.project',string="專案編號",domain=[('purchase_yn','=',False)])
    proj_saleitem = fields.Many2many('neweb.projsaleitem',string="專案清單")

    @api.onchange('proj_no')
    def onclientchange(self):
        ids = []
        myrec = self.env['neweb.projsaleitem'].search([('saleitem_id', '=', self.proj_no.id),('purok','=',False)])
        for rec in myrec:
            ids.append(rec.id)
        res = {}
        res['domain'] = {'proj_saleitem': [('id', 'in', ids)]}
        return res


    def genprojpur_data(self):
        if not self.proj_no:
            raise UserError("未選取專案編號")
        if not self.proj_saleitem :
            raise UserError("未選取專案品項")
        mypurid = self.env.context.get('pur_op_id')
        for rec in self.proj_saleitem:
            self.env.cr.execute("select genprojline(%s,%s)" % (rec.id, mypurid))
        self.env.cr.execute("""select genpidno(%d)""" % mypurid)


    def genprojpur_all(self):
        if not self.proj_no:
            raise UserError("未選取專案編號")
        mypurid = self.env.context.get('pur_op_id')
        myrec = self.env['neweb.projsaleitem'].search([('saleitem_id','=',self.proj_no.id),('purok','=',False)])
        for rec in myrec:
            self.env.cr.execute("select genprojline(%s,%s)" % (rec.id, mypurid))
        self.env.cr.execute("""select genpidno(%d)""" % mypurid)
