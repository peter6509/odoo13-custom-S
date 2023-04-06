# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class CloudRentMemberInWizard(models.TransientModel):
    _name = "cloudrent_household.member_in_wizard"

    @api.depends('house_id')
    def _get_member(self):
        if self.house_id:
            self.member_id = self.house_id.member_id.id
        else:
            self.member_id = False

    project_no = fields.Many2one('cloudrent.household_house',string="案場名稱")
    house_id = fields.Many2one('cloudrent.household_house_line', string="入住房間", required=True)
    member_id = fields.Many2one('cloudrent.household_member', string="新租戶")
    user_id = fields.Many2one('res.users',string="使用者")


    @api.onchange('project_no')
    def onchangeprojectno(self):
        return {'domain': {'house_id': [('house_id', '=', self.project_no.id)]}}

    @api.onchange('member_id')
    def onchangemember(self):
        self.env.cr.execute("""select max(id) from res_users where login='%s'""" % self.member_id.member_no)
        self.user_id = self.env.cr.fetchone()[0]

    def run_member_in(self):
        self.env.cr.execute("""update cloudrent_household_house_line set member_id=%d,user_id=%d,in_used=True where id=%d""" % (self.member_id.id,self.user_id.id,self.house_id.id))
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""update cloudrent_household_member set user_id=%d,house_id=%d where id=%d""" % (self.user_id.id,self.house_id.id,self.member_id.id))
        self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '房號：%s 房客:%s 入租成功 OK！' % (self.house_id.house_no,self.member_id.member_name)
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
