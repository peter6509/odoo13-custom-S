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

class CloudRentVisitCalendar(models.Model):
    _name = "cloudrent.visit_calendar"
    _order = "visit_start_date desc"
    _description = "業者訪視行事曆"

    @api.depends('match_no')
    def _get_visitname(self):
        for rec in self:
            rec.visit_name = rec.match_no.build_lessee.escrow_man

    @api.depends('match_no')
    def _get_visitaddr(self):
        for rec in self:
            rec.visit_address = rec.match_no.writ_addr

    @api.depends('match_no')
    def _get_visitcell(self):
        for rec in self:
            rec.visit_phone = rec.match_no.lessee_cell

    subject = fields.Char(string="主旨")
    escrow_no = fields.Many2one('cloudrent.escrow',string="代管業者",default=lambda self:self.env.user.escrow_no.id)
    member_no = fields.Many2one('cloudrent.escrow_member', string="指派人員", required=True)
    match_no = fields.Many2one('cloudrent.contract_match', string="媒合編號")
    visit_name = fields.Char(string="租戶姓名",store=True,compute=_get_visitname)
    visit_address = fields.Char(string="地址",srtore=True,compute=_get_visitaddr)
    visit_phone = fields.Char(string="聯絡電話",store=True,compute=_get_visitcell)
    visit_date = fields.Datetime(string="訪視日期")
    visit_start_date = fields.Datetime(string="訪視啟始時間")
    visit_end_date = fields.Datetime(string="訪視截止時間")
    state = fields.Selection([('1', '指派'), ('2', '處理中'), ('3', '已結案')], string="處理進度",default='1')
    memo = fields.Text(string="說明")
    visit_id = fields.Many2one('cloudrent.agent_visit_service',string="訪視紀錄")
    sec_id = fields.Many2one('cloudrent.secretary_calendar',string="交辦來源cal_id")
    set_priority = fields.Selection(AVAILABLE_PRIORITIES, select=True,string="重要程度")
    assign_date = fields.Datetime(string="指派時間")
    process_start_date = fields.Datetime(string="處理開始時間")
    process_end_date = fields.Datetime(string="處理結束時間")
    close_date = fields.Datetime(string="結案時間")
    visit_tags = fields.Many2many('cloudrent.visit_calendar_tag', 'visittag_visit_calendar_rel', 'visit_id','tag_id', string="管理師標籤")

    def run_process_start(self):
        myrec = self.env['cloudrent.agent_visit_service']
        res = myrec.create({'escrow_no':self.escrow_no.id,'member_no':self.member_no.id,'match_no':self.match_no.id,'visit_name':self.visit_name,
                            'visit_start_date':self.visit_start_date,'state':'1','calendar_id':self.id})
        self.env.cr.execute("""update cloudrent_sale_calendar set state='2',process_start_date=current_timestamp,visit_id=%d where id=%d""" % (res.id,self.id))
        self.env.cr.execute("""commit""")

    def run_process_complete(self):
        self.env.cr.execute("""update cloudrent_sale_calendar set state='3',process_end_date=current_timestamp,close_date=current_timestamp where id=%d""" % self.id)
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


