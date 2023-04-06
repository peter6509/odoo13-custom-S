# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import api, fields, models
from odoo.exceptions import UserError


class ApproveChangeWizard(models.TransientModel):
    _name = 'approve.change.wizard'

    @api.multi
    def confirmed_approve_change(self):
        eco_ids = self.env['mrp.eco'].browse(self.env.context.get('active_ids'))
        stage_ids = self.env['mrp.eco.stage'].search([('name', '=', '待審核')])
        for rec in eco_ids:
            if rec.stage_id in stage_ids:
                rec.action_apply()
            else:
                raise UserError('有選到不在待審核的單據，請重新審查所選單據')
