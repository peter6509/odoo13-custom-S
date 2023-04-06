# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, fields, api, tools, _
import logging

_logger = logging.getLogger(__name__)


class ProjectPivotReport(models.Model):
    _name = 'neweb_pivot.projectpivotreport'
    _description = "Project Statistics"
    _auto = False


class ProjectPivotanalysisreport(ProjectPivotReport):
    _name = 'neweb_pivot.project_report'
    _order = "proj_dept,proj_date"


    proj_no = fields.Char(string=u"成本分析編號",readonly=True)
    proj_date = fields.Datetime(string=u"日期",readonly=True)
    proj_sale = fields.Many2one('hr.employee',string=u"業務",readonly=True)
    cus_name = fields.Many2one('res.partner',string=u"客戶",readonly=True)
    main_cus_name = fields.Many2one('res.partner',string=u"終端客戶",readonly=True)
    cate_type = fields.Many2one('neweb.buscate',string=u"行業別",readonly=True)
    prod_modeltype = fields.Char(string=u"機種/機型",readonly=True)
    # prod_set = fields.Many2one('neweb.prodset',string=u"組別",readonly=True)
    prod_set1 = fields.Char(string=u"組別", readonly=True)
    prod_serial = fields.Char(string=u"序號",readonly=True)
    # prod_brand = fields.Many2one('neweb.prodbrand',string=u"品牌",readonly=True)
    prod_brand1 = fields.Char(string=u"品牌", readonly=True)
    cost_type = fields.Many2one('neweb.costtype',string=u"成本類型",readonly=True)
    device_amount = fields.Integer(string=u"數量")
    prod_num = fields.Float(digits=(8,0),string=u"數量",readonly=True)
    prod_amount_price = fields.Float(digits=(10,0),string=u"成本金額",readonly=True)
    prod_amount_revenue = fields.Float(digits=(10,0),string=u"銷售金額",readonly=True)
    prod_amount_profit = fields.Float(digits=(9,0),string=u"毛利",readonly=True)
    proj_dept = fields.Many2one('hr.department',string=u"部門",readonly=True)
    vendor_name = fields.Char(string=u"廠商",readonly=True)


    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        # self._cr.execute("""CREATE or REPLACE VIEW %s as (
        #     SELECT proj.id as id,proj.name as proj_no,proj.create_date as proj_date,proj.proj_sale as proj_sale,proj.cus_name as cus_name,
        #            proj.main_cus_name as main_cus_name,proj.cate_type as cate_type,sitem.prod_modeltype as prod_modeltype,
        #            (select getprodset(sitem.prod_set) as prod_set1),sitem.prod_serial as prod_serial,(select getprodbrand(sitem.prod_brand) as prod_brand1),sitem.cost_type as cost_type,
        #            sitem.prod_num as prod_num,round(sitem.prod_num * sitem.prod_price) as prod_amount_price,round(sitem.prod_num * sitem.prod_revenue) as prod_amount_revenue,
        #            count(proj.id) as device_amount,round(sitem.prod_num * (sitem.prod_revenue - sitem.prod_price)) as prod_amount_profit,
        #            (select get_sale_dept(proj.proj_sale)) as proj_dept, (select get_vendor_sname(sitem.supplier)) as vendor_name
        #          from neweb_project proj
        #          LEFT JOIN neweb_projsaleitem sitem ON proj.id = sitem.saleitem_id
        #          where  sitem.prod_num > 0 and sitem.prod_set is not null and sitem.prod_brand is not null and proj.id is not null
        #         GROUP BY proj.id,proj.name,proj.create_date,proj.proj_sale,proj.cus_name,proj.main_cus_name,proj.cate_type,sitem.prod_modeltype,
        #                  sitem.prod_set,sitem.prod_serial,sitem.prod_brand,sitem.cost_type,sitem.prod_num,sitem.prod_revenue,sitem.prod_price,sitem.supplier
        # )""" % self._table)
        # self._cr.execute("""CREATE or REPLACE VIEW %s as (
        #             SELECT proj.id as id,proj.name as proj_no,proj.create_date as proj_date,proj.proj_sale as proj_sale,proj.cus_name as cus_name,
        #                    proj.main_cus_name as main_cus_name,proj.cate_type as cate_type,sitem.prod_modeltype as prod_modeltype,
        #                    (select getprodset(sitem.prod_set) as prod_set1),sitem.prod_serial as prod_serial,(select getprodbrand(sitem.prod_brand) as prod_brand1),sitem.cost_type as cost_type,
        #                    sitem.prod_num as prod_num,round(sitem.prod_num * sitem.prod_price) as prod_amount_price,round(sitem.prod_num * sitem.prod_revenue) as prod_amount_revenue,
        #                    count(proj.id) as device_amount,round(sitem.prod_num * (sitem.prod_revenue - sitem.prod_price)) as prod_amount_profit,
        #                    (select get_sale_dept(proj.proj_sale)) as proj_dept, (select get_vendor_sname(sitem.supplier)) as vendor_name
        #                  from neweb_project proj
        #                  LEFT JOIN neweb_projsaleitem sitem ON proj.id = sitem.saleitem_id
        #                  where  sitem.prod_num > 0 and proj.id is not null
        #                 GROUP BY proj.id,proj.name,proj.create_date,proj.proj_sale,proj.cus_name,proj.main_cus_name,proj.cate_type,sitem.prod_modeltype,
        #                          sitem.prod_set,sitem.prod_serial,sitem.prod_brand,sitem.cost_type,sitem.prod_num,sitem.prod_revenue,sitem.prod_price,sitem.supplier
        #         )""" % self._table)


        self._cr.execute("""drop MATERIALIZED view if exists %s""" % self._table)
        self._cr.execute("""CREATE MATERIALIZED VIEW %s as (
                            SELECT proj.id as id,proj.name as proj_no,proj.create_date as proj_date,proj.proj_sale as proj_sale,proj.cus_name as cus_name,
                                   proj.main_cus_name as main_cus_name,proj.cate_type as cate_type,sitem.prod_modeltype as prod_modeltype,
                                   (select getprodset(sitem.prod_set) as prod_set1),sitem.prod_serial as prod_serial,(select getprodbrand(sitem.prod_brand) as prod_brand1),sitem.cost_type as cost_type,
                                   sitem.prod_num as prod_num,round(sitem.prod_num * sitem.prod_price) as prod_amount_price,round(sitem.prod_num * sitem.prod_revenue) as prod_amount_revenue,
                                   count(proj.id) as device_amount,round(sitem.prod_num * (sitem.prod_revenue - sitem.prod_price)) as prod_amount_profit,
                                   (select get_sale_dept(proj.proj_sale)) as proj_dept, (select get_vendor_sname(sitem.supplier)) as vendor_name
                                 from neweb_project proj
                                 LEFT JOIN neweb_projsaleitem sitem ON proj.id = sitem.saleitem_id
                                 where  sitem.prod_num > 0 and proj.id is not null
                                GROUP BY proj.id,proj.name,proj.create_date,proj.proj_sale,proj.cus_name,proj.main_cus_name,proj.cate_type,sitem.prod_modeltype,
                                         sitem.prod_set,sitem.prod_serial,sitem.prod_brand,sitem.cost_type,sitem.prod_num,sitem.prod_revenue,sitem.prod_price,sitem.supplier
                        )""" % self._table)
        self._cr.execute("""drop index if exists proj_pivot1_idx;""")
        self._cr.execute("""create index proj_pivot1_idx on %s (proj_date)""" % self._table)
        self._cr.execute("""drop index if exists proj_pivot2_idx;""")
        self._cr.execute("""create index proj_pivot2_idx on %s (proj_no)""" % self._table)
        self._cr.execute("""drop index if exists proj_pivot3_idx;""")
        self._cr.execute("""create index proj_pivot3_idx on %s (proj_sale)""" % self._table)
        self._cr.execute("""drop index if exists proj_pivot5_idx;""")
        # self._cr.execute("""create index proj_pivot4_idx on %s (proj_brand1)""" % self._table)
        self._cr.execute("""create index proj_pivot5_idx on %s (cost_type)""" % self._table)
        self._cr.execute("""drop index if exists proj_pivot6_idx;""")
        self._cr.execute("""create index proj_pivot6_idx on %s (cate_type)""" % self._table)
        self._cr.execute("""drop index if exists proj_pivot7_idx;""")
        self._cr.execute("""create index proj_pivot7_idx on %s (cus_name)""" % self._table)


