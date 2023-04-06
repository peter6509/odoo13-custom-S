# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, fields, api, tools, _
import logging

_logger = logging.getLogger(__name__)


class EmpTimesheetPivotReport(models.Model):
    _name = 'neweb_emp_timesheet.timesheetpivotreport'
    _description = "Engineer Timesheet Statistics"
    _auto = False


class EmpTimesheetPivotanalysisreport(EmpTimesheetPivotReport):
    _name = 'neweb_emp_timesheet.emptimesheet_report'
    _description = "工時報工時數樞紐分析"
    _order = "dept_id,timesheet_start_date"


    timesheet_origin = fields.Char(string="來源單號",readonly=True)
    timesheet_start_date = fields.Datetime(string="啟始時間",readonly=True)
    emp_id = fields.Many2one('hr.employee',string="人員",readonly=True)
    dept_id = fields.Many2one('hr.department',string="部門",readonly=True)
    timesheet_hours = fields.Float(string="工時數",readonly=True)
    timesheet_worktype = fields.Many2one('neweb_emp_timesheet.timesheet_worktype',string="工時代碼",readonly=True)
    timesheet_work_categ = fields.Char(string="工時類別",readonly=True)
    timesheet_custom = fields.Char(string="客戶",readonly=True)
    timesheet_sale = fields.Char(string="業務員",readonly=True)




    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT timesheet.id as id,timesheet.timesheet_origin as timesheet_origin,timesheet.timesheet_start_date as timesheet_start_date,
                   timesheet.timesheet_end_date as timesheet_end_date,timesheet.emp_id as emp_id,(select get_sale_dept(timesheet.emp_id)) as dept_id,
                   abs(coalesce(timesheet.timesheet_duration,0)) as timesheet_hours,timesheet.timesheet_desc as timesheet_desc,timesheet.timesheet_worktype as timesheet_worktype,
                   timesheet_categ.worktype_categ as timesheet_work_categ,(select get_timesheetl_cus(timesheet.id)) as timesheet_custom,(select gettimesheet_sale(timesheet.id)) as timesheet_sale
                 from neweb_emp_timesheet_timesheet_calendar_line timesheet
                 LEFT JOIN neweb_emp_timesheet_timesheet_worktype timesheet_categ ON timesheet.timesheet_worktype = timesheet_categ.id
                 where  timesheet.timesheet_start_date is not null and timesheet.timesheet_end_date is not null and timesheet.timesheet_worktype is not null
                GROUP BY timesheet.id,timesheet.emp_id,timesheet.timesheet_origin,timesheet.timesheet_start_date,timesheet.timesheet_end_date,timesheet.timesheet_worktype,timesheet.timesheet_custom,
                   timesheet_categ.worktype_categ
        )""" % self._table)



class EmpTimesheetcostPivotanalysisreport(EmpTimesheetPivotReport):
    _name = 'neweb_emp_timesheet.emptimesheetcost_report'
    _description = "工時報工時數/成本費用樞紐分析"
    _order = "dept_id,timesheet_start_date"


    timesheet_origin = fields.Char(string="來源單號",readonly=True)
    timesheet_start_date = fields.Datetime(string="啟始時間",readonly=True)
    emp_id = fields.Many2one('hr.employee',string="人員",readonly=True)
    dept_id = fields.Many2one('hr.department',string="部門",readonly=True)
    timesheet_hours = fields.Float(string="工時數",readonly=True)
    timesheet_tot_expense = fields.Float(string="工時費用",readonly=True)
    timesheet_tot_cost = fields.Float(string="工時成本",readonly=True)
    timesheet_worktype = fields.Many2one('neweb_emp_timesheet.timesheet_worktype',string="工時代碼",readonly=True)
    timesheet_work_categ = fields.Char(string="工時類別",readonly=True)
    timesheet_custom = fields.Char(string="客戶",readonly=True)
    timesheet_sale = fields.Char(string="業務員",readonly=True)


    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT timesheet.id as id,timesheet.timesheet_origin as timesheet_origin,timesheet.timesheet_start_date as timesheet_start_date,
                   timesheet.timesheet_end_date as timesheet_end_date,timesheet.emp_id as emp_id,(select get_sale_dept(timesheet.emp_id)) as dept_id,
                   abs(coalesce(timesheet.timesheet_duration,0)) as timesheet_hours,timesheet.timesheet_desc as timesheet_desc,timesheet.timesheet_worktype as timesheet_worktype,
                   timesheet_categ.worktype_categ as timesheet_work_categ,(select get_timesheetl_cus(timesheet.id)) as timesheet_custom,(select gettimesheet_sale(timesheet.id)) as timesheet_sale,((select get_emp_expense(timesheet.emp_id)) * abs(timesheet.timesheet_duration)) as timesheet_tot_expense,((select get_emp_cost(timesheet.emp_id)) * abs(timesheet.timesheet_duration)) as timesheet_tot_cost
                 from neweb_emp_timesheet_timesheet_calendar_line timesheet
                 LEFT JOIN neweb_emp_timesheet_timesheet_worktype timesheet_categ ON timesheet.timesheet_worktype = timesheet_categ.id
                 where  timesheet.timesheet_start_date is not null and timesheet.timesheet_end_date is not null and timesheet.timesheet_worktype is not null
                GROUP BY timesheet.id,timesheet.emp_id,timesheet.timesheet_origin,timesheet.timesheet_start_date,timesheet.timesheet_end_date,timesheet.timesheet_worktype,timesheet.timesheet_custom,
                   timesheet_categ.worktype_categ
        )""" % self._table)


class timesheetnocompletepivot(EmpTimesheetPivotReport):
    _name = "neweb_emp_timesheet.noncomplete_report"
    _description = "工程師日報工時數未達標記錄"
    _order = "dept_id,timesheet_date"

    timesheet_date = fields.Datetime(string="日期", readonly=True)
    emp_id = fields.Many2one('hr.employee', string="人員", readonly=True)
    dept_id = fields.Many2one('hr.department', string="部門", readonly=True)
    timesheet_hours = fields.Float(string="工時數", readonly=True)
    mintimesheet_hours = fields.Float(string="最低必填時數",readonly=True)
    no_complete = fields.Integer(string="時數未達標日數",readonly=True)
    illegal_num = fields.Integer(string="記錄不合法筆數",readonly=True)

    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW %s as (
               SELECT workdate.id as id,workdate.timesheet_date as timesheet_date,workdate.emp_id as emp_id,workdate.dept_id as dept_id,
                    (select get_emp_hours(workdate.emp_id,workdate.timesheet_date)) as timesheet_hours,(select get_mintimesheet()) as mintimesheet_hours,
                    (select get_tolerance_num(workdate.emp_id,workdate.timesheet_date)) as no_complete,(select get_illegalnum(workdate.emp_id,workdate.timesheet_date))
                     as illegal_num from neweb_emp_timesheet_workdate_check workdate   
                   GROUP BY workdate.id,workdate.emp_id,workdate.timesheet_date,workdate.dept_id
           )""" % self._table)


