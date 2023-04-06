# -*- coding:utf-8 -*-

from odoo import models, fields, api, _

import logging
from datetime import date
import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
import pytz

_logger = logging.getLogger(__name__)


class Repair(models.Model):
    _name = 'neweb_repair.repair'
    _description = "報修單"
    _sql_constraints = [('repair_no_uniq', 'unique(name)', 'Repair Number must be unique!!')]
    _order = "repair_datetime desc"

    @api.depends('repair_lines')
    def _compute_maintenance_category(self):
        for rec in self:
            for line in rec.repair_lines:
                if line.maintenance_category:
                    rec.maintenance_category = line.maintenance_category
                    break

    @api.depends('customer_id')
    def _get_customer_category(self):
        for rec in self:
            if rec.customer_id.customer_category_id:
                rec.customer_category_id = rec.customer_id.customer_category_id


    @api.depends('repair_lines')
    def _count_repair_line(self):
        for rec in self:
            rec.num_of_repair_lines = len(rec.repair_lines)

    @api.depends('ae_on_site_datetime', 'ae_complete_datetime')
    def _compute_ae_total_ma_time(self):
        try:
            # print(self.id)
            self.env.cr.execute("""select getaetotmatime(%d)""" % self.id)
            myres = self.env.cr.fetchone()[0]
            if myres:
               self.ae_total_ma_time = myres
            else:
               self.ae_total_ma_time = ' '
        except:
            self.ae_total_ma_time = ' '
            # com_dt = datetime.datetime.strptime(self.ae_complete_datetime, DEFAULT_SERVER_DATETIME_FORMAT)
            # onsite_dt = datetime.datetime.strptime(self.ae_on_site_datetime, DEFAULT_SERVER_DATETIME_FORMAT)
            # diff_time = relativedelta(com_dt,onsite_dt).hours
            # # diff_time = com_dt - onsite_dt
            # _logger.info('diff: %s' % diff_time)
            # self.ae_total_ma_time = "%s" % diff_time


    @api.depends('repair_lines', 'repair_datetime', 'ae_response_datetime', 'ae_on_site_datetime',
                 'ae_complete_datetime')
    def _compute_ae_is_sla_delay(self):
        self.ae_is_sla_delay = False
        try:
            self.env.cr.execute("""select chksladelay(%d)""" % self.id)
            myres = self.env.cr.fetchone()[0]
            if myres :
               self.ae_is_sla_delay = True
            else:
               self.ae_is_sla_delay = False
        except:
            self.ae_is_sla_delay = False
        # ori_res_time = None
        # ori_ons_time = None
        # ori_com_time = None
        # ["state","=","repair_closed"]

        # if self.repair_datetime:
        #     ori_repair_time = datetime.datetime.strptime(self.repair_datetime, DEFAULT_SERVER_DATETIME_FORMAT)
        #     for rline in self.repair_lines:
        #         if self.ae_response_datetime:
        #             ori_res_time = datetime.datetime.strptime(self.ae_response_datetime, DEFAULT_SERVER_DATETIME_FORMAT)
        #             chk_res_time = ori_res_time - ori_repair_time
        #             _logger.info("chk_res_time: %s" % chk_res_time)
        #             if rline.repair_sla and rline.repair_sla.response_time:
        #                 sla_res_time = rline.repair_sla.response_time
        #                 if sla_res_time > 0:
        #                     delta_sla_res_time = datetime.timedelta(hours=sla_res_time)
        #                     if chk_res_time > delta_sla_res_time:
        #                         self.ae_is_sla_delay = True
        #
        #         if self.ae_on_site_datetime:
        #             ori_ons_time = datetime.datetime.strptime(self.ae_on_site_datetime, DEFAULT_SERVER_DATETIME_FORMAT)
        #             chk_ons_time = ori_ons_time - ori_repair_time
        #             if rline.repair_sla and rline.repair_sla.onsite_time:
        #                 sla_ons_time = rline.repair_sla.onsite_time
        #                 if sla_ons_time > 0:
        #                     delta_sla_ons_time = datetime.timedelta(hours=sla_ons_time)
        #                     if chk_ons_time > delta_sla_ons_time:
        #                         self.ae_is_sla_delay = True
        #
        #         if self.ae_complete_datetime:
        #             ori_com_time = datetime.datetime.strptime(self.ae_complete_datetime, DEFAULT_SERVER_DATETIME_FORMAT)
        #             chk_com_time = ori_com_time - ori_repair_time
        #             if rline.repair_sla and rline.repair_sla.maintenance_time:
        #                 sla_man_time = rline.repair_sla.maintenance_time
        #                 if sla_man_time > 0:
        #                     delta_sla_man_time = datetime.timedelta(hours=sla_man_time)
        #                     if chk_com_time > delta_sla_man_time:
        #                         self.ae_is_sla_delay = True

    name = fields.Char(string='報修單號', required=True, copy=False, readonly=True, index=True, default='New')
    create_user = fields.Many2one('res.users', string="開單人員", default=lambda self: self.env.uid)
    create_date = fields.Date(string='開單日期', default=fields.Datetime.now)
    repair_type = fields.Selection([
        ('maintenance', 'Maintenance'),
        ('warranty', 'Warranty'),
        ('warranty_maintenance', 'Warranty + Maintenance'),
        ('per_call', 'Per Call'),
        ('outsourcing', '維運'),
        ('others', 'Others')
    ], string="維護類型")

    repair_datetime = fields.Datetime(string='報修時間', required=True, default=fields.Datetime.now)
    customer_id = fields.Many2one('res.partner', string='報修客戶', change_default=True, index=True, required=True)
    customer_category_id = fields.Many2one('neweb_base.customer_category', compute=_get_customer_category)
    contact_user = fields.Many2one('res.partner', string='報修人', change_default=True, index=True)
    contact_user1 = fields.Char(size=30, string="報修人員")

    # contact_tel = fields.Char(related='contact_user.phone', store=False, string='Tel')
    contact_tel = fields.Char(string='報修人/電話', required=True)

    ae_id = fields.Many2one('hr.employee', string='指派工程師')
    device_location = fields.Char(string='設備所在位置')
    contract_id = fields.Many2one('neweb_contract.contract', string='合約')

    ae_response_datetime = fields.Datetime(string='工程師回應時間')
    ae_on_site_datetime = fields.Datetime(string='工程師到場時間')
    ae_complete_datetime = fields.Datetime(string='工程師完修時間')
    ae_is_sla_delay = fields.Boolean(string='SLA Delay', compute=_compute_ae_is_sla_delay)
    ae_total_ma_time = fields.Char(string='Total Time', compute=_compute_ae_total_ma_time)
    # ae_description = fields.Text(string='Description')
    problem = fields.Many2one('neweb_base.problem', string="問題判斷")
    maintenance_category = fields.Many2one('neweb_base.maintenance_category', default=_compute_maintenance_category)
    repair_lines = fields.One2many('neweb_repair.repair_line', 'repair_id', string="維修內容明細")
    num_of_repair_lines = fields.Integer(compute=_count_repair_line)
    repair_work_logs = fields.One2many('neweb_repair.repair_work_log', 'repair_id', string="維修記錄")
    survey_ids = fields.One2many('neweb_repair.repair_questionnaire', 'repair_id', string="顧客滿意度調查")
    survey_remark = fields.Text(string="滿意度調查評論")
    repair_care_call_logs = fields.One2many('neweb_repair.repair_care_call_log', 'repair_id', string="Care Call Logs")

    end_customer = fields.Many2one("res.partner", string="終端客戶")
    device_contact = fields.Char(size=30, string="設備連絡人")
    device_tel = fields.Char(string="設備聯絡人/電話", required=True)

    memo = fields.Text(string='Remark')

    part_ready = fields.Boolean(string='Part Ready', default=True)  # , compute="_compute_part_ready", store=True)
    state = fields.Selection([
        ('repair_draft', _('Draft')),  # 草稿
        ('repair_waiting', _('Waiting')),  # 等料中
        ('repair_AE', _('AE Processing')),  # 工程師處理
        ('repair_Manager', _('Waiting for AE Manager Approval')),  # 指派工程師主管審核
        ('repair_done', _('Done')),  # 結案
        ('repair_cancel', _('Cancel')),  # 作廢
        ('repair_reject', _('Reject')),  # 退回(internal use)
        ('repair_open', _('Open')),  # 進call(internal use)
        ('repair_closed', _('Closed')),  # 結束flow(internal use)
    ], string='Status1', default='repair_draft', copy=False)
    care_call_date = fields.Date(string="Care Call日期")
    # care_call_date = fields.Date(related='repair_care_call_logs.care_call_date',string="Care Call日期")
    manager_note_line = fields.One2many('neweb_repair.manager_note', 'note_id', string="主管備註")
    sales = fields.Many2one('hr.employee', string="業務員", required=True)

    # op_name = fields.Char(string="項目說明",compute="_get_opname")

    # @api.depends()
    # def _get_opname(self):
    #     for rec in self:
    #         myid = rec.id
    #         self.env.cr.execute("""select getopname(%d)""" % myid)
    #         rec.update({'op_name':self.env.cr.fetchone()[0]})

    def reset_token_number_sequences(self):
        sequences = self.env['ir.sequence'].search([('code', '=', 'neweb_repair.repair')])
        for sequence in sequences:
            # print('Sequence#######################', sequence)
            sequence.write({
                'number_next': 1,
            })
        sequences1 = self.env['ir.sequence'].search([('code', '=', 'sale.order')])
        for sequence in sequences1:
            # print('Sequence#######################', sequence)
            sequence.write({
                'number_next': 1,
            })
        sequences2 = self.env['ir.sequence'].search([('code', '=', 'neweb_purinv.purinvoice')])
        for sequence in sequences2:
            # print('Sequence#######################', sequence)
            sequence.write({
                'number_next': 1,
            })
        sequences3 = self.env['ir.sequence'].search([('code', '=', 'neweb_sale_analysis.official_doc')])
        for sequence in sequences3:
            # print('Sequence#######################', sequence)
            sequence.write({
                'number_next': 1,
            })
        sequences4 = self.env['ir.sequence'].search([('code', '=', 'neweb_sale_analysis.travel_report')])
        for sequence in sequences4:
            # print('Sequence#######################', sequence)
            sequence.write({
                'number_next': 1,
            })
        sequences5 = self.env['ir.sequence'].search([('code', '=', 'neweb_sale_analysis.expense_report')])
        for sequence in sequences5:
            # print('Sequence#######################', sequence)
            sequence.write({
                'number_next': 1,
            })

        sequences6 = self.env['ir.sequence'].search([('code', '=', 'purchase.order')])
        for sequence in sequences6:
            # print('Sequence#######################', sequence)
            sequence.write({
                'number_next': 1,
            })



    @api.onchange('ae_id')
    def onclientchangeaeid(self):
        mycontactid = self.contract_id.id
        if not self.sales:
            self.sales = self.contract_id.sales

    # @api.depends('repair_lines')
    # def _get_repair_type(self):
    #     for line in self:
    #         if not line.repair_lines:
    #            line.update({'repair_type':'per_call'})

    # @api.depends('id')
    # def _get_carecalldate(self):
    #     for rec in self:
    #         myid = rec.id
    #         self.env.cr.execute("select get_carecalldate(%s)" % myid)
    #         self.env.cr.execute("commit")

    # 6/4 Peter Update
    # @api.onchange('contact_user')
    # def _contact_user_onchange(self):
    #     for rec in self:
    #         rec.contact_tel = rec.contact_user.phone



    # @api.model
    def get_repair_list(self, vals):
        criterial = []
        if vals.get('timeline'):
            criterial.append(('write_date', '>', vals.get('timeline')))
        if vals.get('repair_num'):
            criterial.append(('name', '>', vals.get('repair_num')))
        if vals.get('serial_num'):
            criterial.append(('repair_lines.contract_line.machine_serial_no', 'in', vals.get('serial_num')))

        repairs = self.env['neweb_repair.repair'].search_read(criterial,
                                                              ['name', 'write_date', 'repair_lines', 'repair_datetime',
                                                               'ae_id', 'ae_response_datetime', 'ae_on_site_datetime',
                                                               'ae_complete_datetime', 'problem'])

        for repair in repairs:
            if repair['ae_id']:
                repair['ae_id'] = repair['ae_id'][1]

            if repair['problem']:
                prob_solvs = self.env['neweb_base.problem_solution'].search_read(
                    [('problem_id', '=', repair['problem'][0])], ['name'])
                if prob_solvs:
                    repair['solutions'] = []
                    for prob_solv in prob_solvs:
                        repair['solutions'].append(prob_solv['name'])
                repair['problem'] = repair['problem'][1]

            if repair['repair_lines']:
                _repair_lines = []
                for repair_line_id in repair['repair_lines']:
                    repair_line_id = self.env['neweb_repair.repair_line'].search_read(
                        [('id', '=', int(repair_line_id))], ['contract_line'])
                    for plid in repair_line_id:
                        if plid['contract_line']:
                            cls = self.env['neweb_contract.contract.line'].search_read(
                                [('id', '=', int(plid['contract_line'][0]))], ['machine_serial_no'])
                            for cl in cls:
                                _repair_lines.append(cl['machine_serial_no'])

                repair['repair_lines'] = _repair_lines

        return repairs

    # @api.model
    def create_repair_from_client(self, vals):
        # _logger.info('Remote Call..........create_repair_from_client %s' % vals)
        # get or create contact user
        ctx = {
            'name': 'New',
            'repair_lines': [],
            'customer_id': None,
            'contact_user': None,
        }
        is_first = True

        rlines = []
        for obj in vals.get('repair_line_ids'):
            # _logger.info('contract line %s ' % obj[2].get('contract_line_id'))
            # _logger.info('problem desc %s ' % obj[2].get('problem_desc'))
            contract_line = self.env['neweb_contract.contract.line'].search(
                [('id', '=', obj[2].get('contract_line_id'))])
            cline_ctx = {
                'contract_line': contract_line.id,
                'problem_desc': obj[2].get('problem_desc'),
                # 'repair_sla':obj[2].get('repair_sla'),
            }
            r_tuple = (0, 0, cline_ctx)
            rlines.append(r_tuple)
            if is_first:
                # _logger.info('customer_name1 : %s' % contract_line)
                # _logger.info('customer_name2 : %s' % contract_line.contract_id)
                # _logger.info('customer_name3 : %s' % contract_line.contract_id.customer_name)
                ctx.update({'customer_id': contract_line.contract_id.customer_name.id})

                contact_user = self.env['res.partner'].search(
                    [('is_company', '=', False), ('parent_id', '=', contract_line.contract_id.customer_name.id),
                     ('name', '=', vals.get('contact_user_name'))])
                # _logger.info('contact_user : %s' % contact_user.name)

                # update by peter 6/4
                # if contact_user:
                #     if vals.get('contact_tel'):
                #         contact_user.write({'phone': vals.get('contact_tel')})
                # else:
                #     contact_user = self.env['res.partner'].create(
                #         {'name': vals.get('contact_user_name'), 'phone': vals.get('contact_tel'),
                #          'parent_id': contract_line.contract_id.customer_name.id})
                # ctx.update({'contact_user': contact_user.id})

                is_first = False

        ctx.update({'repair_lines': rlines})
        # _logger.info('ctx: %s' % ctx)
        repair_obj = self.env['neweb_repair.repair'].create(ctx)
        # _logger.info('repair_obj: %s' % repair_obj.name)

        return {'repair_id': repair_obj.id, 'repair_name': repair_obj.name}

    # @api.one


    @api.onchange('repair_lines', 'customer_id', 'contract_id', 'repair_type', 'id')
    def _repair_lines_onchange(self):
        for rec in self:
            self.env.cr.execute("select get_contact_person(%d)" % rec.contract_id)
            mycontact_tel = self.env.cr.fetchone()
            self.env.cr.execute("select get_contract_enduser(%d)" % rec.contract_id)
            endcustomer = self.env.cr.fetchone()
            if rec.contact_tel == 'NO CONTACT INFO' or not rec.contact_tel:
                rec.update({'contact_tel': mycontact_tel[0], 'sales': rec.contract_id.sales})
            if rec.device_tel == 'NO CONTACT INFO' or not rec.device_tel:
                rec.update({'device_tel': mycontact_tel[0]})
                # rec.update({'contact_tel':mycontact_tel[0],'device_tel':mycontact_tel[0]}
            if int(endcustomer[0]) > 0:
                rec.update({'end_customer': int(endcustomer[0])})
            if len(rec.repair_lines) > 0:
                rec.contract_id = rec.repair_lines[0].contract_line.contract_id
                # if not rec.repair_lines[0].contract_line.contract_id:
                #     self.repair_type = 'per_call'
                # elif self.repair_type == 'per_call':
                #     self.repair_type = ''

                if rec.repair_lines[0].contract_line.contract_id:
                    if rec.repair_lines[0].contract_line.contract_id.customer_name:
                        rec.customer_id = rec.repair_lines[0].contract_line.contract_id.customer_name
                        return {'domain': {'customer_id': [('id', '=', rec.customer_id.id)],
                                           'contract_id': [('id', '=', rec.contract_id.id)]}}

                return {'domain': {'contract_id': [('id', '=', rec.contract_id.id)]}}
            else:
                return {'domain': {'customer_id': [('is_company', '=', True)],
                                   'contract_id': [('state', 'in', ['contract_done']),
                                                   ('customer_name', '=?', rec.customer_id.id)]}}
            # rec.env.cr.execute("""select getmaintype(%d)""" % rec.id)
            # myres = rec.env.cr.fetchone()[0]
            # print("%s" % myres)
            # rec.update({'repair_type':myres})

    # @api.one


    # @api.one
    # @api.depends('repair_lines')
    # def _compute_part_ready(self):
    # 	if self.state in ['repair_draft', 'repair_open', 'repair_waiting', 'repair_AE']:
    # 		self.part_ready = True
    # 		for line in self.repair_lines:
    # 			for part in line.repair_parts:
    # 				product = self.env['product.product'].browse(part.prod.id)
    # 				if part.required_parts_qty > product.qty_available:
    # 					# self.write({'part_ready': False})
    # 					# self.write({'state': 'repair_open'})
    # 					self.part_ready = False
    # 					break
    #
    # 		self.write({'state': 'repair_open'})

    # @api.model
    def _get_login_user(self):
        create_user_id = self.env['res.users'].search([('id', '=', self._uid)])
        # _logger.info("login user: %s" % create_user_id)
        return create_user_id or create_user_id[0] or False

    # @api.model
    def _get_survey_questions(self):
        question_ids = self.env['neweb_repair.question'].search(
            [('questionnaire_id.code', '=', 'repair'), ('disabled', '=', False),
             ('questionnaire_id.disabled', '=', False)])
        # _logger.info("questions: %s" % question_ids)
        rq = self.env['neweb_repair.repair_questionnaire']
        rqs = []
        for qid in question_ids:
            _logger.info("qid: %s" % qid)
            res = rq.create({
                'question_id': qid.id,
                'rating': None,
            })
            rqs.append(res.id)

        return rqs


    def repair_ae_manager(self):
        print ("repair ae manager")
        myrepairid = self.env.context.get('repair_id')
        myrec = self.env['neweb_repair.repair'].search([('id', '=', myrepairid)])
        for obj in myrec:
            if (not obj.ae_complete_datetime) or (not obj.ae_on_site_datetime) or (not obj.ae_response_datetime) or (
                    not obj.problem) or (len(obj.repair_work_logs) < 1):
                raise UserError(_(
                    'You cannot resolve case that missing following data. \n Problem. \n AE Response Time. \n AE On-Site Time. \n AE Complete Time. \n Work Logs.'))

        need_send_warn_mail = False
        mail_tmp_id = self.env['mail.template'].search([('name', '=', 'Repair-SLA_Warn_template')])
        ori_res_time = None
        ori_ons_time = None
        ori_com_time = None

        send_rlines = []

        if self.repair_datetime:
            ori_repair_time = datetime.datetime.strptime(self.repair_datetime, DEFAULT_SERVER_DATETIME_FORMAT)
            for rline in self.repair_lines:
                if self.ae_response_datetime:
                    ori_res_time = datetime.datetime.strptime(self.ae_response_datetime, DEFAULT_SERVER_DATETIME_FORMAT)
                    chk_res_time = ori_res_time - ori_repair_time
                    if rline.repair_sla and rline.repair_sla.response_time:
                        sla_res_time = rline.repair_sla.response_time
                        if sla_res_time > 0:
                            delta_sla_res_time = datetime.timedelta(hours=sla_res_time)
                            if chk_res_time > delta_sla_res_time:
                                if rline.sla_delay_warn:
                                    send_rlines.append(rline)

                if self.ae_on_site_datetime:
                    ori_ons_time = datetime.datetime.strptime(self.ae_on_site_datetime, DEFAULT_SERVER_DATETIME_FORMAT)
                    chk_ons_time = ori_ons_time - ori_repair_time
                    if rline.repair_sla and rline.repair_sla.onsite_time:
                        sla_ons_time = rline.repair_sla.onsite_time
                        if sla_ons_time > 0:
                            delta_sla_ons_time = datetime.timedelta(hours=sla_ons_time)
                            if chk_ons_time > delta_sla_ons_time:
                                if rline.sla_delay_warn:
                                    send_rlines.append(rline)

                if self.ae_complete_datetime:
                    ori_com_time = datetime.datetime.strptime(self.ae_complete_datetime, DEFAULT_SERVER_DATETIME_FORMAT)
                    chk_com_time = ori_com_time - ori_repair_time
                    if rline.repair_sla and rline.repair_sla.maintenance_time:
                        sla_man_time = rline.repair_sla.maintenance_time
                        if sla_man_time > 0:
                            delta_sla_man_time = datetime.timedelta(hours=sla_man_time)
                            if chk_com_time > delta_sla_man_time:
                                if rline.sla_delay_warn:
                                    send_rlines.append(rline)

        if len(send_rlines) > 0:
            _logger.info('rlines ： %s' % send_rlines)
            context = {}
            self.pool['mail.template'].send_mail(self.env.cr, self.env.uid, mail_tmp_id.id, self.id, force_send=True,
                                                 context=context)

        return self.write({'state': 'repair_Manager'})


    def action_close(self):
        if self.ae_reponse_datetime == False:
            raise UserError("工程師回應時間未輸入！")
        if self.ae_on_site_datetime == False:
            raise UserError("工程師到場時間未輸入！")
        if self.ae_complete_datetime == False:
            raise UserError("工程師完修時間未輸入！")
        if self.problem == False:
            raise UserError("Problem Judgment未輸入！")
        return self.write({'state': 'repair_closed'})


    def action_done(self):
        if self.ae_response_datetime == False:
            raise UserError("工程師回應時間未輸入！")
        if self.ae_on_site_datetime == False:
            raise UserError("工程師到場時間未輸入！")
        if self.ae_complete_datetime == False:
            raise UserError("工程師完修時間未輸入！")
        if self.problem == False:
            raise UserError("Problem Judgment未輸入！")
        self.write({'state': 'repair_Manager'})
        return


    def action_open(self):
        # print "ACTION OPEN"
        if self.state in ['repair_draft', 'repair_open', 'repair_waiting', 'repair_AE']:
            self.write({'part_ready': True})
            for line in self.repair_lines:
                for part in line.repair_parts:
                    product = self.env['product.product'].browse(part.prod.id)
                    if part.required_parts_qty > product.qty_available:
                        self.write({'part_ready': False})
                        break
        # _logger.info("part ready: %s" % self.part_ready)
        return self.write({'state': 'repair_open'})


    def repair_check(self):
        if self.state in ['repair_waiting', 'repair_AE']:
            self.write({'part_ready': True})
            for line in self.repair_lines:
                for part in line.repair_parts:
                    product = self.env['product.product'].browse(part.prod.id)
                    if part.required_parts_qty > product.qty_available:
                        self.write({'part_ready': False})
                        break

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            seq_code = self.env['ir.sequence'].next_by_code('neweb_repair.repair') or 'New'
            # curr_ymd = datetime.datetime.strftime(datetime.datetime.now(), '%y%m')
            # cont = self.env['neweb_contract.contract'].browse(vals.get('contract_id')).name or ''
            vals['name'] = seq_code
        if not vals['repair_lines']:
            raise UserError("未輸入報修問題描述,請確認")
        # if 'repair_type' in vals and not vals['repair_type']:
        #     # self.env.cr.execute("""select getmaintype(%d)""" % self.id)
        #     # vals['repair_type'] = self.env.cr.fetchone()[0]
        #     raise  UserError("未輸入報修種類,請確認")

        result = super(Repair, self).create(vals)
        return result

    # @api.model
    def process_sla_warn(self):
        _logger.info("process_SLA_warn")
        mail_tmp_id = self.env['mail.template'].search([('name', '=', 'Repair-SLA_Warn_template')])
        _logger.info("mail tmp id is %s" % mail_tmp_id.id)
        self.pool['mail.template'].send_mail(self.env.cr, self.env.uid, mail_tmp_id.id, self.id, force_send=True,
                                             context=self.env.context)

    # @api.model
    def get_emails(self):
        all_mails = []
        mymachineserialno=' '
        for line in self.repair_lines:
            if not line.machine_serial_no :
                myserialno =' '
            else:
                myserialno = line.machine_serial_no
            mymachineserialno = mymachineserialno +'/ '+ myserialno
        myrec = self.env['neweb_repair.mail_member'].search([])
        for rec in myrec:
            for member in rec.repair_member:
                if not mymachineserialno and member.id == 1125:
                    A = 1
                else:
                    if member.work_email not in all_mails:
                        all_mails.append(member.work_email)

        if self.ae_id and self.ae_id.work_email not in all_mails:
            all_mails.append(self.ae_id.work_email)
            if self.ae_id.parent_id and self.ae_id.parent_id.work_email not in all_mails:
                all_mails.append(self.ae_id.parent_id.work_email)

        if self.contract_id:
            if self.contract_id.sales and self.contract_id.sales.work_email not in all_mails:
                all_mails.append(self.contract_id.sales.work_email)
                if self.contract_id.sales.parent_id and self.contract_id.sales.parent_id.work_email not in all_mails:
                    all_mails.append(self.contract_id.sales.parent_id.work_email)

            if self.contract_id.ae1:
                for rec in self.contract_id.ae1:
                    if rec.active and rec.work_email not in all_mails:
                        all_mails.append(rec.work_email)
                    if rec.parent_id:
                        if rec.parent_id.active and rec.parent_id.work_email not in all_mails:
                            all_mails.append(rec.parent_id.work_email)

        if self.repair_type == 'hw_outsourcing' or self.repair_type == 'soft_outsourcing':

            myrec = self.env['neweb_repair.mail_member'].search([])
            for rec in myrec:
                for member in rec.outsource_member:
                    if member.work_email not in all_mails:
                        all_mails.append(member.work_email)

        return ','.join(str(mail) for mail in all_mails)

    # @api.model
    def _get_context_contract_id(self):
        _logger.info('contract_id:%s' % self.env.context.get('contract_id'))
        if self.env.context.get('contract_id'):
            obj_contract = self.env['neweb_contract.contract'].search(
                [('id', '=', self.env.context.get('contract_id'))])
            return obj_contract or obj_contract[0] or False

    # @api.model
    def _get_context_customer_id(self):
        _logger.info('customer_id:%s' % self.env.context.get('customer_id'))
        if self.env.context.get('customer_id'):
            obj_customer = self.env['res.partner'].search([('id', '=', self.env.context.get('customer_id'))])
            return obj_customer or obj_customer[0] or False

    # @api.model
    def _get_now(self):
        return pytz.utc.localize(datetime.datetime.now()).astimezone(
            pytz.timezone(self.env['res.users'].browse(self._uid).tz))

    _defaults = {
        'create_user': _get_login_user,
        # 'create_date': _get_now,
        # 'repair_datetime': _get_now,
        # 'create_date': datetime.date.today(),
        'survey_ids': _get_survey_questions,
        'contract_id': _get_context_contract_id,
        'customer_id': _get_context_customer_id,
    }


