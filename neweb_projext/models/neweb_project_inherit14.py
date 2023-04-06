# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebProjectInherit14(models.Model):
    _inherit = "neweb.project"

    stockoutno_line = fields.One2many('neweb.stockoutno_line','out_id',string="出貨單號",copy=False)
    main_stockoutno = fields.Many2one('stock.picking',string="主出貨單")



class NewebStockOutNoLine(models.Model):
    _name = "neweb.stockoutno_line"
    _description = "專案成本分析出貨單明細"


    out_id = fields.Many2one('neweb.project',ondelete='cascade')
    name = fields.Many2one('stock.picking',string="出貨單號")


# class NewebStockPickingsetmain(models.Model):
#     _inherit = "stock.picking"
#
#     is_proj_main = fields.Boolean(string="是否為專案主出貨單？",default=False)


