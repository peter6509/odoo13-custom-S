# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class newebprodsetinherit2(models.Model):
    _inherit = "neweb.prodset"

    name1 = fields.Char(string=u"轉換後名稱")
    sname = fields.Char(string=u"簡稱")

    @api.model
    def create(self, vals):
        vals['name1']=vals['name']
        if 'name' in vals and vals['name']:
            myname = vals['name']
            myname1=myname.replace(' ','').replace('/','').replace('    ','').upper()
            vals['name1']=myname1

        if 'sname' in vals and not vals['sname']:
            myname = vals['name']
            myname1 = myname.replace(' ', '').replace('/', '').replace('    ', '').upper()
            vals['sname'] = myname1
        res = super(newebprodsetinherit2,self).create(vals)
        return res


    def write(self, vals):
        if 'name' in vals and vals['name']:
            myname = vals['name']
            vals['name1']=myname.replace(' ','').replace('/','').replace('  ','').upper()
        res = super(newebprodsetinherit2,self).write(vals)
        return res