class RepairManagerNote(models.Model):
    _name = "neweb_repair.manager_note"
    _description = "Manager Note"

    note_id = fields.Many2one('neweb_repair.repair', ondelete='cascade', string="Manager Note")
    note_desc = fields.Text(string="主管Memo")


class RepairLine(models.Model):
    _name = 'neweb_repair.repair_line'
    _description = "Repair Lines"
    _order = 'sequence'

    @api.depends('contract_line')
    def _get_machine_serial_no1(self):
        for rec in self:
            if rec.contract_line:
                self.env.cr.execute("""select getmachineserialno(%d)""" % rec.contract_line.id)
                rec.machine_serial_no1 = self.env.cr.fetchone()[0]
                rec.machine_serial_no = rec.machine_serial_no1
            else:
                rec.machine_serial_no1 = False
                rec.machine_serial_no = False

    @api.depends('contract_line')
    def _compute_sla(self):
        for rec in self:
            if rec.contract_line.prod_sla:
                rec.repair_sla = rec.contract_line.prod_sla
            else:
                rec.repair_sla = False
            # elif rec.contract_line.contract_id:
            #     rec.repair_sla = rec.contract_line.contract_id.sla

    @api.depends('machine_serial_no1')
    def _get_repeatcallnum(self):
        self.env.cr.execute("""select getserialrepcall('%s')""" % self.machine_serial_no1)
        self.repeat_call_num = self.env.cr.fetchone()[0]

    sequence = fields.Integer('sequence', help="Sequence for the handle.", default=10)
    name = fields.Char(related='contract_line.machine_serial_no', store=False)
    contract_line = fields.Many2one('neweb_contract.contract.line', string="機器序號")

    repair_sla = fields.Many2one('neweb_base.sla', string="SLA名稱", compute=_compute_sla)
    sla_delay_warn = fields.Boolean(string="SLA延遲警示")
    maintenance_category = fields.Many2one('neweb_base.maintenance_category',
                                           related="contract_line.prod.maintenance_category_id",
                                           string="維護類型")
    problem_desc = fields.Text(string="問題描述")

    related_parts = fields.One2many('neweb_base.product_link', string="硬體明細",
                                    related="contract_line.prod.prod_ids")
    repair_parts = fields.One2many('neweb_repair.repair_part', 'repair_line_id', string="維修零件")
    repair_id = fields.Many2one('neweb_repair.repair', ondelete='cascade', string="報修")
    state = fields.Selection(related='repair_id.state', store=True)

    # 2016/04/20
    asset_num = fields.Char(string='Asset Number')
    ip_address = fields.Char(string='IP Address')
    memo_desc = fields.Text(related='contract_line.memo', store=False)
    problem_desc = fields.Text(string="問題描述", required=True)
    machine_serial_no = fields.Char(string="序號")
    machine_serial_no1 = fields.Char(string="序號1", store=True,compute=_get_machine_serial_no1)
    repair_timesheet_worktype = fields.Selection([('1', '硬體處理'), ('2', '軟體處理')], string="報修工時分類", default='1')
    repeat_call_num = fields.Integer(string="3個月內Repeat次數", default=0, compute=_get_repeatcallnum)





    @api.onchange('machine_serial_no1')
    def onchangemachineserialno(self):
        self.env.cr.execute("""select getcontractlineid('%s')""" % self.machine_serial_no1)
        myres = self.env.cr.fetchone()
        # if myres[0] > 0 :
        #     self.contract_line = myres[0]
        return {'domain': {'contract_line': [('id', '=', myres[0])]}}
        # self.contract_line = myres[0]

    # @api.model
    # def create(self, vals):
    #     if 'problem_desc' in vals and not vals['problem_desc']:
    #         raise UserError("未輸入 問題描述 ,請確認!")
    #     rec=super(RepairLine,self).create(vals)
    #     return rec
    #
    # @api.multi
    # def write(self, vals):
    #     if 'problem_desc' in vals and not vals['problem_desc']:
    #         raise UserError("未輸入 問題描述 ,請確認!")
    #     rec = super(RepairLine, self).write(vals)
    #     return rec

    # @api.multi
    def _compute_related_parts_prod(self):
        self.related_parts_prod = [e.prod.id for e in self.contract_line.prod.prod_ids]


        # print "%s" % self.contract_line.prod_sla
        # print "%s" % self.repair_sla

    @api.onchange('contract_line')
    def _contract_line_onchange(self):
        self._compute_related_parts_prod()
        self._compute_sla()
        self.related_parts = []
        if self.repair_id.repair_type == 'per_call':
            no_contract_lines = [e.id for e in
                                 self.env['neweb_contract.contract.line'].search([('contract_id', '=', False)])]
            return {'domain': {'contract_line': [('id', 'in', no_contract_lines)]}}
        else:
            contract_lines = [e.id for e in self.env['neweb_contract.contract.line'].search(
                [('contract_id', '=?', self.repair_id.contract_id.id), '|',
                 ('contract_id.customer_name', '=?', self.repair_id.customer_id.id),
                 ('contract_id.end_customer', '=?', self.repair_id.customer_id.id)])]
            return {'domain': {'contract_line': [('id', 'in', contract_lines)]}}

        # @api.onchange('problem')
        # def _problem_onchange(self):
        # 	self.problem_representation = None
        # 	self.problem_solution = None
        # 	problem = self.env['neweb_base.problem'].browse(self.problem.id)
        # 	self.problem_desc = problem.description
        # 	return {'domain': {'problem_representation': [('id', 'in', [e.id for e in problem.problem_representation])], 'problem_solution': [('id', 'in', [e.id for e in problem.problem_solution])]}}

        # @api.onchange('repair_parts')
        # def _repair_parts_onchange(self):
        # 	# self.env.context._context.update({'related_parts_prod': []})
        # 	print self.env.context.get('related_parts_prod', [])


