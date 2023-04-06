# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
import datetime, pytz
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

_logger = logging.getLogger(__name__)


class ContractLine1(models.Model):
    _name = 'neweb_contract.contract.line1'
    _description = "Contract Line1"

    contract_id = fields.Many2one('neweb_contract.contract', ondelete='cascade', string="Contract")
    prod_set = fields.Many2one('neweb.prodset', string="產品組別")
    prod_brand = fields.Many2one('neweb.prodbrand', string="品牌")
    prod_modeltype = fields.Char(string="機種-機型/料號")
    prod_modeltype1 = fields.Many2one('neweb.sitem_modeltype1', string="機型名稱")
    machine_serial_no = fields.Char(string='序號')
    rack_loc = fields.Char(string="櫃位")
    warranty_duedate = fields.Date(string="原廠保固到期日")
    server_name = fields.Char(string="主機名稱")
    machine_used_desc = fields.Char(string="設備用途說明")
    prod_line_os = fields.Text(string="作業系統")
    hd_no = fields.Char(string="硬碟料號")
    hd_num = fields.Integer(string="硬碟數量")
    cpu_no = fields.Char(string="CPU料號")
    cpu_num = fields.Integer(string="CPU數量")
    ram_no = fields.Char(string="RAM料號")
    ram_num = fields.Integer(string="RAM數量")
    expand_card_no = fields.Char(string="擴充卡料號")
    expand_card_num = fields.Integer(striong="擴充卡數量")
    power_no = fields.Char(string="電源料號")
    power_num = fields.Integer(string="電源數量")
    expand_module = fields.Char(string="擴充模組")
    machine_other = fields.Char(string="其他")
    contract_line_id = fields.Integer(string="Origin ID")










