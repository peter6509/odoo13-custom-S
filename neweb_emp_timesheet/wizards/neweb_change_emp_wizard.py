# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebchangeempwizard(models.TransientModel):
    _name = "neweb_emp_timesheet.change_emp"
    _description = "變更定檢行事曆工程師"

    old_emp_id = fields.Many2one('hr.employee',string="原工程師",required=True)
    new_emp_id = fields.Many2one('hr.employee',string="變更工程師",required=True)
    contract_ids = fields.Many2many('neweb_contract.contract','timesheet_change_emp_contract_rel','wiz_id','contract_id',string="合約編號",required=True)
    todo_start_date = fields.Date(string="變更啟始日期")

    @api.onchange('old_emp_id')
    def onchangeemp(self):
        ids=[]
        self.env.cr.execute("""select getoldempcontract(%d)""" % self.old_emp_id.id)
        myrec = self.env.cr.fetchall()
        for line in myrec:
            ids.append(line[0])
        res = {}
        # print "%s" % ids
        res['domain'] = {'contract_ids': [('id', 'in', ids)]}
        return res



    def run_change_emp(self):
        self.env.cr.execute("""select todo_change_emp(%d,%d,'%s',%d)""" % (self.old_emp_id.id,self.new_emp_id.id,self.todo_start_date,self.id))
        self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '工程師變更完成！'
        return {
            'name': '待辦行事曆工程師變更！',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }