# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class gotoprojectwizards(models.TransientModel):
    _name= "neweb.gotoproject"

    project_no = fields.Many2one('neweb.project',string="專案編號")

    def run_gotoproject(self):
        myid = self.project_no.id

        return {'view_name': 'gotoprojectwizard',
                'name': ('搜尋專案'),
                'views': [[False, 'form'], ],
                'res_model': 'neweb.project',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                # 'domain': mydomain,
                'res_id': myid,
                # 'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                'view_mode': 'form',
                'view_type': 'form'
                }