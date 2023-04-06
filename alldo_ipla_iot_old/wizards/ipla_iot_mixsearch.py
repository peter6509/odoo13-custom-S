# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class alldoiplaiotmixsearch(models.TransientModel):
    _name = "alldo_ipla_iot.mix_search_wizard"

    wk_start_date = fields.Date(string="啟始日期", required=True)
    wk_end_date = fields.Date(string="截止日期", required=True)
    product_id = fields.Many2one('product.product', string="產品料號")
    equipment_no = fields.Many2one('maintenance.equipment', string="機台")
    iot_owner = fields.Many2one('hr.employee', string="作業者")
    search_type = fields.Selection([('1','人員/機台/料號 生產效率明細表'),('2','機台稼動率統計表'),('3','人員達成率統計表')],string="查詢類別",default='1')

    def run_mixsearch(self):
        if self.search_type=='1':
            myprodid = 0
            if not self.product_id:
                myprodid = 0
            else:
                myprodid = self.product_id.id
            myownerid = 0
            if not self.iot_owner:
                myownerid = 0
            else:
                myownerid = self.iot_owner.id
            mynodeid = 0
            if not self.equipment_no:
                mynodeid = 0
            else:
                mynodeid = self.equipment_no.id
            self.env.cr.execute("""select genwkperformance('%s','%s',%d,%d,%d)""" % (self.wk_start_date, self.wk_end_date, myprodid, myownerid, mynodeid))
            self.env.cr.execute("""commit""")

            myviewid = self.env.ref('alldo_ipla_iot.iplaiot_workorder_performance_tree')

            return {
                'view_name': 'workorder_performance_list',
                'name': (u'生產數據複合查詢統計'),
                'type': 'ir.actions.act_window',
                'res_model': 'alldo_ipla_iot.workorder_performance_list1',
                'view_id': myviewid.id,
                'view_type': 'form',
                'view_mode': 'tree',
                'target': 'list'}
        elif self.search_type=='2':
            # raise UserError("尚在設計中,請稍待！")
            self.env.cr.execute("""select genwkequipment('%s','%s')""" % (self.wk_start_date,self.wk_end_date))
            self.env.cr.execute("""commit""")
            myviewid = self.env.ref('alldo_ipla_iot.ipla_iot_equipperformance_tree')

            return {
                'view_name': 'equipment_performance_list',
                'name': (u'生產數據機台稼動時間記錄'),
                'type': 'ir.actions.act_window',
                'res_model': 'alldo_ipla_iot.equipment_performance_list',
                'view_id': myviewid.id,
                'view_type': 'form',
                'view_mode': 'tree',
                'target': 'list'}
        else:
            self.env.cr.execute("""select genwkmanperformance('%s','%s')""" % (self.wk_start_date, self.wk_end_date))
            self.env.cr.execute("""commit""")
            myviewid = self.env.ref('alldo_ipla_iot.ipla_iot_manperformance_tree')
            return {
                'view_name': 'man_performance_list',
                'name': (u'人員達成率生產數據'),
                'type': 'ir.actions.act_window',
                'res_model': 'alldo_ipla_iot.man_performance_list',
                'view_id': myviewid.id,
                'view_type': 'form',
                'view_mode': 'tree',
                'target': 'list'}
