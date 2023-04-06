                                                                                               # -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebprojectinherit91(models.Model):
    _inherit = "neweb.sitem_list"

    cost_dept = fields.Many2one('neweb.cost_dept',string=u"部門",domain=lambda self:[('active','=',True)])
    cost_type = fields.Many2one('neweb.costtype',string="成本類型")


class newebprojectinherit92(models.Model):
    _inherit = "neweb.projsaleitem"

    @api.depends('prod_num', 'prod_revenue')
    def _get_revenuetot(self):
        for rec in self:
            rec.prod_revenuetot = round(rec.prod_num * rec.prod_revenue)

    @api.depends('cost_dept')
    def _get_costdept(self):
        mydept = ' '
        for rec in self:
            if not rec.cost_dept:
                mydept = ' '
            else:
                mydept = rec.cost_dept.name
            rec.ccostdept = mydept
            return mydept

    @api.depends('supplier')
    def _get_supplier(self):
        mysupplier = ' '
        for rec in self:
            if not rec.supplier:
                mysupplier = ' '
            else:
                mysupplier = rec.supplier.comp_sname
            rec.csupplier = mysupplier
            return mysupplier

    @api.depends('prod_revenuetot')
    def _get_revenuetot1(self):
        for rec in self:
            mytot = round(rec.prod_revenuetot)
            rec.prod_revenuetot1 = mytot
            return mytot

    cost_dept = fields.Many2one('neweb.cost_dept',string=u"部門",domain=lambda self:[('active','=',True)])
    line_item = fields.Integer(string="項次")
    prod_revenuetot = fields.Float(digits=(10,0),string=u"銷價小計",compute=_get_revenuetot)
    prod_revenuetot1 = fields.Float(digits=(10, 0),compute=_get_revenuetot1)
    ccostdept = fields.Char(string="bf cost dept", compute=_get_costdept)
    csupplier = fields.Char(string="bf supplier", compute=_get_supplier)
    stockin_date = fields.Date(string="收貨日期")
    stockout_date = fields.Date(string="出貨日期")


