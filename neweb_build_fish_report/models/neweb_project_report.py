# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request

class newebprojectreport(models.Model):
    _inherit = "neweb.project"

    @api.depends('setupcost_ids')
    def _have_setupcost(self):
        nnum = 0
        havesetupcost=False
        for rec in self.setupcost_ids:
            nnum = nnum + 1
        if nnum > 0 :
           havesetupcost=True
        self.have_setupcost = havesetupcost
        return havesetupcost

    @api.depends('maincost_ids')
    def _have_maincost(self):
        nnum = 0
        havemaincost = False
        for rec in self.maincost_ids:
            nnum = nnum + 1
        if nnum > 0:
            havemaincost = True
        self.have_maincost = havemaincost
        return havemaincost

    @api.depends('create_date')
    def _get_createdate(self):
        for rec in self:
            self.env.cr.execute("""select create_date::DATE from neweb_project where id=%d""" % rec.id)
            rec.proj_cdate = self.env.cr.fetchone()[0]



    have_setupcost = fields.Boolean(string="setupcost",compute=_have_setupcost)
    have_maincost = fields.Boolean(string="maincost",compute=_have_maincost)
    proj_cdate = fields.Date(string="BF Date",compute=_get_createdate)

    @api.depends('total_analysis_revenue')
    def _get_analysis_revint(self):
        for rec in self:
            rec.total_analysis_revenue_int = round(rec.total_analysis_revenue,0)

    @api.depends('total_analysis_cost')
    def _get_analysis_costint(self):
        for rec in self:
            rec.total_analysis_cost_int = round(rec.total_analysis_cost, 0)

    @api.depends('total_analysis_profit')
    def _get_analysis_profint(self):
        for rec in self:
            rec.total_analysis_profit_int = round(rec.total_analysis_profit, 0)

    #  成本分析印表不要小數點
    total_analysis_revenue_int = fields.Float(digits=(10,0),string="總收入BF",compute=_get_analysis_revint)
    total_analysis_cost_int = fields.Float(digits=(10,0),string="總成本BF",compute=_get_analysis_costint)
    total_analysis_profit_int = fields.Float(digits=(10,0),string="總毛利BF",compute=_get_analysis_profint)

    # 採購明細行 總計

    @api.depends('total_saleitem')
    def _get_totsaleitemint(self):
        for rec in self:
            rec.total_saleitem_int = round(rec.total_saleitem, 0)

    @api.depends('total_saleitem_tax')
    def _get_totsaleitemtaxint(self):
        for rec in self:
            rec.total_saleitem_tax_int = round(rec.total_saleitem_tax, 0)

    @api.depends('total_saleitem_amount')
    def _get_totsaleitemamountint(self):
        for rec in self:
            rec.total_saleitem_amount_int = round(rec.total_saleitem_amount, 0)

    total_saleitem_int = fields.Float(digits=(10,0),string="未稅合計BF",compute=_get_totsaleitemint)
    total_saleitem_tax_int = fields.Float(digits=(9,0),string="稅金BF",compute=_get_totsaleitemtaxint)
    total_saleitem_amount_int = fields.Float(digits=(10,0),string="含稅總計BF",compute=_get_totsaleitemamountint)



    def action_print_neweb_project(self):
        self.ensure_one()
        if self.proj_status != 'Balance' or self.proj_status1 !='Balance':
            raise UserError("成本分析狀態不平,無法列印成本分析報表")
        # base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_project_report/%s" % (bf_url, self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }

class newebprojsaleiteminherit(models.Model):
    _inherit = "neweb.projsaleitem"

    @api.depends('prod_revenue','prod_num')
    def _get_revenuetot(self):
        myrevtot = 0
        for rec in self:
            myrevtot = round(rec.prod_revenue * rec.prod_num)
            rec.prod_revenuetot = myrevtot
            return myrevtot

    @api.depends('prod_revenuetot')
    def _get_revenuetotint(self):
        for rec in self:
            rec.prod_revenuetot_int = round(rec.prod_revenuetot,0)

    @api.depends('prod_price')
    def _get_prodpriceint(self):
        for rec in self:
            rec.prod_price_int = round(rec.prod_price, 0)

    @api.depends('prod_subtot')
    def _get_prodsubtotint(self):
        for rec in self:
            rec.prod_subtot_int = round(rec.prod_subtot, 0)

    # @api.depends('total_saleitem')
    # def _get_totsaleitemint(self):
    #     for rec in self:
    #         rec.total_saleitem_int = round(rec.total_saleitem, 0)
    #
    # @api.depends('total_saleitem_tax')
    # def _get_totsaleitemtaxint(self):
    #     for rec in self:
    #         rec.total_saleitem_tax_int = round(rec.total_saleitem_tax, 0)
    #
    # @api.depends('total_saleitem_amount')
    # def _get_totsaleitemamountint(self):
    #     for rec in self:
    #         rec.total_saleitem_amount_int = round(rec.total_saleitem_amount, 0)

    prod_revenuetot = fields.Float(digits=(13, 0), string="銷價小計", compute=_get_revenuetot)
    prod_revenuetot_int = fields.Float(digits=(10,0),string="銷價小計BF",compute=_get_revenuetotint)
    prod_price_int = fields.Float(digits=(10,0),string="成本單價BF",compute=_get_prodpriceint)
    prod_subtot_int = fields.Float(digits=(10,0),string="成本小計BF",compute=_get_prodsubtotint)
    # total_saleitem_int = fields.Integer(string="未稅合計BF",compute=_get_totsaleitemint)
    # total_saleitem_tax_int = fields.Integer(string="稅金BF",compute=_get_totsaleitemtaxint)
    # total_saleitem_amount_int = fields.Integer(string="含稅總計BF",compute=_get_totsaleitemamountint)

