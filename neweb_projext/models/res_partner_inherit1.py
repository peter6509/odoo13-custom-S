# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api

class newebrespartnerinherit1(models.Model):
    _inherit = "res.partner"

    salesp1 = fields.Integer(string="sale1")
    salesp2 = fields.Integer(string="sale2")
    salesp3 = fields.Integer(string="sale3")
    salesp4 = fields.Integer(string="sale4")
    salesp5 = fields.Integer(string="sale5")


    @api.model
    def create(self, vals):
        res = super(newebrespartnerinherit1, self).create(vals)
        self.env.cr.execute("""select setempids(%d)""" % self.id)
        self.env.cr.execute("""commit""")
        return res

    def write(self, vals):
        res = super(newebrespartnerinherit1, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select setempids(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res