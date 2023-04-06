# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebqcsendmail(models.TransientModel):
    _name = "neweb.qcsendmail_wizard"


    origin = fields.Many2one('stock.picking',string="選擇單號",domain=lambda self:[('stockin_qc','=',True),('stockin_checkman.id','=',self.env.uid)])



    def qc_sendmail(self):
        '''
        This function opens a window to compose an email, with the edi purchase request template message loaded by default
        '''
        # print "%s" % self.origin.id
        myrec=self.env['stock.picking'].search([('id','=',self.origin.id)])
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_stockin', 'email_template_stockinqc_message')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = dict()
        ctx.update({
            'default_model': 'stock.picking',
            'default_res_id': myrec.id,
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
        })

        for line in myrec.stockin_line:
            if line.qc_man.id == self.env.uid :
               line.update({'stockin_qcsendemail':True})

        return {
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'mail.compose.message',
                'views': [(compose_form_id, 'form')],
                'view_id': compose_form_id,
                'target': 'new',
                'context': ctx,
                }
