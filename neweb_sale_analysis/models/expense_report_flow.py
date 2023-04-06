# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request

class newebexpenseflow(models.Model):
    _inherit = "neweb_sale_analysis.expense_report"

    # @api.depends('emp_name')
    # def _get_pos_type(self):
    #     for rec in self:
    #         myrec = self.env['res.users'].search([('id','=',rec.emp_name.id)])
    #         if myrec.has_group('neweb_project.neweb_fn10_gm') or myrec.has_group('neweb_project.neweb_sa10_gm') or myrec.has_group('neweb_project.neweb_cs10_gm') or myrec.has_group('neweb_project.neweb_en10_gm') or myrec.has_group('neweb_project.neweb_on10_gm'):
    #             mypostype='5'
    #         elif myrec.has_group('neweb_project.neweb_sa20_vp') or myrec.has_group('neweb_project.neweb_cs20_vp') or myrec.has_group('neweb_project.neweb_en20_vp') or myrec.has_group('neweb_project.neweb_on20_vp'):
    #             mypostype='4'
    #         elif myrec.has_group('neweb_project.neweb_fn20_mgr') or myrec.has_group('neweb_project.neweb_sa30_ass') or myrec.has_group('neweb_project.neweb_en30_ass') or myrec.has_group('neweb_project.neweb_on30_mgt'):
    #             mypostype='3'
    #         elif myrec.has_group('neweb_project.neweb_cs30_dir') or myrec.has_group('neweb_project.neweb_en40_mgt') or myrec.has_group('neweb_project.neweb_on40_mgt'):
    #             mypostype='2'
    #         else:
    #             mypostype='1'
    #         rec.update({'pos_type':mypostype})
    #         return mypostype

    pos_type = fields.Char(string='簽核判斷字元')
    flow_owner = fields.Many2one('hr.employee',string="OWNER")
    flow_man1 = fields.Many2one('hr.employee',string="一線主管")
    has_man1 = fields.Integer(string="has level1",default=0)
    flow_man2 = fields.Many2one('hr.employee',string="二線主管")
    has_man2 = fields.Integer(string="has level2", default=0)
    flow_man3 = fields.Many2one('hr.employee',string="副總")
    has_man3 = fields.Integer(string="has level3", default=0)
    flow_man4 = fields.Many2one('hr.employee',string="總經理")
    has_man4 = fields.Integer(string="has level4", default=0)
    flow_man5 = fields.Many2one('hr.employee',string="助理")
    write_lock = fields.Boolean(string="防寫",default=False)

    @api.model
    def create(self, vals):
        res = super(newebexpenseflow, self).create(vals)
        self.env.cr.execute("""select genexpenseflowman(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    def write(self, vals):
        if 'x_wkf_state' in vals:
           myflow = True
        else:
           myflow = False
        res = super(newebexpenseflow, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select genexpenseflowman(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        # if self.write_lock==True and myflow==False :
        #     raise UserError("單據已進入簽核流程了,不能異動了!")
        return res

    def expense_start(self):
        self.env.cr.execute("""update neweb_sale_analysis_expense_report set write_lock=True where id=%d""" % self.id)
        self.env.cr.execute("""commit""")

    def expense_email_1_line(self):
        self.env.cr.execute("""update neweb_sale_analysis_expense_report set write_lock=True where id=%d""" % self.id)
        self.env.cr.execute("""commit""")
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        for rec in self:
            local_context = self.env.context.copy()
            if rec.flow_man1.work_email and rec.flow_man1.work_email.strip():
                local_context.update({
                    'email_to': rec.flow_man1.work_email,
                    'order_url': base_url
                })
                template = self.env.ref('neweb_sale_analysis.expense_flow_message')
                template.with_context(local_context).send_mail(self.id, force_send=True)

    def expense_email_2_line(self):
        self.env.cr.execute("""update neweb_sale_analysis_expense_report set write_lock=True where id=%d""" % self.id)
        self.env.cr.execute("""commit""")
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        for rec in self:
            local_context = self.env.context.copy()
            if rec.flow_man2.work_email and rec.flow_man2.work_email.strip():
                local_context.update({
                    'email_to': rec.flow_man2.work_email,
                    'order_url': base_url
                })
                template = self.env.ref('neweb_sale_analysis.expense_flow_message')
                template.with_context(local_context).send_mail(self.id, force_send=True)

    def expense_email_3_line(self):
        self.env.cr.execute("""update neweb_sale_analysis_expense_report set write_lock=True where id=%d""" % self.id)
        self.env.cr.execute("""commit""")
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        for rec in self:
            local_context = self.env.context.copy()
            if rec.flow_man3.work_email and rec.flow_man3.work_email.strip():
                local_context.update({
                    'email_to': rec.flow_man3.work_email,
                    'order_url': base_url
                })
                template = self.env.ref('neweb_sale_analysis.expense_flow_message')
                template.with_context(local_context).send_mail(self.id, force_send=True)

    def expense_email_4_line(self):
        self.env.cr.execute("""update neweb_sale_analysis_expense_report set write_lock=True where id=%d""" % self.id)
        self.env.cr.execute("""commit""")
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        for rec in self:
            local_context = self.env.context.copy()
            if rec.flow_man4.work_email and rec.flow_man4.work_email.strip():
                local_context.update({
                    'email_to': rec.flow_man4.work_email,
                    'order_url': base_url
                })
                template = self.env.ref('neweb_sale_analysis.expense_flow_message')
                template.with_context(local_context).send_mail(self.id, force_send=True)

    def expense_email_1_reject(self):
        self.env.cr.execute("""update neweb_sale_analysis_expense_report set write_lock=False where id=%d""" % self.id)
        self.env.cr.execute("""commit""")
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        for rec in self:
            local_context = self.env.context.copy()
            if rec.flow_owner.work_email and rec.flow_owner.work_email.strip():
                local_context.update({
                    'email_to': rec.flow_owner.work_email,
                    'order_url': base_url
                })
                template = self.env.ref('neweb_sale_analysis.expense_flow_message_reject')
                template.with_context(local_context).send_mail(self.id, force_send=True)

    def expense_email_2_reject(self):
        self.env.cr.execute("""update neweb_sale_analysis_expense_report set write_lock=False where id=%d""" % self.id)
        self.env.cr.execute("""commit""")
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        for rec in self:
            local_context = self.env.context.copy()
            if rec.flow_man1.work_email != False :
                myemailto = rec.flow_owner.work_email + ',' + rec.flow_man1.work_email
            else:
                myemailto = rec.flow_owner.work_email
            if rec.flow_owner.work_email and rec.flow_owner.work_email.strip():
                local_context.update({
                    'email_to': myemailto,
                    'order_url': base_url
                })
                template = self.env.ref('neweb_sale_analysis.expense_flow_message_reject')
                template.with_context(local_context).send_mail(self.id, force_send=True)

    def expense_email_3_reject(self):
        self.env.cr.execute("""update neweb_sale_analysis_expense_report set write_lock=False where id=%d""" % self.id)
        self.env.cr.execute("""commit""")
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        myemailto=''
        for rec in self:
            local_context = self.env.context.copy()
            if rec.flow_man1.work_email != False :
                myemailto = rec.flow_owner.work_email + ',' + rec.flow_man1.work_email
            else:
                myemailto = rec.flow_owner.work_email
            if rec.flow_man2.work_email != False :
                myemailto = myemailto + ',' + rec.flow_man2.work_email
            if rec.flow_owner.work_email and rec.flow_owner.work_email.strip():
                local_context.update({
                    'email_to': myemailto,
                    'order_url': base_url
                })
                template = self.env.ref('neweb_sale_analysis.expense_flow_message_reject')
                template.with_context(local_context).send_mail(self.id, force_send=True)

    def expense_email_4_reject(self):
        self.env.cr.execute("""update neweb_sale_analysis_expense_report set write_lock=False where id=%d""" % self.id)
        self.env.cr.execute("""commit""")
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        myemailto=''
        for rec in self:
            local_context = self.env.context.copy()
            if rec.flow_man1.work_email != False :
                myemailto = rec.flow_owner.work_email + ',' + rec.flow_man1.work_email
            else:
                myemailto = rec.flow_owner.work_email
            if rec.flow_man2.work_email != False :
                myemailto = myemailto + ',' + rec.flow_man2.work_email
            if rec.flow_man3.work_email != False :
                myemailto = myemailto + ',' + rec.flow_man3.work_email
            if rec.flow_owner.work_email and rec.flow_owner.work_email.strip():
                local_context.update({
                    'email_to': myemailto,
                    'order_url': base_url
                })
                template = self.env.ref('neweb_sale_analysis.expense_flow_message_reject')
                template.with_context(local_context).send_mail(self.id, force_send=True)

    def expense_email_complete(self):
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        for rec in self:
            local_context = self.env.context.copy()
            if rec.flow_owner.work_email and rec.flow_owner.work_email.strip():
                local_context.update({
                    'email_to': rec.flow_owner.work_email,
                    'order_url': base_url
                })
                template = self.env.ref('neweb_sale_analysis.expense_flow_message_complete')
                template.with_context(local_context).send_mail(self.id, force_send=True)

