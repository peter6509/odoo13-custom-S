# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class changerepairstatewizard(models.TransientModel):
    _name = "neweb_repair.change_state_wizard"

    repair_no = fields.Many2one('neweb_repair.repair',string="報修單號",required=True)
    now_state = fields.Selection([
        ('repair_draft', u'草稿'),  # 草稿
        ('repair_waiting', u'等料中'),  # 等料中
        ('repair_AE', u'工程師處理'),  # 工程師處理
        ('repair_Manager', u'指派工程師主管審核'),  # 指派工程師主管審核
        ('repair_done', u'完成'),  # 結案
        ('repair_cancel', u'作廢'),  # 作廢
        ('repair_reject', u'退回'),  # 退回(internal use)
        ('repair_open', _('Open')),  # 進call(internal use)
        ('repair_closed', u'結案'),  # 結束flow(internal use)
        ], string='目前狀態')
    new_state = fields.Selection([
        ('repair_draft', u'草稿'),  # 草稿
        ('repair_waiting', u'等料中'),  # 等料中
        ('repair_AE', u'工程師處理'),  # 工程師處理
        ('repair_Manager', u'指派工程師主管審核'),  # 指派工程師主管審核
        ('repair_done', u'完成'),  # 結案
        ('repair_cancel', u'作廢'),  # 作廢
        ('repair_reject', u'退回'),  # 退回(internal use)
        ('repair_open', _('Open')),  # 進call(internal use)
        ('repair_closed', u'結案'),  # 結束flow(internal use)
        ], string='變更狀態')

    @api.onchange('repair_no')
    def onchangerepairno(self):
        myrec = self.env['neweb_repair.repair'].search([('id','=',self.repair_no.id)])
        self.now_state = myrec.state


    @api.onchange('now_state')
    def onchangestate(self):
        if self.now_state == 'repair_draft':
            self.new_state = 'repair_waiting'
        elif self.now_state == 'repair_waiting':
            self.new_state = 'repair_AE'
        elif self.now_state == 'repair_AE':
            self.new_state = 'repair_Manager'
        elif self.now_state == 'repair_Manager':
            self.new_state = 'repair_done'
        elif self.now_state == 'repair_done':
            self.new_state = 'repair_closed'

    def run_repair_state(self):
        myid = self.repair_no.id
        if myid:
           self.env.cr.execute("""update neweb_repair_repair set state='%s' where id=%d""" % (self.new_state,myid))
           self.env.cr.execute("""commit""")

