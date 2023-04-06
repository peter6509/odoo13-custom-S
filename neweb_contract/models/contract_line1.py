# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
import datetime,pytz
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

_logger = logging.getLogger(__name__)


class ContractLine1(models.Model):
    _name = 'neweb_contract.contract.line1'
    _description = "Contract Line1"
    _order = "sequence,contract_line_id"

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
    # hd_no = fields.Char(string="硬碟料號")
    # hd_num = fields.Integer(string="硬碟數量")
    # cpu_no = fields.Char(string="CPU料號")
    # cpu_num = fields.Integer(string="CPU數量")
    # ram_no = fields.Char(string="RAM料號")
    # ram_num = fields.Integer(string="RAM數量")
    # expand_card_no = fields.Char(string="擴充卡料號")
    # expand_card_num = fields.Integer(striong="擴充卡數量")
    # power_no = fields.Char(string="電源料號")
    # power_num = fields.Integer(string="電源數量")
    expand_module = fields.Char(string="擴充模組")
    machine_other = fields.Char(string="其他")
    contract_line_id = fields.Integer(string="Origin ID")
    hd_line = fields.One2many('neweb_contract.hd_line', 'hd_id', string="硬碟明細")
    cpu_line = fields.One2many('neweb_contract.cpu_line', 'cpu_id', string="CPU明細")
    ram_line = fields.One2many('neweb_contract.ram_line', 'ram_id', string="RAM明細")
    expand_card_line = fields.One2many('neweb_contract.expand_card_line', 'expand_card_id', string="擴充卡明細")
    power_line = fields.One2many('neweb_contract.power_line', 'power_id', string="電源明細")
    sequence = fields.Integer('sequence')



    def hd_button(self):
        myrec = self.env['neweb_contract.contract.line1'].search([('id','=',self.id)])
        try:
            form_view_id = self.env.ref("neweb_contract.view_contract_hd_line_form").id
        except Exception as e:
            form_view_id = False
        context = dict(self._context or {})
        return {
            'type': 'ir.actions.act_window',
            'name': '硬碟明細資料',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'neweb_contract.contract.line1',
            'res_id' : myrec.id,
            'views': [(form_view_id, 'form')],
            'domain': [('id', '=', self.id)],
            'target': 'new',
            'view_id': form_view_id ,
            'context': context,
        }


    def cpu_button(self):
        myrec = self.env['neweb_contract.contract.line1'].search([('id', '=', self.id)])
        try:
            form_view_id = self.env.ref("neweb_contract.view_contract_cpu_line_form").id
        except Exception as e:
            form_view_id = False
        context = dict(self._context or {})
        return {
            'type': 'ir.actions.act_window',
            'name': 'CPU明細資料',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'neweb_contract.contract.line1',
            'res_id': myrec.id,
            'views': [(form_view_id, 'form')],
            'domain': [('id', '=', self.id)],
            'target': 'new',
            'view_id': form_view_id,
            'context': context,
        }


    def ram_button(self):
        myrec = self.env['neweb_contract.contract.line1'].search([('id', '=', self.id)])
        try:
            form_view_id = self.env.ref("neweb_contract.view_contract_ram_line_form").id
        except Exception as e:
            form_view_id = False
        context = dict(self._context or {})
        return {
            'type': 'ir.actions.act_window',
            'name': 'RAM明細資料',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'neweb_contract.contract.line1',
            'res_id': myrec.id,
            'views': [(form_view_id, 'form')],
            'domain': [('id', '=', self.id)],
            'target': 'new',
            'view_id': form_view_id,
            'context': context,
        }


    def expand_card_button(self):
        myrec = self.env['neweb_contract.contract.line1'].search([('id', '=', self.id)])
        try:
            form_view_id = self.env.ref("neweb_contract.view_contract_expand_card_line_form").id
        except Exception as e:
            form_view_id = False
        context = dict(self._context or {})
        return {
            'type': 'ir.actions.act_window',
            'name': '擴充卡明細資料',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'neweb_contract.contract.line1',
            'res_id': myrec.id,
            'views': [(form_view_id, 'form')],
            'domain': [('id', '=', self.id)],
            'target': 'new',
            'view_id': form_view_id,
            'context': context,
        }


    def power_button(self):
        myrec = self.env['neweb_contract.contract.line1'].search([('id', '=', self.id)])
        try:
            form_view_id = self.env.ref("neweb_contract.view_contract_power_line_form").id
        except Exception as e:
            form_view_id = False
        context = dict(self._context or {})
        return {
            'type': 'ir.actions.act_window',
            'name': 'POWER明細資料',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'neweb_contract.contract.line1',
            'res_id': myrec.id,
            'views': [(form_view_id, 'form')],
            'domain': [('id', '=', self.id)],
            'target': 'new',
            'view_id': form_view_id,
            'context': context,
        }


class NewebContractHdLine(models.Model):
    _name = 'neweb_contract.hd_line'
    _description = "Hd Line"

    hd_id = fields.Many2one('neweb_contract.contract.line1', ondelete='cascade', string="Hd")
    hd_item = fields.Char(string="項次")
    hd_no = fields.Char(string="硬碟料號")
    hd_num = fields.Integer(string="硬碟數量")

class NewebContractCpuLine(models.Model):
    _name = 'neweb_contract.cpu_line'
    _description = "Cpu Line"

    cpu_id = fields.Many2one('neweb_contract.contract.line1', ondelete='cascade', string="Cpu")
    cpu_item = fields.Char(string="項次")
    cpu_no = fields.Char(string="CPU料號")
    cpu_num = fields.Integer(string="CPU數量")

class NewebContractRamLine(models.Model):
    _name = 'neweb_contract.ram_line'
    _description = "Ram Line"

    ram_id = fields.Many2one('neweb_contract.contract.line1', ondelete='cascade', string="Ram")
    ram_item = fields.Char(string="項次")
    ram_no = fields.Char(string="RAM料號")
    ram_num = fields.Integer(string="RAM數量")

class NewebContractExpandCardLine(models.Model):
    _name = 'neweb_contract.expand_card_line'
    _description = "Expand Card Line"

    expand_card_id = fields.Many2one('neweb_contract.contract.line1', ondelete='cascade', string="Expand Card")
    expand_card_item = fields.Char(string="項次")
    expand_card_no = fields.Char(string="擴充卡料號")
    expand_card_num = fields.Integer(string="擴充卡數量")

class NewebContractPowerLine(models.Model):
    _name = 'neweb_contract.power_line'
    _description = "Power Line"

    power_id = fields.Many2one('neweb_contract.contract.line1', ondelete='cascade', string="Power")
    power_item = fields.Char(string="項次")
    power_no = fields.Char(string="電源料號")
    power_num = fields.Integer(string="電源數量")










