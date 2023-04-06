# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from datetime import datetime
import tempfile,base64,os
import openpyxl,shutil
from openpyxl.styles import Side, Border, colors


class CloudRentAgentGrantReport(models.TransientModel):
    _name = "cloudrent.agent_grant_report"
    _description = "月報列印精靈(每月業者補助費用清冊)"

    report_date = fields.Date(string="製表日期",default=datetime.today(),required=True)
    report_year = fields.Char(string="西元年XXXX",required=True)
    report_month = fields.Selection([('01','一月'),('02','二月'),('03','三月'),('04','四月'),('05','五月'),('06','六月'),('07','七月'),('08','八月'),('09','九月'),('10','十月'),('11','十一月'),('12','十二月')],string='月份',required=True)








