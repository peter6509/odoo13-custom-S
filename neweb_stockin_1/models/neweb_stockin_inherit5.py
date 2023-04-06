# -*- coding: utf-8 -*-
# Author : Peter Wu

import json
from lxml import etree
from odoo import models,fields,api
from odoo.exceptions import UserError

class ProductTemplateInherit(models.Model):
    _inherit = "product.template"

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False, context=None):
        if context is None:
            context = {}
        res = super(ProductTemplateInherit, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                                                  submenu=submenu)

        doc = etree.XML(res['arch'])
        if view_type == 'form':

            for node1 in doc.xpath("//field[@name='default_code']"):
                modifiers = json.loads(node1.get("modifiers"))
                modifiers['required'] = False
                node1.set("modifiers", json.dumps(modifiers))

        res['arch'] = etree.tostring(doc, encoding='unicode')
        return res
