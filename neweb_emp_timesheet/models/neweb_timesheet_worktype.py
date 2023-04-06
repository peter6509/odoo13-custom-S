# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebtimesheetworktype(models.Model):
    _name = "neweb_emp_timesheet.timesheet_worktype"
    _description = "工時代碼主檔"
    _order = "sequence,worktype_code"
    _rec_name = "worktype_code"

    @api.depends('worktype_code')
    def _get_worktypecat(self):
        for rec in self:
            rec.update({'worktype_cat': rec.worktype_code[0:1]})

    sequence = fields.Integer(default=20)
    nitem = fields.Integer(string="ITEM")
    worktype_code = fields.Char(string="工時代號",required=True)
    worktype_link = fields.Selection([('1','專案編號'),('2','合約編號'),('3','人力支援派工單'),('4','None')],default='4',string="連結單據")
    worktype_categ = fields.Char(string="工時分類")
    worktype_desc = fields.Char(string="說明描述")
    worktype_cat = fields.Char(compute=_get_worktypecat,store=True)

    def name_get(self):
        result = []
        for myrec in self:
            myworktypename = "(%s)%s" % (myrec.worktype_code,myrec.worktype_desc)
            result.append((myrec.id, myworktypename))
        return result


    @api.model
    def create(self, vals):
        mywortype = vals['worktype_code']
        mycount = self.env['neweb_emp_timesheet.timesheet_worktype'].search_count([('worktype_code','=',mywortype)])
        if mycount > 0 :
            raise UserError("工時代碼已重複,請確認！")
        res = super(newebtimesheetworktype, self).create(vals)
        self.env.cr.execute("""select sortworktype();""")
        self.env.cr.execute("""commit ;""")
        return res


    def write(self,vals):
        if 'worktype_code' in vals and not vals['worktype_code']:
            raise UserError("未輸入工時代碼,請確認！")
        if 'worktype_code' in vals and vals['worktype_code']:
            mywortype = vals['worktype_code']
            mycount = self.env['neweb_emp_timesheet.timesheet_worktype'].search_count([('worktype_code', '=', mywortype)])
            if mycount > 1:
                raise UserError("工時代碼已重複,請確認！")
        res = super(newebtimesheetworktype, self).write(vals)
        self.env.cr.execute("""select sortworktype();""")
        self.env.cr.execute("""commit""")
        return res

