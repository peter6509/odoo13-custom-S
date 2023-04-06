# -*- coding: utf-8 -*-
# Author: Peter Wu


from odoo import models, fields, api
from odoo.osv.orm import except_orm
import datetime, json


class MMonthWizard(models.TransientModel):
    _name = "mmonth.wizard"  # 月統計報表

    department_id = fields.Many2one('department', 'Department')
    report_year = fields.Char(size=4, default=str(datetime.datetime.today().year))
    report_month = fields.Selection([('1', u'一月'), ('2', u'二月'), ('3', u'三月'), ('4', u'四月'), ('5', u'五月'),
                                     ('6', u'六月'), ('7', u'七月'), ('8', u'八月'), ('9', u'九月'), ('10', u'十月'),
                                     ('11', u'十一月'), ('12', u'十二月')], default=str(datetime.datetime.today().month))

    @api.multi
    def main_month_print(self):
        if int(self.report_year) <= 1900:
            raise except_orm(u"條件不符", u"年度條件必須大於1900年")
        if self.report_year == False:
            raise except_orm(u"條件不符", u"年度條件不可空白")
        if self.report_month == False:
            raise except_orm(u"條件不符", u"月份條件不可空白")
        if self.report_month == '12':
            mystart_date = fields.Datetime.to_string(
                datetime.datetime(int(self.report_year), int(self.report_month), 1))
            myend_date = fields.Datetime.to_string(datetime.datetime(int(self.report_year) + 1, 1, 1))
        else:
            mystart_date = fields.Datetime.to_string(
                datetime.datetime(int(self.report_year), int(self.report_month), 1))
            myend_date = fields.Datetime.to_string(
                datetime.datetime(int(self.report_year), int(self.report_month) + 1, 1))
        data = dict()
        data["department_id"] = self.department_id.id
        data["start_date"] = mystart_date
        data["end_date"] = myend_date
        data["report_year"] = int(self.report_year)
        data["report_month"] = int(self.report_month)

        return self.env['report'].get_action(self, 'maintenance_report.mmonth_report', data=data)
