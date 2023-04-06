# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class cloudrentemetermixsearch(models.TransientModel):
    _name = "cloudrent_household.emeter_mixsearch"

    house_id = fields.Many2one('cloudrent.household_house_line',string="房號",required=True)
    member_id = fields.Char(related='house_id.member_id.member_name')
    start_date = fields.Date(string="啟始日期",required=True)
    end_date = fields.Date(string="截止日期",required=True)

    # @api.onchange('house_id')
    # def onchangehouseid(self):
    #     self.member_id = self.house_id.member_id
    #     return self.house_id.member_id

    def run_emeter_mixsearch(self):
        self.env.cr.execute("""select genemetermixsearch(%d,'%s','%s')""" % (self.house_id.id,self.start_date,self.end_date))
        self.env.cr.execute("""commit""")
        myviewid = self.env.ref('cloudrent_household.cloudrent_mixsearch_line_tree')

        return {
            'view_name': 'cloudrent_mixsearch_line_tree',
            'name': (u'租房區間用電查詢統計'),
            'type': 'ir.actions.act_window',
            'res_model': 'cloudrent_household.emeter_mixsearch_line',
            'view_id': myviewid.id,
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'list'}

