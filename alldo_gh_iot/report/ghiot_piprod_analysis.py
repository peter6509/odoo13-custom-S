# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotpiprodanalysis(models.Model):
    _name = "alldo_gh_iot.piprod_analysis"
    _description = "訂單產品產能分析表"

    po_no = fields.Char(string="訂單號碼")
    product_no = fields.Char(string="產品編號")
    prod_std = fields.Char(string="產能標準量(pcs/H)")
    onepcs_std = fields.Char(string="單片標準時間(M)")
    onepcs_complete = fields.Char(string="單片平均完成時間(S)")
    onepcs_time_total = fields.Char(string="單位產品總花費時間(S)")
    piprod_lines = fields.One2many('alldo_gh_iot.piprod_analysis_line','piprod_id',string="訂單產品產能分析表明細")

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.po_no, myrec.product_no)
            result.append((myrec.id, myname))
        return result



class ghiotpiprodanalysisline(models.Model):
    _name = "alldo_gh_iot.piprod_analysis_line"
    _description = "訂單產品產能分析表明細"

    @api.depends('prod_num','std_num')
    def _get_hitrate_per(self):
        for rec in self:
            if rec.std_num == 0:
                rec.hitrate_per = 0
            else:
                rec.hitrate_per = (rec.prod_num / rec.std_num) * 100

    @api.depends('prod_num','wk_time')
    def _get_prod_power(self):
        for rec in self:
            if rec.wk_time == 0:
                rec.prod_power = 0
            else:
                rec.prod_power = rec.prod_num / rec.wk_time

    @api.depends('prod_power')
    def _get_onepcs_time(self):
        for rec in self:
            if rec.prod_power == 0:
                rec.onepcs_time = 0
            else:
                rec.onepcs_time = 60 / rec.prod_power

    piprod_id = fields.Many2one('alldo_gh_iot.piprod_analysis',string="訂單產品產能分析表",ondelete='cascade')
    eng_type = fields.Char(string="工程類型")
    iot_node = fields.Many2one('maintenance.equipment', string="機台")
    iot_owner = fields.Many2one('hr.employee', string="擔當者")
    prod_num = fields.Float(digits=(8,0),string="產出數量")
    std_num = fields.Float(digits=(8,0),string="標準數量(pcs/H)")
    hitrate_per = fields.Float(digits=(6,2),string="達成率",compute=_get_hitrate_per)
    wk_time = fields.Float(digits=(8,2),string="工時(H)")
    prod_power = fields.Float(digits=(8,2),string="產能(pcs/H)",compute=_get_prod_power)
    onepcs_time = fields.Float(digits=(8,2),string="平均單片時間(M)",compute=_get_onepcs_time)
