# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotdashboard(models.Model):
    _name = "alldo_gh_iot.dashboard"

    equipment_no = fields.Many2one('maintenance.equipment',string="機台")
    iot_status = fields.Selection([('1','生產中'),('2','換線中'),('3','準備中')],string="機台狀態")
    iot_status1 = fields.Char(string="機台狀態")
    wkorder_no = fields.Many2one('alldo_gh_iot.workorder',string="工單號碼")
    order_num = fields.Float(digits=(10,0),string="訂單數量")
    prod_num = fields.Float(digits=(10,0),string="累積生產量")
    product_id = fields.Many2one('product.product',string="產品")
    eng_type = fields.Char(string="工程別")
    emp_no = fields.Many2one('hr.employee',string="作業人員")
    last_duration = fields.Float(digits=(5,0),string="最後工件時差(分鐘)")


    def run_min_dashboard(self):
        self.env.cr.execute("""select genmindashboard()""")
        self.env.cr.execute("""commit""")