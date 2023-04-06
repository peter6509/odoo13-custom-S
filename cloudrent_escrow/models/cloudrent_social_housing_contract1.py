# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class CloudRentSocialHousingContract1(models.Model):
    _name = "cloudrent.social_housing_contract1"
    _description = "社會住宅-包租契約書"

    name = fields.Char(string="契約書單號", default="New", copy=False)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            self.env.cr.execute("""select get_cloudrent_seqno(%d,'%s')""" % (vals['escrow_no'], 'C3'))
            vals['name'] = self.env.cr.fetchone()[0]
        res = super(CloudRentSocialHousingContract1, self).create(vals)
        return res
