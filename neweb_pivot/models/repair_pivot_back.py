# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api, tools, _
import logging

_logger = logging.getLogger(__name__)


class RepairPivotReport(models.Model):
    _name = 'neweb_pivot.repairpivotreport'
    _description = "Repair Statistics"
    _auto = False


class RepairPivotanalysisreport(RepairPivotReport):
    _name = 'neweb_pivot.repair_report'

    repair_dept = fields.Many2one('hr.department',readonly=True,string=u"維護部門")
    repair_ae = fields.Many2one('hr.employee',readonly=True,string=u"維護工程師")
    repair_customer = fields.Many2one('res.partner',readonly=True,string=u"終端客戶")
    repair_parts = fields.Many2one('product.product',readonly=True,string=u"維修料件")
    repair_modeltype = fields.Char(readonly=True,string=u"機種/機型")
    repair_serialno = fields.Char(readonly=True,string=u'序號')
    repair_type = fields.Selection([
        ('maintenance', u'維護'),
        ('warranty', u'保固'),
        ('warranty_maintenance', u'保固+維護'),
        ('per_call', u'Per Call'),
        ('outsourcing', u'維運'),
        ('others', u'其他')
    ], string=u"報修種類",readonly=True)
    repair_problem = fields.Many2one('neweb_base.problem', string="Problem Judgment",readonly=True)
    repair_datetime = fields.Datetime( string=u"報修時間",readonly=True)
    device_amount = fields.Integer(string="次數",readonly=True)
    repair_no = fields.Char(string=u"報修單號",readonly=True)


    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                (select get_repairae_dept(rep.ae_id)) as repair_dept,
                rep.repair_datetime as repair_datetime,
                rep.id as id,
                rep.ae_id as repair_ae,
                rep.end_customer as repair_customer,
                rep.repair_type as repair_type,
                rep.name as repair_no,
                count(rep.id) as device_amount,
                contl.prod_modeltype as repair_modeltype,
                contl.machine_serial_no as repair_serialno,
                replp.prod as repair_parts 
                 from neweb_repair_repair rep,neweb_repair_repair_line repl,neweb_contract_contract_line contl,neweb_repair_repair_part replp
                WHERE rep.state in ('repair_done', 'repair_closed') and rep.id = repl.repair_id and repl.contract_line = contl.id
                   and repl.id = replp.repair_line_id and rep.id is not null
                GROUP BY rep.repair_datetime,rep.id,rep.ae_id,rep.end_customer,rep.repair_type,contl.prod_modeltype,contl.machine_serial_no,replp.prod,rep.name
        )""" % self._table)





                
                



