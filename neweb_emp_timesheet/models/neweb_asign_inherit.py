# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebassigntimesheetinherit(models.Model):
    _inherit = "neweb.assign_complete"
    _description = "人力支援派工完工工時入帳"

    emp_id = fields.Many2one('hr.employee',string="派工工程師")
    assign_start_datetime = fields.Datetime(string="實際開始時間",help="實際時間起迄必須是同一天,如果不同日期請拆開不同筆")
    assign_end_datetime = fields.Datetime(string="實際結束時間",help="實際時間起迄必須是同一天,如果不同日期請拆開不同筆")
    work_type = fields.Many2one('neweb_emp_timesheet.timesheet_worktype',string="工時代碼")

    @api.onchange('emp_id')
    def onchangeemp(self):
        res = {}
        res['domain'] = {'work_type': [('worktype_cat', '=', '4')]}
        return res

    def write(self, vals):
        res = super(newebassigntimesheetinherit, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select update_assignline_datetime(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res


    def unlink(self):
        myuid = self.env.uid
        for rec in self:
            self.env.cr.execute("""select del_assingline_timesheet(%d,%d)""" % (rec.id,myuid))
            self.env.cr.execute("""commit""")
        res = super(newebassigntimesheetinherit, self).unlink()
        return res


class newebassigntimesheetinherit1(models.Model):
    _inherit = "neweb.proj_eng_assign"  ## 裝機＆派工

    @api.model
    def create(self, vals):
        res = super(newebassigntimesheetinherit1, self).create(vals)
        myuid = self.env.uid
        print ("proj_eng_assing:%d" % res.id)
        self.env.cr.execute("""select gen_assigntodo(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gen_assign_timesheet(%d,%d)""" % (res.id,myuid))
        self.env.cr.execute("""commit""")
        return res


    def write(self, vals):
        res = super(newebassigntimesheetinherit1, self).write(vals)
        myuid = self.env.uid
        for rec in self:
            print ("proj_eng_assing:%d" % rec.id)
            self.env.cr.execute("""select gen_assigntodo(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select gen_assign_timesheet(%d,%d)""" % (rec.id,myuid))
            self.env.cr.execute("""commit""")
        return res


    def unlink(self):
        myuid = self.env.uid
        for rec in self:
            self.env.cr.execute("""select del_assigntodo(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select del_assign_timesheet(%d,%d)""" % (rec.id,myuid))
            self.env.cr.execute("""commit""")
        res = super(newebassigntimesheetinherit1, self).unlink()
        return res