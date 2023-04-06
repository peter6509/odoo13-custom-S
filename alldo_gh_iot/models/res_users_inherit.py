# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class resusersinherit(models.Model):
    _inherit = "res.users"

    @api.model
    def create(self, vals):
        if vals['login']=='':
            self.env.cr.execute("""select getlastlogin()""")
            mylogin = self.env.cr.fetchone()[0]
            vals['login']=mylogin
        res = super(resusersinherit, self).create(vals)
        self.env.cr.execute("""update res_users set password='123456' where login='%s'""" % res.login)
        self.env.cr.execute("""commit""")
        return res


    @api.onchange('name')
    def onchangename(self):
        self.env.cr.execute("""select getlastlogin()""")
        mylogin = self.env.cr.fetchone()[0]
        self.login=mylogin

