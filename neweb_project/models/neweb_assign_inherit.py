# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebassigninherit(models.Model):
    _inherit = "neweb.proj_eng_assign"


    @api.depends()
    def _get_setup1(self):
        for rec in self:
            issetup1 = False
            if rec.id:
                self.env.cr.execute("""select getengsetupdesc1(%d)""" % rec.id)
                myres = self.env.cr.fetchone()[0]
                if myres==1:
                    issetup1=True
            rec.is_setup1 = issetup1
        return issetup1


    @api.depends()
    def _get_setup2(self):
        for rec in self:
            issetup2 = False
            if rec.id:
                self.env.cr.execute("""select getengsetupdesc2(%d)""" % rec.id)
                myres = self.env.cr.fetchone()[0]
                if myres == 2:
                    issetup2 = True
            rec.is_setup2 = issetup2
        return issetup2

    @api.depends()
    def _get_servicetype(self):
        for rec in self:
            self.env.cr.execute("""select getengservicetypename(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            rec.servicetypename = myres
            return myres

    #wkf_start = fields.Boolean(string="簽核是否啟始",store=False,default='_check_start',track_visibility='always')
    borrow_need = fields.Selection([('1','內部'),('2','外部'),('3','無')],string="借貨需求",default='1')
    assign_man_date = fields.Date(string="預計執行日期")
    completed_date = fields.Date(string="實際完成日期")
    assign_man_subject = fields.Char(string="派工主旨",required=True,default=' ')
    is_setup1 = fields.Boolean(string="是否公司內組裝",compute=_get_setup1)
    is_setup2 = fields.Boolean(string="是否客戶端組裝",compute=_get_setup2)
    is_attach1 = fields.Boolean(string="出貨簽收單",default=False)
    is_attach2 = fields.Boolean(string="操作手冊",default=False)
    is_attach3 = fields.Boolean(string="其他",default=False)
    assign_mans = fields.Char(string="派工成員")
    service_type1 = fields.Many2many('neweb.ass_service_type', string="服務類別",required=True)
    servicetypename = fields.Char(string="服務類別說明",compute=_get_servicetype)


    @api.model
    def create(self, vals):

        rec = super(newebassigninherit, self).create(vals)
        myassignmans = ""
        i = 0
        for rec1 in rec.assign_man:
            if rec1.employee_ids:
                myassignmans = myassignmans + rec1.employee_ids.name + " /"
                i = i + 1
        if i > 0:
            myassignmans = myassignmans[:-1]
        self.env.cr.execute("""update neweb_proj_eng_assign set assign_mans='%s' where id=%d""" % (myassignmans, rec.id))
        return rec

    def write(self, vals):
        res = super(newebassigninherit, self).write(vals)
        for rec in self:
            myrec = self.env['neweb.proj_eng_assign'].search([('id', '=', rec.id)])
            myassignmans = ""
            i = 0
            for rec1 in myrec.assign_man:
                if rec1.employee_ids:
                    myassignmans = myassignmans + rec1.employee_ids.name + " /"
                    i = i + 1
            if i > 0:
                myassignmans = myassignmans[:-1]
            self.env.cr.execute("""update neweb_proj_eng_assign set assign_mans='%s' where id=%d""" % (myassignmans, rec.id))
            return res



