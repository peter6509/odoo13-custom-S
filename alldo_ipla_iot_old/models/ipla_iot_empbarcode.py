# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, fields, api
from odoo.exceptions import UserError

class iplaiotempinfo(models.Model):
   _name = "alldo_ipla_iot.empinfo"
   _rec_name= "empinfo_date"

   empinfo_date = fields.Date(string="製作日期")
   barcode_line = fields.One2many('alldo_ipla_iot.empbarcode','barcode_id',copy=False)


class iplaiotempbarcode(models.Model):
   _name = "alldo_ipla_iot.empbarcode"
   _description = "人員卡片產生檔"


   barcode_id = fields.Many2one('alldo_ipla_iot.empinfo',ondelete='cascade')
   emp_code1 = fields.Char(string="emp1_code")
   emp_name1 = fields.Char(string="emp1_name")
   emp_code2 = fields.Char(string="emp2_code")
   emp_name2 = fields.Char(string="emp2_name")
   emp_code3 = fields.Char(string="emp3_code")
   emp_name3 = fields.Char(string="emp3_name")
   emp_code4 = fields.Char(string="emp4_code")
   emp_name4 = fields.Char(string="emp4_name")
   emp_code5 = fields.Char(string="emp5_code")
   emp_name5 = fields.Char(string="emp5_name")
   emp_code6 = fields.Char(string="emp6_code")
   emp_name6 = fields.Char(string="emp6_name")
   emp_code7 = fields.Char(string="emp7_code")
   emp_name7 = fields.Char(string="emp7_name")
   emp_code8 = fields.Char(string="emp8_code")
   emp_name8 = fields.Char(string="emp8_name")
   emp_code9 = fields.Char(string="emp9_code")
   emp_name9 = fields.Char(string="emp9_name")
   emp_code10 = fields.Char(string="emp10_code")
   emp_name10 = fields.Char(string="emp10_name")
