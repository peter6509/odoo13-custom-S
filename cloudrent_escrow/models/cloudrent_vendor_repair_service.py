# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class CloudRentVendorRepairService(models.Model):
    _name = "cloudrent.vendor_repair_service"
    _description = "廠商修繕記錄"
    _order = "repair_start_date desc"

    escrow_no = fields.Many2one('cloudrent.escrow',string="代管業者",default=lambda self:self.env.user.escrow_no.id)
    member_no = fields.Many2one('cloudrent.escrow_member',string="修繕人員",required=True)
    match_no = fields.Many2one('cloudrent.contract_match',string="媒合編號",required=True)
    repair_name = fields.Char(string="修繕對象")
    repair_date = fields.Datetime(string="修繕日期")
    repair_start_date = fields.Datetime(string="修繕啟始時間")
    repair_end_date = fields.Datetime(string="修繕截止時間")
    repair_year = fields.Char(string="年")
    repair_month = fields.Char(string="月")
    repair_memo = fields.Text(string="記錄摘要")
    repair_process = fields.Text(string="處理情形")
    state = fields.Selection([('1','處理中'),('2','已結案')],string="處理進度")
    repair1_pic1 = fields.Binary(string="修繕前照片1",attachment=False)
    repair1_pic2 = fields.Binary(string="修繕前照片2",attachment=False)
    repair1_pic3 = fields.Binary(string="修繕前照片3",attachment=False)
    repair2_pic1 = fields.Binary(string="修繕後照片1",attachment=False)
    repair2_pic2 = fields.Binary(string="修繕後照片2",attachment=False)
    repair2_pic3 = fields.Binary(string="修繕後照片3",attachment=False)
    calendar_id = fields.Many2one('cloudrent.repair_calendar',string="行事曆")

    def run_repair_complete(self):
        self.state='2'
        myrec = self.env['cloudrent.repair_calendar'].search([('id','=',self.calendar_id.id)])
        if myrec:
            myrec.run_process_complete()

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='廠商修繕已完成!'
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
            myname = "[%s-%s]%s" % (myrec.match_no.match_no,myrec.repair_name, myrec.member_no.escrow_man)
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
        self.repair_name = self.match_no.build_lessee.escrow_man



