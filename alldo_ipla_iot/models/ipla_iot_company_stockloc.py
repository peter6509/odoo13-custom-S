# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotcompanystockloc(models.Model):
    _name = "alldo_ipla_iot.company_stockloc"

    material_loc = fields.Many2one('stock.location',string="公司原材物料倉庫")
    prod_loc = fields.Many2one('stock.location',string="公司產品倉庫")
    blank_loc = fields.Many2one('stock.location',string="公司毛胚倉庫")
    mo_loc = fields.Many2one('stock.location',string="生產位置倉")
    scrap_loc = fields.Many2one('stock.location',string="公司報廢倉庫")
    trans_loc = fields.Many2one('stock.location',string="內部轉換位置")
    furnace_loc = fields.Many2one('stock.location', string="混合料投料/耗料儲位")
    furnace_prod_id = fields.Many2one('product.product',string="熔爐融液混合料號")
    uncomplete_loc = fields.Many2one('stock.location',string="半成品線邊倉")
    m_categ = fields.Many2one('product.category',string="原料類別")
    r_categ = fields.Many2one('product.category',string="回收料類別")
    pack_categ = fields.Many2one('product.category',string="包材類別")

    @api.model
    def create(self, vals):
        mycount = self.env['alldo_ipla_iot.company_stockloc'].search_count([])
        if mycount > 0 :
            raise UserError("公司倉庫配置只能存在單筆")
        res = super(iplaiotcompanystockloc, self).create(vals)
        return res

    def run_clear_reserved(self):
        self.env.cr.execute("""update stock_quant set reserved_quantity=0""")
        self.env.cr.execute("""commit""")
        # self.env.cr.execute("""update stock_quant set quantity=0 where location_id=14 and quantity < 0 """)
        # self.env.cr.execute("""commit""")



