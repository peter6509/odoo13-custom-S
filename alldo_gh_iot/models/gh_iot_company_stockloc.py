# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotcompanystockloc(models.Model):
    _name = "alldo_gh_iot.company_stockloc"

    prod_loc = fields.Many2one('stock.location',string="公司產品倉庫")
    semi_prod_loc = fields.Many2one('stock.location',string="公司半成品倉庫")
    blank_loc = fields.Many2one('stock.location',string="公司毛胚倉庫")
    mo_loc = fields.Many2one('stock.location',string="生產位置倉")
    scrap_loc = fields.Many2one('stock.location',string="公司報廢倉庫")
    trans_loc = fields.Many2one('stock.location',string="內部轉換位置")
    pbooking_loc = fields.Many2one('stock.location',string="產品預留鎖定位置")
    bbooking_loc = fields.Many2one('stock.location',string="毛胚預留鎖定位置")

    @api.model
    def create(self, vals):
        mycount = self.env['alldo_gh_iot.company_stockloc'].search_count([])
        if mycount > 0 :
            raise UserError("公司倉庫配置只能存在單筆")
        res = super(ghiotcompanystockloc, self).create(vals)
        return res

    def run_clear_reserved(self):
        self.env.cr.execute("""update stock_quant set reserved_quantity=0""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from stock_quant where location_id=14 and quantity < 0 ;""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select autoarchwkorder()""")
        self.env.cr.execute("""commit""")
