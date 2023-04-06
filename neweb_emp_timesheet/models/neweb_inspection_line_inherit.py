# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebinspectionlineinherit(models.Model):
    _inherit = "neweb_contract.inspection_list"

    actual_start_datetime = fields.Datetime(string="實際起始時間",help="實際時間起迄必須是同一天,如果不同日期請拆開不同筆")
    actual_end_datetime = fields.Datetime(string="實際結束時間",help="實際時間起迄必須是同一天,如果不同日期請拆開不同筆")
    emp_id = fields.Many2one('hr.employee',string=u'工程師')

    @api.model
    def create(self, vals):
        res = super(newebinspectionlineinherit, self).create(vals)
        self.env.cr.execute("""select checkinspectiondate(%d)""" % res.id)
        myres = self.env.cr.fetchone()[0]
        # if myres == '1':
        #     raise UserError(u'起始時間或結束時間不能空值！')
        if myres == '2':
            raise UserError("單筆記錄只能同一日期,如有不同日期請創建另一筆！")
        if myres == '3':
            raise UserError("起始時間跟結束時間沒有時間差")
        self.env.cr.execute("""select update_inspection_datetime(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res


    def write(self, vals):
        res = super(newebinspectionlineinherit, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select checkinspectiondate(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            # if myres == '1':
            #     raise UserError(u'起始時間或結束時間不能空值！')
            if myres == '2':
                raise UserError("單筆記錄只能同一日期,如有不同日期請創建另一筆！")
            if myres == '3':
                raise UserError("起始時間跟結束時間沒有時間差")
            self.env.cr.execute("""select update_inspection_datetime(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res


    def unlink(self):
        myuid = self.env.uid
        for rec in self:
            self.env.cr.execute("""select delinspectiontimesheet(%d,%d)""" % (rec.id,myuid))
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select del_plan_ins_calendar(%d,%d)""" % (rec.id,myuid))
            self.env.cr.execute("""commit""")
        res = super(newebinspectionlineinherit, self).unlink()

        return res


class newebcontractcontractinherit(models.Model):
    _inherit = "neweb_contract.contract"

    @api.model
    def create(self, vals):

        res = super(newebcontractcontractinherit, self).create(vals)
        myuid = self.env.uid
        self.env.cr.execute("""select update_inspection_timesheet(%d,%d)""" % (res.id,myuid))
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select update_plan_ins_calendar(%d,%d)""" % (res.id,myuid))
        self.env.cr.execute("""commit""")
        return res


    def write(self, vals):

        res = super(newebcontractcontractinherit, self).write(vals)
        myuid = self.env.uid
        for rec in self:
            self.env.cr.execute("""select update_inspection_timesheet(%d,%d)""" % (rec.id,myuid))
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select update_plan_ins_calendar(%d,%d)""" % (rec.id,myuid))
            self.env.cr.execute("""commit""")
        return res


    def unlink(self):
        myuid = self.env.uid
        for rec in self:
            for rec1 in rec.inspection_line:
                self.env.cr.execute("""select delinspectiontimesheet(%d,%d)""" % (rec1.id,myuid))
                self.env.cr.execute("""commit""")
                self.env.cr.execute("""select del_plan_ins_calendar(%d,%d)""" % (rec1.id,myuid))
                self.env.cr.execute("""commit""")
        res = super(newebcontractcontractinherit, self).unlink()
        return res

    def run_change_eng(self):
        self.env.cr.execute("""select update_plan_ins_calendar(%d,%d)""" % (self.id, self.env.uid))
        self.env.cr.execute("""commit""")


        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '維護工程師變更同步到待辦行事曆完成！'
        return {
             'name': '系統通知訊息',
             'type': 'ir.actions.act_window',
             'view_type': 'form',
             'view_mode': 'form',
             'res_model': 'sh.message.wizard',
             'views': [(view.id, 'form')],
             'view_id': view.id,
             'target': 'new',
             'context': context,
         }