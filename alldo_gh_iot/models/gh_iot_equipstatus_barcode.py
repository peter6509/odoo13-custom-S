# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, fields, api
from odoo.exceptions import UserError

class ghiotequipstatusinfo(models.Model):
   _name = "alldo_gh_iot.equipstatusinfo"
   _rec_name= "print_num"

   print_num = fields.Integer(string="製作份數")
   barcode_line = fields.One2many('alldo_gh_iot.equipstatusbarcode','barcode_id',copy=False)


class ghiotequipstatusbarcode(models.Model):
   _name = "alldo_gh_iot.equipstatusbarcode"
   _description = "設備異常條碼生檔"

   barcode_id = fields.Many2one('alldo_gh_iot.equipstatusinfo',ondelete='cascade')
   status_code1 = fields.Char(string="status1_code")
   status_name1 = fields.Char(string="status1_name")
   status_code2 = fields.Char(string="status2_code")
   status_name2 = fields.Char(string="status2_name")
   status_code3 = fields.Char(string="status3_code")
   status_name3 = fields.Char(string="status3_name")
   status_code4 = fields.Char(string="status4_code")
   status_name4 = fields.Char(string="status4_name")
   status_code5 = fields.Char(string="status5_code")
   status_name5 = fields.Char(string="status5_name")
   status_code6 = fields.Char(string="status6_code")
   status_name6 = fields.Char(string="status6_name")
   status_code7 = fields.Char(string="status7_code")
   status_name7 = fields.Char(string="status7_name")
   status_code8 = fields.Char(string="status8_code")
   status_name8 = fields.Char(string="status8_name")
   status_code9 = fields.Char(string="status9_code")
   status_name9 = fields.Char(string="status9_name")
   status_code10 = fields.Char(string="status10_code")
   status_name10 = fields.Char(string="status10_name")