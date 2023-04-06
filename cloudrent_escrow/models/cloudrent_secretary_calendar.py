# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
AVAILABLE_PRIORITIES = [
    ('0', '最低'),
    ('1', '低'),
    ('2', '普通'),
    ('3', '高'),
    ('4', '最高')]

class CloudRentSecretaryCalendar(models.Model):
    _name = "cloudrent.secretary_calendar"
    _description = "秘書行事曆"
    _order = "sec_start_date desc"

    subject = fields.Char(string="主旨")
    escrow_no = fields.Many2one('cloudrent.escrow', string="代管業者", default=lambda self: self.env.user.escrow_no.id)
    sec_start_date = fields.Datetime(string="指派啟始時間")
    sec_end_date = fields.Datetime(string="指派截止時間")
    member_no = fields.Many2one('cloudrent.escrow_member',string="指派人員")
    match_no = fields.Many2one('cloudrent.contract_match',string="媒合編號")
    memo = fields.Text(string="指派內容說明")
    set_priority = fields.Selection(AVAILABLE_PRIORITIES, select=True,string="重要程度")
    state = fields.Selection([('1', '指派'), ('2', '處理中'), ('3', '已結案')], string="處理進度", default='1')
    assign_date = fields.Datetime(string="指派時間")
    process_start_date = fields.Datetime(string="處理開始時間")
    process_end_date = fields.Datetime(string="處理結束時間")
    close_date = fields.Datetime(string="結案時間")
    assign_type = fields.Selection([('1','管理師'),('2','業務'),('3','修繕廠商')],string="指派類別")
    target_id = fields.Integer(string="TargetID")
    sale_tags = fields.Many2many('cloudrent.sale_calendar_tag','saletag_secretary_calendar_rel','secretary_id','tag_id',string="業務標籤")
    visit_tags = fields.Many2many('cloudrent.visit_calendar_tag','visittag_secretary_calendar_rel','secretary_id','tag_id',string="管理師標籤")
    repair_tags = fields.Many2many('cloudrent.repair_calendar_tag','repairtag_secretary_calendar_rel','secretary_id','tag_id',string="修繕標籤")

    def name_get(self):
        result = []
        for myrec in self:
            if myrec.set_priority == '0':
                mypri = '最低'
            elif myrec.set_priority == '1':
                mypri = '低'
            elif myrec.set_priority == '2':
                mypri = '普通'
            elif myrec.set_priority == '3':
                mypri = '高'
            elif myrec.set_priority == '4':
                mypri = '最高'
            else:
                mypri = '最低'
            myname = "[%s] (%s)" % (myrec.subject,mypri)
            result.append((myrec.id, myname))
        return result

