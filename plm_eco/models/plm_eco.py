# -*- coding: utf-8 -*-
# Author: Jason Wu (jaronemo@msn.com)

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from datetime import date
from odoo.tools.misc import DEFAULT_SERVER_DATE_FORMAT
from py3o.template import Template

include_bom = []


class MrpEco(models.Model):
    _inherit = 'mrp.eco'

    @api.multi
    def _def_employee_id(self):
        employee = self.env["hr.employee"].search([("user_id", "=", self.env.user.id)])
        if employee:
            return employee[0].id

    request_date = fields.Date(string='變更申請日期', required=True, copy=False, default=fields.Date.context_today,
                               track_visibility='onchange')
    origin_note = fields.Char(string='依據來源')
    product_list_ids = fields.One2many('mrp.eco.product.list', 'eco_id')
    product_list_origin_ids = fields.One2many('mrp.eco.product.list.origin', 'eco_id')
    reason_change_desc = fields.Text(string='變更原因', )
    doc_desc = fields.Html(string='附件說明')
    reason_ids = fields.Many2many('mrp.eco.reason', track_visibility='onchange', )
    reason_desc = fields.Text(string='其它說明', )
    employee_id = fields.Many2one('hr.employee', default=_def_employee_id, )
    origin_bom_id = fields.Integer(string='原始版本號', related='bom_id.version', store=True, readonly=True)

    @api.onchange('user_id')
    def _onchange_employee_id(self):
        self.employee_id = False
        employee = self.env["hr.employee"].search([("user_id", "=", self.user_id.id)])
        if employee:
            self.employee_id = employee[0].id
        else:
            raise UserError('此使用者未在員工資料設定關聯')

    @api.multi
    def mrp_bom_component_find(self, origin_id, component_id, level):
        cr = self._cr
        cr.execute("""
                select
                    mbl.sequence,
                    mbl.product_id,
                    mbl.product_qty,
                    mb.product_tmpl_id,
                    mb.id mb_id,
                    (select id from product_product
                     where product_tmpl_id=mb.product_tmpl_id limit 1) compose_id
                from mrp_bom_line mbl inner join mrp_bom mb on mbl.bom_id=mb.id
                where mb.active='true' and mbl.product_id=%s 
            """, (str(component_id),))
        result = cr.fetchall()

        for row in result:
            compose_id = row[5]
            level_txt = ''
            for i in range(1, level):
                level_txt = level_txt + u'-'
            level_txt = level_txt + str(level)
            if row[4] not in include_bom:
                vals = {
                    'eco_id': origin_id,
                    # 'level': level_txt,
                    'product_id': row[1],
                    # 'line': row[0],
                    # 'quantity': row[2],
                    'bom_id': row[4],
                }
                self.env['mrp.eco.product.list'].create(vals)
                self.env['mrp.eco.product.list.origin'].create(vals)
                include_bom.append(row[4])
                self.mrp_bom_component_find(origin_id, compose_id, level + 1)

    @api.multi
    def search_product_list(self):
        if len(self.product_list_ids) >= 1:
            if self.stage_id.name == '新建' or self.stage_id.name == '進行中':
                self.product_list_ids.unlink()
            else:
                raise UserError('待審核 或 已發行生效的 單據無法 進行相關機種的')

        for obj in self:
            products = self.env['product.product'].search([
                ('product_tmpl_id', '=', obj.product_tmpl_id.id)
            ])
            for product in products:
                if product:
                    # self.mrp_bom_component_find(obj.id, obj.product_id.id, 1)
                    # self.mrp_bom_component_find(self._origin.id, product.id, 1)  # 如果用onchange 方法，NEWID時可用此
                    self.mrp_bom_component_find(self.id, product.id, 1)

    @api.multi
    def generate_eco(self):
        vals_list = [{
            'origin_note': '依照' + self.name + '變更而進行升版',
            'type': 'bom',
            'type_id': self.type_id.id,
            'product_tmpl_id': item.bom_id.product_tmpl_id.id,
            'bom_id': item.bom_id.id,
            'stage_id': 2,
        } for item in self.product_list_ids]

        now_ids = self.create(vals_list)
        now_ids.action_new_revision()
        # eco_order_id = self.env['mrp.eco'].search([('id', '=', now_id.id)])

    @api.multi
    def unlink(self):
        for obj in self:
            if obj.stage_id.name == '新建':
                obj.unlink()
            else:
                raise UserError('已執行或進行中的 ECO 單據無法刪除')

    @api.multi
    def reminder_email_eco_details(self):
        if self.employee_id.work_email and self.employee_id.work_email.strip():
            template = self.env.ref('plm_eco.reminder_email_approve_details')
            mail_id = template.send_mail(self.id)
            mail_now = self.env['mail.mail'].browse(mail_id)
            mail_now.send()

    @api.model
    def reminder_email_details_scheduler(self):
        stage_ids = self.env['mrp.eco.stage'].search([('name', '=', '待審核')])
        search_ids = self.search([('stage_id', 'in', stage_ids.ids), ('effectivity', '=', 'date'), ])
        for r in search_ids:
            reminder_days = 10
            due_date = str(r.effectivity_date.date())
            mydate = datetime.strptime(due_date, DEFAULT_SERVER_DATE_FORMAT).date()
            mydate = mydate - timedelta(days=reminder_days)
            curr_date = datetime.today().date()
            if curr_date == mydate:
                if r.employee_id.work_email and r.employee_id.work_email.strip():
                    template = self.env.ref('plm_eco.reminder_email_approve_details')
                    mail_id = template.send_mail(r.id)
                    mail_now = self.env['mail.mail'].browse(mail_id)
                    mail_now.send()
        return True


class MrpEcoProductList(models.Model):
    _name = 'mrp.eco.product.list'
    _description = '相關機種'

    eco_id = fields.Many2one('mrp.eco', ondelete='cascade')
    bom_id = fields.Many2one('mrp.bom', 'Product')
    product_id = fields.Many2one('product.product', 'Component')
    categ_id = fields.Many2one('product.category', string='產品類別', readonly=True,
                               related='bom_id.product_tmpl_id.categ_id')


class MrpEcoProductListOrigin(models.Model):
    _name = 'mrp.eco.product.list.origin'
    _description = '相關機種'

    eco_id = fields.Many2one('mrp.eco', ondelete='cascade')
    bom_id = fields.Many2one('mrp.bom', 'Product')
    product_id = fields.Many2one('product.product', 'Component')
    categ_id = fields.Many2one('product.category', string='產品類別', readonly=True,
                               related='bom_id.product_tmpl_id.categ_id')
