# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models ,fields , api, _
import json,logging,re
from odoo.exceptions import UserError
from lxml import etree


class saleinherit(models.Model):
    _inherit = "sale.order"

    date_order1 = fields.Date('報價日期', default=fields.Datetime.now().strftime('%Y-%m-%d'))
    user_id = fields.Many2one('res.users',default=lambda self:self.env.user.id)

    def action_confirm(self):
        saleno = self.name
        partnerid = self.partner_id.id
        dateorder = fields.Datetime.now()
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
        self._action_confirm()
        if self.env.user.has_group('sale.group_auto_done_setting'):
            self.action_done()

        myrec = self.env['stock.picking']

        myres = myrec.create({'picking_type_id': 2,
                              'location_id': 8,
                              'location_dest_id': 5,
                              'move_type': 'direct',
                              'company_id': 1,
                              'date': dateorder ,
                               'origin': saleno,
                              'stockin_type': '1',
                              'stockout_type': '1',
                              'state': 'assigned',
                               'partner_id': partnerid,
                              'product_id': 2,
                              'move_lines': [
                                  (0, 0,
                                   {'product_id': 2, 'company_id': 1, 'location_id': 8,'name': '銷售商品','date': dateorder,
                                    'date_expected': dateorder,'procure_method': 'make_to_stock',
                                    'location_dest_id': 5,'product_uom_qty': 1,'product_uom': 1,
                                    })]})

        # myres.action_confirm()
        # self.env.cr.commit()
        # myres.action_done()
        # self.env.cr.commit()
        return True

    # def action_confirm(self):
    #     if self._get_forbidden_state_confirm() & set(self.mapped('state')):
    #         raise UserError(_(
    #             'It is not allowed to confirm an order in the following states: %s'
    #         ) % (', '.join(self._get_forbidden_state_confirm())))
    #
    #     for order in self.filtered(lambda order: order.partner_id not in order.message_partner_ids):
    #         order.message_subscribe([order.partner_id.id])
    #     self.write({
    #         'state': 'sale',
    #         'date_order': fields.Datetime.now()
    #     })
    #     self._action_confirm()
    #     if self.env.user.has_group('sale.group_auto_done_setting'):
    #         self.action_done()
    #     self.env.cr.execute("""select gensalestockout(%d)""" % self.id)
    #     self.env.cr.execute("""commit""")
    #     return True
    #
