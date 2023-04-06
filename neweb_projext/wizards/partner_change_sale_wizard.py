# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class partnerchangesalewizard(models.TransientModel):
    _name = "neweb.change_sale_wizard"

    old_sale_id = fields.Many2one('hr.employee',string="原業務員",required=True)
    old_parent_id = fields.Many2one('hr.employee',string="原業務主管")

    @api.onchange('old_sale_id')
    def onchangesale(self):
        myrec =  self.env['hr.employee'].search([('id','=',self.old_sale_id.id)])
        if myrec:
            self.old_parent_id=myrec.parent_id.id

    def run_change_sale(self):
        self.env.cr.execute("""select runchangesale(%d)""" % self.old_sale_id.id)
        self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '已將原業務員客戶移轉給原業務員主管'
        return {
            'name': '移轉完成！',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }