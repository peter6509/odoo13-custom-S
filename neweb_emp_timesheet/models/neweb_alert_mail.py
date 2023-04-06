# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class newebinspectionalertmail(models.Model):
    _name = "neweb_emp_timesheet.inspection_alert_mail"
    _description = "定檢警示通知信發送"


    emp_id = fields.Many2one('hr.employee', string="工程師")
    dept_id = fields.Many2one('hr.department', string="部門")
    cus_id = fields.Many2one('res.partner', string="客戶")
    contract_no = fields.Many2one('neweb_contract.contract', string="合約")
    inspection_datetime = fields.Datetime(string="排定日期時間")
    inspection_complete = fields.Selection([('Y', "已完成"), ('N', "未完成")], default='N', string="狀態")
    inspection_alert1 = fields.Boolean(string="已警示1?", default=False)
    inspection_alert2 = fields.Boolean(string="已警示2?", default=False)
    alert_date1 = fields.Date(string="警示日期1")
    alert_date2 = fields.Date(string="警示日期2")
    emp_manager = fields.Many2one('hr.employee', string="主管")
    inspection_name = fields.Char(string="事件名稱")
    inspection_sequence = fields.Integer(string="source id")

    def delmailmessage(self):
        self.env.cr.execute("""select delmailmessage()""")
        self.env.cr.execute("""commit""")


    def rungenalertmail1(self):
        self.env.cr.execute("""select run_inspection_alert_mail1()""")
        self.env.cr.execute("""commit""")
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_emp_timesheet', 'neweb_inspection_alert_mail1')[1]
        except ValueError:
            template_id = False
        myrec = self.env['neweb_emp_timesheet.inspection_alert_mail'].search([])
        for rec in myrec:
            self.env['mail.template'].browse(template_id).send_mail(rec.id)
            self.env.cr.execute("""update neweb_emp_timesheet_inspection_calendar set inspection_alert1=TRUE 
                 where id=%d""" % rec.inspection_sequence)
            self.env.cr.execute("""commit""")

    def rungenalertmail2(self):
        self.env.cr.execute("""select run_inspection_alert_mail2()""")
        self.env.cr.execute("""commit""")

        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_emp_timesheet', 'neweb_inspection_alert_mail2')[1]
        except ValueError:
            template_id = False
        myrec = self.env['neweb_emp_timesheet.inspection_alert_mail'].search([])
        for rec in myrec:
            self.env['mail.template'].browse(template_id).send_mail(rec.id)
            self.env.cr.execute("""update neweb_emp_timesheet_inspection_calendar set inspection_alert2=TRUE 
                         where id=%d""" % rec.inspection_sequence)
            self.env.cr.execute("""commit""")