class RepairPart(models.Model):
    _name = 'neweb_repair.repair_part'
    _description = "Repair Parts"

    @api.depends('prod')
    def _get_maintenance_category(self):
        for rec in self:
            _logger.info("1: %s" % rec.prod)
            _logger.info("2: %s" % rec.prod.product_tmpl_id)

            if rec.repair_line_id.contract_line.prod.maintenance_category_id:
                _logger.info("3: %s" % rec.repair_line_id.contract_line.prod.maintenance_category_id)
                rec.part_maintenance_category_id = rec.repair_line_id.contract_line.prod.maintenance_category_id

    @api.onchange('prod', 'required_parts_qty')
    def _prod_onchange(self):
        product = self.env['product.product'].browse(self.prod.id)
        if product and self.required_parts_qty > product.qty_available:
            return {'warning': {'title': _('warning'), 'message': (
                    _('%s inventory shortage. available: %d') % (product.name, product.qty_available))}}

    name = fields.Char(related='prod.name', store=False)
    prod = fields.Many2one('product.product', string="料號", required=True)
    required_parts_qty = fields.Integer(string="需求數量")
    used_parts_qty = fields.Integer(string="耗用數量")
    repair_line_id = fields.Many2one('neweb_repair.repair_line', ondelete='cascade', string="維修明細")
    state = fields.Selection(related='repair_line_id.state', store=True)
    part_maintenance_category_id = fields.Many2one('neweb_base.maintenance_category',default=_get_maintenance_category)
    parts_categ = fields.Many2one('neweb_repair.parts_categ', string='零件類別')


