# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class acmeiotquantreportwizard(models.TransientModel):
    _name = "alldo_acme_iot.quant_report_wizard"

    report_type = fields.Selection([('1','自選批次號條碼'),('2','全選批次號條碼')],string="列印類別",default='2')
    quant_ids = fields.Many2many('stock.quant',string="批次號")

    @api.onchange('report_type')
    def onchangereporttype(self):
        self.env.cr.execute("""select genalllotid()""")
        myrec = self.env.cr.fetchall()
        ids = []
        for rec in myrec:
            ids.append(rec[0])
        return {'domain': {'quant_ids': [('id', 'in', ids)]}}

    def run_quant_report(self):
        self.env.cr.execute("""delete from alldo_acme_iot_quant_report""")
        self.env.cr.execute("""commit""")
        quant_rec = self.env['alldo_acme_iot.quant_report']
        if self.report_type=='1':
           nitem = 1
           ncount = 1
           for rec in self.quant_ids:
               lotcode = rec.lot_id.name
               if nitem == 1:
                  if ncount == 1:
                     myrec = quant_rec.create({'quant_line':[(0,0,{'lot_code1':lotcode})]})
                  else:
                      self.env.cr.execute("""select addquantline('%s')""" % (lotcode))
                      self.env.cr.execute("""commit""")
               elif nitem == 2:
                  self.env.cr.execute("""select updatequantline(%d,'%s')""" % (2,lotcode))
                  self.env.cr.execute("""commit""")
               elif nitem == 3:
                  self.env.cr.execute("""select updatequantline(%d,'%s')""" % (3, lotcode))
                  self.env.cr.execute("""commit""")
               elif nitem == 4:
                  self.env.cr.execute("""select updatequantline(%d,'%s')""" % (4, lotcode))
                  self.env.cr.execute("""commit""")
               elif nitem == 5:
                  self.env.cr.execute("""select updatequantline(%d,'%s')""" % (5, lotcode))
                  self.env.cr.execute("""commit""")
               elif nitem == 6:
                  self.env.cr.execute("""select updatequantline(%d,'%s')""" % (6, lotcode))
                  self.env.cr.execute("""commit""")
               elif nitem == 7:
                  self.env.cr.execute("""select updatequantline(%d,'%s')""" % (7, lotcode))
                  self.env.cr.execute("""commit""")
               elif nitem == 8:
                   self.env.cr.execute("""select updatequantline(%d,'%s')""" % (8, lotcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 9:
                   self.env.cr.execute("""select updatequantline(%d,'%s')""" % (9, lotcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 10:
                   self.env.cr.execute("""select updatequantline(%d,'%s')""" % (10, lotcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 11:
                   self.env.cr.execute("""select updatequantline(%d,'%s')""" % (11, lotcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 12:
                   self.env.cr.execute("""select updatequantline(%d,'%s')""" % (12, lotcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 13:
                   self.env.cr.execute("""select updatemoldline(%d,'%s')""" % (13, lotcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 14:
                   self.env.cr.execute("""select updatequantline(%d,'%s')""" % (14, lotcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 15:
                   self.env.cr.execute("""select updatequantline(%d,'%s')""" % (15, lotcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 16:
                   self.env.cr.execute("""select updatequantline(%d,'%s')""" % (16, lotcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 17:
                   self.env.cr.execute("""select updatequantline(%d,'%s')""" % (17, lotcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 18:
                   self.env.cr.execute("""select updatequnatline(%d,'%s')""" % (18, lotcode))
                   self.env.cr.execute("""commit""")
               elif nitem == 19:
                   self.env.cr.execute("""select updatequantline(%d,'%s')""" % (19, lotcode))
                   self.env.cr.execute("""commit""")
               else:
                   self.env.cr.execute("""select updatequantline(%d,'%s')""" % (20, lotcode))
                   self.env.cr.execute("""commit""")
                   nitem = 0
               nitem = nitem + 1
               ncount = ncount + 1
        else:
            quant1_rec = self.env['stock.quant'].search([('company_id','=',1),('lot_id','!=',False),('location_id','=',19),('quantity','>',0)])
            mold_rec = self.env['alldo_acme_iot.quant_report']
            nitem = 1
            ncount = 1
            for rec in quant1_rec:
                lotcode = rec.lot_id.name
                if nitem == 1:
                    if ncount == 1:
                        myrec = mold_rec.create({'quant_line': [(0, 0, {'lot_code1': lotcode})]})
                    else:
                        self.env.cr.execute("""select addquantline('%s')""" % (lotcode))
                        self.env.cr.execute("""commit""")
                elif nitem == 2:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (2, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 3:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (3, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 4:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (4, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 5:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (5, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 6:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (6, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 7:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (7, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 8:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (8, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 9:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (9, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 10:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (10, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 11:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (11, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 12:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (12, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 13:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (13, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 14:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (14, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 15:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (15, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 16:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (16, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 17:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (17, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 18:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (18, lotcode))
                    self.env.cr.execute("""commit""")
                elif nitem == 19:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (19, lotcode))
                    self.env.cr.execute("""commit""")
                else:
                    self.env.cr.execute("""select updatequantline(%d,'%s')""" % (20, lotcode))
                    self.env.cr.execute("""commit""")
                    nitem = 0
                nitem = nitem + 1
                ncount = ncount + 1

        myviewid = self.env.ref('alldo_acme_iot.alldo_acme_stock_quant_report_action')
        myrec = self.env['alldo_acme_iot.quant_report'].search([])
        myid = myrec[0].id
        return {'view_name': 'views_quant_report_action',
                'name': (u'quant report item Data'),
                'views': [[False,'form']],
                'res_model': 'alldo_acme_iot.quant_report',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'view_id': myviewid.id,
                'target': 'current',
                'view_mode': 'form',
                'view_type': 'form'
                }