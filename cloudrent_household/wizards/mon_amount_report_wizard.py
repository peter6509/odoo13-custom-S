# -*- coding: utf-8 -*-
# Author : Peter Wu

import json,logging,re
from odoo import models,fields,api, _
from odoo.exceptions import UserError
from lxml import etree

class monamountreportwizard(models.TransientModel):
    _name = "cloudrent.mon_amount_report_wizard"

    project_no = fields.Many2one('cloudrent.household_house',string="案場名稱")
    house_id = fields.Many2one('cloudrent.household_house_line',string="房號")
    start_date = fields.Date(string="計算啟始日期")
    end_date = fields.Date(string="計算截止日期")

    @api.onchange('project_no')
    def onclientchange(self):
        return {'domain': {'house_id': [('house_id', '=', self.project_no.id)]}}


    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False,context=None):
        if context is None:
            context={}
        res = super(monamountreportwizard, self).fields_view_get(view_id=view_id,view_type=view_type,toolbar=toolbar,submenu=submenu)

        doc = etree.XML(res['arch'])
        if view_type=='form':
            for node in doc.xpath("//field[@name='project_no']"):
                modifiers = json.loads(node.get("modifiers"))
                modifiers['required'] = True
                node.set("modifiers", json.dumps(modifiers))
            for node1 in doc.xpath("//field[@name='start_date']"):
                modifiers = json.loads(node1.get("modifiers"))
                modifiers['required'] = True
                node1.set("modifiers", json.dumps(modifiers))

            for node2 in doc.xpath("//field[@name='end_date']"):
                modifiers = json.loads(node2.get("modifiers"))
                modifiers['required'] = True
                node2.set("modifiers", json.dumps(modifiers))


        res['arch'] = etree.tostring(doc, encoding='unicode')
        return res

    # @api.model
    # def fields_view_get(self, view_id=None, view_type='form',
    #                     toolbar=False, submenu=False):
    #     ret_val = super(ResConfigSettings, self).fields_view_get(
    #         view_id=view_id, view_type=view_type,
    #         toolbar=toolbar, submenu=submenu)
    #
    #     can_install_modules = self.env['ir.module.module'].check_access_rights(
    #         'write', raise_exception=False)
    #
    #     doc = etree.XML(ret_val['arch'])
    #
    #     for field in ret_val['fields']:
    #         if not field.startswith("module_"):
    #             continue
    #         for node in doc.xpath("//field[@name='%s']" % field):
    #             if not can_install_modules:
    #                 node.set("readonly", "1")
    #                 modifiers = json.loads(node.get("modifiers"))
    #                 modifiers['readonly'] = True
    #                 node.set("modifiers", json.dumps(modifiers))
    #
    #     ret_val['arch'] = etree.tostring(doc, encoding='unicode')
    #     return ret_val

    def run_mon_amount(self):
        A=1

