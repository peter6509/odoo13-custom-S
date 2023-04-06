# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebrepaircalendar(models.Model):
    _name = "neweb_emp_timesheet.repair_calendar"
    _description = "客戶報修行事曆"

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
    def _get_repairname(self):
        for rec in self:
            rec.update({'repair_name': "[%s]%s-%s" % (rec.repair_no.name, rec.cus_id.name, rec.emp_id.name)})

    emp_id = fields.Many2one('hr.employee',string="工程師")
    dept_id = fields.Many2one('hr.department',string="部門",compute=_get_empdept,store=True)
    cus_id = fields.Many2one('res.partner',string="客戶")
    contract_no = fields.Many2one('neweb_contract.contract',string="合約")
    repair_no = fields.Many2one('neweb_repair.repair',string="報修單號")
    repair_datetime = fields.Datetime(string="報修日期時間")
    repair_complete = fields.Selection([
        ('repair_draft', u'草稿'),  # 草稿
        ('repair_waiting', u'等待中'),  # 等料中
        ('repair_AE', u'工程師處理中'),  # 工程師處理
        ('repair_Manager',  u'等待工程師主管審核'),  # 指派工程師主管審核
        ('repair_done', u'完成'),  # 結案
        ('repair_cancel', u'取消'),  # 作廢
        ('repair_reject', u'退回'),  # 退回(internal use)
        ('repair_open', u'開啟'),  # 進call(internal use)
        ('repair_closed', u'結案'),  # 結束flow(internal use)
    ], string=u'狀態', default='repair_draft')
    emp_manager = fields.Many2one('hr.employee',string="主管",compute=_get_empmanager,store=True)
    repair_name = fields.Char(string="事件名稱",compute=_get_repairname,store=True)
    repair_sequence = fields.Integer(string="repair origin id")


    def write(self, vals):
        if 'repair_datetime' in vals:
            raise UserError("報修記錄無法改變時間！")
        res = super(newebrepaircalendar, self).write(vals)
        return res



