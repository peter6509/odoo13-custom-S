# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class newebsaleinherit2(models.Model):
    _inherit = "sale.order"

    contact_address = fields.Many2one('res.partner', string=u"地址")
    quotation_address = fields.Char(string=u"銷售單地址")


    @api.depends('partner_id')
    def _get_qaddress(self):
        myaddress = self.env['res.partner'].search([('id', '=', self.partner_id.id)]).street
        self.quotation_address = myaddress
        return myaddress

    @api.onchange('partner_id')
    def onchange_partnerid1(self):
        if self.partner_id:
            myrec = self.env['res.partner'].search([('parent_id', '=', self.partner_id.id)])
            ids = []
            for item in myrec:
                ids.append(item.id)
            res = {}

            # print "%s" % ids
            res['domain'] = {'contact_address': [('id', 'in', ids)]}
            return res

    @api.onchange('partner_id')
    def onchange_partner3(self):
        self.user_id = self.env.uid
        # self.env.cr.execute("""select getsaleowner(%d)""" % self.partner_id.id)
        # myres = self.env.cr.fetchone()
        # if myres[0] != 0:
        #     self.user_id = myres[0]

    @api.model
    def create(self,vals):
        # if 'contact_id' in vals and not vals['contact_id']:
        #     mycontactid = vals['contact_id']
        #     vals['quotation_address'] = self.env['res.partner'].search([('id','=', mycontactid)]).street
        # else:
        #     mypartnerid = vals['partner_id']
        #     vals['quotation_address'] = self.env['res.partner'].search([('id','=', mypartnerid)])
        res = super(newebsaleinherit2,self).create(vals)
        self.env.cr.execute("""select setcontactaddress(%d)""" % res.id)
        return res


    def write(self,vals):
        # if 'contact_id' in vals and not vals['contact_id']:
        #     mycontactid = vals['contact_id']
        #     vals['quotation_address'] = self.env['res.partner'].search([('id','=', mycontactid)]).street
        # else:
        #     mypartnerid = self.partner_id.id
        #     vals['quotation_address'] = self.env['res.partner'].search([('id','=', mypartnerid)]).street
        res = super(newebsaleinherit2,self).write(vals)
        self.env.cr.execute("""select setcontactaddress(%d)""" % self.id)
        return res

