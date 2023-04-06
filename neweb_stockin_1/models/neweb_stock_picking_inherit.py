# -*- coding: utf-8 -*-
# Author : Peter Wu

import json
from odoo import models,fields,api, _
from odoo.exceptions import UserError
from lxml import etree

class NewebStockPickingInherit(models.Model):
    _inherit = "stock.picking"

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False, context=None):
        if context is None:
            context = {}
        res = super(NewebStockPickingInherit, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,submenu=submenu)
        doc = etree.XML(res['arch'])
        if view_type == 'form':
            for node3 in doc.xpath("//field[@name='scheduled_date']"):
                node3.set('string', '(出/收)貨日期')
        res['arch'] = etree.tostring(doc, encoding='unicode')
        return res
