# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api, _
from odoo.exceptions import UserError


class acmeiotsonoseq(models.Model):
    _name = "alldo_acme_iot.so_sequence"
    _description = "銷售單序號檔"

    so_prefixcode = fields.Char(string="銷單前綴碼")
    so_year = fields.Char(string="年碼")
    so_seq = fields.Integer(string="流水號")


class respartnerinherit(models.Model):
    _inherit = "res.partner"

    so_prefixcode = fields.Char(string="客戶訂單前綴碼")



class acmeiotsonocreate(models.Model):
    _inherit = "sale.order"

    is_openwkorder = fields.Boolean(string="是否已開工單",default=False)
    momarkup_ratio = fields.Float(digits=(5,1),string="投產增耗比率%",compute='_get_ngratio',store=True)
    is_update_markup = fields.Boolean(string="是否已變動增耗",default=False)

    # @api.depends('product_id')
    # def _get_ngratio(self):
    #     A=1


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
        try:
            for rec in self:
                rec._action_confirm()
        except Exception as inst:
            A=1
            # raise UserError("鑄件產品要投入工單生產,請一張報價單打單一產品,才能自動產生生產命令!")
        if self.env.user.has_group('sale.group_auto_done_setting'):
            self.action_done()
        self.env.cr.execute("""select updatemomarkupratio(%d)""" % self.id)
        self.env.cr.execute("""commit""")
        return True



    # def action_confirm(self):
    #     for rec in self:
    #         super(acmeiotsonocreate, rec)._action_confirm()
    #

    # def run_mo_markup(self):
    #     self.env.cr.execute("""select updatemomarkupratio()""")
    #     self.env.cr.execute("""commit""")

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.name,myrec.partner_id.name)
            result.append((myrec.id, myname))
        return result

    # @api.model
    # def create(self,vals):
    #     res = super(acmeiotsonocreate, self).create(vals)
    #     self.env.cr.execute("""select getsonoseq(%d)""" % res.id)
    #     self.env.cr.execute("""commit""")
    #     return res


class acmeiotsonolinecreate(models.Model):
    _inherit = 'sale.order.line'

    is_openwkorder = fields.Boolean(string="是否已開工單", default=False)