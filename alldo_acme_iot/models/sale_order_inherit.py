# -*- coding: utf-8 -*-
# Author : Peter Wu

import json,logging,re
from odoo import models,fields,api, _
from odoo.exceptions import UserError
from lxml import etree

class acmesaleorderinherit1(models.Model):
    _inherit = "sale.order"

    so_pi = fields.Char(string="PI單號",required=True)
    active = fields.Boolean(string="ACTIVE",default=True)
    prod_desc = fields.Char(string="料號說明")
    shipping_complete = fields.Boolean(string="結案",default=False)


    def run_completed(self):
        # RUN SO -> WO -> MO -> SUB Closed complete
        # self.env.cr.execute("""select gen_complete_task(%d)""" % self.id)
        # self.env.cr.execute("""commit""")
        A=1
    def del_sale_order(self):
        myid = self.env.uid
        myrec = self.env['res.users'].search([('id','=',myid)])
        if myrec.has_group('alldo_acme_iot.group_iot_manager'):
            self.env.cr.execute("""select delsaleorder(%d)""" % self.id)
            self.env.cr.execute("""commit""")

            myviewid = self.env.ref('sale.view_quotation_tree_with_onboarding')

            return {
                'view_name': 'sale_order',
                'name': (u'銷售單 tree view'),
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order',
                'view_id': myviewid.id,
                'flags': {'action_buttons': True},
                'view_type': 'form',
                'view_mode': 'tree',
                'target': 'current'}
        else:
            raise UserError("您無權限刪除銷售訂單")

    def create(self, vals):

        res = super(acmesaleorderinherit1, self).create(vals)
        self.env.cr.execute("""select gensaleproddesc(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    def write(self, vals):

        res = super(acmesaleorderinherit1, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select gensaleproddesc(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res

    def run_archive(self):
        for rec in self:
            if rec.active==False:
                rec.active=True
            else:
                rec.active=False

    def run_sale_report(self):
        self.env.cr.execute("""select gensaleshipping(%d)""" % (self.id))
        self.env.cr.execute("""commit""")

        myrec = self.env['alldo_acme_iot.stockpicking_report1'].search([])
        myid = myrec[0].id
        myviewid = self.env.ref('alldo_acme_iot.acme_iot_shipping_report_action1')
        return {'view_name': 'acme_iot_shipping_report_action1',
                'name': (u'sale_order info item Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_acme_iot.stockpicking_report1',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'target': 'current',
                'view_id': myviewid.id,
                'view_mode': 'form',
                'view_type': 'form'
                }

    def action_confirm(self):
        if self._get_forbidden_state_confirm() & set(self.mapped('state')):
            raise UserError(_(
                'It is not allowed to confirm an order in the following states: %s'
            ) % (', '.join(self._get_forbidden_state_confirm())))

        for order in self.filtered(lambda order: order.partner_id not in order.message_partner_ids):
            order.message_subscribe([order.partner_id.id])
        self.write({
            'state': 'sale',
            'date_order': fields.Datetime.now()
        })
        self.env.cr.commit()
        self.env.cr.execute("""select changequant(%d)""" % self.id)
        self.env.cr.execute("""commit""")
        self.env.cr.commit()
        self._action_confirm()
        # if self.env.user.has_group('sale.group_auto_done_setting'):
        self.action_done()
        return True



