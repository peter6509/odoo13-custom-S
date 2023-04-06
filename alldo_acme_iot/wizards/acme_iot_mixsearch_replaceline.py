# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class alldoacmeiotmixsearchreplaceline(models.TransientModel):
    _name = "alldo_acme_iot.mix_search_replaceline_wizard"
    _description = "工程師換線複合查詢統計"

    wk_start_date = fields.Date(string="啟始日期", required=True)
    wk_end_date = fields.Date(string="截止日期", required=True)
    product_id = fields.Many2one('product.product', string="產品料號")
    equipment_no = fields.Many2one('maintenance.equipment', string="機台")
    replace_type = fields.Selection([('P','備模'),('L','架模'),('B','烘模')],string="類別")
    iot_owner = fields.Many2one('hr.employee', string="作業者")

    def run_mixsearch_replaceline(self):
        if not self.product_id and not self.equipment_no and not self.iot_owner:
            raise UserError("至少要有一個查詢元素")
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
        if not self.replace_type:
            myreplacetype='0'
        else:
            myreplacetype=self.replace_type
        self.env.cr.execute("""select genreplineperformance('%s','%s',%d,%d,%d,'%s')""" % (self.wk_start_date, self.wk_end_date, myprodid, myownerid,myequipid,myreplacetype))
        self.env.cr.execute("""commit""")

        myviewid = self.env.ref('alldo_acme_iot.acme_iot_replaceline_list_tree')

        return {
            'view_name': 'acme_iot_replaceline_list_tree',
            'name': (u'工程師換線複合查詢統計'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_acme_iot.replaceline_list',
            'view_id': myviewid.id,
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'list'}

