# -*- coding: utf-8 -*-
import logging
import pytz

# from core.biznavi.tools import compose_body
from odoo.exceptions import ValidationError
from odoo import models, fields, api, _
import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

_logger = logging.getLogger(__name__)


class Contract(models.Model):
    _name = 'neweb_contract.contract'
    # _inherit = ['mail.thread', 'ir.needaction_mixin']
    _description = "合約"
    _sql_constraints = [('contract_no_uniq', 'unique(name)', 'Contract Number must be unique!!')]
    _defaults = {
        'is_sales_contract': True,
    }

    @api.depends('contract_line_ids')
    def _count_contract_line(self):
        for rec in self:
            rec.num_of_contract_lines = len(rec.contract_line_ids)

    def _get_form_url(self):
        check_url_m = False
        check_url_a = False
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        _logger.info('baseurl : %s' % base_url)
        menu_ids = self.env['ir.ui.menu'].search([('name', '=', 'Contract'), ('parent_id', '!=', None)])
        if menu_ids:
            menu_id = menu_ids[0].id
            check_url_m = True
        action_ids = self.env['ir.actions.actions'].search([('name', '=', 'Contract')])
        if action_ids:
            action_id = action_ids[0].id
            check_url_a = True
        for rec in self:
            if check_url_m and check_url_a:
                rec.form_url = "%s/web?#id=%s&view_type=form&model=neweb_contract.contract&menu_id=%s&action=%s" % (
                    base_url, rec.id, menu_id, action_id)
            else:
                rec.form_url = ""

    is_sales_contract = fields.Boolean(string="買賣合約")
    is_warranty_contract = fields.Boolean(string="保固合約")
    is_rental_contract = fields.Boolean(string="租賃合約")
    is_maintenance_contract = fields.Boolean(string="維護合約")
    is_outsourcing_service = fields.Boolean(string="維運合約")

    name = fields.Char(string="合約編號", copy=False, readonly=True, index=True, default='New')
    project_no = fields.Char(string="專案編號",index=True)
    customer_name = fields.Many2one('res.partner', string="客戶名稱", change_default=True, index=True)
    end_customer = fields.Many2one('res.partner', string="終端客戶", change_default=True, index=True)
    clinch_date = fields.Date(string="承交日疑")

    weekly_maintain_day = fields.Selection([('1', 'Mon-Fri'), ('2', 'Mon-Sun')], string='Weekly Maintain Day',default='1')
    daily_maintain_hour_start = fields.Selection(
        [('0', "00:00"), ('1', "00:30"), ('2', "01:00"), ('3', "01:30"), ('4', "02:00"), ('5', "02:30"), ('6', "03:00"), ('7', "03:30"), ('8', "04:00"), ('9', "04:30"), ('10', "05:00"), ('11', "05:30"), ('12', "06:00"), ('13', "06:30"), ('14', "07:00"), ('15', "07:30"), ('16', "08:00"), ('17', "08:30"), ('18', "09:00"), ('19', "09:30"),
         ('20', "10:00"), ('21', "10:30"), ('22', "11:00"), ('23', "11:30"), ('24', "12:00"), ('25', "12:30"), ('26', "13:00"), ('27', "13:30"), ('28', "14:00"), ('29', "14:30"), ('30', "15:00"), ('31', "15:30"), ('32', "16:00"), ('32', "16:30"), ('34', "17:00"), ('35', "17:30"), ('36', "18:00"), ('37', "18:30"), ('38', "19:00"),
         ('39', "19:30"), ('40', "20:00"), ('41', "20:30"), ('42', "21:00"), ('43', "21:30"), ('44', "22:00"), ('45', "22:30"), ('46', "23:00"), ('47', "23:30")], string="每日維護開始時間",default='16')
    daily_maintain_hour_end = fields.Selection(
        [('0', "00:00"), ('1', "00:30"), ('2', "01:00"), ('3', "01:30"), ('4', "02:00"), ('5', "02:30"), ('6', "03:00"), ('7', "03:30"), ('8', "04:00"), ('9', "04:30"), ('10', "05:00"), ('11', "05:30"), ('12', "06:00"), ('13', "06:30"), ('14', "07:00"), ('15', "07:30"), ('16', "08:00"), ('17', "08:30"), ('18', "09:00"), ('19', "09:30"),
         ('20', "10:00"), ('21', "10:30"), ('22', "11:00"), ('23', "11:30"), ('24', "12:00"), ('25', "12:30"), ('26', "13:00"), ('27', "13:30"), ('28', "14:00"), ('29', "14:30"), ('30', "15:00"), ('31', "15:30"), ('32', "16:00"), ('32', "16:30"), ('34', "17:00"), ('35', "17:30"), ('36', "18:00"), ('37', "18:30"), ('38', "19:00"),
         ('39', "19:30"), ('40', "20:00"), ('41', "20:30"), ('42', "21:00"), ('43', "21:30"), ('44', "22:00"), ('45', "22:30"), ('46', "23:00"), ('47', "23:30")], string="每日維護截止時間",default='38')

    maintenance_start_date = fields.Date(string="維護啟始日期")
    maintenance_end_date = fields.Date(string="維護截止日期")
    maintenance_warn = fields.Boolean(string="維護警示")
    maintenance_warn_days = fields.Integer(string="維護警示日數")
    maintenance_warn_users = fields.Many2many('hr.employee', 'neweb_contract_maintenance_warn_users_rel', string="維護警示通知人員")
    site_check = fields.Boolean(string="Site Check")
    site_check_upload = fields.Boolean(string="Site Check Uploaded")
    sla = fields.Many2one('neweb_base.sla',domain=[('disabled','=',False)] ,string="SLA Name")
    penalties = fields.Text(string="Penalties Description")

    warranty_start_date = fields.Date(string="保固開始日期")
    warranty_end_date = fields.Date(string="保固截止日期")
    warranty_warn = fields.Boolean(string="保固警示")
    warranty_warn_days = fields.Integer(string="Warranty Warn Days")
    warranty_warn_users = fields.Many2many('hr.employee','neweb_contract_warranty_warn_users_rel', string="Warranty Warn Employee")
    deployment = fields.Boolean(string="Deployment")
    project = fields.Boolean(string="Project")
    inspection_warn = fields.Boolean(string="定檢警示")
    inspection_method = fields.Selection(
        [('none', 'None'), ('monthly', 'Monthly'), ('bimonthly', 'Bimonthly'), ('quarterly', 'Quarterly'),
         ('semiannually', 'Semiannually'), ('annually', 'Annually'), ('remote', 'Remote')],
        string='定檢模式')
    inspection_date = fields.Text(string="定檢日期")
    cur_inspection_date = fields.Char(string="Regular Inspection Date")
    # inspection_dates = fields.One2many('neweb_contract.inspection_date', 'contract_id', string="Regular Inspection Date")
    inspection_warn_days = fields.Integer(string="定檢到期警示天數")
    inspection_warn_users = fields.Many2many('hr.employee','neweb_contract_inspection_warn_users_rel', string="定檢警示通知人員")

    tx_price = fields.Float(string="Transaction Price")

    sales_dept = fields.Many2one('hr.department', string="Sales Department")
    sales = fields.Many2one('hr.employee', string="Sales Representative")
    ae_dept = fields.Many2one('hr.department', string="Engineer Department")
    ae = fields.Many2one('hr.employee', string="Engineer")
    contract_memo = fields.Text(string='Remark')

    contact_person = fields.Many2one('res.partner', string="連絡人")
    need_recovery_rehearsal = fields.Boolean(string="需回復演練")
    recovery_rehearsal_datetime = fields.Datetime(string="回復演練時間")
    recovery_rehearsal_description = fields.Text(string="回復演練說明")
    recovery_rehearsal_status = fields.Char(string="回復演練狀況")

    value_added_service_ids = fields.Many2many('neweb_base.value_added_service', string="加值服務")
    is_locked = fields.Boolean(string="合約鎖定")

    contract_line_ids = fields.One2many('neweb_contract.contract.line', 'contract_id', string="Contract Lines")
    contract_line_ids1 = fields.One2many('neweb_contract.contract.line1', 'contract_id', string="Contract Lines1")
    # contract_line_ma_ids = fields.One2many(related='contract_line_ids', string="Contract Lines", required=True)
    num_of_contract_lines = fields.Integer(compute=_count_contract_line)
    form_url = fields.Char(compute=_get_form_url)
    # contract_line_detail = fields.Text(compute="_get_contract_line_detail")
    state = fields.Selection([
        ('contract_draft', _('Draft')),  # 合約草稿
        ('contract_approv1', _('Waiting for Officer Approval')),  # 待申請人主管簽核
        ('contract_approv2', _('Waiting for Sales Approval')),  # 待業務簽核
        ('contract_approv3', _('Waiting for Marketing Approval')),  # 待Marketing簽核
        ('contract_approv4', _('Waiting for Sales AM Approval')),  # 待業務協理簽核
        ('contract_approv5', _('Waiting for Sales VP Approval')),  # 待業務部副總簽核
        ('contract_approv6', _('Waiting for Service VP Approval')),  # 待服務部副總簽核
        ('contract_approv7', _('Waiting for GM Approval')),  # 待總經理簽核
        ('contract_approv8', _('Waiting for Contract Upload')),  # 待業助上傳合約附件
        ('contract_done', _('Done')),  # 合約完成
    ], string='Status', index=True, readonly=True, default='contract_draft', copy=False)
    ae1_name = fields.Char(string="工程師")
    ae1_dept = fields.Char(string="工程師部門")


    @api.onchange('sla')
    def _get_sla(self):
        contractid = self.env.context.get('contract_id')
        slaid = self.sla.id
        # print "%s %s" % (contractid,slaid)
        if contractid and slaid:
           self.env.cr.execute("select gen_prodsla(%s,%s)" % (contractid,slaid))


    def copy(self, default=None):
        _logger.info("call write!!")
        default = dict(default or {})
        _logger.info("default : %s" % default)
        _logger.info("self : %s" % self)
        default.update(
            name=_("%s (copy)") % (self.name or '')
        )
        rec = super(Contract, self).copy(default)
        _logger.info("rec : %s" % rec)
        for cl in self.contract_line_ids:
            _logger.info("cl: %s" % cl)
            self.env['neweb_contract.contract.line'].create({'prod': cl.prod.id, 'machine_serial_no': cl.machine_serial_no, 'contract_id': rec.id})
        return rec


    def relate_maintenance_target(self):
        context = dict(self.env.context or {})
        _logger.info("relate_maintenance_target call!!")
        view_id = self.env.ref('neweb_contract.contract_maintenance_target_popup_tree').id
        _logger.info("view id: %s" % view_id)
        # context['active_id'] = self.id
        _logger.info("ctx: %s" % context)
        # return {
        #     'name': _('Journal Items'),
        #     'view_type': 'form',
        #     'view_mode': 'tree',
        #     'res_model': 'account.move.line',
        #100 rows     'view_id': False,
        #     'type': 'ir.actions.act_window',
        #     'domain': [('statement_id', 'in', self.ids)],
        #     'context': context,
        # }
        return {
            'name': _('Select Maintenance Target'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'tree',
            'res_model': 'neweb_contract.contract.line',
            # 'view_id': view_id,
            'view_id': False,
            # 'domain': [('machine_serial_no', '!=', None)],
            'target': 'new',
            'context': context,
        }

    # @api.one
    # @api.depends('contract_line_ids')
    # def _get_contract_line_detail(self):
    # 	for rec in self:
    # 		rec.contract_line_detail = ("%s\n%s" % ('Maintenance Target (Code)', '-------------------------------------------------'))
    # 		for cl in rec.contract_line_ids:
    # 			# _logger.info("abc:%s" % cl.prod)
    # 			rec.contract_line_detail = ("%s \n%s (%s)" % ((rec.contract_line_detail or ''), cl.prod.name, cl.prod.default_code))
    # 			for prd in cl.prod.prod_ids:
    # 				rec.contract_line_detail = ("%s \n  - %s (%s) x %s" % ((rec.contract_line_detail or ''), prd.prod.name, prd.prod.default_code, prd.quantity))

    # @api.one

    # @api.one

    # @api.model
    def get_emails(self, employees):
        return ','.join(str(e.work_email) for e in employees)

    # @api.model
    def process_site_check_warn(self):
        _logger.info("process_site_check_warn")
        mail_tmp_id = self.env['mail.template'].sudo().search([('name', '=', 'Contract-Site_Check_Warn_template')])
        contracts = self.env['neweb_contract.contract'].sudo().search([('site_check', '=', True), ('site_check_upload', '=', False)])
        for contract in contracts:
            self.pool['mail.template'].sudo().send_mail(self.env.cr, self.env.uid, mail_tmp_id.id, contract.id, force_send=True, context=self.env.context)

    # @api.model
    def process_warranty_warn(self):
        _logger.info("process_warranty_warn")
        # Contract-Warranty_Warn_template
        mail_tmp_id = self.env['mail.template'].sudo().search([('name', '=', 'Contract-Warranty_Warn_template')])
        # _logger.info("mail tmp id is %s" % mail_tmp_id.id)
        now = pytz.utc.localize(datetime.datetime.now()).astimezone(pytz.timezone(self.env['res.users'].browse(self._uid).tz))
        contracts = self.env['neweb_contract.contract'].sudo().search([('warranty_warn', '=', True), ('warranty_start_date', '<=', now.strftime(DEFAULT_SERVER_DATE_FORMAT)), ('warranty_end_date', '>=', now.strftime(DEFAULT_SERVER_DATE_FORMAT))])
        for contract in contracts:
            end_date = datetime.datetime.strptime(contract.warranty_end_date, DEFAULT_SERVER_DATE_FORMAT)
            if (contract.is_sales_contract or contract.is_rental_contract) and now.strftime(DEFAULT_SERVER_DATE_FORMAT) == (end_date - datetime.timedelta(days=contract.warranty_warn_days)).strftime(DEFAULT_SERVER_DATE_FORMAT):
                self.pool['mail.template'].sudo().send_mail(self.env.cr, self.env.uid, mail_tmp_id.id, contract.id,
                                                     force_send=True, context=self.env.context)

    # @api.model
    def process_maintenance_warn(self):
        _logger.info("process_maintenance_warn")
        # Contract-Maintenance_Warn_template
        mail_tmp_id = self.env['mail.template'].sudo().search([('name', '=', 'Contract-Maintenance_Warn_template')])
        # _logger.info("mail tmp id is %s" % mail_tmp_id.id)
        now = pytz.utc.localize(datetime.datetime.now()).astimezone(pytz.timezone(self.env['res.users'].browse(self._uid).tz))
        contracts = self.env['neweb_contract.contract'].sudo().search([('maintenance_warn', '=', True), ('maintenance_start_date', '<=', now.strftime(DEFAULT_SERVER_DATE_FORMAT)), ('maintenance_end_date', '>=', now.strftime(DEFAULT_SERVER_DATE_FORMAT))])
        for contract in contracts:
            end_date = datetime.datetime.strptime(contract.maintenance_end_date, DEFAULT_SERVER_DATE_FORMAT)
            if contract.is_maintenance_contract and now.strftime(DEFAULT_SERVER_DATE_FORMAT) == (end_date - datetime.timedelta(days=contract.maintenance_warn_days)).strftime(DEFAULT_SERVER_DATE_FORMAT):
                self.pool['mail.template'].sudo().send_mail(self.env.cr, self.env.uid, mail_tmp_id.id, contract.id, force_send=True, context=self.env.context)

    # @api.model
    def process_inspection_warn(self):
        _logger.info("process_inspection_warn")
        # Contract-Inspection_Warn_template
        mail_tmp_id = self.env['mail.template'].sudo().search([('name', '=', 'Contract-Inspection_Warn_template')])
        # _logger.info("mail tmp id is %s" % mail_tmp_id)
        self.env.cr.execute("select check_inspection_warn()")
        myid = self.env.cr.fetchall()
        contracts = self.env['neweb_contract.contract'].sudo().search([('id','in',myid)])
        for contract in contracts:
            self.pool['mail.template'].sudo().send_mail(self.env.cr, self.env.uid, mail_tmp_id.id, contract.id,
                                                 force_send=True, context=self.env.context)
        # now = pytz.utc.localize(datetime.datetime.now()).astimezone(pytz.timezone(self.env['res.users'].browse(self._uid).tz))
        # contracts = self.env['neweb_contract.contract'].search([('inspection_warn', '=', True), ('maintenance_start_date', '<=', now.strftime(DEFAULT_SERVER_DATE_FORMAT)), ('maintenance_end_date', '>=', now.strftime(DEFAULT_SERVER_DATE_FORMAT))])
        # for contract in contracts:
        #     for d in contract.inspection_date.split(','):
        #         inspection_date = datetime.datetime.strptime(d, '%Y%m%d')
        #         if contract.is_maintenance_contract and now.strftime('%Y-%m-%d') == (inspection_date - datetime.timedelta(days=contract.inspection_warn_days)).strftime(DEFAULT_SERVER_DATE_FORMAT):
        #             contract.cur_inspection_date = inspection_date.strftime(DEFAULT_SERVER_DATE_FORMAT)
        #             self.pool['mail.template'].send_mail(self.env.cr, self.env.uid, mail_tmp_id.id, contract.id,
        #                                                  force_send=True, context=self.env.context)

    # @api.one
    @api.constrains('inspection_date')
    def _check_inspection_date(self):
        if self.inspection_date:
            for d in self.inspection_date.split(','):
	            # todo-neweb20161012 new feature
                # if len(d)!=8:
	             #    raise ValidationError((_("Inspection date '%s' format error!")) % d)
                try:
                    datetime.datetime.strptime(d, '%Y%m%d')
                except ValueError:
                    raise ValidationError((_("Inspection date '%s' format error!")) % d)

    # @api.one
    @api.constrains('is_warranty_contract', 'is_rental_contract', 'is_maintenance_contract', 'is_outsourcing_service')
    def _check_contract_type(self):
        if not (self.is_warranty_contract or self.is_rental_contract or self.is_maintenance_contract or self.is_outsourcing_service):
            raise ValidationError(_("Please select at least one contract type!"))

    # @api.one
    @api.constrains('warranty_start_date', 'warranty_end_date')
    def _check_warranty_date(self):
        if self.warranty_start_date and self.warranty_end_date and self.warranty_start_date > self.warranty_end_date:
            raise ValidationError(_("Warranty end day must later then warranty start day!"))

    # @api.one
    @api.constrains('maintenance_start_date', 'maintenance_end_date')
    def _check_maintenance_date(self):
        if self.maintenance_start_date and self.maintenance_end_date and self.maintenance_start_date > self.maintenance_end_date:
            raise ValidationError(_("Maintenance end day must later then maintenance start day!"))

    @api.onchange('name')
    def _name_onchange(self):
        if self.name:
            self.name = self.name.upper()

    @api.onchange('project_no')
    def _project_no_onchange(self):
        if self.project_no:
            self.project_no = self.project_no.upper()

    @api.onchange('site_check')
    def _site_check_onchange(self):
        if not self.daily_maintain_hour_start:
           self.daily_maintain_hour_start = '16'
        if not self.daily_maintain_hour_end:
           self.daily_maintain_hour_end = '34'
        if not self.weekly_maintain_day:
           self.weekly_maintain_day = '1'
        if self.site_check:
            return {'warning': {'title': 'Site Check', 'message': _('Remember to upload the document!')}}

    @api.onchange('deployment')
    def _deployment_onchange(self):
        if self.deployment:
            self.project = False

    @api.onchange('project')
    def _project_onchange(self):
        if self.project:
            self.deployment = False

    # todo-neweb20161012 new feature
    # @api.onchange('maintenance_start_date', 'maintenance_end_date')
    # def _set_default_value_on_recovery_rehearsal_datetime(self):
    #     if self.maintenance_start_date and self.maintenance_end_date:
    #         start_dt = datetime.datetime.strptime(self.maintenance_start_date, DEFAULT_SERVER_DATE_FORMAT)
    #         end_dt = datetime.datetime.strptime(self.maintenance_end_date, DEFAULT_SERVER_DATE_FORMAT)
    #         self.recovery_rehearsal_datetime = start_dt + ((end_dt - start_dt)/2)

    # @api.multi
    # def write(self, vals):
    # 	_logger.info('vals:%s' % vals)
    # 	body = compose_body(self, vals)
    # 	if body:
    # 		user = self.env['res.users'].browse(self.env.uid)
    # 		partner_ids = [user.partner_id.id]
    # 		self.message_post(body=body, partner_ids=partner_ids)
    # 	return super(Contract, self).write(vals)

    # @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        context = self._context or {}
        # _logger.info('ctx:%s' % context)
        # _logger.info('args:%s' % args)

        return super(Contract, self).search(args, offset, limit, order, count=count)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            # _logger.info('is_sales_contract: %s' % vals.get('is_sales_contract'))
            # _logger.info('is_rental_contract: %s' % vals.get('is_rental_contract'))
            # _logger.info('is_maintenance_contract: %s' % vals.get('is_maintenance_contract'))
            # _logger.info('is_outsourcing_service: %s' % vals.get('is_outsourcing_service'))
            # _logger.info('is_project: %s' % vals.get('project'))
            seq_code = ''
            curr_ymd = datetime.datetime.strftime(datetime.datetime.now(), '%y%m%d')

            if vals.get('is_warranty_contract') == True and vals.get('is_maintenance_contract') == True:
                if vals.get('project') == True:
                    seq_code = self.env['ir.sequence'].next_by_code('neweb_contract.contract.svc') or 'New'
                else:
                    seq_code = self.env['ir.sequence'].next_by_code('neweb_contract.contract.pms') or 'New'
            else:
                if vals.get('is_warranty_contract') == True:
                    if vals.get('project') == True or vals.get('deployment') == True:
                        seq_code = self.env['ir.sequence'].next_by_code('neweb_contract.contract.svc') or 'New'
                    else:
                        seq_code = self.env['ir.sequence'].next_by_code('neweb_contract.contract.pus') or 'New'
                elif vals.get('is_maintenance_contract') == True:
                    seq_code = self.env['ir.sequence'].next_by_code('neweb_contract.contract.mss') or 'New'
                elif vals.get('is_outsourcing_service') == True:
                    if vals.get('project') == True:
                        seq_code = self.env['ir.sequence'].next_by_code('neweb_contract.contract.svc') or 'New'
                    else:
                        seq_code = self.env['ir.sequence'].next_by_code('neweb_contract.contract.asg') or 'New'
                elif vals.get('is_rental_contract') == True:
                    if vals.get('project') == True:
                        seq_code = self.env['ir.sequence'].next_by_code('neweb_contract.contract.svc') or 'New'
                    else:
                        seq_code = self.env['ir.sequence'].next_by_code('neweb_contract.contract.lrs') or 'New'

            vals['name'] = seq_code[:3] + curr_ymd + seq_code[3:]
            _logger.info('contract created: %s' % vals['name'])
        return super(Contract, self).create(vals)

	# todo-neweb20161012 copy issue
    # @api.one
    # def copy(self, default=None):
    #     default = dict(default or {})
    #     default.update(name="New")
    #
    #     return super(Contract, self).copy(default=default)

    _defaults = {
        'is_locked': False
    }

        # @api.model
        # def create(self, vals):
        # 	_logger.info("call create!!")
        # 	_logger.info("VAL: %s" % vals)
        # 	obj_targets = self.env['neweb_base.maintenance_target'].search(
        # 		[('prod.id', '=', vals.get('prod')), ('machine_serial_no', '=', vals.get('machine_serial_no'))])
        # 	if len(obj_targets) < 1:
        # 		if vals.get('prod') and vals.get('machine_serial_no'):
        # 			self.env['neweb_base.maintenance_target'].create(
        # 				{'prod': vals.get('prod'), 'machine_serial_no': vals.get('machine_serial_no')})
        #
        # 	return super(ContractLine, self).create(vals)

        # @api.mulit
        # def write(self):
        # 	_logger.info("call write!!")
        # 	_logger.info("VAL: %s" % vals)
        # 	for rec in self:
        # 		# _logger.info("rec : %s, %s" % (rec.prod.id, rec.machine_serial_no))
        # 		obj_targets = self.env['neweb_base.maintenance_target'].search(
        # 			[('prod.id', '=', rec.prod.id), ('machine_serial_no', '=', rec.machine_serial_no)])
        # 		# _logger.info("obj_targets: %s" % obj_targets)
        # 		if vals.get('prod'):
        # 			for obj_target in obj_targets:
        # 				obj_target.prod = vals.get('prod')
        #
        # 		if vals.get('machine_serial_no'):
        # 			for obj_target in obj_targets:
        # 				obj_target.machine_serial_no = vals.get('machine_serial_no')
        #
        # 	return super(ContractLine, self).write(vals)

# class InspectionDate(models.Model):
# 	_name = 'neweb_contract.inspection_date'
# 	_description = "Inspection Date"
#
# 	name = fields.Date(string="Inspection Date")
# 	contract_id = fields.Many2one('neweb_contract.contract', ondelete='cascade', string="Contract")
