# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api


class CloudRentMonthdownload(models.Model):
    _name = "cloudrent.month_download"
    _description = "媒合月報下載暫存區"
    _order = "create_date desc"

    match_year = fields.Char(string="年度")
    match_month = fields.Char(string="月份")
    escrow_no = fields.Many2one('cloudrent.escrow', string="代管業者")
    xls_file = fields.Binary(string="月報下載",attachment=False)
    xls_file_name = fields.Char(string="檔名")