class newebprojectinherit93(models.Model):
    _inherit = "neweb.project"

    @api.depends('acceptance_step', 'proj_step')
    def _get_projaccstepnew(self):
        for rec in self:
            myprojaccstep = ' '
            if (rec.acceptance_step == False or rec.acceptance_step == '') and (
                    rec.proj_step != False or rec.proj_step != ''):
                myprojaccstep = rec.proj_step
            elif (rec.acceptance_step != False or rec.acceptance_step != '') and (
                    rec.proj_step == False or rec.proj_step == ''):
                myprojaccstep = rec.acceptance_step
            if myprojaccstep == False:
                myprojaccstep = ' '
            rec.proj_acceptance_step = myprojaccstep
            return myprojaccstep

    @api.depends('main_other', 'proj_other_desc')
    def _get_mainotherdesc(self):
        for rec in self:
            mymainotherdesc = ' '
            if (rec.main_other == False or rec.main_other == '') and (
                    rec.proj_other_desc != False or rec.proj_other_desc != ''):
                mymainotherdesc = rec.proj_other_desc
            elif (rec.main_other != False or rec.main_other != '') and (
                    rec.proj_other_desc == False or rec.proj_other_desc == ''):
                mymainotherdesc = rec.main_other_desc
            if mymainotherdesc == False :
                mymainotherdesc = ' '
            rec.main_other_desc = mymainotherdesc
            return mymainotherdesc

    @api.depends('complete_days', 'proj_complete_days')
    def _get_pcompletedays(self):
        for rec in self:
            mypcompletedays = ' '
            if (rec.complete_days == False or rec.complete_days == '') and (
                    rec.proj_complete_days != False or rec.proj_complete_days != ''):
                mypcompletedays = rec.proj_complete_days
            elif (rec.complete_days != False or rec.complete_days != '') and (
                    rec.proj_complete_days == False or rec.proj_complete_days == ''):
                mypcompletedays = rec.proj_complete_days
            if mypcompletedays == False :
                mypcompletedays = ' '
            rec.pcomplete_days = mypcompletedays
            return mypcompletedays

    setupcost_ids = fields.One2many('neweb.setupcost_line','project_id',copy=False,track_visibility="onchange")
    maincost_ids = fields.One2many('neweb.maincost_line','project_id',copy=False,track_visibility="onchange")
    have_contract = fields.Selection([('Y',u'有合約'),('N',u'無合約')],string=u"有無合約？",default='N')
    proj_write_num = fields.Integer(string=u"專案變動次數",default=0)
    acceptanced_date1 = fields.Date(string="預計驗收日")
    acceptanced_date2 = fields.Date(string="實際驗收日")
    projsaleitem_status = fields.Selection([('1','貨在公司待貨齊'),('2','貨在公司待出貨'),('3','貨在公司測試安裝中'),('4','貨在客戶端待貨齊'),('5','貨在客戶端待裝機'),('6','貨在客戶端裝機中'),('7','貨在客戶端待驗收'),('8','貨在客戶端驗收中')],string="貨的狀態")
    projsaleitem_completed = fields.Boolean(string="是否已結案?",default=False)
    proj_acceptance_step = fields.Char(string="專案驗收階段",compute=_get_projaccstepnew)
    main_other_desc = fields.Text(string="專案其他說明",compute=_get_mainotherdesc)
    pcomplete_days = fields.Char(string="專案完工日數",compute=_get_pcompletedays)


    def write(self, vals):
        res = super(newebprojectinherit93, self).write(vals)
        for rec in self:
            if not rec.acceptanced_date1 and rec.proj_write_num > 0:
                raise UserError("""預計驗收日不能空白""")
            mystatus = ''
            mystatus1 = ''
            self.env.cr.execute("""select get_discount_amount(%d)""" % rec.id)
            mydiscountamount = self.env.cr.fetchone()[0]
            self.env.cr.execute("select updatecalcost(%d)" % rec.id)
            analysis_status = self.env.cr.fetchone()[0]
            if not analysis_status:
                mystatus1 = "成本分析收入金額總計不合,請確認！報價單優惠總價(未税):NT$ %s" % mydiscountamount
            else:
                mystatus1 = 'Balance'
                # raise UserError(mystatus)
            self.env.cr.execute("""select clearcostline(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select gencostdeptdata(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select getsetupanalysistotrev(%d)""" % rec.id)
            mysetupanalysisrev = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select getsetupanalysistotcost(%d)""" % rec.id)
            mysetupanalysiscost = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select getmainanalysistotrev(%d)""" % rec.id)
            mymainanalysisrev = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select getmainanalysistotcost(%d)""" % rec.id)
            mymainanalysiscost = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select getsetupdeptrev(%d)""" % rec.id)
            mysetupdeptrev = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select getsetupdeptcost(%d)""" % rec.id)
            mysetupdeptcost = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select getmaindeptrev(%d)""" % rec.id)
            mymaindeptrev = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select getmaindeptcost(%d)""" % rec.id)
            mymaindeptcost = self.env.cr.fetchone()[0]

            if abs(mysetupanalysisrev - mysetupdeptrev) > 10:
                mystatus = mystatus + '(建置)成本分析收入:%s ,(建置)歸戶收入:%s 不合！' % (mysetupanalysisrev,mysetupdeptrev)
            elif abs(mymainanalysisrev - mymaindeptrev) > 10:
                mystatus = mystatus + '(維護)成本分析收入:%s ,(維護)歸戶收入:%s 不合！' % (mymainanalysisrev, mymaindeptrev)
            # elif abs(mysetupanalysiscost - mysetupdeptcost) > 10:
            #     mystatus = mystatus + '(建置)成本分析成本:%s ,(建置)歸戶成本:%s 不合！' % (mysetupanalysiscost, mysetupdeptcost)
            elif abs(mymainanalysiscost - mymaindeptcost) > 10:
                mystatus = mystatus + '(維護)成本分析成本:%s ,(維護)歸戶成本:%s 不合！' % (mymainanalysiscost, mymaindeptcost)
            else:
                mystatus = 'Balance'
            if mystatus == 'Balance':
                self.env.cr.execute("""update neweb_project set proj_status='Balance',proj_write_num=coalesce(proj_write_num,0)+1 where id=%d""" % rec.id)
            else:
                self.env.cr.execute("""update neweb_project set proj_status='%s',proj_write_num=coalesce(proj_write_num,0)+1where id=%d""" % (mystatus, rec.id))
            if mystatus1 == 'Balance':
                self.env.cr.execute("""update neweb_project set proj_status1='Balance',proj_write_num=coalesce(proj_write_num,0)+1 where id=%d""" % rec.id)
            else:
                self.env.cr.execute("""update neweb_project set proj_status1='%s',proj_write_num=coalesce(proj_write_num,0)+1 where id=%d""" % (mystatus1, rec.id))
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select gencostdeptper(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select genprojlineitem(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select gensaleprojectno(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select checkprojstatus(%d)""" % rec.id)
            projstatus = self.env.cr.fetchone()[0]
            # if not projstatus:
            #     raise UserError('成本歸戶收入與成本不平,請確認 收入平衡與成本歸戶狀態描述')
        return res

