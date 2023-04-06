# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebchiinvoicing8wizard(models.TransientModel):
    _name = "neweb_chi_invoicing.chiinvoicing8_wizard"
    _description = "(維護)進貨憑證整批匯出精靈"


    export_user = fields.Many2one('res.users', string="匯出人員", default=lambda self: self.env.uid)


    def run_invoicing8_export(self):
        # self.env.cr.execute("""delete from neweb_chi_invoicing_package_purchase""")
        # self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gen_unexport_mainpurinv(%d)""" % (self.export_user.id))
        myid = self.env['neweb_chi_invoicing.un_export_purinv'].search([])
        if not myid:
            raise UserError("沒有需匯出的進項項目,請確認")
        self.env.cr.execute("""select prerunpackageexport()""")
        self.env.cr.execute("""commit""")
        return {'view_name': 'newebchiunexportpurinvselect',
                'name': ('進項購貨明細資料'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'neweb_chi_invoicing.un_export_purinv',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'current',
                'res_id': myid.id,
                'flags': {'action_buttons': False, 'initial_mode': 'edit'},
                'view_mode': 'form',
                'view_type': 'form'
                }