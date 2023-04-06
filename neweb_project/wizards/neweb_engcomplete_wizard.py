# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models, fields, api
from odoo.exceptions import UserError



class newebengcompletewizard(models.TransientModel):
    _name = "neweb.engcomplete_wizard"

    assign_no = fields.Many2one('neweb.proj_eng_assign', string="派工單號", required=True, domain=[('state','=','2')])

    # @api.multi
    def neweb_engcomplete_wizard(self):
        myengcomplete = self.env['neweb.proj_eng_assign'].search([('id','=',self.assign_no.id)])
        myengcomplete.write({'state':'3'})
        myproject = self.env['neweb.project'].search([('id','=',myengcomplete.proj_no.id)])
        myproject.write({'state':'4'})

        return {'view_name': 'newebengcompletewizard',
                'name': ('人力支援派工維護'),
                'views': [[False, 'form'], ],
                'res_model': 'neweb.proj_eng_assign',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'current',
                # 'domain': mydomain,
                'res_id': myengcomplete.id,
                'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }
