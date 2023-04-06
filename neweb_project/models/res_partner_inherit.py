# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class respartnerinherit(models.Model):
    _inherit = "res.partner"

    self_receive_type = fields.Selection([('1', '現金'), ('2', '支票')], string="親領項目", default='2')
    fax = fields.Char(string="FAX", default='-')


    @api.model
    def create(self, vals):
        if 'property_account_receivable_id' in vals and not vals['property_account_receivable_id']:
            vals['property_account_receivable_id'] = 2
        if 'property_account_payable_id' in vals and not vals['property_account_payable_id']:
            vals['property_account_payable_id'] = 3
        if 'vat' in vals and not vals['vat']:
            raise UserError("客戶統編不能空值！")
        res = super(respartnerinherit, self).create(vals)

        self.env.cr.execute("""select getsaleowner(%d)""" % res.id)
        myres = self.env.cr.fetchone()
        if myres[0] != 0:
            self.env.cr.execute("""update res_partner set user_id=%d where id=%d""" % (myres[0], res.id))
        return res


    def write(self, vals):
        res = super(respartnerinherit, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select getsaleowner(%d)""" % rec.id)
            myres = self.env.cr.fetchone()
            if myres[0] != 0 :
                self.env.cr.execute("""update res_partner set user_id=%d where id=%d""" % (myres[0],rec.id))
        return res


