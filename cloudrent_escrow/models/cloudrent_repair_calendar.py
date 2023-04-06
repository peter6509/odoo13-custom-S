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

class CloudRentRepairCalendar(models.Model):
    _name = "cloudrent.repair_calendar"
    _order = "repair_start_date desc"
    _description = "修繕廠商行事曆"

    @api.depends('match_no')
    def _get_repairname(self):
        for rec in self:
            rec.repair_name = rec.match_no.build_lessee.escrow_man

    @api.depends('match_no')
    def _get_repairaddr(self):
        for rec in self:
            rec.repair_address = rec.match_no.writ_addr

    @api.depends('match_no')
    def _get_repaircell(self):
        for rec in self:
            rec.repair_phone = rec.match_no.lessee_cell

    subject = fields.Char(string="主旨")
    escrow_no = fields.Many2one('cloudrent.escrow',string="代管業者",default=lambda self:self.env.user.escrow_no.id)
    member_no = fields.Many2one('cloudrent.escrow_member', string="指派廠商", required=True)
    match_no = fields.Many2one('cloudrent.contract_match', string="媒合編號")
    repair_name = fields.Char(string="修繕租戶姓名",store=True,compute=_get_repairname)
    repair_address = fields.Char(string="修繕地址",srtore=True,compute=_get_repairaddr)
    repair_phone = fields.Char(string="聯絡電話",store=True,compute=_get_repaircell)
    repair_date = fields.Datetime(string="修繕日期")
    repair_start_date = fields.Datetime(string="修繕啟始時間")
    repair_end_date = fields.Datetime(string="修繕截止時間")
    state = fields.Selection([('1', '指派'), ('2', '處理中'), ('3', '已結案')], string="處理進度",default='1')
    memo = fields.Text(string="說明")
    repair_id = fields.Many2one('cloudrent.vendor_repair_service',string="修繕紀錄")
    sec_id = fields.Many2one('cloudrent.secretary_calendar',string="交辦來源cal_id")
    set_priority = fields.Selection(AVAILABLE_PRIORITIES, select=True,string="重要程度")
    assign_date = fields.Datetime(string="指派時間")
    process_start_date = fields.Datetime(string="處理開始時間")
    process_end_date = fields.Datetime(string="處理結束時間")
    close_date = fields.Datetime(string="結案時間")
    repair_tags = fields.Many2many('cloudrent.repair_calendar_tag', 'repairtag_repair_calendar_rel', 'repair_id','tag_id', string="修繕標籤")

    def run_process_start(self):
        self.env.cr.execute("""update cloudrent_repair_calendar set state='2',process_start_date=current_timestamp where id=%d""" % self.id)
        self.env.cr.execute("""commit""")

    def run_process_complete(self):
        self.env.cr.execute("""update cloudrent_repair_calendar set state='3',process_end_date=current_timestamp,close_date=current_timestamp where id=%d""" % self.id)
        self.env.cr.execute("""commit""")

    def name_get(self):
        result = []
        for myrec in self:
            if myrec.set_priority=='0':
                mypri = '最低'
            elif myrec.set_priority=='1':
                mypri = '低'
            elif myrec.set_priority=='2':
                mypri = '普通'
            elif myrec.set_priority=='3':
                mypri = '高'
            elif myrec.set_priority=='4':
                mypri = '最高'
            else:
                mypri = '最低'
            myname = "[%s] (%s)" % (myrec.subject,mypri)
            result.append((myrec.id, myname))
        return result