class ProjectPivotanalysisreport1(ProjectPivotReport):
    _name = 'neweb_pivot.project_report1'
    _order = "proj_dept,proj_date"

    proj_no = fields.Char(string=u"成本分析編號", readonly=True)
    proj_date = fields.Datetime(string=u"日期", readonly=True)
    proj_sale = fields.Many2one('hr.employee', string=u"業務", readonly=True)
    cus_name = fields.Many2one('res.partner', string=u"客戶", readonly=True)
    main_cus_name = fields.Many2one('res.partner', string=u"終端客戶", readonly=True)
    cate_type = fields.Many2one('neweb.buscate', string=u"行業別", readonly=True)
    cost_type = fields.Many2one('neweb.costtype', string=u"成本類型", readonly=True)
    prod_amount_price = fields.Float(digits=(10, 0), string=u"成本金額", readonly=True)
    prod_amount_revenue = fields.Float(digits=(10, 0), string=u"銷售金額", readonly=True)
    prod_amount_profit = fields.Float(digits=(9, 0), string=u"毛利", readonly=True)
    proj_dept = fields.Many2one('hr.department', string=u"部門", readonly=True)


    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        # self._cr.execute("""CREATE or REPLACE VIEW %s as (
        #         SELECT proj.id as id,proj.name as proj_no,proj.create_date as proj_date,proj.proj_sale as proj_sale,proj.cus_name as cus_name,
        #                proj.main_cus_name as main_cus_name,proj.cate_type as cate_type,panalysis.analysis_costtype as cost_type,
        #                panalysis.analysis_cost as prod_amount_price,panalysis.analysis_revenue as prod_amount_revenue,
        #                panalysis.analysis_profit as prod_amount_profit,(select get_sale_dept(proj.proj_sale)) as proj_dept
        #              from neweb_project proj
        #              LEFT JOIN neweb_projanalysis panalysis ON proj.id = panalysis.analysis_id
        #             GROUP BY proj.id,proj.name,proj.create_date,proj.proj_sale,proj.cus_name,proj.main_cus_name,proj.cate_type,
        #                      panalysis.analysis_costtype,panalysis.analysis_revenue,panalysis.analysis_cost,panalysis.analysis_profit
        #     )""" % self._table)

        self._cr.execute("""drop materialized view if exists %s""" % self._table)
        self._cr.execute("""CREATE MATERIALIZED VIEW %s as (
                        SELECT proj.id as id,proj.name as proj_no,proj.create_date as proj_date,proj.proj_sale as proj_sale,proj.cus_name as cus_name,
                               proj.main_cus_name as main_cus_name,proj.cate_type as cate_type,panalysis.analysis_costtype as cost_type,
                               panalysis.analysis_cost as prod_amount_price,panalysis.analysis_revenue as prod_amount_revenue,
                               panalysis.analysis_profit as prod_amount_profit,(select get_sale_dept(proj.proj_sale)) as proj_dept
                             from neweb_project proj
                             LEFT JOIN neweb_projanalysis panalysis ON proj.id = panalysis.analysis_id
                            GROUP BY proj.id,proj.name,proj.create_date,proj.proj_sale,proj.cus_name,proj.main_cus_name,proj.cate_type,
                                     panalysis.analysis_costtype,panalysis.analysis_revenue,panalysis.analysis_cost,panalysis.analysis_profit
                    )""" % self._table)

        self._cr.execute("""drop index if exists proj_pivot1_idx;""")
        self._cr.execute("""create index proj_pivot1_idx on %s (proj_date)""" % self._table)
        self._cr.execute("""drop index if exists proj_pivot2_idx;""")
        self._cr.execute("""create index proj_pivot2_idx on %s (proj_no)""" % self._table)
        self._cr.execute("""drop index if exists proj_pivot3_idx;""")
        self._cr.execute("""create index proj_pivot3_idx on %s (proj_sale)""" % self._table)
        # self._cr.execute("""drop index if exists proj_pivot4_idx;""")
        # self._cr.execute("""create index proj_pivot4_idx on %s (proj_brand1)""" % self._table)
        self._cr.execute("""drop index if exists proj_pivot5_idx;""")
        self._cr.execute("""create index proj_pivot5_idx on %s (cost_type)""" % self._table)
        self._cr.execute("""drop index if exists proj_pivot6_idx;""")
        self._cr.execute("""create index proj_pivot6_idx on %s (cate_type)""" % self._table)
        self._cr.execute("""drop index if exists proj_pivot7_idx;""")
        self._cr.execute("""create index proj_pivot7_idx on %s (cus_name)""" % self._table)
        self._cr.execute("""drop index if exists proj_pivot8_idx;""")
        self._cr.execute("""create index proj_pivot8_idx on %s (main_cus_name)""" % self._table)
