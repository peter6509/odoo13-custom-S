# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _
import logging

_logger = logging.getLogger(__name__)


class RepairReport(models.Model):
    _name = 'neweb_repair.repair.report'
    _description = "Repair Statistics"
    _auto = False


class RepairReportMaintenanceCategory(RepairReport):
    _name = 'neweb_repair.repair.maintenance_category.report'

    repair_datetime = fields.Datetime(readonly=True, string="Repair Datetime")
    prod = fields.Many2one('product.product', readonly=True, string="Product")
    maintenance_category = fields.Many2one('neweb_base.maintenance_category', readonly=True, string="Maintenance Category")
    device_amount = fields.Integer(readonly=True, string="# of Device")

    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                rep.repair_datetime as repair_datetime,
                pr.id as id,
                pr.id as prod,
                pt.maintenance_category_id as maintenance_category,
                count(repl.id) as device_amount
            FROM neweb_repair_repair_line repl
            JOIN neweb_repair_repair rep on rep.id = repl.repair_id
            JOIN neweb_contract_contract_line contl on contl.id = repl.contract_line
            LEFT JOIN product_template pt ON pt.id = contl.prod
            LEFT JOIN product_product pr ON pt.id = pr.product_tmpl_id
            WHERE rep.state in ('repair_done', 'repair_closed')
            GROUP BY rep.repair_datetime, pr.id, pt.maintenance_category_id
        )""" % self._table)


class RepairReportProblem(RepairReport):
    _name = 'neweb_repair.repair.problem.report'

    repair_datetime = fields.Datetime(readonly=True, string="Repair Datetime")
    problem = fields.Many2one('neweb_base.problem', readonly=True, string="Problem")
    maintenance_category = fields.Many2one('neweb_base.maintenance_category', readonly=True, string="Maintenance Category")
    device_amount = fields.Integer(readonly=True, string="# of Device")

    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                rep.repair_datetime as repair_datetime,
                prob.id as id,
                prob.id as problem,
                pt.maintenance_category_id as maintenance_category,
                count(repl.id) as device_amount
            FROM neweb_repair_repair_line repl
            JOIN neweb_repair_repair rep on rep.id = repl.repair_id
            JOIN neweb_contract_contract_line contl on contl.id = repl.contract_line
            LEFT JOIN product_template pt ON pt.id = contl.prod
            LEFT JOIN product_product pr ON pt.id = pr.product_tmpl_id
            JOIN neweb_base_problem prob on prob.id = rep.problem
            WHERE rep.state in ('repair_done', 'repair_closed')
            GROUP BY rep.repair_datetime, prob.id, pt.maintenance_category_id
        )""" % self._table)


class RepairReportPart(RepairReport):
    _name = 'neweb_repair.repair.part.report'

    repair_datetime = fields.Datetime(readonly=True, string="Repair Datetime")
    part_no = fields.Char(readonly=True, string="Part No")
    maintenance_category = fields.Many2one('neweb_base.maintenance_category', readonly=True, string="Maintenance Category")
    device_amount = fields.Integer(readonly=True, string="# of Device")

    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                p.prod as id,
                rep.repair_datetime as repair_datetime,
                pt.serial_num as part_no,
                p.part_maintenance_category_id as maintenance_category,
                count(repl.id) as device_amount
            from
                neweb_repair_repair_part p
            LEFT JOIN product_product pr ON pr.id = p.prod
            LEFT JOIN product_template pt ON pr.product_tmpl_id = pt.id
            JOIN neweb_repair_repair_line repl ON repl.id = p.repair_line_id
            JOIN neweb_repair_repair rep ON rep.id = repl.repair_id
            WHERE rep.state in ('repair_done', 'repair_closed')
            GROUP BY p.prod, rep.repair_datetime, pt.serial_num,p. part_maintenance_category_id
        )""" % self._table)


class RepairReportCompleteTime(RepairReport):
    _name = 'neweb_repair.repair.complete_time.report'

    repair_datetime = fields.Datetime(readonly=True, string="Repair Datetime")
    ae = fields.Many2one('hr.employee', readonly=True, string="AE")
    avg_complete_time = fields.Integer(readonly=True, string="Avg. Complete Time(Hours)")

    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                rep.id as id,
                rep.ae_id as ae,
                rep.repair_datetime as repair_datetime,
                extract(epoch from avg(rep.ae_complete_datetime - rep.repair_datetime))/3600 as avg_complete_time
            FROM neweb_repair_repair rep
            WHERE rep.state in ('repair_done', 'repair_closed')
            GROUP BY id, ae, repair_datetime
        )""" % self._table)


