# -*- coding: utf-8 -*-
# Author : Peter Wu

import json
from odoo import models,fields,api, _
from odoo.exceptions import UserError
from lxml import etree


class newebrespartnerinherit(models.Model):
    _inherit = "res.partner"

    fax = fields.Char(string="FAX", default='-')

    @api.onchange('name')
    def onchangename(self):
        myrec = self.env['neweb_enhancement.sale_purchase_account'].search([])
        for rec in myrec:
            mysaleid = rec.sale_id.id
            mypurchaseid = rec.purchase_id.id
        self.property_account_receivable_id = mysaleid
        self.property_account_payable_id = mypurchaseid


    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False, context=None):
        if context is None:
            context = {}
        res = super(newebrespartnerinherit, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                                                 submenu=submenu)

        doc = etree.XML(res['arch'])
        if view_type == 'form':
            for node in doc.xpath("//field[@name='user_id']"):
                node.addnext(etree.Element('field',{'name':'emp_ids','string':'專案成本分析業務組員','nolabel':'0','widget':'many2many_tags'}))
                modifiers = json.loads(node.get("modifiers"))
                modifiers['invisible'] = True
                node.set("modifiers", json.dumps(modifiers))

            for node1 in doc.xpath("//field[@name='related_user_id']"):
                modifiers = json.loads(node1.get("modifiers"))
                modifiers['invisible'] = True
                node1.set("modifiers", json.dumps(modifiers))

            for node2 in doc.xpath("//field[@name='customer_category_id']"):
                modifiers = json.loads(node2.get("modifiers"))
                modifiers['invisible'] = True
                node2.set("modifiers", json.dumps(modifiers))

            for node3 in doc.xpath("//page[@string='Sales & Purchase']"):
                node3.set('string','銷售 & 採購')

            for node4 in doc.xpath("//page[@string='Additional Info']"):
                node4.set('string', '附加資訊')


            for node5 in doc.xpath("//field[@name='function']"):
                modifiers = json.loads(node5.get("modifiers"))
                modifiers['invisible'] = True
                node5.set("modifiers", json.dumps(modifiers))
            for node6 in doc.xpath("//field[@name='title']"):
                modifiers = json.loads(node6.get("modifiers"))
                modifiers['invisible'] = True
                node6.set("modifiers", json.dumps(modifiers))
            for node7 in doc.xpath("//field[@name='comp_create_date']"):
                node7.set('string', '公司成立日')
            for node8 in doc.xpath("//field[@name='paidup_capital']"):
                node8.set('string', '資本額')
            for node9 in doc.xpath("//field[@name='payment']"):
                modifiers = json.loads(node9.get("modifiers"))
                modifiers['invisible'] = True
                node9.set("modifiers", json.dumps(modifiers))
                #node9.set('string', '付款')
            for node10 in doc.xpath("//field[@name='payment_days']"):
                modifiers = json.loads(node10.get("modifiers"))
                if self.env.user.has_group('neweb_project.neweb_cs30_dir'):
                    modifiers['readonly'] = False
                else:
                    modifiers['readonly'] = True
                node10.set("modifiers", json.dumps(modifiers))
                node10.set('string', '付款天數')
            for node11 in doc.xpath("//field[@name='checkout_date']"):
                node11.set('string', '結帳日')
            for node12 in doc.xpath("//field[@name='pay_date']"):
                modifiers = json.loads(node12.get("modifiers"))
                # modifiers['invisible'] = True
                # node12.set("modifiers", json.dumps(modifiers))
                node12.set('string', '撥款日')
            for node13 in doc.xpath("//field[@name='credit_limit']"):
                node13.set('string', '信用額度')
            for node14 in doc.xpath("//field[@name='credit_rulelist']"):
                node14.set('string', '信用條件')


        res['arch'] = etree.tostring(doc, encoding='unicode')
        return res