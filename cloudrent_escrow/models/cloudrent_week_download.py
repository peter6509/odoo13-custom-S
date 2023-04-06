# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api


class CloudRentWeekdownload(models.Model):
    _name = "cloudrent.week_download"
    _description = "週報下載暫存區"
    _order = "create_date desc"

    match_year = fields.Char(string="年度")
    week_seq = fields.Integer(string="週次")
    escrow_no = fields.Many2one('cloudrent.escrow', string="代管業者")
    xls_file = fields.Binary(string="週報下載",attachment=False)
    xls_file_name = fields.Char(string="檔名")
