# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newetimesheetrepairinherit(models.Model):
    _inherit = "neweb_repair.repair"

    repair_type = fields.Selection([
        ('per_call', 'Per Call'),
        ('warranty_maintenance', '支援原廠保固服務'),
        ('warranty_software','支援原廠軟體處理'),
        ('hw_maintenance', '硬體處理_維護'),
        ('soft_maintenance', '軟體處理_維護'),
        ('hw_outsourcing', '硬體處理_維運'),
        ('soft_outsourcing', '軟體處理_維運'),
        ('no_warranty_support', '非合約的人力支援'),
    ], string="Repair Type")

    # @api.onchange('repair_lines.problem_desc')
    # def onchangecustomerid(self):
    #     myid = self.id
    #     if myid:
    #         print("%d" % myid)
    #         self.env.cr.execute("""select getmaintype(%d)""" % myid)
    #         myres = self.env.cr.fetchone()[0]
    #         print('%s' % myres)
    #         self.repair_type=myres


    @api.model
    def create(self,vals):
        res = super(newetimesheetrepairinherit, self).create(vals)
        myuid = self.env.uid
        self.env.cr.execute("""select getmaintype(%d)""" % res.id)
        myres = self.env.cr.fetchone()[0]
        self.env.cr.execute("""update neweb_repair_repair set repair_type='%s' where id=%d and repair_type is null""" % (myres,res.id))

        self.env.cr.execute("""select updaterepaircalendar(%d,%d)""" % (res.id,myuid))
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select update_repair_timesheet(%d,%d)""" % (res.id,myuid))
        self.env.cr.execute("""commit""")
        return res

    def write(self, vals):
        if 'repair_type' in vals and not vals['repair_type']:
            raise UserError("報修種類不能空白,工時系統必要條件！")
        res = super(newetimesheetrepairinherit, self).write(vals)
        myuid = self.env.uid
        for rec in self:
            self.env.cr.execute("""select updaterepaircalendar(%d,%d)""" % (rec.id,myuid))
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select update_repair_timesheet(%d,%d)""" % (rec.id,myuid))
            self.env.cr.execute("""commit""")
        return res

    def unlink(self):
        myuid = self.env.uid
        for rec in self:
            self.env.cr.execute("""select delrepaircalendar(%d,%d)""" % (rec.id,myuid))
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select del_repair_timesheet(%d,%d)""" % (rec.id,myuid))
            self.env.cr.execute("""commit""")
        res = super(newetimesheetrepairinherit, self).unlink()
        return res


class newebrepairworkloginherit(models.Model):
    _inherit = "neweb_repair.repair_work_log"


    work_start_datetime = fields.Datetime(string="維修啟始時間",help="實際時間起迄必須是同一天,如果不同日期請拆開不同筆")
    work_end_datetime = fields.Datetime(string="維修截止時間",help="實際時間起迄必須是同一天,如果不同日期請拆開不同筆")
    work_emp = fields.Many2one('hr.employee',string="維修工程師",default=lambda self:self._get_workemp())

    def _get_workemp(self):
        myres = self.env['hr.employee'].search([('user_id','=',self.env.uid)])
        if myres:
            return myres[0].id

    @api.model
    def create(self, vals):
        res =super(newebrepairworkloginherit, self).create(vals)
        self.env.cr.execute("""select checkrepairdate(%d)""" % res.id)
        myres = self.env.cr.fetchone()[0]
        # if myres=='1':
        #     raise UserError('起始時間或結束時間不能空值！')
        if myres=='2':
            raise UserError("單筆記錄只能同一日期,如有不同日期請創建另一筆！")
        if myres=='3':
            raise UserError("起始時間跟結束時間沒有時間差")
        return res

    def write(self, vals):

        res = super(newebrepairworkloginherit, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select checkrepairdate(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            # if myres == '1':
            #     raise UserError('起始時間或結束時間不能空值！')
            if myres == '2':
                raise UserError("單筆記錄只能同一日期,如有不同日期請創建另一筆！")
            if myres == '3':
                raise UserError("起始時間跟結束時間沒有時間差")
        return res


    def unlink(self):
        myuid = self.env.uid
        self.env.cr.execute("""select del_repair_work_log(%d,%d)""" % (self.id,myuid))
        self.env.cr.execute("""commit""")
        res = super(newebrepairworkloginherit, self).unlink()
        return res




