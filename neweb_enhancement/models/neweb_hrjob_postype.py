# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class newebhrjobpostype(models.Model):
    _inherit = "hr.job"

    pos_type = fields.Selection([('1','一線人員'),('2','一線主管'),('3','二線主管'),('4','副總'),('5','總經理')],string="簽核職務")