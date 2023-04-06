# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class cloudrentLandlordContract(models.Model):
    _name = "cloudrent.landlord_contract"
    _description = "CloudRent房東合約管理"

    name = fields.Char(string="合約編號", default='New', copy=False)
    project_no = fields.Many2many('cloudrent.household_house', 'cloudrent_landlord_contract_house_rel','contract_id','house_id',string="簽約案場", required=True)
    line_user_ids = fields.One2many('cloudrent.landlord_line_user','contract_id',string="房東LINE User",copy=False)
    landlord_pid = fields.Char(string="身分證號", required=True)
    contract_type = fields.Selection([('1', '新約'), ('2', '續約')], string="合約類型", default='1')
    landlord_name = fields.Char(string="房東姓名")
    landlord_email = fields.Char(string="EMAIL")
    income_date = fields.Date(string="簽約日期")
    start_rental = fields.Date(string="起租日期")
    end_rental = fields.Date(string="退租日期")
    landlord_address1 = fields.Char(string="聯絡地址1")
    landlord_address2 = fields.Char(string="聯絡地址2")
    landlord_phone1 = fields.Char(string="聯絡電話1")
    landlord_phone2 = fields.Char(string="聯絡電話2")
    landlord_phone3 = fields.Char(string="聯絡電話3")
    landlord_phone4 = fields.Char(string="聯絡電話4")
    landlord_desc = fields.Text(string="備註")
    states = fields.Selection([('1', '草稿'), ('2', '已生效'), ('3', '已失效')], string="合約狀態", default='1')
    active = fields.Boolean(string="ACTIVE", default=True)
    contract_attachment = fields.Binary(string="合約PDF")
    month_fee = fields.Integer(string="每月月租(每戶)元？",default=0)
    have_contract_data = fields.Boolean(string="合約管理資料輸入服務?",default=False)
    contract_data_fee = fields.Integer(string="合約管理資料輸入(每筆)元？",default=0)
    have_emeter = fields.Boolean(string="雲端數位電錶租用?",default=False)
    emeter_fee = fields.Integer(string="雲端數位電錶租用(每月)元?",default=0)
    have_account_push = fields.Boolean(string="帳務推送服務?",default=False)
    account_push_fee = fields.Integer(string="帳務推送(每則)元?",default=0)
    have_call_notice = fields.Boolean(string="逾期催繳服務?",default=False)
    call_notice_fee = fields.Integer(string="逾期催繳(每則)元?",default=0)
    have_repair_message = fields.Boolean(string="報修訊息推送服務?",default=False)
    repair_message_fee = fields.Integer(string="報修訊息推送(每則)元？",default=0)



    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('cloudrent.landlord_contract') or _('New')
        res = super(cloudrentLandlordContract, self).create(vals)
        return res

    def landlord_user_update(self):   # 房東系統使用者/Line 使用者變更 Refresh
        A=1


class cloudrentLandlordLineUser(models.Model):
    _name = "cloudrent.landlord_line_user"
    _description = "房東LINE User"

    contract_id = fields.Many2one('cloudrent.landlord_contract',ondelete='cascade')
    landlord_pid = fields.Char(string="身份字號")
    landlord_name = fields.Char(string="姓名")
    user_id = fields.Many2one('res.users', string="使用者")
    line_user_id = fields.Char(string='Line User ID')
    line_rich_menu_id = fields.Char(string='Line Rich menu ID')
    active = fields.Boolean(string="ARCHIVE",default=True)


