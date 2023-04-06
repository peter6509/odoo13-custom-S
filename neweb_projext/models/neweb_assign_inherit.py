# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebprojextassigninherit(models.Model):
    _inherit = "neweb.proj_eng_assign"

    perm_member = fields.Many2many('hr.employee', 'hr_employee_projengassign_rel', 'ass_id', 'emp_id', string="有權限名單")
    owner_man1 = fields.Many2one('hr.employee', string="有權人1")
    owner_man2 = fields.Many2one('hr.employee', string="有權人2")
    owner_man3 = fields.Many2one('hr.employee', string="有權人3")
    owner_man4 = fields.Many2one('hr.employee', string="有權人4")
    owner_man5 = fields.Many2one('hr.employee', string="有權人5")
    owner_man6 = fields.Many2one('hr.employee', string="有權人6")

    @api.model
    def create(self, vals):
        res = super(newebprojextassigninherit, self).create(vals)
        # self.env.cr.execute("""select genassengperm(%d)""" % res.id)
        # self.env.cr.execute("""commit""")
        return res


    def write(self,vals):
        res = super(newebprojextassigninherit, self).write(vals)
        # for rec in self:
        #     self.env.cr.execute("""select genassengperm(%d)""" % rec.id)
        #     self.env.cr.execute("""commit""")
        return res

    def run_clean_setupprod(self):
        self.env.cr.execute("""delete from neweb_setup_prod where setup_id=%d""" % self.id)
        self.env.cr.execute("""commit""")

