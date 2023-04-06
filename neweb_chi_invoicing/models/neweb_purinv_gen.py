# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebpurinvgen(models.Model):
    _inherit = "neweb_purinv.invoiceline"

    is_gen = fields.Boolean(string="產出進項資料",default=False)
    gen_date = fields.Date(string="進項產出日期")
    gen_cdate = fields.Char(string="C進項產出日期")
    gen_man = fields.Many2one('hr.employee',string="進項產出人員")
    is_m_gen = fields.Boolean(string="產出維護進項資料",default=False)
    gen_m_date = fields.Date(string="維護進項產出日期")
    gen_m_cdate = fields.Date(string="C維護進項產出日期")
    gen_m_man = fields.Many2one('hr.employee', string="維護進項產出人員")
    main_purno = fields.Char(string="維護進貨單號")

    def get_select(self):
        for rec in self:
            if rec.is_gen == True:
                rec.update({'is_gen': False})
                self.env.cr.execute("""select genunselectpuritem(%d)""" % rec.id)
                self.env.cr.execute("""commit""")
            else:
                rec.update({'is_gen': True})
                myid = self.env.uid
                self.env.cr.execute("""select genselectpuritem(%d,%d)""" % (rec.id,self.env.uid))
                self.env.cr.execute("""commit""")

                # 先全選
                # myviewid = self.env.ref('neweb_chi_invoicing.neweb_purchase_select_form')
                # myrec = self.env['neweb_chi_invoicing.purchase_select'].search([])
                # myid = myrec[0].id
                # return {
                #     'view_name': 'newebinvoicingexportwizard',
                #     'name': ('進銷存 purchase 分批選單'),
                #     'type': 'ir.actions.act_window',
                #     'res_model': 'neweb_chi_invoicing.purchase_select',
                #     'view_id': myviewid.id,
                #     'res_id' : myid,
                #     'view_type': 'form',
                #     'view_mode': 'form',
                #     'target': 'main',
                #     'context' : {'invoiceopen_id': self.invline_id.id},
                #     }

    def get_m_select(self):
        for rec in self:
            if rec.is_m_gen == True:
                rec.update({'is_m_gen': False})
            else:
                rec.update({'is_m_gen': True})


    def write(self, vals):
        if 'is_gen' in vals and vals['is_gen'] :
            self.env.cr.execute("""select getexportempid(%d)""" % self.env.user.id)
            vals['gen_man'] = self.env.cr.fetchone()[0]
        if 'is_m_gen' in vals and vals['is_m_gen'] :
            self.env.cr.execute("""select getexportempid(%d)""" % self.env.user.id)
            vals['gen_m_man'] = self.env.cr.fetchone()[0]
        res = super(newebpurinvgen, self).write(vals)
        return res




class newebchiinvoicingproject(models.Model):
    _inherit = "neweb.project"


    def write(self, vals):

        res = super(newebchiinvoicingproject, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select genprojchiprodno(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res