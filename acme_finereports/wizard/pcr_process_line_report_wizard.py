# -*- coding: utf-8 -*-
from odoo import fields,api,models,_


class ZimoPcrProcessLineReportWizard(models.TransientModel):
    _name = 'zimo.pcr.process.line.report.wizard'
    _description = '生产单明细报表'

    mo_name = fields.Char('任务单号')



    def open_table(self):
        self.ensure_one()
        domain = []
        if self.mo_name:
            domain.append(('mo_name','ilike',self.mo_name),)
        return {
            'name': _("在制品明细报表"),
            'view_mode': 'tree,form,pivot',
            'res_model': 'zimo.pcr.process.line.report',
            'domain': domain,
            'type': 'ir.actions.act_window',
                }


