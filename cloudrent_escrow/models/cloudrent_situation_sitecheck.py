# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class CloudRentSituationSiteCheck(models.Model):
    _name = "cloudrent.situation_sitecheck"
    _description = "屋況及租屋安全檢核表"

    name = fields.Char(string="檢核單號", default="New", copy=False)
    build_no = fields.Many2one('cloudrent.build', string="物件編號")
    lessor_no = fields.Many2one('cloudrent.escrow_member', string="出租人")
    escrow_no = fields.Many2one('cloudrent.escrow', string="代管業者")
    applyfor_filename = fields.Char(string='檔名')
    applyfor_attach = fields.Binary(attachment=False, string="申請書夾檔")
    leadid = fields.Many2one('crm.lead', string="業務pipeline")


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            self.env.cr.execute("""select get_cloudrent_seqno(%d,'%s')""" % (vals['escrow_no'], 'A6'))
            vals['name'] = self.env.cr.fetchone()[0]
        res = super(CloudRentSituationSiteCheck, self).create(vals)
        return res



