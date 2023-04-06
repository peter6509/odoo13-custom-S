# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebhrholiday(models.Model):
    _name = "neweb_emp_timesheet.hrholiday"
    _description = "公司年度例假日主檔"
    _rec_name = "hr_holiday_year"
    _order = "hr_holiday_year"

    hr_holiday_year = fields.Char(string="年度",size=4)
    hr_holiday_line = fields.One2many('neweb_emp_timesheet.hrholiday_line','holiday_id',string="假日明細",copy=False)


    @api.model
    def create(self, vals):
        if 'hr_holiday_year' in vals and not vals['hr_holiday_year']:
            raise UserError("未輸入年度")
        if int(vals['hr_holiday_year']) <= 2018 or int(vals['hr_holiday_year']) >= 2030:
            raise UserError("年度數字不正確")
        myhoyear = vals['hr_holiday_year']
        mycount = self.env['neweb_emp_timesheet.hrholiday'].search_count([('hr_holiday_year','=',myhoyear)])
        if mycount > 0 :
            raise UserError("年度重複了")
        res = super(newebhrholiday, self).create(vals)
        self.env.cr.execute("""select gen_holiday_line(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select genhototimesheet(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        # self.env.cr.execute("""select gen_workdate_data(%d)""" % res.id)
        # self.env.cr.execute("""commit""")
        return res

    def write(self, vals):
        if 'hr_holiday_year' in vals and not vals['hr_holiday_year']:
            raise UserError("未輸入年度")
        if 'hr_holiday_year' in vals and vals['hr_holiday_year']:
            raise UserError("不能修改年度")
        res = super(newebhrholiday, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select regenholidayitem(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select delhototimesheet(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select genhototimesheet(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            # self.env.cr.execute("""select gen_workdate_data(%d)""" % rec.id)
            # self.env.cr.execute("""commit""")
        return res


    def unlink(self):
        for rec in self:
            self.env.cr.execute("""select delhototimesheet(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        res = super(newebhrholiday, self).unlink()
        return res


    def run_timesheet_holiday(self):
        myid = self.env.context.get("holidayyear")


class newebhrholidayline(models.Model):
    _name = "neweb_emp_timesheet.hrholiday_line"
    _description = "公司年度例假日明細檔"
    _order = "nitem"

    holiday_id = fields.Many2one('neweb_emp_timesheet.hrholiday',required=True,ondelete='cascade')
    nitem = fields.Integer(string="ITEM",default=1)
    holiday_date = fields.Date(string="休假日期")
    holiday_memo = fields.Text(string="假日說明")


    def unlink(self):
        for rec in self:
            self.env.cr.execute("""select delholinetotimesheet(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        res = super(newebhrholidayline, self).unlink()
        return res


