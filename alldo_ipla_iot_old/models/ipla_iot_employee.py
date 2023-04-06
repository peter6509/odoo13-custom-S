# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class alldoiplaiotempinerit(models.Model):
    _inherit = "hr.employee"

    emp_code = fields.Char(string="員工編號")
    attendance_line = fields.One2many('alldo_ipla_iot.emp_attendance','attendance_id',string="出勤明細")
    duty_type = fields.Selection([('1',u'正常上班'),('2',u'正常下班'),('3','加班上班'),('4','加班下班')],string=u"出勤狀態",default='2')
    duty_name = fields.Char(string="出勤狀態",compute='_get_duty')
    duty_datetime = fields.Datetime(string="最後異動時間")

    @api.depends('duty_type')
    def _get_duty(self):
        for rec in self:
            if rec.duty_type=='1':
               rec.duty_name='正常上班'
            elif rec.duty_type=='2':
               rec.duty_name='正常下班'
            elif rec.duty_type=='3':
               rec.duty_name = '加班上班'
            elif  rec.duty_type=='4':
                rec.duty_name = '加班下班'
    @api.model
    def create(self, vals):
        if 'emp_code' in vals and not vals['emp_code']:
            raise UserError("未輸入 員工編號！")
        mycount = self.env['hr.employee'].search_count([('emp_code', '=', vals['emp_code'])])
        if mycount > 0:
            raise UserError("員工編號已重複！")
        res = super(alldoiplaiotempinerit, self).create(vals)
        return res

    def _write(self, vals):
        res = super(alldoiplaiotempinerit, self)._write(vals)
        for rec in self:
            mycount = self.env['hr.employee'].search_count([('emp_code','=',rec.emp_code)])
            if mycount > 1 :
                raise UserError("員工編號已重複！")

        return res



class alldoiplaiotempattendance(models.Model):
    _name = "alldo_ipla_iot.emp_attendance"
    _description = "員工出勤時間表"
    _order = "attendance_date desc"

    attendance_id = fields.Many2one('hr.employee',ondelete='cascade',required=True)
    attendance_date = fields.Datetime(string="刷卡時間")
    attendance_type = fields.Selection([('1','正常上班'),('2','正常下班'),('3','加班上班'),('4','加班下班')],string="刷卡類別")
    attendance_name = fields.Char(string="刷卡說明",compute='_get_attendancename')

    @api.depends('attendance_type')
    def _get_attendancename(self):
        for rec in self:
            if rec.attendance_type=='1' :
                rec.attendance_name='正常上班'
            elif rec.attendance_type=='2':
                rec.attendance_name='正常下班'
            elif rec.attendance_type=='3':
                rec.attendance_name = '加班上班'
            elif rec.attendance_type=='4':
                rec.attendance_name = '加班下班'
    


