# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request

class repairflow(models.Model):
    _inherit = "neweb_repair.repair"

    # pos_type = fields.Char(string='簽核判斷字元')
    # flow_owner = fields.Many2one('hr.employee', string="OWNER")
    # flow_man1 = fields.Many2one('hr.employee', string="一線主管")
    # has_man1 = fields.Integer(string="has level1", default=0)
    # flow_man2 = fields.Many2one('hr.employee', string="二線主管")
    # has_man2 = fields.Integer(string="has level2", default=0)
    # flow_man3 = fields.Many2one('hr.employee', string="副總")
    # has_man3 = fields.Integer(string="has level3", default=0)
    # flow_man4 = fields.Many2one('hr.employee', string="總經理")
    # has_man4 = fields.Integer(string="has level4", default=0)
    # write_lock = fields.Boolean(string="防寫", default=False)

    # @api.model
    # def create(self, vals):
    #     res = super(repairflow, self).create(vals)
    #     self.env.cr.execute("""select genrepairflowman(%d)""" % res.id)
    #     self.env.cr.execute("""commit""")
    #     return res
    #
    # def write(self, vals):
    #     if 'x_wkf_state' in vals:
    #         myflow = True
    #     else:
    #         myflow = False
    #     res = super(repairflow, self).write(vals)
    #     for rec in self:
    #         self.env.cr.execute("""select genrepairflowman(%d)""" % rec.id)
    #         self.env.cr.execute("""commit""")
    #     # if self.write_lock == True and myflow == False:
    #     #     raise UserError("單據已進入簽核流程了,不能異動了!")
    #     return res


    def wk_repair_ae_process(self):  # 維修中
        # self.env.cr.execute("""update neweb_repair_repair set write_lock=True where id=%d""" % self.id)
        # self.env.cr.execute("""commit""")
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        for rec in self:
            local_context = self.env.context.copy()
            # if rec.flow_man1.work_email and rec.flow_man1.work_email.strip():
            local_context.update({
                # 'email_to': rec.flow_man1.work_email,
                'order_url': base_url
            })
            template = self.env.ref('neweb_repair.mail_template_repair_ae_process1')
            template.with_context(local_context).send_mail(self.id, force_send=True)


    def wk_repair_waiting(self):  # 待料中
        # self.env.cr.execute("""update neweb_repair_repair set write_lock=True where id=%d""" % self.id)
        # self.env.cr.execute("""commit""")
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        for rec in self:
            local_context = self.env.context.copy()
            # if rec.flow_man1.work_email and rec.flow_man1.work_email.strip():
            local_context.update({
                # 'email_to': rec.flow_man1.work_email,
                'order_url': base_url
            })
            template = self.env.ref('neweb_repair.mail_template_repair_waiting1')
            template.with_context(local_context).send_mail(self.id, force_send=True)

    def wk_repair_ae_manager(self):  # 工程師結案
        # self.env.cr.execute("""update neweb_repair_repair set write_lock=True where id=%d""" % self.id)
        # self.env.cr.execute("""commit""")
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        for rec in self:
            local_context = self.env.context.copy()
            # if rec.flow_man1.work_email and rec.flow_man1.work_email.strip():
            local_context.update({
                # 'email_to': rec.flow_man1.work_email,
                'order_url': base_url
            })
            template = self.env.ref('neweb_repair.mail_template_repair_ae_manager1')
            template.with_context(local_context).send_mail(self.id, force_send=True)

    def wk_repair_done(self):  # care call
        # self.env.cr.execute("""update neweb_repair_repair set write_lock=True where id=%d""" % self.id)
        # self.env.cr.execute("""commit""")
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        for rec in self:
            local_context = self.env.context.copy()
            # if rec.flow_man1.work_email and rec.flow_man1.work_email.strip():
            local_context.update({
                # 'email_to': rec.flow_man1.work_email,
                'order_url': base_url
            })
            template = self.env.ref('neweb_repair.mail_template_repair_done1')
            template.with_context(local_context).send_mail(self.id, force_send=True)