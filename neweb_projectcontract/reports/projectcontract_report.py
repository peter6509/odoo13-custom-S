# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api, tools, _
import logging

_logger = logging.getLogger(__name__)


class ProjectContractReport(models.Model):
    _name = 'neweb_projectcontract.revenue_report'
    _description = "Project Revenue Statistics"
    _auto = False


class ProjectContractRevenueReport(ProjectContractReport):
    _name = 'neweb_projectcontract.revenue_analysis_report'

    sales_id = fields.Many2one('hr.employee',string="業務",readonly=True)
    contract_no = fields.Char(string="合約編號",readonly=True)
    project_no = fields.Char(string="成本分析編號",readonly=True)
    customer_no = fields.Many2one('res.partner',string="客戶名稱",readonly=True)
    main_type = fields.Many2one('neweb.routine_maintenance',string="維護方式",readonly=True)
    revenue_date = fields.Date(string="日期",readonly=True)
    revenue_amount = fields.Float(digits=(10, 1), string="收入分攤金額",readonly=True)
    # device_amount = fields.Integer(readonly=True, string="# of Device")
    # rev_sum = fields.Float(digits=(11,1),string="收入合計")

    # @api.model
    def init(self):
        # tools.drop_view_if_exists(self._cr, self._table)
        self.env.cr.execute("""drop view if exists neweb_projectcontract_revenue_analysis_report cascade""")
        self.env.cr.execute("""CREATE or REPLACE VIEW neweb_projectcontract_revenue_analysis_report as (
            SELECT
                A.sales_id as sales_id,
                concat(A.contract_no,'-',A.project_no) as contract_no,
                A.project_no as project_no,
                A.customer_name as customer_no,
                A.main_type as main_type,
                REV.revenue_date as revenue_date,
                coalesce(REV.revenue_amount,0) as revenue_amount,
                REV.id as id 
            FROM neweb_projectcontract_revenue_cost_analysis A
            LEFT JOIN neweb_projectcontract_revenue_analysis REV ON A.id = REV.revenue_id  
            where REV.revenue_amount > 0   
            GROUP BY A.sales_id,A.contract_no,A.project_no,A.customer_name,A.main_type,REV.revenue_date,REV.id
        )""" )


class ProjectContractCostReport(ProjectContractReport):
    _name = 'neweb_projectcontract.cost_analysis_report'

    sales_id = fields.Many2one('hr.employee',string="業務",readonly=True)
    contract_no = fields.Char(string="合約編號",readonly=True)
    project_no = fields.Char(string="成本分析編號",readonly=True)
    purchase_no = fields.Many2one('purchase.order',string="採購單號")
    vendor_no = fields.Many2one('res.partner',string="供應商",readonly=True)
    cost_type = fields.Many2one('neweb_purchase.costtype',string="成本類型")
    cost_date = fields.Date(string="日期",readonly=True)
    cost_amount = fields.Float(digits=(10, 1), string="成本分攤金額",readonly=True)
    # device_amount = fields.Integer(readonly=True, string="# of Device")
    # cost_sum = fields.Float(digits=(11,1),string="合計")

    # @api.model
    def init(self):
        # tools.drop_view_if_exists(self._cr, self._table)
        self.env.cr.execute("""drop view if exists neweb_projectcontract_cost_analysis_report cascade""")
        self.env.cr.execute("""CREATE or REPLACE VIEW neweb_projectcontract_cost_analysis_report as (
            SELECT
                A.sales_id as sales_id,
                concat(A.contract_no,'-',A.project_no) as contract_no,
                A.project_no as project_no,
                COST.vendor_no as vendor_no,
                COST.cost_type as cost_type,
                COST.cost_date as cost_date,
                COST.cost_amount as cost_amount,
                COST.id as id
            FROM neweb_projectcontract_revenue_cost_analysis A
            LEFT JOIN neweb_projectcontract_cost_analysis COST ON A.id = COST.cost_id  
            where COST.cost_amount > 0     
            GROUP BY A.sales_id,A.contract_no,A.project_no,COST.vendor_no,COST.cost_type,COST.cost_date,COST.id
        )""")


