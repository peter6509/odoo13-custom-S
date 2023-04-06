# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models ,fields , api, _
import json,logging,re
from odoo.exceptions import UserError
from lxml import etree


class saleinherit(models.Model):
    _inherit = "sale.order"

    call_service_response1 = fields.Many2one('neweb_base.sla', domain=[('disabled', '=', False)], string="叫修時效")

    @api.onchange('name')
    def onchangesaleorder(self):
        res = {}
        if self.env.user.has_group('neweb_project.neweb_sa40_user') :
            res['domain'] = {'partner_id': ['|','|','|','|',('salesp1', '=', self.env.uid),('salesp2', '=', self.env.uid),('salesp3', '=', self.env.uid),('salesp4', '=', self.env.uid),('salesp5', '=', self.env.uid)]}
        else:
            res['domain'] = {'partner_id':[(1,'=',1)]}
        return res


    # @api.model
    # def fields_view_get(self, view_id=None, view_type='tree', toolbar=False, submenu=False, context=None):
    #     if context is None:
    #         context = {}
    #     res = super(saleinherit, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
    #                                                               submenu=submenu)
    #
    #     doc = etree.XML(res['arch'])
    #
    #     if view_type == 'tree':
    #         for node in doc.xpath("//field[@name='amount_total']"):
    #             modifiers = json.loads(node.get("modifiers"))
    #             node.addnext(etree.Element('field', {'name': 'sitem_amounttot', 'string': '總計', 'nolabel': '0',}))
    #             node.set("modifiers", json.dumps(modifiers))
    #         for node1 in doc.xpath("//field[@name='amount_total']"):
    #             modifiers = json.loads(node1.get("modifiers"))
    #             modifiers['invisible'] = True
    #             node1.set("modifiers", json.dumps(modifiers))
    #         res['arch'] = etree.tostring(doc)
    #     return res