class RepairReportProductBrand(RepairReport):
    _name = 'neweb_repair.repair.product_brand.report'

    repair_datetime = fields.Datetime(readonly=True, string="Repair Datetime")
    prod_brand = fields.Char(readonly=True, string="Brand")
    device_amount = fields.Integer(readonly=True, string="# of Device")

    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                rep.id as id,
                rep.repair_datetime as repair_datetime,
                pt.brand as prod_brand,
                count(repl.id) as device_amount
            FROM neweb_repair_repair_line repl
            JOIN neweb_repair_repair rep on rep.id = repl.repair_id
            JOIN neweb_contract_contract_line contl on contl.id = repl.contract_line
            LEFT JOIN product_template pt ON pt.id = contl.prod
            LEFT JOIN product_product pr ON pt.id = pr.product_tmpl_id
            WHERE rep.state in ('repair_done', 'repair_closed')
            GROUP BY rep.repair_datetime, rep.id, pt.brand
        )""" % self._table)


class RepairReportProductModel(RepairReport):
    _name = 'neweb_repair.repair.product_model.report'

    repair_datetime = fields.Datetime(readonly=True, string="Repair Datetime")
    prod_model = fields.Char(readonly=True, string="Model")
    device_amount = fields.Integer(readonly=True, string="# of Device")

    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                rep.id as id,
                rep.repair_datetime as repair_datetime,
                pt.model as prod_model,
                count(repl.id) as device_amount
            FROM neweb_repair_repair_line repl
            JOIN neweb_repair_repair rep on rep.id = repl.repair_id
            JOIN neweb_contract_contract_line contl on contl.id = repl.contract_line
            LEFT JOIN product_template pt ON pt.id = contl.prod
            LEFT JOIN product_product pr ON pt.id = pr.product_tmpl_id
            WHERE rep.state in ('repair_done', 'repair_closed')
            GROUP BY rep.repair_datetime, rep.id, pt.model
        )""" % self._table)


class RepairReportProductSerial(RepairReport):
    _name = 'neweb_repair.repair.product_serial.report'

    repair_datetime = fields.Datetime(readonly=True, string="Repair Datetime")
    prod_serial = fields.Char(readonly=True, string="Serial")
    device_amount = fields.Integer(readonly=True, string="# of Device")

    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                rep.id as id,
                rep.repair_datetime as repair_datetime,
                pt.serial as prod_serial,
                count(repl.id) as device_amount
            FROM neweb_repair_repair_line repl
            JOIN neweb_repair_repair rep on rep.id = repl.repair_id
            JOIN neweb_contract_contract_line contl on contl.id = repl.contract_line
            LEFT JOIN product_template pt ON pt.id = contl.prod
            LEFT JOIN product_product pr ON pt.id = pr.product_tmpl_id
            WHERE rep.state in ('repair_done', 'repair_closed')
            GROUP BY rep.repair_datetime, rep.id, pt.serial
        )""" % self._table)


class RepairReportProductSerialno(RepairReport):
    _name = 'neweb_repair.repair.product_serial_no.report'

    name = fields.Char(string=u"報修單號",readonly=True)
    repair_datetime = fields.Datetime(readonly=True, string=u"報修時間")
    end_customer = fields.Many2one('res.partner',string=u"終端客戶")
    ae_id = fields.Many2one('hr.employee',string=u"派工工程師")
    prod_serial_no = fields.Char(readonly=True, string=u"機器序號")
    prod_serial = fields.Char(readonly=True,string=u"機型")
    device_amount = fields.Integer(readonly=True, string="# of Device")

    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                rep.id as id,
                rep.name as name,
                rep.repair_datetime as repair_datetime,
                rep.end_customer as end_customer,
                rep.ae_id as ae_id,
                repl.machine_serial_no as prod_serial_no,
                pt.serial as prod_serial,
                count(repl.id) as device_amount
            FROM neweb_repair_repair_line repl
            JOIN neweb_repair_repair rep on rep.id = repl.repair_id
            JOIN neweb_contract_contract_line contl on contl.id = repl.contract_line
            LEFT JOIN product_template pt ON pt.id = contl.prod
            LEFT JOIN product_product pr ON pt.id = pr.product_tmpl_id
            WHERE rep.state not in ('repair_cancel')
            GROUP BY rep.repair_datetime, rep.id, pt.serial,repl.machine_serial_no,rep.ae_id
        )""" % self._table)