class newebprojanalysisbf(models.Model):
    _inherit = "neweb.projanalysis"

    @api.depends('analysis_revenue')
    def _get_anarevenueint(self):
        for rec in self:
            rec.analysis_revenue_int = round(rec.analysis_revenue,0)

    @api.depends('analysis_cost')
    def _get_anacostint(self):
        for rec in self:
            rec.analysis_cost_int = round(rec.analysis_cost, 0)

    @api.depends('analysis_profit')
    def _get_anaprofitint(self):
        for rec in self:
            rec.analysis_profit_int = round(rec.analysis_profit, 0)

    analysis_revenue_int = fields.Float(digits=(10,0),string="收入BF",compute=_get_anarevenueint)
    analysis_cost_int = fields.Float(digits=(10,0),string="成本BF",compute=_get_anacostint)
    analysis_profit_int = fields.Float(digits=(10,0),string="毛利BF",compute=_get_anaprofitint)


class newebsetupcostlinebf(models.Model):
    _inherit = "neweb.setupcost_line"

    @api.depends('r6_revenue')
    def _get_r6revint(self):
        for rec in self:
            rec.r6_revenue_int = round(rec.r6_revenue,0)

    @api.depends('nt_revenue')
    def _get_ntrevint(self):
        for rec in self:
            rec.nt_revenue_int = round(rec.nt_revenue, 0)

    @api.depends('networking_revenue')
    def _get_networkingrevint(self):
        for rec in self:
            rec.networking_revenue_int = round(rec.networking_revenue, 0)

    @api.depends('pm_revenue')
    def _get_pmrevint(self):
        for rec in self:
            rec.pm_revenue_int = round(rec.pm_revenue, 0)

    @api.depends('subtot_revenue')
    def _get_subtotrevint(self):
        for rec in self:
            rec.subtot_revenue_int = round(rec.subtot_revenue,0)

    r6_revenue_int = fields.Float(digits=(10,0),string="R6 BF",compute=_get_r6revint)
    nt_revenue_int = fields.Float(digits=(10,0),string="NT BF",compute=_get_ntrevint)
    networking_revenue_int = fields.Float(digits=(10,0),string="Networking BF",compute=_get_networkingrevint)
    pm_revenue_int = fields.Float(digits=(10,0),string="PS BF",compute=_get_pmrevint)
    subtot_revenue_int = fields.Float(digits=(10,0),string="subtot BF",compute=_get_subtotrevint)


class newebmaincostlinebf(models.Model):
    _inherit = "neweb.maincost_line"

    @api.depends('r6_revenue')
    def _get_r6revint(self):
        for rec in self:
            rec.r6_revenue_int = round(rec.r6_revenue,0)

    @api.depends('nt_revenue')
    def _get_ntrevint(self):
        for rec in self:
            rec.nt_revenue_int = round(rec.nt_revenue, 0)

    @api.depends('networking_revenue')
    def _get_networkingrevint(self):
        for rec in self:
            rec.networking_revenue_int = round(rec.networking_revenue, 0)

    @api.depends('support_revenue')
    def _get_suprevint(self):
        for rec in self:
            rec.support_revenue_int = round(rec.support_revenue, 0)

    @api.depends('subtot_revenue')
    def _get_subtotrevint(self):
        for rec in self:
            rec.subtot_revenue_int = round(rec.subtot_revenue, 0)

    r6_revenue_int = fields.Float(digits=(10,0),string="R6 BF",compute=_get_r6revint)
    nt_revenue_int = fields.Float(digits=(10,0),string="NT BF",compute=_get_ntrevint)
    networking_revenue_int = fields.Float(digits=(10,0),string="Networking BF", compute=_get_networkingrevint)
    support_revenue_int = fields.Float(digits=(10,0),string="support BF",compute=_get_suprevint)
    subtot_revenue_int = fields.Float(digits=(10,0),string="subtot BF", compute=_get_subtotrevint)
