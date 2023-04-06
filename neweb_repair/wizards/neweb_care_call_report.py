# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _

class newebcarecallreportwizard(models.TransientModel):
    _name = "neweb_repair.care_call_report_wizard"

    care_start_date = fields.Date(string="Care Start Date")
    care_end_date = fields.Date(string="Care End Date")

    def run_care_call_list(self):
        self.env.cr.execute("""select getcarecalllist('%s','%s')""" % (self.care_start_date,self.care_end_date))
        myids = self.env.cr.fetchall()
        myid=[]
        for rec in myids:
            myid.append(rec[0])
        mydomain = "[('id','in',%s)]" % myid


        return {
            'name': _('Care Call List Search'),
            'view_type': 'form',
            'view_mode': 'tree',
            'view_id': self.env.ref('neweb_repair.repair_tree').id,
            'res_model': 'neweb_repair.repair',
            'domain': mydomain,
            'type': 'ir.actions.act_window',
            'target': 'self',
        }


