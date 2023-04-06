# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api


class travelreportinherit(models.Model):
    _inherit ="neweb_sale_analysis.travel_report"

    @api.depends('user_id')
    def _get_empno(self):
        for rec in self:
            self.env.cr.execute("""select getempnum(%d)""" % rec.user_id.id)
            myempnum = self.env.cr.fetchone()[0]
            rec.empno = myempnum
            return myempnum

    empno = fields.Char(string=u"員工編號",compute=_get_empno)
    perm_member = fields.Many2many('hr.employee', 'hr_employee_travel_report_rel', 'travel_id', 'emp_id', string="有權限名單")



    @api.model
    def create(self, vals):
        res = super(travelreportinherit, self).create(vals)
        self.env.cr.execute("""select gentravelperm(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    def write(self, vals):

        res = super(travelreportinherit, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select gentravelperm(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res