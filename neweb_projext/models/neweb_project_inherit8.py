# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebprojectinherit8(models.Model):
    _inherit = "neweb.project"

    @api.depends('stamp_duty_type', 'total_analysis_revenue')
    def _get_stampduty(self):
        mystampduty=0
        for rec in self:
            if rec.stamp_duty_type == '1':
                mystampduty = 12
                # rec.update({'stamp_duty': 12})
            elif rec.stamp_duty_type == '2':
                mystampduty = int(rec.total_analysis_revenue * 0.001)
            rec.stamp_duty = mystampduty
            return mystampduty


    stamp_duty_type = fields.Selection([('1','買賣'),('2','承攬')],string="印花稅類別",default='2',onchange_default=True)
    stamp_duty = fields.Integer(string="印花稅",compute=_get_stampduty,track_visibility='always')
    stampduty_apply = fields.Boolean(string="印花稅申報(財務人員專用)",default=False)



    @api.onchange('stamp_duty_type','total_analysis_revenue')
    def onclientchangeduty(self):
        if self.stamp_duty_type=='1':
            self.stamp_duty = 12
        elif self.stamp_duty_type=='2' :
            self.stamp_duty = int(self.total_analysis_revenue * 0.001)
        else:
            self.stamp_duty = 0



class newebprojectcostdept(models.Model):
    _name = "neweb.cost_dept"
    _description = "成本歸屬部門別"
    _order = "sequence,id"


    name = fields.Char(string="成本部門名稱",required=True)
    sequence = fields.Integer(string="SEQ",default=20)
    active = fields.Boolean(string="生效", default=True)


    @api.model
    def create(self, vals):
        myres = self.env['neweb.cost_dept'].search_count([('name','=',vals['name'])])
        if myres > 1:
            raise UserError("成本部門名稱已重複！")
        res = super(newebprojectcostdept, self).create(vals)
        return res

    # @api.multi
    # def write(self, vals):
    #
    #     res = super(newebprojectcostdept, self).write(vals)
    #     return res
