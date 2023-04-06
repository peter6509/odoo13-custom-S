# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iplamanperformancesearch(models.TransientModel):
    _name = "alldo_ipla_iot.man_performance_wizard"
    _description = "鑄造工程三個月內實際生產量"

    std_owner = fields.Many2one('hr.employee',string="參考人員",required=True)
    product_no = fields.Many2one('product.template',string="產品")
