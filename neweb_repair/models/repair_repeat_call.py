# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebrepairrepeatcall(models.Model):
    _name = "neweb_repair.repeat_call_report"
    _order = "tot_amount desc,prod_serial_no,repair_datetime"

    name = fields.Char(string="報修單號", readonly=True)
    repair_datetime = fields.Datetime(readonly=True, string="報修時間")
    end_customer = fields.Many2one('res.partner', string="終端客戶")
    ae_id = fields.Many2one('hr.employee', string="派工工程師")
    prod_serial_no = fields.Char(readonly=True, string="機器序號")
    prod_serial = fields.Char(readonly=True, string="機型")
    device_amount = fields.Integer(readonly=True, string="次數")
    tot_amount = fields.Integer(string="期間總次數")
    problem_desc = fields.Text(string="問題描述")
    process_desc = fields.Text(string="處理說明")



class newebrepeatcalldownload(models.Model):
    _name = "neweb_repair.repeatcall_excel_download"
    _description = "REPEAT_CALL 資料夾"
    _order = "create_date desc"
    _rec_name = "xls_file"


    xls_file = fields.Binary(string="Repeat Call Excel 下載",attachment=False)
    xls_file_name = fields.Char(string="下載檔名")
    run_desc = fields.Char(string="匯出說明")
