# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class alldoghiotmixsearchreplaceline(models.TransientModel):
    _name = "alldo_gh_iot.mix_search_replaceline_wizard"

    wk_start_date = fields.Date(string="啟始日期", required=True)
    wk_end_date = fields.Date(string="截止日期", required=True)
    product_id = fields.Many2one('product.product', string="產品料號")
    equipment_no = fields.Many2one('maintenance.equipment', string="機台")
    iot_owner = fields.Many2one('hr.employee', string="作業者")

    def run_mixsearch_replaceline(self):
        # if not self.product_id and not self.equipment_no and not self.iot_owner:
        #     raise UserError("至少要有一個查詢元素")
        if not self.product_id:
            myprodid = 0
        else:
            myprodid = self.product_id.id
        if not self.iot_owner:
            myownerid = 0
        else:
            myownerid = self.iot_owner.id
        if not self.equipment_no:
            myequipid = 0
        else:
            myequipid = self.equipment_no.id
        self.env.cr.execute("""select genreplineperformance('%s','%s',%d,%d,%d)""" % (self.wk_start_date, self.wk_end_date, myprodid, myownerid,myequipid))
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select calreplacewknum()""")
        self.env.cr.execute("""commit""")

        myviewid = self.env.ref('alldo_gh_iot.gh_iot_replaceline_list_tree')

        return {
            'view_name': 'gh_iot_replaceline_list_tree',
            'name': (u'工程師架機複合查詢統計'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_gh_iot.replaceline_list',
            'view_id': myviewid.id,
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'list'}

