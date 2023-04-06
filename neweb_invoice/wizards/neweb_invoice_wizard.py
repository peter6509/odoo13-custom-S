# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebinvoicewizard(models.TransientModel):
    _name = "neweb_invoice.invoiceopen_wizard"


    project_no = fields.Many2one('neweb.project',domain=lambda self:[('invoice_complete','=',False)],string="請選擇專案編號")

    def gen_project_invoice(self):
        myproj = self.project_no
        myrev1 = self.env.ref('neweb_project.neweb_costtype_1')    # 銷售
        myrev2 = self.env.ref('neweb_project.neweb_costtype_2')    # 專案
        myrev3 = self.env.ref('neweb_project.neweb_costtype_3')    # 建置
        myrev4 = self.env.ref('neweb_project.neweb_costtype_4')    # 維護
        myrev5 = self.env.ref('neweb_project.neweb_costtype_5')    # 維護人力
        myrev6 = self.env.ref('neweb_project.neweb_costtype_6')    # 利息
        myrev7 = self.env.ref('neweb_project.neweb_costtype_7')    # 租賃
        myrev8 = self.env.ref('neweb_project.neweb_costtype_8')    # 其他

        myname = self.env['ir.sequence'].next_by_code('neweb_invoice.invoiceopen')
        # try:
        self.env.cr.execute("select gen_invoicedata(%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (myproj.id,myrev1.id,myrev2.id,myrev3.id,myrev4.id,myrev5.id,myrev6.id,myrev7.id,myrev8.id))
        myrec = self.env['neweb_invoice.invoiceopen'].search([('project_no','=',myproj.id)])
        myrec.write({'name':myname})
        return {'view_name': '發票開立申請',
                'name': ('專案合約發票開立作業'),
                'views': [[False, 'form'], ],
                'res_model': 'neweb_invoice.invoiceopen',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                # 'domain' : mydomain,
                'res_id': myrec.id,
                'view_mode': 'form',
                'view_type': 'form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }
        # except Exception as inst:
        #     raise UserError("查無此成本分析編號或此成本分析編號已開立完成")
