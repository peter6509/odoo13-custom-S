# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class ghiotsonoseq(models.Model):
    _name = "alldo_gh_iot.so_sequence"
    _description = "銷售單序號檔"

    so_prefixcode = fields.Char(string="銷單前綴碼")
    so_year = fields.Char(string="年碼")
    so_seq = fields.Integer(string="流水號")


class respartnerinherit(models.Model):
    _inherit = "res.partner"

    so_prefixcode = fields.Char(string="客戶訂單前綴碼")



class ghiotsonocreate(models.Model):
    _inherit = "sale.order"

    is_openwkorder = fields.Boolean(string="是否已開工單",default=False)

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.name,myrec.partner_id.name)
            result.append((myrec.id, myname))
        return result

    @api.model
    def create(self,vals):
        res = super(ghiotsonocreate, self).create(vals)
        self.env.cr.execute("""select getsonoseq(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res


class ghiotsonolinecreate(models.Model):
    _inherit = 'sale.order.line'

    is_openwkorder = fields.Boolean(string="是否已開工單", default=False)