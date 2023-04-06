# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _
import logging
from datetime import datetime

_logger = logging.getLogger(__name__)


class ContractReport(models.Model):
    _name = 'neweb_contract.contract.report'
    _description = "Contracts Statistics"
    _auto = False

    # date = fields.Date(readonly=True)


class ContractReportTxPrice(ContractReport):
    _name = 'neweb_contract.contract.tx_price.report'

    tx_price = fields.Float(string=u"總收入金額", readonly=True)
    date = fields.Date(readonly=True)
    contract_no = fields.Char(string=u'合約編號')
    end_customer = fields.Many2one('res.partner',string=u'終端客戶')
    month = fields.Integer(readonly=True)

    # @api.model
    def init(self):
        # _logger.info("self._table: %s" % self._table)
        # tools.drop_view_if_exists(cr, self._table)

        tools.drop_view_if_exists(self._cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                ncc.id as id,
                ncc.clinch_date as date,
                to_char(ncc.clinch_date, 'MM')::Int as month,
                npj.total_analysis_revenue as tx_price,
                ncc.end_customer as end_customer,
                ncc.name as contract_no
            FROM neweb_contract_contract ncc,neweb_project npj where 
            ncc.project_no = npj.NAME and tx_price is not NULL 
        )""" % self._table)


class ContractReportAE(ContractReport):
    _name = 'neweb_contract.contract.ae.report'

    nbr = fields.Integer(string='# of Target Device', readonly=True)
    ae = fields.Many2one('hr.employee', string="Engineer", readonly=True)
    date = fields.Date(readonly=True)
    end_customer = fields.Many2one('res.partner',string=u"終端客戶")

    # @api.model
    def init(self):
        # _logger.info("self._table: %s" % self._table)
        tools.drop_view_if_exists(self._cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                ncc.id as id,
                ncc.ae as ae,
                ncc.clinch_date as date,
                ncc.end_customer as end_customer,
                count(nccl.*) as nbr
            FROM neweb_contract_contract_line nccl
            JOIN neweb_contract_contract ncc on ncc.id = nccl.contract_id
            WHERE ncc.state = 'contract_done'
            GROUP BY ncc.id, ncc.ae, ncc.clinch_date
        )""" % self._table)


class ContractReportSLA(ContractReport):
    _name = 'neweb_contract.contract.sla.report'

    nbr = fields.Integer(string='# of Target Device', readonly=True)
    sla = fields.Many2one('neweb_base.sla', string="SLA Name", readonly=True)
    date = fields.Date(readonly=True)

    # @api.model
    def init(self):
        # _logger.info("self._table: %s" % self._table)
        tools.drop_view_if_exists(self._cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                nccl.id as id,
                nccl.prod_sla as sla,
                ncc.clinch_date as date,
                count(nccl.prod) as nbr
            FROM neweb_contract_contract_line nccl
            JOIN neweb_contract_contract ncc on ncc.id = nccl.contract_id
            WHERE ncc.state = 'contract_done'
            GROUP BY nccl.id, nccl.prod_sla, ncc.clinch_date
        )""" % self._table)


class ContractReportProductCategory(ContractReport):
    _name = 'neweb_contract.contract.product_category.report'

    nbr = fields.Integer(string='# of Target Device', readonly=True)
    prod_categ = fields.Many2one('product.category', string="Product Category", readonly=True)
    date = fields.Date(readonly=True)

    # @api.model
    def init(self):
        # _logger.info("self._table: %s" % self._table)
        tools.drop_view_if_exists(self._cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                nccl.id as id,
                pt.categ_id as prod_categ,
                ncc.clinch_date as date,
                count(nccl.prod) as nbr
            FROM neweb_contract_contract_line nccl
            JOIN neweb_contract_contract ncc on ncc.id = nccl.contract_id
            JOIN product_template pt on nccl.prod = pt.id
            LEFT JOIN product_category pc on pc.id = pt.categ_id
            WHERE ncc.state = 'contract_done'
            GROUP BY nccl.id, pt.categ_id, ncc.clinch_date
        )""" % self._table)


class ContractReportBrandCategory(ContractReport):
    _name = 'neweb_contract.contract.product_brand.report'

    nbr = fields.Integer(string='# of Target Device', readonly=True)
    prod_brand = fields.Char(string="Brand", readonly=True)
    date = fields.Date(readonly=True)

    # @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                nccl.id as id,
                pt.brand as prod_brand,
                ncc.clinch_date as date,
                count(nccl.prod) as nbr
            FROM neweb_contract_contract_line nccl
            JOIN neweb_contract_contract ncc on ncc.id = nccl.contract_id
            JOIN product_template pt on nccl.prod = pt.id
            LEFT JOIN product_category pc on pc.id = pt.categ_id
            WHERE ncc.state = 'contract_done'
            GROUP BY nccl.id, pt.brand, ncc.clinch_date
        )""" % self._table)


class ContractReportModelCategory(ContractReport):
    _name = 'neweb_contract.contract.product_model.report'

    nbr = fields.Integer(string='# of Target Device', readonly=True)
    prod_model = fields.Char(string="Model", readonly=True)
    date = fields.Date(readonly=True)

    # @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                nccl.id as id,
                pt.model as prod_model,
                ncc.clinch_date as date,
                count(nccl.prod) as nbr
            FROM neweb_contract_contract_line nccl
            JOIN neweb_contract_contract ncc on ncc.id = nccl.contract_id
            JOIN product_template pt on nccl.prod = pt.id
            LEFT JOIN product_category pc on pc.id = pt.categ_id
            WHERE ncc.state = 'contract_done'
            GROUP BY nccl.id, pt.model, ncc.clinch_date
        )""" % self._table)


class ContractReportSerialCategory(ContractReport):
    _name = 'neweb_contract.contract.product_serial.report'

    nbr = fields.Integer(string='# of Target Device', readonly=True)
    prod_serial = fields.Char(string="Serial", readonly=True)
    date = fields.Date(readonly=True)

    # @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                nccl.id as id,
                pt.serial as prod_serial,
                ncc.clinch_date as date,
                count(nccl.prod) as nbr
            FROM neweb_contract_contract_line nccl
            JOIN neweb_contract_contract ncc on ncc.id = nccl.contract_id
            JOIN product_template pt on nccl.prod = pt.id
            LEFT JOIN product_category pc on pc.id = pt.categ_id
            WHERE ncc.state = 'contract_done'
            GROUP BY nccl.id, pt.serial, ncc.clinch_date
        )""" % self._table)