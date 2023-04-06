# -*- coding: utf-8 -*-
# Author : Peter Wu
from __future__ import division
import datetime
from collections import defaultdict
import itertools
import operator
from operator import itemgetter
from io import StringIO
import base64
import string


from odoo import models,fields,api, _
from odoo.exceptions import UserError


class crmteamtargetgp(models.Model):
    _name = "neweb_sale_analysis.team_targetgp"
    _order = "team_id"
    _description = "總銷售團隊業績統計"

    @api.depends('team_total_q1_gp', 'team_total_q2_gp', 'team_total_q3_gp', 'team_total_q4_gp')
    def _get_yeartotgp(self):
        for rec in self:
            rec.team_total_year_gp = rec.team_total_q1_gp + rec.team_total_q2_gp + rec.team_total_q3_gp + rec.team_total_q4_gp

    @api.depends('team_total_q1_magp', 'team_total_q1_magp1', 'team_total_q1_sigp')
    def _get_q1tot(self):
        for rec in self:
            rec.team_total_q1_gp = rec.team_total_q1_magp + rec.team_total_q1_magp1 + rec.team_total_q1_sigp

    @api.depends('team_total_q2_magp', 'team_total_q2_magp1', 'team_total_q2_sigp')
    def _get_q2tot(self):
        for rec in self:
            rec.team_total_q2_gp = rec.team_total_q2_magp + rec.team_total_q2_magp1 + rec.team_total_q2_sigp

    @api.depends('team_total_q3_magp', 'team_total_q3_magp1', 'team_total_q3_sigp')
    def _get_q3tot(self):
        for rec in self:
            rec.team_total_q3_gp = rec.team_total_q3_magp + rec.team_total_q3_magp1 + rec.team_total_q3_sigp

    @api.depends('team_total_q4_magp', 'team_total_q4_magp1', 'team_total_q4_sigp')
    def _get_q4tot(self):
        for rec in self:
            rec.team_total_q4_gp = rec.team_total_q4_magp + rec.team_total_q4_magp1 + rec.team_total_q4_sigp

    @api.depends('saleq_lines_ids.sale_quarter', 'saleq_lines_ids.oldma_revenue')
    def _get_q1oldma(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q1':
                    myvalue = myvalue + line.oldma_revenue
            rec.team_total_q1_magp = myvalue

    @api.depends('saleq_lines_ids.sale_quarter', 'saleq_lines_ids.newma_revenue')
    def _get_q1newma(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q1':
                    myvalue = myvalue + line.newma_revenue
            rec.team_total_q1_magp1 = myvalue

    @api.depends('saleq_lines_ids.sale_quarter', 'saleq_lines_ids.newma_revenue1')
    def _get_q1newma1(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q1':
                    myvalue = myvalue + line.newma_revenue1
            rec.team_total_q1_magp2 = myvalue

    @api.depends('saleq_lines_ids.sale_quarter', 'saleq_lines_ids.si_revenue')
    def _get_q1si(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q1':
                    myvalue = myvalue + line.si_revenue
            rec.team_total_q1_sigp = myvalue

    ################

    @api.depends('saleq_lines_ids')
    def _get_q2oldma(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q2':
                    myvalue = myvalue + line.oldma_revenue
            rec.team_total_q2_magp = myvalue

    @api.depends('saleq_lines_ids')
    def _get_q2newma(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q2':
                    myvalue = myvalue + line.newma_revenue
            rec.team_total_q2_magp1 = myvalue

    @api.depends('saleq_lines_ids.sale_quarter', 'saleq_lines_ids.newma_revenue1')
    def _get_q2newma1(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q2':
                    myvalue = myvalue + line.newma_revenue1
            rec.team_total_q2_magp2 = myvalue

    @api.depends('saleq_lines_ids')
    def _get_q2si(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q2':
                    myvalue = myvalue + line.si_revenue
            rec.team_total_q2_sigp = myvalue

    ################
    @api.depends('saleq_lines_ids')
    def _get_q3oldma(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q3':
                    myvalue = myvalue + line.oldma_revenue
            rec.team_total_q3_magp = myvalue

    @api.depends('saleq_lines_ids')
    def _get_q3newma(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q3':
                    myvalue = myvalue + line.newma_revenue
            rec.team_total_q3_magp1 = myvalue

    @api.depends('saleq_lines_ids.sale_quarter', 'saleq_lines_ids.newma_revenue1')
    def _get_q3newma1(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q3':
                    myvalue = myvalue + line.newma_revenue1
            rec.team_total_q3_magp2 = myvalue

    @api.depends('saleq_lines_ids')
    def _get_q3si(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q3':
                    myvalue = myvalue + line.si_revenue
            rec.team_total_q3_sigp = myvalue

    ####################
    @api.depends('saleq_lines_ids')
    def _get_q4oldma(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q4':
                    myvalue = myvalue + line.oldma_revenue
            rec.team_total_q4_magp = myvalue

    @api.depends('saleq_lines_ids')
    def _get_q4newma(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q4':
                    myvalue = myvalue + line.newma_revenue
            rec.team_total_q4_magp1 = myvalue

    @api.depends('saleq_lines_ids.sale_quarter', 'saleq_lines_ids.newma_revenue1')
    def _get_q4newma1(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q4':
                    myvalue = myvalue + line.newma_revenue1
            rec.team_total_q4_magp2 = myvalue

    @api.depends('saleq_lines_ids')
    def _get_q4si(self):
        for rec in self:
            myvalue = 0
            for line in rec.saleq_lines_ids:
                if line.sale_quarter == 'Q4':
                    myvalue = myvalue + line.si_revenue
            rec.team_total_q4_sigp = myvalue

    @api.depends('team_target_q1_gp', 'team_target_q2_gp', 'team_target_q3_gp', 'team_target_q4_gp')
    def _get_gp(self):
        for rec in self:
            rec.team_target_year_gp = rec.team_target_q1_gp + rec.team_target_q2_gp + rec.team_target_q3_gp + \
                                      rec.team_target_q4_gp

    @api.depends('team_target_q1_magp', 'team_target_q1_sigp')
    def _get_q1gp(self):
        for rec in self:
            rec.team_target_q1_gp = rec.team_target_q1_magp + rec.team_target_q1_sigp

    @api.depends('team_target_q2_magp', 'team_target_q2_sigp')
    def _get_q2gp(self):
        for rec in self:
            rec.team_target_q2_gp = rec.team_target_q2_magp + rec.team_target_q2_sigp

    @api.depends('team_target_q3_magp', 'team_target_q3_sigp')
    def _get_q3gp(self):
        for rec in self:
            rec.team_target_q3_gp = rec.team_target_q3_magp + rec.team_target_q3_sigp

    @api.depends('team_target_q4_magp', 'team_target_q4_sigp')
    def _get_q4gp(self):
        for rec in self:
            rec.team_target_q4_gp = rec.team_target_q4_magp + rec.team_target_q4_sigp

    team_id = fields.Many2one('crm.team',string="銷售團隊",required=True)
    team_lines_ids = fields.One2many('neweb_sale_analysis.teammember_targetgp','team_line_id',required=True,copy=True)
    team_lines1_ids = fields.One2many('neweb_sale_analysis.teammember_utargetgp', 'team_line_id', required=True,copy=True)
    saleq_lines_ids = fields.One2many('neweb_sale_analysis.sale_revenueq','saleq_line_id',required=True,copy=True)
    salem_lines_ids = fields.One2many('neweb_sale_analysis.sale_revenuem', 'salem_line_id', required=True, copy=True)
    salel_lines_ids = fields.One2many('neweb_sale_analysis.sale_revenuel', 'salel_line_id', required=True, copy=True)
    team_target_year = fields.Char(size=4,string="年度",required=True)
    team_target_year_gp = fields.Float(string="年度團隊目標GP",default=0)
    team_target_q1_gp = fields.Float(string="Q1團隊目標GP",default=0)
    team_target_q1_magp = fields.Float(string="Q1團隊MA目標GP",default=0)
    team_target_q1_sigp = fields.Float(string="Q1團隊SI目標GP", default=0)
    team_target_q2_gp = fields.Float(string="Q2團隊目標GP",default=0)
    team_target_q2_magp = fields.Float(string="Q2團隊MA目標GP", default=0)
    team_target_q2_sigp = fields.Float(string="Q2團隊SI目標GP", default=0)
    team_target_q3_gp = fields.Float(string="Q3團隊目標GP",default=0)
    team_target_q3_magp = fields.Float(string="Q3團隊MA目標GP", default=0)
    team_target_q3_sigp = fields.Float(string="Q3團隊SI目標GP", default=0)
    team_target_q4_gp = fields.Float(string="Q4團隊目標GP",default=0)
    team_target_q4_magp = fields.Float(string="Q4團隊MA目標GP", default=0)
    team_target_q4_sigp = fields.Float(string="Q4團隊SI目標GP", default=0)
    team_total_year_gp = fields.Float(string="年度團隊實際GP",default=0,compute=_get_yeartotgp)
    team_total_q1_gp = fields.Float(string="Q1團隊實際GP",default=0,compute=_get_q1tot)
    team_total_q1_magp = fields.Float(string="Q1實際 OLD_MA GP",default=0,compute=_get_q1oldma)
    team_total_q1_magp1 = fields.Float(string="Q1實際 NEW_MA GP", default=0,compute=_get_q1newma)
    team_total_q1_magp2 = fields.Float(string="Q1實際 NEW_MA認列", default=0,compute=_get_q1newma1)
    team_total_q1_sigp = fields.Float(string="Q1實際 SI GP", default=0,compute=_get_q1si)
    team_total_q2_gp = fields.Float(string="Q2團隊實際GP",default=0,compute=_get_q2tot)
    team_total_q2_magp = fields.Float(string="Q2實際 OLD_MA GP", default=0,compute=_get_q2oldma)
    team_total_q2_magp1 = fields.Float(string="Q2實際 NEW_MA GP", default=0,compute=_get_q2newma)
    team_total_q2_magp2 = fields.Float(string="Q2實際 NEW_MA認列", default=0,compute=_get_q2newma1)
    team_total_q2_sigp = fields.Float(string="Q2實際 SI GP", default=0,compute=_get_q2si)
    team_total_q3_gp = fields.Float(string="Q3團隊實際GP",default=0,compute=_get_q3tot)
    team_total_q3_magp = fields.Float(string="Q3實際 OLD_MA GP", default=0,compute=_get_q3oldma)
    team_total_q3_magp1 = fields.Float(string="Q3實際 NEW_MA GP", default=0,compute=_get_q3newma)
    team_total_q3_magp2 = fields.Float(string="Q3實際 NEW_MA認列", default=0,compute=_get_q3newma1)
    team_total_q3_sigp = fields.Float(string="Q3實際 SI GP", default=0,compute=_get_q3si)
    team_total_q4_gp = fields.Float(string="Q4團隊實際GP",default=0,compute=_get_q4tot)
    team_total_q4_magp = fields.Float(string="Q4實際 OLD_MA GP", default=0,compute=_get_q4oldma)
    team_total_q4_magp1 = fields.Float(string="Q4實際 NEW_MA GP", default=0,compute=_get_q4newma)
    team_total_q4_magp2 = fields.Float(string="Q4實際 NEW_MA認列", default=0,compute=_get_q4newma1)
    team_total_q4_sigp = fields.Float(string="Q4實際 SI GP", default=0,compute=_get_q4si)
    is_generation = fields.Boolean(string="是否已展開", default=False)


    def name_get(self):
        result = []
        for myrec in self:
            mycrmteamname = "%s (%s)" % (myrec.team_id.name,myrec.team_target_year)
            result.append((myrec.id, mycrmteamname))
        return result


    def crmteam_genline(self):
        myactiveid = self.env.context.get("teamid")
        myteamid=self.env['neweb_sale_analysis.team_targetgp'].search([('id','=',myactiveid)])
        #print "%s" % myteamid.id
        self.env.cr.execute("select crmteam_genline(%s)" % myteamid.id)
        self.env.cr.execute("commit")

    def saleanalysis_excel(self):
        mysaleanalysisid = self.env.context.get("saleanalysis_id")
        myteamtargetgprec = self.env['neweb_sale_analysis.team_targetgp'].search([('id','=',mysaleanalysisid)])
        myteammembertargetgprec = self.env['neweb_sale_analysis.teammember_targetgp'].search([('team_line_id','=',myteamtargetgprec.id)])
        mysalerevenueqrec = self.env['neweb_sale_analysis.sale_revenueq'].search([('saleq_line_id','=',myteamtargetgprec.id)])
        mysalerevenuemrec = self.env['neweb_sale_analysis.sale_revenuem'].search([('salem_line_id','=',myteamtargetgprec.id)])
        mysalerevenuelrec = self.env['neweb_sale_analysis.sale_revenuel'].search([('salel_line_id','=',myteamtargetgprec.id)])
        self.ensure_one()

        import xlwt


        borders = xlwt.Borders()  # Create Borders
        borders.left = xlwt.Borders.THIN  # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        borders.left_colour = 0x40
        borders.right_colour = 0x40
        borders.top_colour = 0x40
        borders.bottom_colour = 0x40

        center_alignment = xlwt.Alignment()  # Create Alignment
        center_alignment.horz = xlwt.Alignment.HORZ_CENTER
        center_alignment.vert = xlwt.Alignment.VERT_CENTER

        title_font = xlwt.Font()  # Create the Font
        title_font.height = 0x00C8 * 2

        title_style = xlwt.XFStyle()  # Create Style
        title_style.borders = borders  # Add Borders to Style
        title_style.alignment = center_alignment
        title_style.font = title_font

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('成本分析-業務團隊業績統計表')

        ws.write_merge(0, 2, 0, 13, "成本分析-業務團隊業績統計表", title_style)

        content_font = xlwt.Font()
        content_font.height = 0x00C8 * 1
        content_style = xlwt.XFStyle()  # Create Style

        content_style.borders = borders  # Add Borders to Style

        content_alignment = xlwt.Alignment()  # Create Alignment
        content_alignment.horz = xlwt.Alignment.HORZ_LEFT
        content_alignment.vert = xlwt.Alignment.VERT_CENTER
        content_style.alignment = content_alignment
        content_style.alignment.wrap = 1
        content_style.font = content_font

        row = 3
        ws.write(row, 0, "業務團隊目標", title_style)
        row += 1
        date = fields.Date.today()
        ws.write(row, 0, "銷售團隊：", content_style)
        ws.write(row, 1, "%s" % myteamtargetgprec.team_id.name, content_style)
        ws.write(row, 2, "年度：", content_style)
        ws.write(row, 3, "%s" % myteamtargetgprec.team_target_year, content_style)
        ws.write(row, 4, "年度團隊目標GP",content_style)
        ws.write(row, 5, "%s" % myteamtargetgprec.team_target_year_gp,content_style)
        ws.write(row, 6, "年度團隊實際GP",content_style)
        ws.write(row, 7, "%s" % myteamtargetgprec.team_total_year_gp,content_style)
        ws.row(row).height = 300
        row += 2
        ws.write(row, 0, "業務團隊個別目標", title_style)
        # teammember_targetgp
        titles1 = [
            "業務人員",
            "個人年度目標GP",
            "個人年度實際GP",
            "個人年度達成率",
            "個人Q1目標GP",
            "個人Q1實際GP",
            "個人Q1達成率",
            "個人Q2目標GP",
            "個人Q2實際GP",
            "個人Q2達成率",
            "個人Q3目標GP",
            "個人Q3實際GP",
            "個人Q3達成率",
            "個人Q4目標GP",
            "個人Q4實際GP",
            "個人Q4達成率"
        ]

        row += 1
        col = 0
        # if myrange
        for title in titles1:
            ws.write(row, col, title, content_style)
            col += 1

        ws.row(row).height = 500
        ws.col(0).width = 7200
        ws.col(1).width = 7200
        ws.col(2).width = 3600
        ws.col(3).width = 7200
        ws.col(4).width = 3600
        ws.col(5).width = 3600
        ws.col(6).width = 3600
        ws.col(7).width = 3600
        ws.col(8).width = 3600
        ws.col(9).width = 3600
        ws.col(10).width = 3600
        ws.col(11).width = 3600
        ws.col(12).width = 3600
        ws.col(13).width = 3600
        ws.col(14).width = 3600
        ws.col(15).width = 3600
        ws.col(16).width = 3600
        row += 1

        for line in myteammembertargetgprec:
            ws.write(row, 0, line.salesempid.resource_id.name, content_style)
            ws.write(row, 1, line.teammember_target_year_gp, content_style)
            ws.write(row, 2, line.teammember_total_year_gp, content_style)
            if line.teammember_target_year_gp==0:
               mygprate=0
            else:
               mygprate = (line.teammember_total_year_gp/line.teammember_target_year_gp)*100
            ws.write(row, 3, mygprate, content_style)
            ws.write(row, 4, line.teammember_target_q1_gp, content_style)
            ws.write(row, 5, line.teammember_total_q1_gp, content_style)
            if line.teammember_target_q1_gp==0:
               myq1gprate=0
            else:
               myq1gprate = (line.teammember_total_q1_gp/line.teammember_target_q1_gp)*100
            ws.write(row, 6, myq1gprate, content_style)
            ws.write(row, 7, line.teammember_target_q2_gp, content_style)
            ws.write(row, 8, line.teammember_total_q2_gp, content_style)
            if line.teammember_target_q2_gp==0:
               myq2gprate=0
            else:
               myq2gprate = (line.teammember_total_q2_gp / line.teammember_target_q2_gp) * 100
            ws.write(row, 9, myq2gprate, content_style)
            ws.write(row, 10, line.teammember_target_q3_gp, content_style)
            ws.write(row, 11, line.teammember_total_q3_gp, content_style)
            if line.teammember_target_q3_gp == 0:
                myq3gprate = 0
            else:
                myq3gprate = (line.teammember_total_q3_gp / line.teammember_target_q3_gp) * 100
            ws.write(row, 12, myq3gprate, content_style)
            ws.write(row, 13, line.teammember_target_q4_gp, content_style)
            ws.write(row, 14, line.teammember_total_q4_gp, content_style)
            if line.teammember_target_q4_gp == 0:
                myq4gprate = 0
            else:
                myq4gprate = (line.teammember_total_q4_gp / line.teammember_target_q4_gp) * 100
            ws.write(row, 15, myq4gprate, content_style)
            row += 1
        row += 2
        ws.write(row, 0, "業務(季)業績表", title_style)
        # sale_revenueq
        titles2 = [
            "業務人員",
            "季度",
            "SI收入",
            "SI毛利",
            "SI毛利率",
            "Service",
            "Service毛利",
            "Service毛利率",
            "MA舊約收入",
            "MA舊約成本",
            "MA舊約毛利",
            "MA新約收入",
            "MA新約成本",
            "MA新約毛利",
        ]
        row += 1
        col = 0
        # if myrange
        for title in titles2:
            ws.write(row, col, title, content_style)
            col += 1
        row += 1
        for line in mysalerevenueqrec:
            ws.write(row, 0, line.salesempid.resource_id.name, content_style)
            ws.write(row, 1, line.sale_quarter, content_style)
            ws.write(row, 2, line.si_revenue, content_style)
            ws.write(row, 3, line.si_profit, content_style)
            ws.write(row, 4, line.si_profitrate, content_style)
            ws.write(row, 5, line.service_revenue, content_style)
            ws.write(row, 6, line.service_profit, content_style)
            ws.write(row, 7, line.service_profitrate, content_style)
            ws.write(row, 8, line.oldma_revenue, content_style)
            ws.write(row, 9, line.oldma_cost, content_style)
            ws.write(row, 10, line.oldma_profit, content_style)
            ws.write(row, 11, line.newma_revenue, content_style)
            ws.write(row, 12, line.newma_cost, content_style)
            ws.write(row, 13, line.newma_profit, content_style)
            row += 1

        row += 2
        ws.write(row, 0, "業務(月)業績表", title_style)
        # sale_revenueq
        titles3 = [
            "業務人員",
            "月份",
            "SI收入",
            "SI毛利",
            "SI毛利率",
            "Service",
            "Service毛利",
            "Service毛利率",
            "MA舊約收入",
            "MA舊約成本",
            "MA舊約毛利",
            "MA新約收入",
            "MA新約成本",
            "MA新約毛利",
        ]
        row += 1
        col = 0
        # if myrange
        for title in titles3:
            ws.write(row, col, title, content_style)
            col += 1
        row += 1
        for line in mysalerevenuemrec:
            ws.write(row, 0, line.salesempid.resource_id.name, content_style)
            ws.write(row, 1, line.sale_month, content_style)
            ws.write(row, 2, line.si_revenue, content_style)
            ws.write(row, 3, line.si_profit, content_style)
            ws.write(row, 4, line.si_profitrate, content_style)
            ws.write(row, 5, line.service_revenue, content_style)
            ws.write(row, 6, line.service_profit, content_style)
            ws.write(row, 7, line.service_profitrate, content_style)
            ws.write(row, 8, line.oldma_revenue, content_style)
            ws.write(row, 9, line.oldma_cost, content_style)
            ws.write(row, 10, line.oldma_profit, content_style)
            ws.write(row, 11, line.newma_revenue, content_style)
            ws.write(row, 12, line.newma_cost, content_style)
            ws.write(row, 13, line.newma_profit, content_style)
            row += 1

        row += 2
        ws.write(row, 0, "業務業績明細表", title_style)
        # sale_revenueq
        titles4 = [
            "專案編號",
            "業務人員",
            "客戶名稱",
            "產品",
            "發票/簽約日",
            "SI收入",
            "SI毛利",
            "SI毛利率",
            "Service",
            "Service毛利",
            "Service毛利率",
            "MA舊約收入",
            "MA舊約成本",
            "MA舊約毛利",
            "MA新約收入",
            "MA新約成本",
            "MA新約毛利",
        ]
        row += 1
        col = 0
        # if myrange
        for title in titles4:
            ws.write(row, col, title, content_style)
            col += 1
        row += 1
        for line in mysalerevenuelrec:
            ws.write(row, 0, line.project_no, content_style)
            ws.write(row, 1, line.salesempid.resource_id.name, content_style)
            ws.write(row, 2, line.cus_name, content_style)
            ws.write(row, 3, line.prod_name, content_style)
            ws.write(row, 4, line.invoice_date, content_style)
            ws.write(row, 5, line.si_revenue, content_style)
            ws.write(row, 6, line.si_profit, content_style)
            ws.write(row, 7, line.si_profitrate, content_style)
            ws.write(row, 8, line.service_revenue, content_style)
            ws.write(row, 9, line.service_profit, content_style)
            ws.write(row, 10, line.service_profitrate, content_style)
            ws.write(row, 11, line.oldma_revenue, content_style)
            ws.write(row, 12, line.oldma_cost, content_style)
            ws.write(row, 13, line.oldma_profit, content_style)
            ws.write(row, 14, line.newma_revenue, content_style)
            ws.write(row, 15, line.newma_cost, content_style)
            ws.write(row, 16, line.newma_profit, content_style)
            row += 1
        output = StringIO.StringIO()
        wb.save(output)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        # self.state = '2'
        mydate = datetime.datetime.now()


        myxlsfilename = _("%s-%s成本分析業績表.xls" % (myteamtargetgprec.team_id.name, myteamtargetgprec.team_target_year))

        myrec = self.env['neweb_sale_analysis.saleanalysis_excel_download']
        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})
        myviewid = self.env.ref('neweb_sale_analysis.saleanalysis_excel_download_view_tree')

        return {
            'view_name': 'SaleAnalysis',
            'name': ('成本分析業績統計表'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_sale_analysis.saleanalysis_excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': False},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}



    @api.model
    def create(self,vals):
        myteamid = vals['team_id']
        myteamtargetyear = vals['team_target_year']
        mycount = self.env['neweb_sale_analysis.team_targetgp'].search_count([('team_id','=',myteamid),('team_target_year','=',myteamtargetyear)])
        if mycount > 0 :
           raise UserError("年度團隊業績資料重覆了,請確認...")
        res = super(crmteamtargetgp,self).create(vals)
        self.env.cr.execute("""select gentargetgp(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    # @api.multi
    def write(self, vals):
        res = super(crmteamtargetgp, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select gentargetgp(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res


class crmteammembertargetgp(models.Model):
    _name = "neweb_sale_analysis.teammember_targetgp"
    _order = "sales_id"
    _description = '銷售團隊個人業績目標'

    team_line_id = fields.Many2one('neweb_sale_analysis.team_targetgp',ondelete='cascade')
    sales_id = fields.Many2one('res.users',string="業務人員")
    salesempid = fields.Many2one('hr.employee',string="員工")
    # teammember_target_year_gp = fields.Float(digits=(10,0),string="年度個人目標GP",default=0)
    # teammember_target_q1_gp = fields.Float(digits=(10,0),string="Q1個人目標GP",default=0)
    # teammember_target_q1_magp = fields.Float(digits=(10,0),string="Q1個人MA GP",default=0)
    # teammember_target_q1_sigp = fields.Float(digits=(10, 0), string="Q1個人SI GP", default=0)
    # teammember_target_q2_gp = fields.Float(digits=(10,0),string="Q2個人目標GP",default=0)
    # teammember_target_q2_magp = fields.Float(digits=(10, 0), string="Q2個人MA GP", default=0)
    # teammember_target_q2_sigp = fields.Float(digits=(10, 0), string="Q2個人SI GP", default=0)
    # teammember_target_q3_gp = fields.Float(digits=(10,0),string="Q3個人目標GP",default=0)
    # teammember_target_q3_magp = fields.Float(digits=(10, 0), string="Q3 個人MA GP", default=0)
    # teammember_target_q3_sigp = fields.Float(digits=(10, 0), string="Q3 個人SI GP", default=0)
    # teammember_target_q4_gp = fields.Float(digits=(10,0),string="Q4個人目標GP",default=0)
    # teammember_target_q4_magp = fields.Float(digits=(10, 0), string="Q4 個人MA GP", default=0)
    # teammember_target_q4_sigp = fields.Float(digits=(10, 0), string="Q4 個人SI GP", default=0)
    teammember_total_year_gp = fields.Float(digits=(10,0),string="年度個人實際GP",default=0)
    teammember_total_q1_gp = fields.Float(digits=(10,0),string="Q1個人實際GP",default=0)
    teammember_total_q1_magp = fields.Float(digits=(10, 0), string="Q1 實際MA GP", default=0)
    teammember_total_q1_sigp = fields.Float(digits=(10, 0), string="Q1 實際SI GP", default=0)
    teammember_total_q2_gp = fields.Float(digits=(10,0),string="Q2個人實際GP",default=0)
    teammember_total_q2_magp = fields.Float(digits=(10, 0), string="Q2 實際MA GP", default=0)
    teammember_total_q2_sigp = fields.Float(digits=(10, 0), string="Q2 實際SI GP", default=0)
    teammember_total_q3_gp = fields.Float(digits=(10,0),string="Q3個人實際GP",default=0)
    teammember_total_q3_magp = fields.Float(digits=(10, 0), string="Q3 實際MA GP", default=0)
    teammember_total_q3_sigp = fields.Float(digits=(10, 0), string="Q3 實際SI GP", default=0)
    teammember_total_q4_gp = fields.Float(digits=(10,0),string="Q4個人實際GP",default=0)
    teammember_total_q4_magp = fields.Float(digits=(10, 0), string="Q4 實際MA GP", default=0)
    teammember_total_q4_sigp = fields.Float(digits=(10, 0), string="Q4 實際SI GP", default=0)


class crmteammembertargetgp(models.Model):
    _name = "neweb_sale_analysis.teammember_utargetgp"
    _order = "sales_id"
    _description = '銷售團隊個人業績目標'

    team_line_id = fields.Many2one('neweb_sale_analysis.team_targetgp',ondelete='cascade')
    sales_id = fields.Many2one('res.users',string="業務人員")
    salesempid = fields.Many2one('hr.employee',string="員工")
    teammember_target_year_gp = fields.Float(digits=(10,0),string="年度個人目標GP",default=0)
    teammember_target_q1_gp = fields.Float(digits=(10,0),string="Q1個人目標GP",default=0)
    teammember_target_q1_magp = fields.Float(digits=(10,0),string="Q1個人MA GP",default=0)
    teammember_target_q1_sigp = fields.Float(digits=(10, 0), string="Q1個人SI GP", default=0)
    teammember_target_q2_gp = fields.Float(digits=(10,0),string="Q2個人目標GP",default=0)
    teammember_target_q2_magp = fields.Float(digits=(10, 0), string="Q2個人MA GP", default=0)
    teammember_target_q2_sigp = fields.Float(digits=(10, 0), string="Q2個人SI GP", default=0)
    teammember_target_q3_gp = fields.Float(digits=(10,0),string="Q3個人目標GP",default=0)
    teammember_target_q3_magp = fields.Float(digits=(10, 0), string="Q3 個人MA GP", default=0)
    teammember_target_q3_sigp = fields.Float(digits=(10, 0), string="Q3 個人SI GP", default=0)
    teammember_target_q4_gp = fields.Float(digits=(10,0),string="Q4個人目標GP",default=0)
    teammember_target_q4_magp = fields.Float(digits=(10, 0), string="Q4 個人MA GP", default=0)
    teammember_target_q4_sigp = fields.Float(digits=(10, 0), string="Q4 個人SI GP", default=0)



class salememberrevenueq(models.Model):
    _name = "neweb_sale_analysis.sale_revenueq"
    _order = "sales_id,sale_quarter"
    _description = '銷售業績依季度狀況表'

    saleq_line_id = fields.Many2one('neweb_sale_analysis.team_targetgp',ondelete='cascade')
    sales_id = fields.Many2one('res.users',string="業務人員")
    salesempid = fields.Many2one('hr.employee', string="員工")
    sale_quarter = fields.Selection([('1','Q1'),('2','Q2'),('3','Q3'),('4','Q4')],string="季度")
    si_revenue = fields.Float(digits=(10,0),string="SI收入",default=0)
    si_profit = fields.Float(digits=(8,0),string="SI毛利",default=0)
    si_profitrate = fields.Float(digits=(5,2),string="SI毛利率",default=0)
    service_revenue = fields.Float(digits=(10, 0), string="Service收入",default=0)
    service_profit = fields.Float(digits=(8, 0), string="Service毛利",default=0)
    service_profitrate = fields.Float(digits=(5, 2), string="Service毛利率",default=0)
    oldma_revenue = fields.Float(digits=(10, 0), string="MA舊約收入",default=0)
    oldma_cost = fields.Float(digits=(10, 0), string="MA舊約成本",default=0)
    oldma_profit = fields.Float(digits=(8, 0), string="MA舊約毛利",default=0)
    newma_revenue = fields.Float(digits=(10, 0), string="MA新約收入",default=0)
    newma_revenue1 = fields.Float(digits=(10, 0), string="MA新約比率", default=0)
    newma_cost = fields.Float(digits=(10, 0), string="MA新約成本",default=0)
    newma_profit = fields.Float(digits=(8, 0), string="MA新約毛利",default=0)


class salememberrevenuem(models.Model):
    _name = "neweb_sale_analysis.sale_revenuem"
    _order = "sales_id,id asc"
    _description = '銷售業績依月份狀況表'

    salem_line_id = fields.Many2one('neweb_sale_analysis.team_targetgp',ondelete='cascade')
    sales_id = fields.Many2one('res.users',string="業務人員")
    salesempid = fields.Many2one('hr.employee', string="員工")
    sale_month = fields.Selection([('1','一月'),('2','二月'),('3','三月'),('4','四月'),('5','五月'),('6','六月'),('7','七月'),('8','八月'),('9','九月'),('10','十月'),('11','十一月'),('12','十二月')],string="月份")
    si_revenue = fields.Float(digits=(10,0),string="SI收入",default=0)
    si_profit = fields.Float(digits=(8,0),string="SI毛利",default=0)
    si_profitrate = fields.Float(digits=(5,2),string="SI毛利率",default=0)
    service_revenue = fields.Float(digits=(10, 0), string="Service收入",default=0)
    service_profit = fields.Float(digits=(8, 0), string="Service毛利",default=0)
    service_profitrate = fields.Float(digits=(5, 2), string="Service毛利率",default=0)
    oldma_revenue = fields.Float(digits=(10, 0), string="MA舊約收入",default=0)
    oldma_cost = fields.Float(digits=(10, 0), string="MA舊約成本",default=0)
    oldma_profit = fields.Float(digits=(8, 0), string="MA舊約毛利",default=0)
    newma_revenue = fields.Float(digits=(10, 0), string="MA新約收入",default=0)
    newma_revenue1 = fields.Float(digits=(10, 0), string="MA新約比率", default=0)
    newma_cost = fields.Float(digits=(10, 0), string="MA新約成本",default=0)
    newma_profit = fields.Float(digits=(8, 0), string="MA新約毛利",default=0)


class salememberrevenuelinel(models.Model):
    _name = "neweb_sale_analysis.sale_revenuel"
    _order = "sales_id,invoice_date"
    _description = '銷售業績明細狀況表'

    salel_line_id = fields.Many2one('neweb_sale_analysis.team_targetgp',ondelete='cascade')
    sales_id = fields.Many2one('res.users',string="業務人員")
    salesempid = fields.Many2one('hr.employee', string="員工")
    monthday = fields.Char(size=4,string="月日")
    cus_name = fields.Char(string="客戶名稱")
    prod_name = fields.Char(string="產品名稱")
    invoice_date = fields.Date(string="開立發票日")
    si_revenue = fields.Float(digits=(10, 0), string="SI收入",default=0)
    si_profit = fields.Float(digits=(8, 0), string="SI毛利",default=0)
    si_profitrate = fields.Float(digits=(5, 2), string="SI毛利率",default=0)
    service_revenue = fields.Float(digits=(10, 0), string="Service收入",default=0)
    service_profit = fields.Float(digits=(8, 0), string="Service毛利",default=0)
    service_profitrate = fields.Float(digits=(5, 2), string="Service毛利率",default=0)
    oldma_revenue = fields.Float(digits=(10, 0), string="MA舊約收入",default=0)
    oldma_cost = fields.Float(digits=(10, 0), string="MA舊約成本",default=0)
    oldma_profit = fields.Float(digits=(8, 0), string="MA舊約毛利",default=0)
    newma_revenue = fields.Float(digits=(10, 0), string="MA新約收入",default=0)
    newma_revenue1 = fields.Float(digits=(10, 0), string="MA新約比率",default=0)
    newma_cost = fields.Float(digits=(10, 0), string="MA新約成本",default=0)
    newma_profit = fields.Float(digits=(8, 0), string="MA新約毛利",default=0)
    project_no = fields.Char(size=15,string="專案編號")
    sale_memo = fields.Text(string="備註")





