# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import fields,models,api
from odoo.exceptions import UserError,Warning


class newebstocklineqc(models.Model):
    _name = "neweb.stockinline_qcout"

    stockin_machinetype = fields.Char(string="機種")
    stockin_modeltype = fields.Char(string="機型")
    stockin_prodno = fields.Char(string="料號")
    stockin_spec = fields.Char(string="規格說明")
    stockin_serial = fields.Char(string="序號")
    stockin_qcoutnum = fields.Float(digits=(10,0), string="拒收數量")
    stockin_desc = fields.Char(string="備註")
    origin = fields.Char(string="採購單號")
    stockin_checkman = fields.Many2one('res.users', string="檢測工程師")
    sequence_id = fields.Integer()



class newebstocklineqc(models.TransientModel):
    _name = "neweb.stockinline_qc"

    stockin_id = fields.Integer()
    stockin_machinetype = fields.Char(string="機種")
    stockin_modeltype = fields.Char(string="機型")
    stockin_prodno = fields.Char(string="料號")
    stockin_spec = fields.Char(string="規格說明")
    stockin_serial = fields.Char(string="序號")
    stockin_num = fields.Float(digits=(10,0), string="收貨數量")
    stockin_qcnum = fields.Float(digits=(10,0), string="允收數量")
    stockin_check = fields.Selection([('1', 'OK'), ('2', 'NG')], string="測試狀況",default='1')
    stockin_desc = fields.Char(string="備註")
    origin = fields.Char(string="採購單號")
    sequence_id = fields.Integer()
    stockin_checkdo = fields.Selection([('1','是'),('2','否')],string="檢驗否？",default='2')


    def name_get(self):
        result = []
        for myrec in self:
            mytext1 = myrec.origin

            mycheckqcitem = "[來源單號:%s]" % (mytext1)
            result.append((myrec.id, mycheckqcitem))
        return result




    def qc_check(self):
        myqcid = self.env.context.get('qc_op_id')
        myrec = self.env['neweb.stockinline_qc'].search([('id', '=', myqcid)])
        mystockinrec = self.env['stock.picking'].search([('origin', '=', myrec.origin)])
        if myrec.stockin_num > myrec.stockin_qcnum:
            myqcrec = self.env['neweb.stockinline_qcout'].search([])
            myqcrec.create({'stockin_machinetype': myrec.stockin_machinetype,
                            'stockin_modeltype': myrec.stockin_modeltype,
                            'stockin_prodno': myrec.stockin_prodno,
                            'stockin_spec': myrec.stockin_spec,
                            'stockin_serial': myrec.stockin_serial,
                            'stockin_qcoutnum': (myrec.stockin_num - myrec.stockin_qcnum),
                            'stockin_desc': myrec.stockin_desc,
                            'origin': myrec.origin,
                            'sequence_id': myrec.sequence_id,
                            'stockin_checkman': mystockinrec.stockin_checkman.id})

            mystockinrec.write({'state': 'partially_available'})
            mypackoperline = self.env['stock.pack.operation'].search([('picking_id', '=', mystockinrec.id)])
            mypackoperline.write({'qty_done': 0})
            mystockinlist = self.env['neweb.stockin_list'].search([('id', '=', myrec.sequence_id)])
            mystockinlist.write({'stockin_check': '1',
                                 'stockin_num': mystockinlist.stockin_num - (myrec.stockin_num - myrec.stockin_qcnum),
                                 'stockin_serial': myrec.stockin_serial})
            mypitemlist = self.env['neweb.pitem_list'].search([('id', '=', mystockinlist.stockin_sequence_id)])
            mypitem_innum = mypitemlist.pitem_stockin_num - (myrec.stockin_num - myrec.stockin_qcnum)
            self.env.cr.execute("select qcwritepitem(%s,%s)" % (mystockinlist.stockin_sequence_id,mypitem_innum))
            # mypitemlist.write(
            #     {'pitem_stockin_num': mypitemlist.pitem_stockin_num - (myrec.stockin_num - myrec.stockin_qcnum),
            #      'pitem_stockin_complete': False})
        else:
            mystockinlist = self.env['neweb.stockin_list'].search([('id', '=', myrec.sequence_id)])
            mystockinlist.write({'stockin_check': '1',
                                 'stockin_serial': myrec.stockin_serial})

        self.env.cr.execute("select gencheckqc(%d)" % mystockinrec.id)
        myrec.update({'stockin_checkdo':'1'})

        viewid = self.env.ref('neweb_stockin.neweb_stockinqcedit_action')
        return {'view_name': 'newebstocklineqc',
                'name': ('檢驗進貨選單'),
                'views': [[False, 'tree'], [False, 'form']],
                'res_model': 'neweb.stockinline_qc',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'view_id': viewid.id,
                'domain': [],
                'flags': {'action_buttons': True},
                'view_mode': 'tree,form',
                'view_type': 'form'
                }




class newebstockinqc(models.TransientModel):
    _name = "neweb.stockin_qc"

    @api.model
    def _get_qcmandomain(self):
        res={}
        myid=self.env.uid
        myrec = self.env['stock.picking'].search([('stockin_qc','=',True),('stockin_checkyn','=',False),('stockin_checkman','=',self.env.uid)])
        ids=[]
        for line in myrec:
            ids.append(line.id)
        res['domain']={'origin':[('id','in',ids)]}
        return res

    origin = fields.Many2one('stock.picking',string="採購單號")
    # domain 作在 neweb_stockinqc_wizard.xml 裡面


    def get_qc_data(self):
        mystockpickingid = self.origin.id
        # print "%s" % mystockpickingid
        mystockpingrec = self.env['stock.picking'].search([('id','=',mystockpickingid)])
        self.env.cr.execute("delete from neweb_stockin_qc")
        self.env.cr.execute("delete from neweb_stockinline_qc")
        mystockinqclinerec = self.env['neweb.stockinline_qc'].search([])

        for line in mystockpingrec.stockin_line :

            if line.stockin_check == '2' and line.qc_man.id == self.env.uid :
               mystockinqclinerec.create({'stockin_id':mystockpickingid,
                                          'stockin_machinetype':line.stockin_machinetype,
                                          'stockin_modeltype':line.stockin_modeltype,
                                          'stockin_prodno':line.stockin_prodno,
                                          'stockin_spec':line.stockin_spec,
                                          'stockin_num':line.stockin_num,
                                          'stockin_serial': line.stockin_serial,
                                          'stockin_qcnum' : line.stockin_num,
                                          'stockin_check':'1',
                                          'origin': mystockpingrec.origin,
                                          'sequence_id':line.id})
            else:
                raise UserError("此進貨單沒有需您檢驗的項目")


        viewid = self.env.ref('neweb_stockin.neweb_stockinqcedit_action')
        return {'view_name': 'newebstockinqc',
                'name': ('檢驗進貨選單'),
                'views': [[False,'tree'],[False, 'form']],
                'res_model': 'neweb.stockinline_qc',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'view_id': viewid.id,
                'domain' : [],
                'flags': {'action_buttons': True},
                'view_mode': 'tree,form',
                'view_type': 'form'
                }
