# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class CloudRentAgentVisitService(models.Model):
    _name = "cloudrent.agent_visit_service"
    _description = "租戶訪視記錄"
    _order = "visit_start_date desc"

    escrow_no = fields.Many2one('cloudrent.escrow',string="管理業者",required=True)
    member_no = fields.Many2one('cloudrent.escrow_member',string="訪視人員",required=True)
    match_no = fields.Many2one('cloudrent.contract_match',string="媒合編號",required=True)
    visit_name = fields.Char(string="訪視對象")
    visit_date = fields.Datetime(string="訪視日期")
    visit_start_date = fields.Datetime(string="訪視啟始時間")
    visit_end_date = fields.Datetime(string="訪視截止時間")
    visit_year = fields.Char(string="年")
    visit_month = fields.Char(string="月")
    visit_type = fields.Selection([('1','電訪'),('2','家訪'),('3','其他')],string="訪視方式")
    require_item = fields.Selection([('1','無特殊情況'),('2','可能無力支付租金'),('3','其他情況')],string="必要項目")
    other_alert = fields.Selection([('1','房客有急難或身心狀況不佳'),('2','違法行為疑慮'),('3','入住與申請資料不符疑慮'),('4','不當使用或裝修'),('5','住宅安全疑慮'),('6','其他')],string="其他情形通報")
    visit_memo = fields.Text(string="記錄摘要")
    visit_process = fields.Text(string="處理情形")
    state = fields.Selection([('1','處理中'),('2','已結案')],string="處理進度")
    visit_pic = fields.Binary(string="照片1",attachment=False)
    visit_pic1 = fields.Binary(string="照片2",attachment=False)
    visit_pic2 = fields.Binary(string="照片3",attachment=False)
    visit_pic3 = fields.Binary(string="照片4",attachment=False)
    visit_pic4 = fields.Binary(string="照片5",attachment=False)
    visit_pic5 = fields.Binary(string="照片6",attachment=False)
    visit_pic6 = fields.Binary(string="照片7",attachment=False)
    visit_pic7 = fields.Binary(string="照片8",attachment=False)
    visit_pic8 = fields.Binary(string="照片9",attachment=False)
    visit_pic9 = fields.Binary(string="照片10",attachment=False)
    calendar_id = fields.Many2one('cloudrent.visit_calendar',string="行事曆")

    def run_visit_complete(self):
        self.state='2'
        myrec = self.env['cloudrent.visit_calendar'].search([('id','=',self.calendar_id.id)])
        if myrec:
           myrec.run_process_complete()

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='訪視記錄已完成！'
        return {
            'name':'Success',
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'sh.message.wizard',
            'views':[(view.id,'form')],
            'view_id':view.id,
            'target':'new',
            'context':context,
            }
    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.match_no.match_no, myrec.member_no.escrow_man)
            result.append((myrec.id, myname))
        return result

    @api.onchange('escrow_no')
    def onchangeescrowno(self):
        self.member_no = self.escrow_no.bus_management.id
        self.env.cr.execute("""select getonlinematch()""")
        myrec = self.env.cr.fetchall()
        myids = []
        for rec in myrec:
            myids.append(rec[0])
        return {'domain': {'match_no': [('id', 'in', myids)]}}

    @api.depends('match_no')
    def onchangematchno(self):
        self.visit_name = self.match_no.build_lessee.escrow_man



