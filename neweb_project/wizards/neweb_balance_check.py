# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebBalanceCheck(models.TransientModel):
    _name = "neweb.balance_check_wizard"

    @api.onchange('project_id')
    def _get_proj_status(self):
        mystatus = ''
        mystatus1 = ''
        self.env.cr.execute("""select get_discount_amount(%d)""" % self.project_id.id)
        mydiscountamount = self.env.cr.fetchone()[0]
        self.env.cr.execute("select updatecalcost(%d)" % self.project_id.id)
        analysis_status = self.env.cr.fetchone()[0]
        if not analysis_status:
            mystatus = "成本分析收入金額總計不合,請確認！報價單優惠總價(未税):NT$ %s" % mydiscountamount

        else:
            mystatus = 'Balance'

        # self.env.cr.execute("""select getsetupanalysistotrev(%d)""" % self.project_id.id)
        # mysetupanalysisrev = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getsetupanalysistotcost(%d)""" % self.project_id.id)
        # mysetupanalysiscost = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getmainanalysistotrev(%d)""" % self.project_id.id)
        # mymainanalysisrev = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getmainanalysistotcost(%d)""" % self.project_id.id)
        # mymainanalysiscost = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getsetupdeptrev(%d)""" % self.project_id.id)
        # mysetupdeptrev = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getsetupdeptcost(%d)""" % self.project_id.id)
        # mysetupdeptcost = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getmaindeptrev(%d)""" % self.project_id.id)
        # mymaindeptrev = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getmaindeptcost(%d)""" % self.project_id.id)
        # mymaindeptcost = self.env.cr.fetchone()[0]
        #
        # if abs(mysetupanalysisrev - mysetupdeptrev) > 10:
        #     mystatus1 = mystatus1 + '(建置)成本分析收入:%s ,(建置)歸戶收入:%s 不合！' % (mysetupanalysisrev, mysetupdeptrev)
        # elif abs(mymainanalysisrev - mymaindeptrev) > 10:
        #     mystatus1 = mystatus1 + '(維護)成本分析收入:%s ,(維護)歸戶收入:%s 不合！' % (mymainanalysisrev, mymaindeptrev)
        # # elif abs(mysetupanalysiscost - mysetupdeptcost) > 10:
        # #     mystatus = mystatus + '(建置)成本分析成本:%s ,(建置)歸戶成本:%s 不合！' % (mysetupanalysiscost, mysetupdeptcost)
        # elif abs(mymainanalysiscost - mymaindeptcost) > 10:
        #     mystatus1 = mystatus1 + '(維護)成本分析成本:%s ,(維護)歸戶成本:%s 不合！' % (mymainanalysiscost, mymaindeptcost)
        # else:
        #     mystatus1 = 'Balance'
        # if mystatus1 == 'Balance':
        #     self.env.cr.execute(
        #         """update neweb_project set proj_status='Balance',proj_write_num=0 where id=%d""" % self.project_id.id)
        #
        # else:
        #     self.env.cr.execute(
        #         """update neweb_project set proj_status='%s',proj_write_num=coalesce(proj_write_num,0)+1 where id=%d""" % (
        #             mystatus1, self.project_id.id))
        if mystatus == 'Balance':
            self.env.cr.execute("""update neweb_project set proj_status1='Balance' where id=%d""" % self.project_id.id)
        else:
            self.env.cr.execute(
                """update neweb_project set proj_status1='%s' where id=%d""" % (mystatus, self.project_id.id))
        self.env.cr.execute("""commit""")
        self.proj_status = mystatus
        # self.proj_status1 = mystatus

    @api.onchange('project_id')
    def _get_proj_status1(self):
        mystatus = ''
        mystatus1 = ''
        # self.env.cr.execute("""select get_discount_amount(%d)""" % self.project_id.id)
        # mydiscountamount = self.env.cr.fetchone()[0]
        # self.env.cr.execute("select updatecalcost(%d)" % self.project_id.id)
        # analysis_status = self.env.cr.fetchone()[0]
        # if not analysis_status:
        #     mystatus = "成本分析收入金額總計不合,請確認！報價單優惠總價(未税):NT$ %s" % mydiscountamount
        #
        # else:
        #     mystatus = 'Balance'

        self.env.cr.execute("""select getsetupanalysistotrev(%d)""" % self.project_id.id)
        mysetupanalysisrev = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getsetupanalysistotcost(%d)""" % self.project_id.id)
        mysetupanalysiscost = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getmainanalysistotrev(%d)""" % self.project_id.id)
        mymainanalysisrev = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getmainanalysistotcost(%d)""" % self.project_id.id)
        mymainanalysiscost = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getsetupdeptrev(%d)""" % self.project_id.id)
        mysetupdeptrev = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getsetupdeptcost(%d)""" % self.project_id.id)
        mysetupdeptcost = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getmaindeptrev(%d)""" % self.project_id.id)
        mymaindeptrev = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getmaindeptcost(%d)""" % self.project_id.id)
        mymaindeptcost = self.env.cr.fetchone()[0]

        if abs(mysetupanalysisrev - mysetupdeptrev) > 10:
            mystatus1 = mystatus1 + '(建置)成本分析收入:%s ,(建置)歸戶收入:%s 不合！' % (mysetupanalysisrev, mysetupdeptrev)
        elif abs(mymainanalysisrev - mymaindeptrev) > 10:
            mystatus1 = mystatus1 + '(維護)成本分析收入:%s ,(維護)歸戶收入:%s 不合！' % (mymainanalysisrev, mymaindeptrev)
        # elif abs(mysetupanalysiscost - mysetupdeptcost) > 10:
        #     mystatus = mystatus + '(建置)成本分析成本:%s ,(建置)歸戶成本:%s 不合！' % (mysetupanalysiscost, mysetupdeptcost)
        elif abs(mymainanalysiscost - mymaindeptcost) > 10:
            mystatus1 = mystatus1 + '(維護)成本分析成本:%s ,(維護)歸戶成本:%s 不合！' % (mymainanalysiscost, mymaindeptcost)
        else:
            mystatus1 = 'Balance'
        if mystatus1 == 'Balance':
            self.env.cr.execute(
                """update neweb_project set proj_status='Balance',proj_write_num=0 where id=%d""" % self.project_id.id)

        else:
            self.env.cr.execute(
                """update neweb_project set proj_status='%s',proj_write_num=coalesce(proj_write_num,0)+1 where id=%d""" % (
                    mystatus1, self.project_id.id))
        # if mystatus == 'Balance':
        #     self.env.cr.execute("""update neweb_project set proj_status1='Balance' where id=%d""" % self.project_id.id)
        # else:
        #     self.env.cr.execute(
        #         """update neweb_project set proj_status1='%s' where id=%d""" % (mystatus, self.project_id.id))
        self.env.cr.execute("""commit""")
        self.proj_status1 = mystatus1
        # self.proj_status1 = mystatus

    project_id = fields.Many2one('neweb.project',string="專案成本分析",default=lambda self:self.env.context.get('proj_op_id'))
    proj_status = fields.Char(string="收入平衡狀態", compute=_get_proj_status)
    proj_status1 = fields.Char(string="成本歸戶狀態", compute=_get_proj_status1)


    def run_balance_check(self):
        mystatus = ''
        mystatus1 = ''
        self.env.cr.execute("""select get_discount_amount(%d)""" % self.project_id.id)
        mydiscountamount = self.env.cr.fetchone()[0]
        self.env.cr.execute("select updatecalcost(%d)" % self.project_id.id)
        analysis_status = self.env.cr.fetchone()[0]
        if not analysis_status:
            mystatus = "成本分析收入金額總計不合,請確認！報價單優惠總價(未税):NT$ %s" % mydiscountamount

        else:
            mystatus = 'Balance'

        self.env.cr.execute("""select getsetupanalysistotrev(%d)""" % self.project_id.id)
        mysetupanalysisrev = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getsetupanalysistotcost(%d)""" % self.project_id.id)
        mysetupanalysiscost = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getmainanalysistotrev(%d)""" % self.project_id.id)
        mymainanalysisrev = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getmainanalysistotcost(%d)""" % self.project_id.id)
        mymainanalysiscost = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getsetupdeptrev(%d)""" % self.project_id.id)
        mysetupdeptrev = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getsetupdeptcost(%d)""" % self.project_id.id)
        mysetupdeptcost = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getmaindeptrev(%d)""" % self.project_id.id)
        mymaindeptrev = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getmaindeptcost(%d)""" % self.project_id.id)
        mymaindeptcost = self.env.cr.fetchone()[0]

        if abs(mysetupanalysisrev - mysetupdeptrev) > 10:
            mystatus1 = mystatus1 + '(建置)成本分析收入:%s ,(建置)歸戶收入:%s 不合！' % (mysetupanalysisrev, mysetupdeptrev)
        elif abs(mymainanalysisrev - mymaindeptrev) > 10:
            mystatus1 = mystatus1 + '(維護)成本分析收入:%s ,(維護)歸戶收入:%s 不合！' % (mymainanalysisrev, mymaindeptrev)
        # elif abs(mysetupanalysiscost - mysetupdeptcost) > 10:
        #     mystatus = mystatus + '(建置)成本分析成本:%s ,(建置)歸戶成本:%s 不合！' % (mysetupanalysiscost, mysetupdeptcost)
        elif abs(mymainanalysiscost - mymaindeptcost) > 10:
            mystatus1 = mystatus1 + '(維護)成本分析成本:%s ,(維護)歸戶成本:%s 不合！' % (mymainanalysiscost, mymaindeptcost)
        else:
            mystatus1 = 'Balance'
        if mystatus1 == 'Balance':
            self.env.cr.execute("""update neweb_project set proj_status='Balance',proj_write_num=0 where id=%d""" % self.project_id.id)

        else:
            self.env.cr.execute("""update neweb_project set proj_status='%s',proj_write_num=coalesce(proj_write_num,0)+1 where id=%d""" % (
                mystatus1, self.project_id.id))
        if mystatus == 'Balance':
            self.env.cr.execute("""update neweb_project set proj_status1='Balance' where id=%d""" % self.project_id.id)
        else:
            self.env.cr.execute("""update neweb_project set proj_status1='%s' where id=%d""" % (mystatus, self.project_id.id))
        self.env.cr.execute("""commit""")
        self.proj_status = mystatus1
        self.proj_status1 = mystatus
