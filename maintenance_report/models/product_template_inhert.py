# _*_ coding: utf-8 _*_
# Author: Peter Wu

from odoo import models, fields, api


class prod_temp_inherit(models.Model):
    _inherit = "product.template"

    maker_name = fields.Many2one('res.partner', String=u"製造商")
    safe_qty = fields.Float(digits=(6, 1), String=u"安全量", default=0)
    disp_supp_name = fields.Char(size=20, String=u"供應商", compute='_get_supplier_name', store=False)
    low_qty = fields.Float(digitals=(6, 0), compute='_get_sum_qty', store=False, string=u"安全差異量",track_visibility="always")
    stocklocation = fields.Char(size=6, string=u'儲位')
    depart_use = fields.Text(string=u"使用單位")

    @api.one
    @api.depends('seller_ids')
    def _get_supplier_name(self):
        self.ensure_one()
        disp_name = ''
        if len(self.seller_ids) > 0:
            for seller in self.seller_ids:
                disp_name = seller.name.name
        else:
            disp_name = 'None'
        self.disp_supp_name = disp_name
        return disp_name

    @api.multi
    @api.depends('qty_available', 'safe_qty')
    def _get_sum_qty(self):
        for rec in self:
            sum_qty = rec.qty_available - rec.safe_qty
            rec.update({'low_qty':sum_qty})

