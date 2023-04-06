# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebinspectioncalendar(models.Model):
    _name = "neweb_emp_timesheet.inspection_calendar"
    _description = "工程師定保行事曆"
    _rec_name = 'inspection_name'

    @api.depends('emp_id')
    def _get_empmanager(self):
        for rec in self:
            mymanager = self.env['hr.employee'].search([('id', '=', rec.emp_id.id)]).parent_id
            rec.update({'emp_manager': mymanager})

    @api.depends('emp_id')
    def _get_empdept(self):
        for rec in self:
            mydept = self.env['hr.employee'].search([('id', '=', rec.emp_id.id)]).department_id
            rec.update({'dept_id': mydept})

    @api.depends('emp_id')
    def _get_inspectionname(self):
        for rec in self:
            rec.update({'inspection_name': "[%s]%s-%s" % (rec.contract_no.name, rec.cus_id.name, rec.emp_id.name)})

    emp_id = fields.Many2one('hr.employee',string="工程師")
    dept_id = fields.Many2one('hr.department',string="部門",compute=_get_empdept,store=True)
    cus_id = fields.Many2one('res.partner',string="客戶")
    contract_no = fields.Many2one('neweb_contract.contract',string="合約")
    inspection_datetime = fields.Datetime(string="排定日期時間")
    inspection_complete = fields.Selection([('Y',"已完成"),('N',"未完成")],default='N',string="狀態")
    inspection_alert1 = fields.Boolean(string="已警示1?",default=False)
    inspection_alert2 = fields.Boolean(string="已警示2?",default=False)
    alert_date1 = fields.Date(string="警示日期1")
    alert_date2 = fields.Date(string="警示日期2")
    emp_manager = fields.Many2one('hr.employee',string="主管",compute=_get_empmanager,store=True)
    inspection_name = fields.Char(string="事件名稱",compute=_get_inspectionname,store=True)
    inspection_sequence = fields.Integer(string="inspection origin id")
    inspection_start_datetime = fields.Datetime(string="實際維護啟始時間")
    inspection_end_datetime = fields.Datetime(string="實際維護截止時間")
    inspection_memo = fields.Text(string="Memo")



    def write(self,vals):

        res = super(newebinspectioncalendar, self).write(vals)
        myuid = self.env.uid
        for rec in self:
            self.env.cr.execute("""select checkinspectiondate1(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]

            if myres == '2':
                raise UserError("單筆記錄只能同一日期,如有不同日期請創建另一筆！")
            if myres == '3':
                raise UserError("起始時間跟結束時間沒有時間差")
            self.env.cr.execute("""select update_inscalendar_datetime(%d,%d)""" % (rec.id,myuid))
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select inspection_ch_todo(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res



