# -*- coding: utf-8 -*-
# Author : Peter Wu

import json
from lxml import etree
from odoo import models,fields,api
from odoo.exceptions import UserError

class stockmovelineInherit(models.Model):
    _inherit = "stock.move.line"

    @api.depends('reference')
    def _get_origin1(self):
        for rec in self:
            if rec.reference:
                myrec = self.env['stock.picking'].search([('name','=',rec.reference)])
                rec.origin1 = myrec.origin
            else:
                rec.origin1 = ' '

    @api.depends('reference')
    def _get_partner(self):
        for rec in self:
            if rec.reference:
                myrec = self.env['stock.picking'].search([('name', '=', rec.reference)])
                rec.mv_partner_id = myrec.partner_id



    origin1 = fields.Char(string="來源說明",store=True,compute=_get_origin1)
    mv_partner_id = fields.Many2one('res.partner',string="業務夥伴",compute=_get_partner)

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False, context=None):
        if context is None:
            context = {}
        res = super(stockmovelineInherit, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                                                  submenu=submenu)

        doc = etree.XML(res['arch'])
        if view_type == 'form':
            for node1 in doc.xpath("//field[@name='origin']"):
                modifiers = json.loads(node1.get("modifiers"))
                modifiers['readonly'] = False
                node1.set("modifiers", json.dumps(modifiers))

        res['arch'] = etree.tostring(doc, encoding='unicode')
        return res

    # @api.onchange('origin1')
    # def onchangeorigin1(self):
    #     for rec in self:
    #         myorigin = rec.origin
    #         if myorigin:
    #            rec.origin = myorigin + rec.origin1
    #         else:
    #            rec.origin = rec.origin1
