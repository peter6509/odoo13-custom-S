
# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebgroupmember(models.Model):
    _name = "neweb_sale_analysis.group_member"

    op_id = fields.Many2one('neweb_sale_analysis.op_program',string="作業",required=True)
    leader_man = fields.Many2one('hr.employee',string="管理員",required=True)
    group_owner = fields.Many2many('hr.employee','group_member_hr_employee_rel','gmember_id','emp_id',string="人員",required=True)


    def name_get(self):
        result = []
        for myrec in self:
            mymembername = "%s(%s)" % (myrec.op_id.name, myrec.leader_man.name)
            result.append((myrec.id, mymembername))
        return result


class newebgroupop(models.Model):
    _name = "neweb_sale_analysis.op_program"

    name = fields.Char(string="作業名稱",required=True)
    op_name = fields.Char(string="代號",required=True)

    @api.model
    def create(self,vals):
        mycount = self.env['neweb_sale_analysis.op_program'].search_count([('name','=',self.name)])
        if mycount > 0 :
            raise UserError("作業名稱已存在,不能再新增！")
        res = super(newebgroupop, self).create(vals)
        return res
