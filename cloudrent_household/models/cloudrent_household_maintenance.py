# -*- coding: utf-8 -*-
# Author : Peter Wu

import json,logging,re
from odoo import models,fields,api, _
from odoo.exceptions import UserError
from lxml import etree

class cloudrenthouseholdmaintenance(models.Model):
    _name = "cloudrent.household_maintenance"
    _description = "租房修繕通報"
    _order = "main_require_date desc,main_house_id"

    name = fields.Char(string="報修單號",required=True, copy=False, readonly=True, index=True, default='New')
    main_house_id = fields.Many2one('cloudrent.household_house_line',string="房號",required=True)
    main_require_date = fields.Date(string="修繕通報時間",default=fields.Date.today())
    equip_id = fields.Many2one('cloudrent.equip_list',string="設備")
    main_memo = fields.Text(string="問題狀況描述")
    main_user_id = fields.Many2one('res.users',string="報修帳號",default=lambda self:self.env.uid)
    main_rating = fields.Selection([('1','一般'),('2','中等'),('3','緊急')],string="報修需求程度",default='1')
    state = fields.Selection([('1','修繕通報'),('2','預約現場勘驗'),('3','廠商估價'),('4','派工修繕'),('5','滿意度調查'),('6','結案')],string="報修處理狀態",default='1')
    repair_memo = fields.Text(string="處理相關說明")
    repair_date = fields.Date(string="開始處理日期")
    complete_memo = fields.Text(string="處理完成說明")
    complete_date = fields.Date(string="完修日期")
    main_doc = fields.Binary(string="相關文件",attachment=False)
    doc_file_name = fields.Char(string="檔名")

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            seq_code = self.env['ir.sequence'].next_by_code('cloudrent.repair') or 'New'
            vals['name'] = seq_code
        res = super(cloudrenthouseholdmaintenance, self).create(vals)

        return res

    @api.onchange('main_house_id')
    def onchangehouseid(self):
        myids = []
        myhouseid = self.main_house_id.id
        myrec = self.env['cloudrent.equip_list'].search([('equip_id', '=', myhouseid)])
        for rec in myrec:
            myids.append(rec.id)
        return {'domain': {'equip_id': [('id', 'in', myids)]}}


    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False, context=None):
        if context is None:
            context = {}
        res = super(cloudrenthouseholdmaintenance, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,submenu=submenu)

        doc = etree.XML(res['arch'])
        if view_type == 'form':
            if self.env['res.users'].has_group('cloudrent_household.group_cloudrent_manager') or self.env['res.users'].has_group('cloudrent_household.group_cloudrent_ass'):
                for node in doc.xpath("//field[@name='repair_memo']"):
                    modifiers = json.loads(node.get("modifiers"))
                    modifiers['readonly'] = False
                    node.set("modifiers", json.dumps(modifiers))
                for node1 in doc.xpath("//field[@name='repair_date']"):
                    modifiers = json.loads(node1.get("modifiers"))
                    modifiers['readonly'] = False
                    node1.set("modifiers", json.dumps(modifiers))
                for node2 in doc.xpath("//field[@name='complete_memo']"):
                    modifiers = json.loads(node2.get("modifiers"))
                    modifiers['readonly'] = False
                    node2.set("modifiers", json.dumps(modifiers))
                for node3 in doc.xpath("//field[@name='complete_date']"):
                    modifiers = json.loads(node3.get("modifiers"))
                    modifiers['readonly'] = False
                    node3.set("modifiers", json.dumps(modifiers))
                for node4 in doc.xpath("//field[@name='main_doc']"):
                    modifiers = json.loads(node4.get("modifiers"))
                    modifiers['readonly'] = False
                    node4.set("modifiers", json.dumps(modifiers))
                for node5 in doc.xpath("//field[@name='state']"):
                    modifiers = json.loads(node5.get("modifiers"))
                    modifiers['readonly'] = False
                    node5.set("modifiers", json.dumps(modifiers))


        res['arch'] = etree.tostring(doc, encoding='unicode')
        return res