# @api.one



class RepairWorkLog(models.Model):
    _name = 'neweb_repair.repair_work_log'
    _description = "Repair Work Log"

    work_date = fields.Date(string="維修日期",
                            default=lambda self: datetime.datetime.now().strftime(DEFAULT_SERVER_DATE_FORMAT))
    work_log = fields.Text(string="維修內容")
    repair_id = fields.Many2one('neweb_repair.repair', ondelete='cascade', string="報修單")
    state = fields.Selection(related='repair_id.state', store=True)


class RepairCareCallLog(models.Model):
    _name = 'neweb_repair.repair_care_call_log'
    _description = "Repair Care Call Log"

    care_call_date = fields.Date(string="Care Call日期",
                                 default=lambda self: datetime.datetime.now().strftime(DEFAULT_SERVER_DATE_FORMAT))
    care_call_log = fields.Text(string="Care Call內容")
    repair_id = fields.Many2one('neweb_repair.repair', ondelete='cascade', string="報修單")
    state = fields.Selection(related='repair_id.state', store=True)

    @api.model
    def create(self, vals):
        myid = self.repair_id
        res = super(RepairCareCallLog, self).create(vals)
        self.env.cr.execute("select get_carecalldate(%d)" % myid)
        self.env.cr.execute("commit")
        return res


class RepairQuestionnaire(models.Model):
    _name = 'neweb_repair.repair_questionnaire'
    _description = "Repair Questionnaire"

    question_id = fields.Many2one('neweb_repair.question', string='問題')
    rating = fields.Selection([
        ('', ''),
        ('1', _('Very Dissatisfied')),
        ('2', _('Somewhat Dissatisfied')),
        ('3', _('Neither Satisfied Nor Dissatisfied')),
        ('4', _('Somewhat Satisfied')),
        ('5', _('Very Satisfied'))
    ], string="級別")

    repair_id = fields.Many2one('neweb_repair.repair', ondelete='cascade', string="報修單")
    state = fields.Selection(related='repair_id.state', store=True)


class RepairPartsCateg(models.Model):
    _name = "neweb_repair.parts_categ"

    name = fields.Char(string="零件類別名稱", required=True)

    @api.model
    def create(self, vals):
        myname = self.name
        mycount = self.env['neweb_repair.parts_categ'].search_count([('name', '=', myname)])
        if mycount > 0:
            raise UserError("零件類別重複,請確認")
        res = super(RepairPartsCateg, self).create(vals)
        return res
