# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class CloudRentApplyforEscrow1(models.Model):
    _name = "cloudrent.applyfor_escrow1"
    _description = "出租人出租住宅申請書(代管)"

    name = fields.Char(string="申請書單號", default="New", copy=False)
    build_no = fields.Many2one('cloudrent.build',string="物件編號")
    lessor_no = fields.Many2one('cloudrent.escrow_member',string="出租人")
    escrow_no = fields.Many2one('cloudrent.escrow',string="代管業者")
    applyfor_filename = fields.Char(string='檔名')
    applyfor_attach = fields.Binary(attachment=False,string="申請書夾檔")
    leadid = fields.Many2one('crm.lead',string="業務pipeline")
    doclineid = fields.Many2one('cloudrent.lessor_doc_line',string="DOC Line ID")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            self.env.cr.execute("""select get_cloudrent_seqno(%d,'%s')""" % (vals['escrow_no'], 'A2'))
            vals['name'] = self.env.cr.fetchone()[0]
        res = super(CloudRentApplyforEscrow1, self).create(vals)
        return res
