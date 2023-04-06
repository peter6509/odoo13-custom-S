# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
import datetime, pytz
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

_logger = logging.getLogger(__name__)


class ContractLine(models.Model):
    _name = 'neweb_contract.contract.line'
    _description = "Contract Line"
    # _sql_constraints = [('contract_machine_serial_no_uniq', 'unique(contract_id, machine_serial_no)',
    #                      'Contract + Machine Serial No must be unique!!')]
    _rec_name = 'machine_serial_no'


    sequence = fields.Integer('sequence', help="Sequence for the handle.", default=10)

    prod = fields.Many2one('product.template', string="Product")
    prod_modeltype = fields.Char(string="機種-機型/料號")
    prod_modeltype1 = fields.Many2one('neweb.sitem_modeltype1',string="機型名稱")
    machine_serial_no = fields.Char(string='Machine Serial No')
    maintain_partner = fields.Many2one('res.partner', string="Partner")

    # prod_category = fields.Char(string="Maintenance Category", compute='_get_prod_category')
    maintenance_category = fields.Char(string="Maintenance Category", related='prod.maintenance_category_id.name')

    prod_sla = fields.Many2one('neweb_base.sla', string="SLA",domain=[('disabled','=',False)])
    contract_id = fields.Many2one('neweb_contract.contract', ondelete='cascade', string="Contract")
    memo = fields.Text(string='Remark')

    special_warn = fields.Boolean(string="Special Warn")
    special_warn_date = fields.Date(string="Special Warn Date")
    special_warn_days = fields.Integer(string="Special Warn Days")
    special_warn_users = fields.Many2many('hr.employee', string="Special Warn Employee")

    related_user = fields.Many2one('res.users', related="contract_id.customer_name.related_user_id", store=False)

    is_maintenance_target = fields.Boolean(related='prod.is_maintenance_target')
    x_locked = fields.Boolean(related='contract_id.is_locked', store=True)
    contract_start_date = fields.Date(string="合約啟始日")
    contract_end_date = fields.Date(string="合約終止日")
    prod_line_os = fields.Text(string="作業系統")
    os_has_contract = fields.Boolean(string="作業系統有簽約?",default=False)
    prod_line_firmware = fields.Text(string="Firmware")
    prod_line_db = fields.Text(string="資料庫")
    db_has_contract = fields.Boolean(string="DB有簽約？",default=False)
    prod_set = fields.Many2one('neweb.prodset', string="產品組別")
    prod_brand = fields.Many2one('neweb.prodbrand',string="品牌")
    is_active = fields.Boolean()
    machine_loc = fields.Char(string="設備位址")
    rack_loc = fields.Char(string="櫃位")
    main_service_rule_newl = fields.Many2one('neweb.main_service_rule',string="維護時段")
    routine_maintenance_newl = fields.Many2one('neweb.routine_maintenance',string="定檢週期")
    account_eng = fields.Many2one('hr.employee',string="工程師")
    warranty_duedate = fields.Date(string="原廠保固到期日")
    server_name = fields.Char(string="主機名稱")
    machine_used_desc = fields.Char(string="設備用途說明")
    hd_no = fields.Char(string="硬碟料號")
    hd_num = fields.Integer(string="硬碟數量")
    cpu_no = fields.Char(string="CPU料號")
    cpu_num = fields.Integer(string="CPU數量")
    ram_no = fields.Char(string="RAM料號")
    ram_num = fields.Integer(string="RAM數量")
    expand_card_no = fields.Char(string="擴充卡料號")
    expand_card_num = fields.Integer(striong="擴充卡數量")
    power_no = fields.Char(string="電源料號")
    power_num = fields.Integer(string="電源數量")
    expand_module = fields.Char(string="擴充模組")
    machine_other = fields.Char(string="其他")


    def name_get(self):
        res = []
        for line in self:
            if line.machine_serial_no:
                dn = line.machine_serial_no.strip()
            else:
                dn = _('No SN')

            try :
               dn += ' (' + line.prod_modeltype.strip() + ') '
            except Exception as inst:
               print ("No Data Found")
                
            if line._context.get('show_detail'):
                if line.contract_id:
                    dn += '=>'
                    if line.contract_id.customer_name:
                       dn += line.contract_id.customer_name.name.strip() + ': '
                       dn += line.contract_id.name.strip()
            line.display_name = dn.strip()

            self.env.cr.execute("""select contractisactive(%d)""" % line.id)
            myres = self.env.cr.fetchone()
            if myres[0] :
                res = [(line.id, dn.strip())]
            else :
                res = [(line.id, '')]
        return res

    def _compute_related_user(self):
        if self.contract_id:
            if self.contract_id.end_customer:
                self.related_user = self.contract_id.end_customer.related_user
            if not self.related_user and self.contract_id.customer_name:
                self.related_user = self.contract_id.customer_name.related_user


    def get_emails(self, employees):
        return ','.join(str(e.work_email) for e in employees)


    def process_special_warn(self):
        _logger.info("process_special_warn")
        # Contract-Special_Warn_template
        mail_tmp_id = self.env['mail.template'].search([('name', '=', 'Contract-Special_Warn_template')])
        _logger.info("mail tmp id is %s" % mail_tmp_id.id)
        now = datetime.datetime.now()
        contract_lines = self.env['neweb_contract.contract.line'].search(
            [('special_warn', '=', True), ('special_warn_date', '>=', now.strftime(DEFAULT_SERVER_DATE_FORMAT))])
        for contract_line in contract_lines:
            end_date = datetime.datetime.strptime(contract_line.special_warn_date, DEFAULT_SERVER_DATE_FORMAT)
            if now.strftime(DEFAULT_SERVER_DATE_FORMAT) == (
                        end_date - datetime.timedelta(days=contract_line.special_warn_days)).strftime(
                DEFAULT_SERVER_DATE_FORMAT):
                self.pool['mail.template'].send_mail(self.env.cr, self.env.uid, mail_tmp_id.id, contract_line.id,
                                                     force_send=True, context=self.env.context)


    @api.onchange('machine_serial_no')
    def _machine_serial_no_onchange(self):
        if self.machine_serial_no:
            self.machine_serial_no = self.machine_serial_no.upper()



