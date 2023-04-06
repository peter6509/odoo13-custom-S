# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class newebprojext(models.Model):
    _inherit = "neweb.project"

    @api.depends('create_date')
    def _get_createdate(self):
        for rec in self:
            mydate = False
            try:
                self.env.cr.execute("""select create_date::DATE from neweb_project where id=%d""" % rec.id)
                mydate = self.env.cr.fetchone()[0]
                rec.create_date1 = mydate
            except Exception as inst:
                mydate = False
            return mydate

    call_service_response = fields.Many2one('neweb_base.sla', domain=[('disabled', '=', False)], string="叫修時效")
    main_service_rule_new = fields.Many2one('neweb.main_service_rule', string="維護服務時段")
    routine_maintenance_new = fields.Many2one('neweb.routine_maintenance', string="定期維護條款")
    proj_pay1 = fields.Many2one('neweb.payment_term_rule', string="付款條件")
    company_id = fields.Many2one('res.company', string="My Company", default=1)
    create_date1 = fields.Date(string="Create Date",compute=_get_createdate)

    @api.model
    def create(self, vals):
        res = super(newebprojext, self).create(vals)
        self.env.cr.execute("""select check_cusproject(%d)""" % res.id)
        myresult = self.env.cr.fetchone()
        # if not myresult[0]:
        #     raise UserError("客戶專案/標案名稱不能空白!!")
        self.env.cr.execute("""select genstockout_projno(%d)""" % res.id)
        self.env.cr.execute("""select genmainrec(%d)""" % res.id)
        self.env.cr.execute("""select gencreditlimit(%d)""" % res.id)
        self.env.cr.execute("""select setpaymentterm(%d)""" % res.id)
        self.env.cr.execute("""select setprodserial(%d)""" % res.id)
        return res

    def write(self, vals):
        res = super(newebprojext, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select check_cusproject(%d)""" % rec.id)
            myresult = self.env.cr.fetchone()
            # if not myresult[0]:
            #     raise UserError("客戶專案/標案名稱不能空白!!")
            self.env.cr.execute("""select genstockout_projno(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select genmainrec(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select gencreditlimit(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select setpaymentterm(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select setprodserial(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select checkinvoiceprojsum(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            # self.env.cr.execute("""select genstampduty(%d)""" % self.id)
            # self.env.cr.execute("""commit""")
            return res


class newebprojextsaleorder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        if 'project_name' in vals and not vals['project_name']:
            vals['project_name']='-'
            # raise UserError("專案名稱不能空白!!")
        res = super(newebprojextsaleorder, self).create(vals)
        return res


    def write(self, vals):
        res = super(newebprojextsaleorder, self).write(vals)
        # for rec in self:
        #     self.env.cr.execute("""select check_projectname(%d)""" % rec.id)
        #     myresult = self.env.cr.fetchone()
        #     if myresult[0]:
        #         raise UserError("專案名稱不能空白!!")

        return res

    @api.onchange('partner_id')
    def onchange_partnerid(self):
        self.env.cr.execute("""select getpayterm(%d)""" % self.partner_id.id)
        myresult = self.env.cr.fetchone()
        if myresult[0] != '0':
            self.open_account_day = myresult[0]

    def cancel_done(self):
        myid = self.env.context.get('saleorderid')
        myrec = self.env['sale.order'].search([('id', '=', myid)])
        self.env.cr.execute("""select hasproj(%d)""" % myid)
        myresult = self.env.cr.fetchone()
        if myresult[0]:
            raise UserError("請先刪除專案成本分析,才能解鎖")
        myrec.write({'state': 'draft'})


# class newebprojextrespartner(models.Model):
#     _inherit = "res.partner"
#
#     credit_rule_memo = fields.Text(string="信用條件")