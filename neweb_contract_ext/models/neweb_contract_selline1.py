# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewConSelcontract(models.Model):
    _name = "neweb_contract.contract_sel"
    _description = "舊約勾選項目HEAD"

    sel_line = fields.One2many('neweb_contract.contract_selline', 'sel_id', string="勾選項目LINE")
    contract_id = fields.Integer(string="Origin 合約ID")
    contract_id1 = fields.Integer(string="NEW 合約ID")

    def allsel_button(self):
        myrec = self.env['neweb_contract.contract_selline'].search([])
        myrec.selitem=True

    def allnosel_button(self):
        myrec = self.env['neweb_contract.contract_selline'].search([])
        myrec.selitem=False

    def selectbtn(self):
        myid = self.env['neweb_contract.contract_sel'].search([]).contract_id1
        myrec = self.env['neweb_contract.contract'].search([('id','=',myid)])
        self.env.cr.execute("""select gencontractselline()""")
        self.env.cr.execute("""commit""")
        return {'view_name': 'neweb_contract_contract',
                'name': ('合約主檔'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'neweb_contract.contract',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': myrec.id,
                'view_mode': 'form',
                'view_type': 'form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }

class NewebConSelLine1(models.Model):
    _name = "neweb_contract.contract_selline"
    _description = "舊約勾選項目LINE"

    sel_id = fields.Many2one('neweb_contract.contract_sel', string="勾選項目")
    contract_id = fields.Integer(string="合約ID")
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
    expand_module = fields.Char(string="擴充模組")
    machine_other = fields.Char(string="其他")
    machine_loc = fields.Char(string="設備位址")
    contract_line_id = fields.Integer(string="Origin ID")
    selitem = fields.Boolean(string="勾選",default=False)

    def sel_button(self):
        if self.selitem==False:
            self.selitem=True
        else:
            self.selitem=False


