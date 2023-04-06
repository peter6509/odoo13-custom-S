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

class CloudRentSaleCalendar(models.Model):
    _name = "cloudrent.sale_calendar"
    _description = "業務媒合行事曆"

    subject = fields.Char(string="主旨")
    lead_date = fields.Datetime(string="時間")
    lead_start_date = fields.Datetime(string="起始時間")
    lead_end_date = fields.Datetime(string="截止時間")
    escrow_no = fields.Many2one('cloudrent.escrow',string="代管業者",default=lambda self:self.env.user.escrow_no.id)
    member_no = fields.Many2one('cloudrent.escrow_member', string="業務", required=True)
    match_no = fields.Many2one('cloudrent.contract_match', string="媒合編號")
    lessor_name = fields.Char(string="出租人姓名")
    build_address = fields.Char(string="地址")
    lessor_cell = fields.Char(string="出租人行動")
    lessee_name = fields.Char(string="承租人姓名")
    lessee_cell = fields.Char(string="承租人行動")
    stage_id = fields.Many2one('crm.stage',string="目前階段")
    memo = fields.Text(string="說明")
    state = fields.Selection([('1', '指派'), ('2', '處理中'), ('3', '已結案')], string="處理進度", default='1')
    lead_id = fields.Many2one('crm.lead',string="CRM Lead")
    sec_id = fields.Many2one('cloudrent.secretary_calendar', string="交辦來源cal_id")
    set_priority = fields.Selection(AVAILABLE_PRIORITIES, select=True,string="重要程度")
    assign_date = fields.Datetime(string="指派時間")
    process_start_date = fields.Datetime(string="處理開始時間")
    process_end_date = fields.Datetime(string="處理結束時間")
    close_date = fields.Datetime(string="結案時間")
    sale_tags = fields.Many2many('cloudrent.sale_calendar_tag','saletag_sale_calendar_rel', 'sale_id','tag_id', string="業務標籤")

    def run_process_start(self):
        self.env.cr.execute("""update cloudrent_sale_calendar set state='2',process_start_date=current_timestamp where id=%d""" % self.id)
        self.env.cr.execute("""commit""")

    def run_process_complete(self):
        self.env.cr.execute("""update cloudrent_sale_calendar set state='3',process_end_date=current_timestamp,close_date=current_timestamp where id=%d""" % self.id)
        self.env.cr.execute("""commit""")


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



