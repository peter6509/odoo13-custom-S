# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebexcelsetseq(models.Model):
    _name = "neweb_chi_invoicing.excelset_seq"


    set_date = fields.Date(string="日期")
    sales_num = fields.Integer(string="銷項流水號",default=1)
    purchase_num = fields.Integer(string="進項流水號",default=1)
    project_num = fields.Integer(string="專案流水號",default=1)
    product_num = fields.Integer(string="產品流水號",default=1)