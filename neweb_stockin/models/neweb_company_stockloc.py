# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebcompanystockloc(models.Model):
    _name = "neweb.company_stockloc"

    tp_outloc = fields.Many2one('stock.picking.type',string="總庫交貨位置")
    tp_inloc = fields.Many2one('stock.picking.type',string="總庫收貨位置")
    tc_outloc = fields.Many2one('stock.picking.type', string="中庫交貨位置")
    tc_inloc = fields.Many2one('stock.picking.type', string="中庫收貨位置")
    tk_outloc = fields.Many2one('stock.picking.type', string="高庫交貨位置")
    tk_inloc = fields.Many2one('stock.picking.type', string="高庫收貨位置")
    ts_outloc = fields.Many2one('stock.picking.type', string="南庫交貨位置")
    ts_inloc = fields.Many2one('stock.picking.type', string="南庫收貨位置")
    th_outloc = fields.Many2one('stock.picking.type', string="竹庫交貨位置")
    th_inloc = fields.Many2one('stock.picking.type', string="竹庫收貨位置")

    @api.model
    def create(self, vals):
        mycount = self.env['neweb.company_stockloc'].search_count([])
        if mycount > 0 :
            raise UserError("公司倉庫配置只能存在單筆")
        res = super(newebcompanystockloc, self).create(vals)
        return res

    def run_check_stock_quant(self):    # Cron Job 每日執行一次檢查
        self.env.cr.execute("""select check_stock_quant();""")
        self.env.cr.execute("""commit""")







