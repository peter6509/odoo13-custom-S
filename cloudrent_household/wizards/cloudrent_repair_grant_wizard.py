# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class CloudRentRepairGrantWizard(models.Model):
    _name = "cloudrent.repair_grant_wizard"
    _description = "修繕補助申請精靈"

    house_id = fields.Many2one('cloudrent.household_house_line',string="租房",required=True)
    grant_start = fields.Date(string="補助修繕起始日",required=True)
    grant_end = fields.Date(string="補助修繕截止日",required=True)
    grant_alert = fields.Date(string="到期前警示日期",required=True)
    grant_amount = fields.Float(digits=(5,0),string="補助款金額",required=True)
    setup_man = fields.Many2one('res.users',string="建檔人",default=lambda self:self.env.uid)

    def run_repair_grant(self):
        self.env.cr.execute("""select chkrepairgrant(%d,'%s','%s',%s)""" % (self.house_id.id,self.grant_start,self.grant_end,self.grant_amount))
        myres = self.env.cr.fetchone()[0]
        if not myres: # 補助款尚未建立
            myrec = self.env['cloudrent.household_house_line'].search([('id','=',self.house_id.id)])
            myrec.write({'repair_grant_line':[(0,0,{'grant_start':self.grant_start,'grant_end':self.grant_end,
                                                    'grant_alert':self.grant_alert,'grant_amount':self.grant_amount,
                                                     'setup_man':self.setup_man.id})]})

            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message']='租戶修繕補助款已建檔完成'
            return {
                'name':'Success',
                'type':'ir.actions.act_window',
                'view_type':'form',
                'view_mode':'form',
                'res_model':'sh.message.wizard',
                'views':[(view.id,'form')],
                'view_id':view.id,
                'target':'new',
                'context':context,
                }
        else:
            raise UserError("""該戶補助款已建檔了,請確認""")

