# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class EraMemberOutWizard(models.TransientModel):
    _name = "era_household.member_out_wizard"

    @api.depends('house_id')
    def _get_member(self):
        if self.house_id:
            self.member_id = self.house_id.member_id.id
        else:
            self.member_id = False

    project_no = fields.Many2one('era.household_house', string="案場名稱")
    house_id = fields.Many2one('era.household_house_line', string="退租房間", required=True)
    member_id = fields.Many2one('era.household_member', string="原租戶")
    old_archive = fields.Boolean(string="立即歸檔？",default=True)

    @api.onchange('project_no')
    def onchangeprojectno(self):
        return {'domain': {'house_id': [('house_id', '=', self.project_no.id)]}}

    @api.onchange('house_id')
    def onchangehouseid(self):
        # myrec = self.env['era.household_house_line'].search([('id','=',self.house_id.id)])
        # self.member_id = myrec.member_id.id
        return {'domain': {'member_id': [('house_id', '=', self.house_id.id)]}}


    def run_member_out(self):
        if self.old_archive:
            self.env.cr.execute("""select era_chkout_archive(%d,'%s')""" % (self.member_id.id,True))
            self.env.cr.execute("""commit""")
        else:
            self.env.cr.execute("""select era_chkout_archive(%d,'%s')""" % (self.member_id.id,False))
            self.env.cr.execute("""commit""")

        self.env.cr.execute("""update era_household_house_line set member_id=null,user_id=null,in_used=False where id=%d""" % self.house_id.id)
        self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '房號：%s 房客:%s 退租成功 OK！' % (self.house_id.house_no,self.member_id.member_name)
        return {
            'name': '系統通知訊息',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }
