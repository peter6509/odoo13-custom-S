# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models, fields, api
from odoo.exceptions import UserError



class newebengassignworkwizard(models.TransientModel):
    _name = "neweb.engassignwork_wizard"

    assign_no = fields.Many2one('neweb.proj_eng_assign', string=u"派工單號", required=True,track_visibility='always' )
    assign_member = fields.Many2many('res.users',string=u"指派工程人員")


    @api.onchange('assign_no')
    def onchange_client(self):
        myrec = self.env['neweb.proj_eng_assign'].search([('assign_no','=',self.assign_no.assign_no)])
        self.assign_member=myrec.assign_man



    @api.multi
    def neweb_engassignman_wizard(self):
        if not self.assign_no:
           raise UserError("未選取派工單號")
        myengassign = self.env['neweb.proj_eng_assign'].search([('id','=',self.assign_no.id)])
        myengassign.write({'assign_man':[(5,0)]})
        for mymember in self.assign_member:
            myengassign.write({'assign_man':[(4,[mymember.id])]})
        myengassign.write({'state':'2'})
        myproject = self.env['neweb.project'].search([('id','=',myengassign.proj_no.id)])
        myproject.write({'state':'3'})

        return {'view_name': 'newebengassignworkwizard',
                'name': (u'人力支援派工維護'),
                'views': [[False, 'form'], ],
                'res_model': 'neweb.proj_eng_assign',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'current',
                # 'domain': mydomain,
                'res_id': myengassign.id,
                'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }

