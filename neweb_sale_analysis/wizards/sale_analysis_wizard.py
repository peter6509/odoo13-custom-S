# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import datetime

class saleanalysiswizard(models.TransientModel):
    _name = "neweb_sale_analysis.saleanalysis_wizard"


    sale_team = fields.Many2one('crm.team',string="銷售團隊",require=True)
    sale_year = fields.Char(size=4,string="業績年度",default=lambda self:str(datetime.date.today().year),require=True)
    sale_quarter = fields.Selection([('1','Q1'),('2','Q2'),('3','Q3'),('4','Q4'),('5','ALL')],string="季度",require=True)



    def saleanalysis_run(self):
        if not self.sale_quarter:
            raise UserError("未選擇季度")
        mystartdate = self.sale_year + '-01-01'
        self.env.cr.execute("""select cleansaleteamtarget(%d,'%s')""" % (self.sale_team.id, mystartdate))
        if self.sale_quarter == '1':
            mystartdate = self.sale_year + '-01-01'
            myenddate = self.sale_year + '-03-31'
            self.env.cr.execute("""select runsaleanalysis(%d,'%s','%s','%s')""" % (
            self.sale_team.id, mystartdate, myenddate, self.sale_quarter))
            self.env.cr.execute("""select calsaleanalysis(%d,'%s','%s','%s')""" % (
            self.sale_team.id, mystartdate, myenddate, self.sale_quarter))

        if self.sale_quarter == '2':
            mystartdate = self.sale_year + '-04-01'
            myenddate = self.sale_year + '-06-30'
            self.env.cr.execute("""select runsaleanalysis(%d,'%s','%s','%s')""" % (
            self.sale_team.id, mystartdate, myenddate, self.sale_quarter))
            self.env.cr.execute("""select calsaleanalysis(%d,'%s','%s','%s')""" % (
            self.sale_team.id, mystartdate, myenddate, self.sale_quarter))
        if self.sale_quarter == '3':
            mystartdate = self.sale_year + '-07-01'
            myenddate = self.sale_year + '-09-30'
            self.env.cr.execute("""select runsaleanalysis(%d,'%s','%s','%s')""" % (
            self.sale_team.id, mystartdate, myenddate, self.sale_quarter))
            self.env.cr.execute("""select calsaleanalysis(%d,'%s','%s','%s')""" % (
            self.sale_team.id, mystartdate, myenddate, self.sale_quarter))
        if self.sale_quarter == '4':
            mystartdate = self.sale_year + '-10-01'
            myenddate = self.sale_year + '-12-31'
            self.env.cr.execute("""select runsaleanalysis(%d,'%s','%s','%s')""" % (
            self.sale_team.id, mystartdate, myenddate, self.sale_quarter))
            self.env.cr.execute("""select calsaleanalysis(%d,'%s','%s','%s')""" % (
            self.sale_team.id, mystartdate, myenddate, self.sale_quarter))
        if self.sale_quarter == '5':
            mystartdate = self.sale_year + '-01-01'
            myenddate = self.sale_year + '-03-31'
            self.env.cr.execute("""select runsaleanalysis(%d,'%s','%s','1')""" % (
                self.sale_team.id, mystartdate, myenddate))
            self.env.cr.execute("""select calsaleanalysis(%d,'%s','%s','1')""" % (
                self.sale_team.id, mystartdate, myenddate))
            mystartdate = self.sale_year + '-04-01'
            myenddate = self.sale_year + '-06-30'
            self.env.cr.execute("""select runsaleanalysis(%d,'%s','%s','2')""" % (
                self.sale_team.id, mystartdate, myenddate))
            self.env.cr.execute("""select calsaleanalysis(%d,'%s','%s','2')""" % (
                self.sale_team.id, mystartdate, myenddate))
            mystartdate = self.sale_year + '-07-01'
            myenddate = self.sale_year + '-09-30'
            self.env.cr.execute("""select runsaleanalysis(%d,'%s','%s','3')""" % (
                self.sale_team.id, mystartdate, myenddate))
            self.env.cr.execute("""select calsaleanalysis(%d,'%s','%s','3')""" % (
                self.sale_team.id, mystartdate, myenddate))
            mystartdate = self.sale_year + '-10-01'
            myenddate = self.sale_year + '-12-31'
            self.env.cr.execute("""select runsaleanalysis(%d,'%s','%s','4')""" % (
                self.sale_team.id, mystartdate, myenddate))
            self.env.cr.execute("""select calsaleanalysis(%d,'%s','%s','4')""" % (
                self.sale_team.id, mystartdate, myenddate))


        self.env.cr.execute("commit")
        myselect = self.env['neweb_sale_analysis.team_targetgp'].search([('team_id','=',self.sale_team.id),('team_target_year','=',self.sale_year)])

        return {'view_name': 'crmteamtargetgp',
                'name': ('銷售團隊業績統計'),
                'views': [[False, 'form'], [False, 'tree'], ],
                'res_model': 'neweb_sale_analysis.team_targetgp',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myselect.id,
                'target': 'main',
                'flags': {'action_buttons': False},
                'view_mode': 'form',
                'view_type': 'form'
                }

