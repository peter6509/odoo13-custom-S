# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotmoldreportwizard(models.TransientModel):
    _name = "alldo_ipla_iot.mold_report_wizard"

    report_type = fields.Selection([('1','自選模具條碼'),('2','全選模具條碼')],string="列印類別",default='1')
    mold_ids = fields.Many2many('alldo_ipla_iot.ipla_mold',string="模具")

    def run_mold_report(self):
        self.env.cr.execute("""delete from alldo_ipla_iot_mold_report""")
        self.env.cr.execute("""commit""")
        mold_rec = self.env['alldo_ipla_iot.mold_report']
        if self.report_type=='1':
           nitem = 1
           ncount = 1
           for rec in self.mold_ids:
               moldcode = self.env['alldo_ipla_iot.ipla_mold'].search([('id','=',rec.id)]).mold_no
               if nitem == 1:
                  if ncount == 1:
                     myrec = mold_rec.create({'mold_line':[(0,0,{'mold_code1':moldcode})]})
                  else:
                      self.env.cr.execute("""select addmoldline('%s')""" % (moldcode))
                      self.env.cr.execute("""commit""")
               elif nitem == 2:
                  self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (2,moldcode))
                  self.env.cr.execute("""commit""")
               elif nitem == 3:
                  self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (3, moldcode))
                  self.env.cr.execute("""commit""")
               elif nitem == 4:
                  self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (4, moldcode))
                  self.env.cr.execute("""commit""")
               elif nitem == 5:
                  self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (5, moldcode))
                  self.env.cr.execute("""commit""")
               elif nitem == 6:
                  self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (6, moldcode))
                  self.env.cr.execute("""commit""")
               elif nitem == 7:
                  self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (7, moldcode))
                  self.env.cr.execute("""commit""")
               elif nitem == 8:
                   self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (8, moldcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 9:
                   self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (9, moldcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 10:
                   self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (10, moldcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 11:
                   self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (11, moldcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 12:
                   self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (12, moldcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 13:
                   self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (13, moldcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 14:
                   self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (14, moldcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 15:
                   self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (15, moldcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 16:
                   self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (16, moldcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 17:
                   self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (17, moldcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 18:
                   self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (18, moldcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 19:
                   self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (19, moldcode))
                   self.env.cr.execute("""commit""")
               else:
                   self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (20, moldcode))
                   self.env.cr.execute("""commit""")
                   nitem = 0
               nitem = nitem + 1
               ncount = ncount + 1
        else:
            mold1_rec = self.env['alldo_ipla_iot.ipla_mold'].search([('active','=',True)])
            mold_rec = self.env['alldo_ipla_iot.mold_report']
            nitem = 1
            ncount = 1
            for rec in mold1_rec:
                moldcode = rec.mold_no
                if nitem == 1:
                    if ncount == 1:
                        myrec = mold_rec.create({'mold_line': [(0, 0, {'mold_code1': moldcode})]})
                    else:
                        self.env.cr.execute("""select addmoldline('%s')""" % (moldcode))
                        self.env.cr.execute("""commit""")
                elif nitem == 2:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (2, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 3:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (3, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 4:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (4, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 5:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (5, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 6:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (6, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 7:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (7, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 8:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (8, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 9:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (9, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 10:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (10, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 11:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (11, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 12:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (12, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 13:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (13, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 14:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (14, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 15:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (15, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 16:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (16, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 17:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (17, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 18:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (18, moldcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 19:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (19, moldcode))
                    self.env.cr.execute("""commit""")
                else:
                    self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (20, moldcode))
                    self.env.cr.execute("""commit""")
                    nitem = 0
                nitem = nitem + 1
                ncount = ncount + 1

        myviewid = self.env.ref('alldo_ipla_iot.alldo_ipla_mold_report_action')
        myrec = self.env['alldo_ipla_iot.mold_report'].search([])
        myid = myrec[0].id
        return {'view_name': 'views_mold_report_action',
                'name': (u'mold report item Data'),
                'views': [[False,'form']],
                'res_model': 'alldo_ipla_iot.mold_report',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'view_id': myviewid.id,
                'target': 'current',
                'view_mode': 'form',
                'view_type': 'form'
                }