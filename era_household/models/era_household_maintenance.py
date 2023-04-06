# -*- coding: utf-8 -*-
# Author : Peter Wu

import json,logging,re
from odoo import models,fields,api, _
from odoo.exceptions import UserError
from lxml import etree

class erahouseholdmaintenance(models.Model):
    _name = "era.household_maintenance"
    _order = "main_require_date desc,main_house_id"

    main_house_id = fields.Many2one('era.household_house_line',string="房號",required=True)
    main_require_date = fields.Date(string="報修時間",default=fields.Date.today())
    main_memo = fields.Text(string="問題描述")
    main_user_id = fields.Many2one('res.users',string="報修帳號",default=lambda self:self.env.uid)
    main_rating = fields.Selection([('1','一般'),('2','中等'),('3','緊急')],string="報修需求程度",default='1')
    state = fields.Selection([('1','待處理設施報修'),('2','已進行處理中'),('3','已處理完成')],string="報修處理狀態",default='1')
    repair_memo = fields.Text(string="處理相關說明")
    repair_date = fields.Date(string="開始處理日期")
    complete_memo = fields.Text(string="處理完成說明")
    complete_date = fields.Date(string="完修日期")
    main_doc = fields.Binary(string="相關文件",attachment=False)
    doc_file_name = fields.Char(string="檔名")

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False, context=None):
        if context is None:
            context = {}
        res = super(erahouseholdmaintenance, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,submenu=submenu)

        doc = etree.XML(res['arch'])
        if view_type == 'form':
            if self.env['res.users'].has_group('era_household.group_era_manager') or self.env['res.users'].has_group('era_household.group_era_ass'):
                for node in doc.xpath("//field[@name='repair_memo']"):
                    modifiers = json.loads(node.get("modifiers"))
                    modifiers['readonly'] = False
                    node.set("modifiers", json.dumps(modifiers))
                for node in doc.xpath("//field[@name='repair_date']"):
                    modifiers = json.loads(node.get("modifiers"))
                    modifiers['readonly'] = False
                    node.set("modifiers", json.dumps(modifiers))
                for node in doc.xpath("//field[@name='complete_memo']"):
                    modifiers = json.loads(node.get("modifiers"))
                    modifiers['readonly'] = False
                    node.set("modifiers", json.dumps(modifiers))
                for node in doc.xpath("//field[@name='complete_date']"):
                    modifiers = json.loads(node.get("modifiers"))
                    modifiers['readonly'] = False
                    node.set("modifiers", json.dumps(modifiers))
                for node in doc.xpath("//field[@name='main_doc']"):
                    modifiers = json.loads(node.get("modifiers"))
                    modifiers['readonly'] = False
                    node.set("modifiers", json.dumps(modifiers))
                for node in doc.xpath("//field[@name='state']"):
                    modifiers = json.loads(node.get("modifiers"))
                    modifiers['readonly'] = False
                    node.set("modifiers", json.dumps(modifiers))


        res['arch'] = etree.tostring(doc, encoding='unicode')
        return res





