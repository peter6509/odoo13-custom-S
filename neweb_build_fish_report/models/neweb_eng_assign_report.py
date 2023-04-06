# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request

class newebbfengassign(models.Model):
    _inherit = "neweb.proj_eng_assign"

    @api.depends()
    def _get_projno(self):
        for rec in self:
            self.env.cr.execute("""select getengprojno(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            rec.projno = myres
            return myres


    @api.depends()
    def _get_projcusname(self):
        for rec in self:
            self.env.cr.execute("""select getengprojcusname(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            rec.projcusname = myres
            return myres

    @api.depends()
    def _get_projsalename(self):
        for rec in self:
            self.env.cr.execute("""select getengprojsalename(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            rec.projsalename = myres
            return myres

    @api.depends()
    def _get_setupcontactname(self):
        for rec in self:
            self.env.cr.execute("""select getengsetupcontact(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            rec.setupcontactname = myres
            return myres

    @api.depends()
    def _get_assignman(self):
        for rec in self:
            self.env.cr.execute("""select getengassignman(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            rec.assignman=myres
            return myres

    @api.depends()
    def _get_servicename(self):
        for rec in self:
           self.env.cr.execute("""select getengservicename(%d)""" % rec.id)
           myres = self.env.cr.fetchone()[0]
           rec.servicename = myres
           return myres

    @api.depends()
    def _get_servicetypename(self):
        for rec in self:
            self.env.cr.execute("""select getengservicetypename(%d)""" % rec.id)
            myres = self.env.cr.fetchone()[0]
            rec.servicetypename = myres
            return myres



    projno = fields.Char(string="專案編號",compute=_get_projno)
    projcusname = fields.Char(string="客戶名稱",compute=_get_projcusname)
    projsalename = fields.Char(string="專屬業務",compute=_get_projsalename)
    setupcontactname = fields.Char(string="裝機聯絡人",compute=_get_setupcontactname)
    assignman = fields.Char(string="指派工程師",compute=_get_assignman)
    servicename = fields.Char(string="服務名稱",compute=_get_servicename)
    servicetypename = fields.Char(string="服務類別",compute=_get_servicetypename)


    def action_print_eng_assign(self):
        self.ensure_one()
        # base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_eng_assign_report/%s" % (bf_url,self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }
