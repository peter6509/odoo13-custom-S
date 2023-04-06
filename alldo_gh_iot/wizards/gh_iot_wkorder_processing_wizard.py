# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class wkorderprocessingwizard(models.TransientModel):
    _name = "alldo_gh_iot.wk_processing_wizard"

    product_no = fields.Many2one('product.product',string="產品",required=True)
    mo_no = fields.Many2one('alldo_gh_iot.workorder',string="工單號碼",required=True)

    @api.onchange('product_no')
    def onchangeprodno(self):
        myrec = self.env['alldo_gh_iot.workorder'].search([('product_no','=',self.product_no.id),('state','!=','4')])
        myrec.sorted(key=lambda r: r.name,reverse=True)
        ids = []
        if not myrec:
            return {'domain': {'mo_no': [(1, '=', 1)]}}
        else:
            for rec in myrec:
                ids.append(rec.id)
            return {'domain': {'mo_no': [('id', 'in', ids)]}}

    def run_genwkprocessing(self):
        self.env.cr.execute("""select genwkorderprocessing(%d)""" % self.mo_no.id)
        self.env.cr.execute("""commit""")

        myrec = self.env['alldo_gh_iot.processing_view'].search([])
        myid = myrec[0].id
        myviewid = self.env.ref('alldo_gh_iot.ghiot_processing_view_form')
        return {'view_name': 'wkorder_processing',
                'name': (u'wkordr processing Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_gh_iot.processing_view',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'target': 'self',
                'view_id': myviewid.id,
                # 'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }