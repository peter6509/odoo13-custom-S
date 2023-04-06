# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class EraHouseMemberCHKWizard(models.TransientModel):
    _name = "era.household_member_chk_wizard"

    passcode = fields.Char(string="PASSCODE",required=True)

    def run_household_member_chk(self):
        if self.passcode != '!99999ibm':
            raise UserError("PASSCODE Error!")
        self.env.cr.execute("""select genhousememberisused()""")
        self.env.cr.execute("""commit""")

        myviewid = self.env.ref('era_household.view_era_house_member_chk_tree')
        return {
            'view_name': 'era_house_member_chk',
            'name': ('租房會員帳號檢測'),
            'type': 'ir.actions.act_window',
            'res_model': 'era.house_member_chk',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}
