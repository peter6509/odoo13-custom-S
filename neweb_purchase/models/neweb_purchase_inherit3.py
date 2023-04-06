# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api


class newebpurchaseinherit3(models.Model):
    _inherit = "purchase.order"

    @api.depends('display_line')
    def _get_purchase_no(self):
        mypid = ""
        myno = ""
        for rec in self.display_line:
            if mypid == '':
                mypid = rec.pitem_origin_no
                myno = rec.pitem_origin_no
            else:
                if myno != rec.pitem_origin_no:
                    if rec.pitem_origin_no:
                        mypid = mypid + '/ ' + rec.pitem_origin_no
                        myno = rec.pitem_origin_no
        self.PID = mypid
        return mypid

    purchase_contract_type = fields.Selection([('1','無合約'),('2','有合約')],string="單據類型",default='1')
    PID = fields.Char(string="PID",compute=_get_purchase_no)
    pidno = fields.Char(string="來源單號")



    @api.model
    def create(self, vals):

        res = super(newebpurchaseinherit3, self).create(vals)
        self.env.cr.execute("""select genpitemlitem1(%d)""" % res.id)
        self.env.cr.execute("""commit;""")
        return res

    def write(self, vals):

        res = super(newebpurchaseinherit3, self).write(vals)
        self.env.cr.execute("""select genpitemlitem1(%d)""" % self.id)
        self.env.cr.execute("""commit;""")
        return res

