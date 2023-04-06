# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class CloudRentMaintenanceWizard(models.TransientModel):
    _name = "cloudrent.maintenance_wizard"
    _description = "租戶修繕創建精靈"

    project_no = fields.Many2one('cloudrent.household_house',string="案場",required=True)
    house_id = fields.Many2one('cloudrent.household_house_line',string="租房",required=True)
    landlord_owner = fields.Many2one('cloudrent.household_member',string="所屬房東")
    member_id = fields.Many2one('cloudrent.household_member',string="租戶")
    manager_id = fields.Many2one('cloudrent.household_member',string="指派管理師",required=True)
    require_date = fields.Date(string="通報日期",required=True)

    @api.onchange('project_no')
    def onchangeprojno(self):
        myids = []
        myrec = self.env['cloudrent.household_house_line'].search([('house_id', '=', self.project_no.id)])
        for rec in myrec:
            myids.append(rec.id)
        return {'domain': {'house_id': [('id', 'in', myids)]}}

    @api.onchange('house_id')
    def onchangehouse(self):
        self.landlord_owner = self.house_id.landlord_owner.id
        self.member_id = self.house_id.member_id.id

    def gen_maintenance(self):
        myrec = self.env['cloudrent.household_maintenance']
        mymainrec = myrec.create({'house_id':self.house_id.id,'flow_man2':self.landlord_owner.id,
                                  'member_id':self.member_id.id,'flow_man1':self.manager_id.id,
                                  'require_date':self.require_date,'flow_owner':self.env.uid,'state':'1'})
        myid1 = mymainrec.id

        return {'view_name': 'cloudrent_maintenance',
                'name': ('雲房修繕單記錄'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'cloudrent.household_maintenance',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'self',
                'res_id': myid1,
                'view_mode': 'form',
                'view_type': 'form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }

