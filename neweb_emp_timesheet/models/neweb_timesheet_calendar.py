# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import datetime,pytz
#from datetime import datetime,timedelta,time

from datetime import datetime,time
from dateutil.relativedelta import relativedelta

class newebtimesheetcalendar(models.Model):
    _name = "neweb_emp_timesheet.timesheet_calendar"
    inherit = "calendar"
    _description = "工程師工時報工行事曆主檔"
    _order = "timesheet_yearmonth,emp_id"

    emp_id = fields.Many2one('hr.employee',domain=[('active','=',True)],string="員工",
                             default=lambda self:self._get_emp(),)
    timesheet_yearmonth = fields.Char(size=(7),string="工時年月",required=True)
    is_closed = fields.Boolean(string="關帳",default=False)
    level_manager = fields.Integer(string="簽核層數")
    running_level = fields.Integer(string="目前待簽階層")
    emp_manager1 = fields.Many2one('hr.employee',domain=[('active','=',True)])
    emp_manager2 = fields.Many2one('hr.employee',domain=[('active','=',True)])
    emp_manager3 = fields.Many2one('hr.employee',domain=[('active','=',True)])
    emp_manager4 = fields.Many2one('hr.employee',domain=[('active','=',True)])
    emp_manager5 = fields.Many2one('hr.employee',domain=[('active','=',True)])
    emp_approve1 = fields.Datetime(string="Level1 Manager簽核時間")
    line_ids = fields.One2many('neweb_emp_timesheet.timesheet_calendar_line','line_id',copy=False)


    def daily_recheck_calendar(self):
        self.env.cr.execute("""select recheckcalendar()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select recheckduration()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gentimesheetsale()""")
        self.env.cr.execute("""commit""")


    def _get_emp(self):
        myuid = self.env.uid
        myemprec = self.env['hr.employee'].search([('user_id','=',myuid)])
        if myemprec:
            myres = myemprec[0].id
        else:
            myres = None
        return myres



    def name_get(self):
        result = []
        for myrec in self:
            mytimesheetname = "%s [%s]" % (myrec.emp_id.name,myrec.timesheet_yearmonth)
            result.append((myrec.id, mytimesheetname))
        return result

    @api.model
    def create(self, vals):
        myempid = vals['emp_id']
        mytimesheet = vals['timesheet_yearmonth']
        self.env.cr.execute("""select checkemptimesheet(%d,'%s')""" % (myempid,mytimesheet))
        myres = self.env.cr.fetchone()[0]
        if myres:
            myempname = self.env['hr.employee'].search([('id','=',myempid)]).name
            raise UserError("（人員：%s 工時年月：%s) 的工時記錄已建檔,請確認！" % (myempname,mytimesheet))
        res = super(newebtimesheetcalendar, self).create(vals)
        self.env.cr.execute("""select sorttimesheetitem(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res


    def write(self,vals):
        res=super(newebtimesheetcalendar, self).write(vals)
        for rec in self:
            mylogin = self.env.uid
            self.env.cr.execute("""select getadjustowner(%d)""" % mylogin)
            canadj = self.env.cr.fetchone()[0]
            if rec.is_closed == True and not canadj:
                raise UserError("工時表已關帳,無法修改了！")

            self.env.cr.execute("""select sorttimesheetitem(%d)""" % rec.id)
            self.env.cr.execute("""commit""")

        return res

class newebtimesheetcalendarline(models.Model):
    _name = "neweb_emp_timesheet.timesheet_calendar_line"
    _description = "工程師工時報工行事曆明細檔"
    _order = "emp_id,timesheet_start_date"
    _rec_name = 'timesheet_name'

    @api.depends('emp_id', 'timesheet_worktype', 'timesheet_desc','timesheet_custom')
    def _get_timesheetname(self):
        myname = ' '
        for rec in self:
            if not rec.timesheet_custom:
                if not rec.emp_id:
                    myname = "本日是休假日-[%s]" % rec.timesheet_desc
                else:
                    myname = "[%s %s]%s" % (rec.timesheet_worktype.worktype_code, rec.timesheet_worktype.worktype_desc,rec.emp_id.name)
            else:
                if not rec.emp_id:
                    myname = "本日是休假日-[%s]" % rec.timesheet_desc
                else:
                    myname = "[%s %s]%s-%s" % (rec.timesheet_worktype.worktype_code,rec.timesheet_custom.name, rec.timesheet_worktype.worktype_desc,rec.emp_id.name)
            rec.update({'timesheet_name': myname})
            return myname


    def _get_startdt(self):
        self.env.cr.execute("""select get_startdt()""")
        myres = self.env.cr.fetchone()[0]
        self.timesheet_start_date = myres
        return myres

    line_id = fields.Many2one('neweb_emp_timesheet.timesheet_calendar',ondelete='cascade')
    sequence = fields.Integer(default=20)
    nitem = fields.Integer(string="ITEM")
    emp_id = fields.Many2one('hr.employee',default=lambda self:self._get_emp(),store=True,string="員工")
    # emp_id1 = fields.Many2many('hr.employee','neweb_timesheet_hr_employee_rel','time_id','emp_id', default=lambda self: self._get_emp(), string="員工1")
    timesheet_start_date = fields.Datetime(string="開始時間",required=True)
    timesheet_end_date = fields.Datetime(string="截止時間",required=True)
    timesheet_duration = fields.Float(digits=(4,1),string="時間",default=0)
    timesheet_worktype = fields.Many2one('neweb_emp_timesheet.timesheet_worktype',string="工時代碼",required=True)
    timesheet_custom = fields.Many2one('res.partner',string="客戶/供應商",domain=[('is_company','=',True)])
    timesheet_origin = fields.Char(string='單據號碼')
    timesheet_desc = fields.Text(string="工時說明")
    duration = fields.Float(string="時間長(hr)")
    timesheet_name = fields.Char(compute=_get_timesheetname)
    origin_id = fields.Integer(string="來源資料ID")
    origin_type = fields.Selection([('1','定保'),('2','報修'),('3','人力派工單'),('4','裝機派工')],string="工時來源")
    is_locked = fields.Boolean(string="鎖定?",default=False)
    is_complete = fields.Selection([('ok','OK'),('ng','NG')],string="資料狀況",default='ok')
    sale_id = fields.Many2one('hr.employee',string="業務人員")
    timesheet_pivottype = fields.Selection([('1','建置工時'),('2','維護工時'),('3','維運工時'),('4','保固支援工時'),('5','一般工時')])

    def _get_emp(self):
        myuid = self.env.uid
        myemprec = self.env['hr.employee'].search([('user_id','=',myuid)])
        if myemprec:
            myres = myemprec[0].id
        else:
            myres = None
        return myres


    @api.onchange('timesheet_origin')
    def onchangeorigin(self):
        self.env.cr.execute("""select get_timesheet_origin('%s')""" % self.timesheet_origin)
        myres = self.env.cr.fetchone()[0]
        if myres != 0 :
           self.timesheet_custom = myres
        self.env.cr.execute("""select gettimesheetsale('%s')""" % self.timesheet_origin)
        myres = self.env.cr.fetchone()[0]
        if myres != 0:
            self.sale_id = myres


    #def name_get(self):
    #    result = []
    #    for myrec in self:
    #        mytimesheetlinename = "%s [%s]" % (myrec.emp_id.name, myrec.timesheet_worktype.worktype_code)
    #        result.append((myrec.id, mytimesheetlinename))
    #    return result


    @api.model
    def create(self, vals):
        myinputtype = self.env.context.get('calendarinput' or False)
        if 'timesheet_start_date' in vals and not vals['timesheet_start_date'] :
            raise UserError("日期時間未輸入")
        if myinputtype == 1:
            self.env.cr.execute("""select getempidbyuserid(%d)""" % self.env.uid)
            myempid = self.env.cr.fetchone()[0]
            mystartdate = vals['timesheet_start_date']
            print(mystartdate[0:7])
            self.env.cr.execute("""select gettimesheetlineid(%d,'%s')""" % (myempid, mystartdate[0:7]))
            mylineid = self.env.cr.fetchone()[0]
            if mylineid > 0:
                vals['line_id'] = mylineid
        if 'timesheet_worktype' in vals and not vals['timesheet_worktype']:
            raise UserError("未輸入工時代碼,請確認！")
        self.env.cr.execute("""select getworktype(%d)""" % vals['timesheet_worktype'])
        myres = self.env.cr.fetchone()[0]
        if myres[0:1] == '4' and not vals['timesheet_origin'] and not vals['sale_id']:
            raise UserError("沒有輸入單號,需要指定業務員")
        if 'line_id' not in vals and myinputtype:
            if 'emp_id' in vals and not vals['emp_id']:
                self.env.cr.execute("""select getempidbyuserid(%d)""" % self.env.user_id)
                vals['emp_id'] = self.env.cr.fetchone()[0]
            if 'emp_id' in vals and vals['emp_id'] and 'timesheet_start_date' in vals and vals['timesheet_start_date'] :
                myempid = vals['emp_id']
                mystartdate = vals['timesheet_start_date']
                self.env.cr.execute("""select gettimesheetlineid(%d,'%s')""" % (myempid,mystartdate[0:7]))
                mylineid = self.env.cr.fetchone()[0]
                if mylineid > 0 :
                    vals['line_id']=mylineid

        res = super(newebtimesheetcalendarline, self).create(vals)
        self.env.cr.execute("""select checklinetimeerror(%d)""" % res.id)
        myres = self.env.cr.fetchone()[0]
        if myres:
            raise UserError("輸入的工時的日期有跨日,或歸屬年月不正確,請確認！")
        self.env.cr.execute("""select checkcalendarline(%d)""" % res.id)
        self.env.cr.execute("""commit""")

        return res

    def write(self, vals):
        # if 'timesheet_start_date' in vals:
        #      raise UserError("已存檔工時記錄無法移動！")
        if 'timesheet_worktype' in vals and not vals['timesheet_worktype']:
            raise UserError("未輸入工時代碼,請確認！")

        res = super(newebtimesheetcalendarline, self).write(vals)
        for rec in self:
            mylogin = self.env.uid
            self.env.cr.execute("""select getadjustowner(%d)""" % mylogin)
            canadj = self.env.cr.fetchone()[0]
            if rec.is_locked == True and not canadj:
                raise UserError("工時表已關帳,無法修改了!")
            self.env.cr.execute("""select getworktype(%d)""" % rec.timesheet_worktype.id)
            myres = self.env.cr.fetchone()[0]
            # print "worktype:%s" % myres
            # print "timesheet_origin:%s" % rec.timesheet_origin
            # print "sale_id:%s" % rec.sale_id.id
            if myres[0:1] == '4' and rec.timesheet_origin == False and rec.sale_id.id == False :
                raise UserError("沒有輸入單號,需要指定業務員")
            self.env.cr.execute("""select checklinetimeerror(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            #if myres:
            #    raise UserError("輸入的工時的日期有跨日,或歸屬年月不正確,請確認！")
            self.env.cr.execute("""select checkcalendarline(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res


class newebtimesheetlock(models.Model):
    _name = "neweb_emp_timesheet.timesheet_lock"
    _description = "工時報工關帳鎖定設定"
    _rec_name = "yearmonth"

    yearmonth = fields.Char(size=7,string="鎖定工時年月",required=True)
    lock_date = fields.Date()

    @api.model
    def create(self, vals):
        myres = self.env['neweb_emp_timesheet.timesheet_lock'].search_count([])
        if myres > 0:
            raise UserError('只能一筆記錄')
        res = super(newebtimesheetlock, self).create(vals)
        self.env.cr.execute("""select setlocktimesheetdate()""")
        self.env.cr.execute("""commit""")
        return res

    def write(self, vals):
        res = super(newebtimesheetlock, self).write(vals)
        self.env.cr.execute("""select setlocktimesheetdate()""")
        self.env.cr.execute("""commit""")
        return res


class newebtimesheetadjustowner(models.Model):
    _name = "neweb_emp_timesheet.timesheet_adjustowner"
    _description = "關帳後可調整人員"
    _rec_name = "timesheet_adjustowner"

    timesheet_adjustowner = fields.Many2one('res.users',string='可調整人員')

