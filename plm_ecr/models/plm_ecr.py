# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.http import request

class MrpEcrOrder(models.Model):
    _name = 'mrp.ecr.order'
    _description = 'For Company Employee use ECR Order to Engineer Check'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # @api.model
    # def _get_default_name(self):
    #     return self.env['ir.sequence'].next_by_code('mrp.ecr.order')

    @api.model
    def _company_get(self):
        company_id = self.env['res.company']._company_default_get(self._name)
        return self.env['res.company'].browse(company_id.id)

    @api.multi
    def _def_department_id(self):
        employee = self.env["hr.employee"].search([("user_id", "=", self.env.user.id)])
        if employee:
            return employee[0].department_id

    @api.multi
    def _def_employee_id(self):
        employee = self.env["hr.employee"].search([("user_id", "=", self.env.user.id)])
        if employee:
            return employee[0].id

    name = fields.Char(string='申請編號', Readonly=True, default='New', track_visibility='onchange', required=True,
                       copy=False)
    ecr_date = fields.Date(string='申請日期', required=True, track_visibility='onchange',
                           states={"confirmed": [("readonly", False)], "reject": [("readonly", True)],
                                   "done": [("readonly", True)], })

    # product_name = fields.Char(string='產品型號', required=True, track_visibility='onchange',
    #                            states={"reject": [("readonly", True)],
    #                                    "done": [("readonly", True)], })
    # product_jpg_name = fields.Char(string='品(圖)名', track_visibility='onchange',
    #                                states={"reject": [("readonly", True)],
    #                                        "done": [("readonly", True)], })
    # product_jpg_number = fields.Char(string='品(圖)號', track_visibility='onchange',
    #                                  states={"reject": [("readonly", True)],
    #                                          "done": [("readonly", True)], })
    # product_id = fields.Many2one('product.product', string='產品代碼', required=True, track_visibility='onchange',
    #                              states={"confirmed": [("readonly", False)], "reject": [("readonly", True)],
    #                                      "done": [("readonly", True)], })
    department_id = fields.Many2one("hr.department", default=_def_department_id, required=True, string='申請部門',
                                    track_visibility='onchange',
                                    states={"confirmed": [("readonly", False)], "reject": [("readonly", True)],
                                            "done": [("readonly", True)], })
    company_id = fields.Many2one('res.company', string='公司',
                                 required=True,
                                 default=_company_get,
                                 track_visibility='onchange')
    employee_id = fields.Many2one('hr.employee', default=_def_employee_id, string='申請', track_visibility='onchange',
                                  domain="[('department_id', '=', department_id)]",
                                  states={"confirmed": [("readonly", False)], "reject": [("readonly", True)],
                                          "done": [("readonly", True)], })
    state = fields.Selection([("draft", "草稿"), ("confirmed", "申請中"), ('reject', '拒絕'), ('done', '已完成')],
                             default="draft", string='狀態',
                             copy=False)

    reason_desc = fields.Text(string='申請原因說明', states={"reject": [("readonly", True)],
                                                       "done": [("readonly", True)], })
    reason_change_desc = fields.Text(string='變更內容及說明', states={"reject": [("readonly", True)],
                                                               "done": [("readonly", True)], })
    cost_diff = fields.Text(string='成本差異說明')
    change_agree = fields.Selection([('A', '同意 ( 簽發“設計變更 ECO 單”)'), ('B', '不同意')], string='是否同意變更',
                                    track_visibility='onchange',
                                    states={"reject": [("readonly", True)], "done": [("readonly", True)]})
    change_agree_desc = fields.Text(string='原因說明', states={"reject": [("readonly", True)],
                                                           "done": [("readonly", True)], })
    approve_user = fields.Many2one('res.users', string='執行人',
                                   states={"reject": [("readonly", True)], "done": [("readonly", True)], })
    approve_employee_id = fields.Many2one('hr.employee')
    reason_ids = fields.Many2many('mrp.ecr.reason', track_visibility='onchange', states={"reject": [("readonly", True)],
                                                                                         "done": [
                                                                                             ("readonly", True)], })
    # ecr_line_ids = fields.One2many('mrp.ecr.order.line', 'order_id', copy=True,
    #                                track_visibility='onchange')
    product_tmpl_id = fields.Many2one('product.template', string='產品')
    mrp_eco_id = fields.Many2one('mrp.eco', string='設計變更 ECO 單單號：')
    member_ids = fields.Many2many('eco.tracking.member')

    sale_reason_desc = fields.Text(string='業務意見', )
    sale_employee = fields.Char(string='業務單位負責人員')
    manage_reason_desc = fields.Text(string='生管說明', )
    manage_employee = fields.Char(string='生管單位負責人員')

    purchase_reason_desc = fields.Text(string='採購說明', )
    purchase_employee = fields.Char(string='採購單位負責人員')

    wms_reason_desc = fields.Text(string='倉管說明', )
    wms_employee = fields.Char(string='倉管單位負責人員')

    qc_reason_desc = fields.Text(string='品保說明', )
    qc_employee = fields.Char(string='品保單位負責人員')

    assembly_reason_desc = fields.Text(string='組裝說明', )
    assembly_employee = fields.Char(string='組裝單位負責人員')

    manufacture_reason_desc = fields.Text(string='製造處說明', )
    manufacture_employee = fields.Char(string='製造單位負責人員')

    manager_reason_desc = fields.Text(string='管理處說明', )
    manager_employee = fields.Char(string='管理處負責人員')

    @api.onchange('approve_user')
    def _onchange_employee_id(self):
        self.approve_employee_id = False
        employee = self.env["hr.employee"].search([("user_id", "=", self.approve_user.id)])
        if employee:
            self.approve_employee_id = employee[0].id
        else:
            raise UserError('此執行人未在員工資料設定關聯郵件')

    @api.multi
    def reminder_email_ecr_details(self):
        if self.employee_id.work_email and self.employee_id.work_email.strip() and self.approve_employee_id.work_email and self.approve_employee_id.work_email.strip():
            template = self.env.ref('plm_ecr.reminder_email_ecr_order_details')
            mail_id = template.send_mail(self.id)
            # mail_now = self.env['mail.mail'].browse(mail_id)
            # mail_now.send()

    @api.multi
    def reminder_email_ecr_member_details(self):
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        for rec in self.member_ids:
            local_context = self.env.context.copy()
            if rec.tracking_member.work_email and rec.tracking_member.work_email.strip():
                local_context.update({
                    'email_to': rec.tracking_member.work_email,
                    'order_url': base_url
                })
                template = self.env.ref('plm_ecr.reminder_email_ecr_order_member_details')
                template.with_context(local_context).send_mail(self.id, force_send=True)
                # mail_now = self.env['mail.mail'].browse(mail_id)
                # mail_now.send()

    @api.multi
    def button_confirmed(self):
        self.ensure_one()
        self.write({'state': 'confirmed'})

    @api.multi
    def button_reject(self):
        self.ensure_one()
        if self.change_agree == 'B' and len(self.change_agree_desc) <= 0:
            raise UserError('因不同意此申請單，故請填寫拒絕申請之原因')
        else:
            self.write({'state': 'reject'})

    @api.multi
    def button_done(self):
        self.ensure_one()
        self.write({'state': 'done'})

    @api.multi
    def generate_eco_order(self):
        self.ensure_one()
        eco = self.env['mrp.eco']
        type_ids = self.env['mrp.eco.type'].search([('name', '=', '現有產品變更')])
        bom_id = self.env['mrp.bom'].search(
            [('product_tmpl_id', '=', self.product_tmpl_id.id), ('active', '=', True)])
        vals = {
            'name': '依照 ' + self.name,
            'type': 'bom',
            'type_id': type_ids.id,
            'product_tmpl_id': self.product_tmpl_id.id,
            'bom_id': bom_id.id,
            'stage_id': 1,
            'origin_note': '依照 ' + self.name,
        }

        now_id = eco.create(vals)
        self.mrp_eco_id = now_id.id
        # now_ids.action_new_revision()

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'mrp.ecr.order') or 'New'
        result = super(MrpEcrOrder, self).create(vals)
        return result

# class MrpEcrOrderLine(models.Model):
#     _name = 'mrp.ecr.order.line'
#     _description = 'MrpEcoOrderLine Product'
#     _order = 'sequence, id'
#
#     order_id = fields.Many2one(comodel_name='mrp.ecr.order', ondelete='cascade', required=True, index=True)
#     sequence = fields.Integer(string='Sequence', default=1, )
#     product_tmp_id = fields.Many2one('product.template', string='品(圖)名',)
