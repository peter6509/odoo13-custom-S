# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError


class newebchiinvoicing2wizard(models.Model):
    _name = "neweb_chi_invoicing.chiinvoicing2_wizard"
    _description = "銷售憑證單筆匯出精靈"

    project_no = fields.Many2one('neweb.project',string="專案編號")
    # roject_no = fields.Many2one('neweb.project', string="專案編號",
    #                             domain=lambda self: [('chi_export_outcome', '=', False)])
    export_user = fields.Many2one('res.users', string="匯出人員", default=lambda self: self.env.uid)

    def run_invoicing2_export(self):
        if not self.project_no:
            raise UserError("未選定成本分析編號")
        self.env.cr.execute("""select gen_unexport_saleinv1(%d,%d)""" % (self.project_no.id,self.export_user.id))
        myid = self.env['neweb_chi_invoicing.un_export_invoiceopen'].search([])
        if not myid:
            raise UserError("沒有需匯出的銷項項目,請確認")
        self.env.cr.execute("""select prerunpackageexport()""")
        self.env.cr.execute("""commit""")
        return {'view_name': 'newebchiunexportprojselect',
                'name': ('專案購貨明細資料'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'neweb_chi_invoicing.un_export_invoiceopen',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'current',
                'res_id': myid.id,
                'flags': {'action_buttons': False, 'initial_mode': 'edit'},
                'view_mode': 'form',
                'view_type': 'form'
                }
