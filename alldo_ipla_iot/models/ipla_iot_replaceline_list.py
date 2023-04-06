# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotreplacelinelist(models.Model):
    _name = "alldo_ipla_iot.replaceline_list"

    order_id = fields.Many2one('alldo_ipla_iot.workorder', ondelete='cascade')
    partner_id = fields.Many2one('res.partner',string="客戶")
    product_no = fields.Many2one('product.product',string="產品")
    eng_type = fields.Char(string="工序")
    replace_owner = fields.Many2one('hr.employee', string="工程師")
    equipment_id = fields.Many2one('maintenance.equipment', string="機台")
    replace_type = fields.Selection([('P', '備模'), ('L', '架模'), ('B', '烘模')], string="類別")
    replace_start_datetime = fields.Char(string="啟始時間")
    replace_end_datetime = fields.Char(string="截止時間")
    replace_duration = fields.Float(digits=(6, 1), string="時間(分)")
