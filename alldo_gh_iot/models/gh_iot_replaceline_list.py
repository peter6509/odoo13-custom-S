# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotreplacelinelist(models.Model):
    _name = "alldo_gh_iot.replaceline_list"
    _order = "replace_start_datetime,replace_owner,eng_type"

    order_id = fields.Many2one('alldo_gh_iot.workorder', ondelete='cascade',string="工單")
    partner_id = fields.Many2one('res.partner',string="客戶")
    product_no = fields.Many2one('product.product',string="產品")
    eng_type = fields.Char(string="工序")
    replace_owner = fields.Many2one('hr.employee', string="工程師")
    equipment_id = fields.Many2one('maintenance.equipment', string="機台")
    replace_start_datetime = fields.Char(string="架機啟始時間")
    replace_end_datetime = fields.Char(string="架機截止時間")
    replace_duration = fields.Float(digits=(6, 1), string="時間(H)")
    wk_start_datetime = fields.Char(string="生產啟始時間")
    wk_end_datetime = fields.Char(string="生產結束時間")
    wk_num = fields.Float(digits=(6,0),string="數量")
