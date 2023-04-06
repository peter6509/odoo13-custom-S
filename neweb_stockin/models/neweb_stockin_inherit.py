# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
from datetime import datetime,timedelta


class newebpurselectableline(models.Model):
    _name = "neweb.purselectableline"
    _description = "採購選單=>進貨檢驗明細"

    pitem_id = fields.Many2one('neweb.purselectable',required=True, ondelete='cascade')
    pitem_machine_type = fields.Char(string="機種")
    pitem_model_type = fields.Char(string="機種-機型/料號")
    pitem_prod_no = fields.Char(string="料號")
    pitem_spec = fields.Char(string="規格說明")
    pitem_warranty = fields.Char(string="保固期限")
    pitem_num = fields.Float(digits=(10,0), string="收貨數量", required=True)
    pitem_stockin_num = fields.Float(digits=(10,0), string="已進數量", default=0)
    purchase_no = fields.Char(related='pitem_id.name', string="採購單號")
    origin_id = fields.Integer()
    selectyn = fields.Boolean(default=False, string="選")


    def get_select(self):
        for rec in self:
           if rec.selectyn == True:
              rec.update({'selectyn': False})
           else:
              rec.update({'selectyn': True})


class newebpurselectable(models.Model):
    _name = "neweb.purselectable"
    _description = "採購選單主表=>進貨檢驗"

    name = fields.Char(string="採購單號")
    display_line = fields.One2many('neweb.purselectableline', 'pitem_id', copy=True, string="明細資料")

    def selectbtn(self):
        myid = self.env.ref('neweb_project.neweb_product_purchase_1')
        mycount=self.env['neweb.purselectableline'].search_count([('pitem_id','=',self.id),('selectyn','=',True)])
        if mycount == 0:
            raise UserError("未選取進貨明細資料...")
        mystockid = self.env.context.get('stockin_op_id')
        for line in self.display_line:
            if line.selectyn == True:
                self.env.cr.execute("select genstockinline(%s,%s,%s)" % (line.origin_id, mystockid, myid.id))
        myid = self.env['stock.picking'].search([('id', '=', mystockid)])
        return {'view_name': 'newebpurselectable',
                'name': ('進貨作業'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'stock.picking',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': myid.id,
                'view_mode': 'form',
                'view_type': 'form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }



    def noselect(self):
        mystockid = self.env.context.get('stockin_op_id')
        myid = self.env['stock.picking'].search([('id', '=', mystockid)])
        return {'view_name': 'newebpurselectable',
                'name': ('進貨作業'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'stock.picking',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': myid.id,
                'view_mode': 'form',
                'view_type': 'form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }


    def selectall(self):
        myid = self.env.ref('neweb_project.neweb_product_purchase_1')
        mystockid = self.env.context.get('stockin_op_id')
        mystockinrec = self.env['stock.picking'].search([('id', '=', self.env.context.get('stockin_op_id'))])
        mypurchaseno = mystockinrec.origin
        mypurchaseid = self.env['purchase.order'].search([('name', '=', mypurchaseno)])
        mypurline = self.env['neweb.pitem_list'].search(
            [('pitem_id', '=', mypurchaseid.id), ('pitem_stockin_complete', '=', False)])
        for line in mypurline:
            self.env.cr.execute("select genstockinline(%s,%s,%s)" % (line.id, mystockid, myid.id))
        myid = self.env['stock.picking'].search([('id', '=', mystockid)])
        return {'view_name': 'newebpurselectable',
                'name': ('進貨作業'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'stock.picking',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': myid.id,
                'view_mode': 'form',
                'view_type': 'form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                 }


class newebsaleselectableline(models.Model):
    _name = "neweb.saleselectableline"
    _description ="銷貨選單=>客戶出貨明細"

    sitem_id = fields.Many2one('neweb.saleselectable',required=True, ondelete='cascade')
    sitem_machinetype = fields.Char(string="機種")
    sitem_modeltype = fields.Char(string="機種-機型/料號")
    sitem_prodno = fields.Char(string="料號")
    sitem_spec = fields.Char(string="規格說明")
    sitem_desc = fields.Char(string="備註")
    sitem_num = fields.Float(digits=(10,0), string="交貨數量", required=True)
    sitem_price = fields.Float(digits=(13,2), string="單價")
    sitem_stockout_num = fields.Float(digits=(10,0), string="已交數量", default=0)
    sale_no = fields.Char(related='sitem_id.name', string="成本分析")
    origin_id = fields.Integer()
    selectyn = fields.Boolean(default=False, string="選")
    line_item = fields.Integer(string="序")


    def get_select(self):
        for rec in self:
            if rec.selectyn == True:
                rec.update({'selectyn': False})
            else:
                rec.update({'selectyn': True})



class newebsaleselectable(models.Model):
    _name = "neweb.saleselectable"
    _description = "銷貨選單主表=>客戶出貨"

    name = fields.Char(string="銷售單號")
    display_line = fields.One2many('neweb.saleselectableline', 'sitem_id', copy=True, string="明細資料")

    def selectbtn(self):
        myid = self.env.ref('neweb_project.neweb_product_sale_2')
        mycount = self.env['neweb.saleselectableline'].search_count([('sitem_id', '=', self.id), ('selectyn', '=', True)])
        if mycount == 0:
            raise UserError("未選取出貨明細資料...")
        mystockid = self.env.context.get('stockout_op_id')
        for line in self.display_line:
            if line.selectyn==True:
               # 舊邏輯
               #self.env.cr.execute("select genstockoutline(%s,%s,%s)" % (line.origin_id, mystockid, myid.id))
               self.env.cr.execute("select genstockoutline1(%s,%s,%s)" % (line.origin_id, mystockid, myid.id))
        myrecid = self.env['stock.picking'].search([('id', '=', mystockid)])
        return {'view_name': 'newebsaleselectable',
                'name': ('出貨作業'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'stock.picking',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': myrecid.id,
                'view_mode': 'form',
                'view_type': 'form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }


    def noselect(self):
        mystockid = self.env.context.get('stockout_op_id')
        myrecid = self.env['stock.picking'].search([('id', '=', mystockid)])
        return {'view_name': 'newebsaleselectable',
                'name': ('出貨作業'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'stock.picking',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': myrecid.id,
                'view_mode': 'form',
                'view_type': 'form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }


    def selectall(self):
        myid = self.env.ref('neweb_project.neweb_product_sale_2')
        # mycount = self.env['neweb.saleselectableline'].search_count(
        #     [('sitem_id', '=', self.id), ('selectyn', '=', True)])
        # if mycount == 0:
        #     raise UserError("未選取出貨明細資料...")
        mystockid = self.env.context.get('stockout_op_id')
        for line in self.display_line:
            self.env.cr.execute("select genstockoutline1(%s,%s,%s)" % (line.origin_id, mystockid, myid.id))
        myrecid = self.env['stock.picking'].search([('id', '=', mystockid)])
        return {'view_name': 'newebsaleselectable',
                'name': ('出貨作業'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'stock.picking',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': myrecid.id,
                'view_mode': 'form',
                'view_type': 'form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }



class newebdsselectable(models.TransientModel):
    _name = "neweb.dsselectable"

    name = fields.Char(string="採購單號")
    display_line = fields.One2many('neweb.dsselectableline', 'ds_id', copy=True, string="明細資料")

    def trans_stockds_list(self):
        myid = self.env.ref('neweb_project.neweb_product_purchase_1')
        if len(self.display_line) == 0:
            raise UserError("未選取交貨明細資料...")
        mystockid = self.env.context.get('stockds_op_id')
        for line in self.display_line:
            print("%s,%s" % (line.id, mystockid))
            self.env.cr.execute("select genstockdsline(%s,%s,%s)" % (line.origin_id, mystockid,myid.id))


    def trans_stockds_all(self):
        myid = self.env.ref('neweb_project.neweb_product_purchase_1')
        mystockid = self.env.context.get('stockds_op_id')
        mystockinrec = self.env['stock.picking'].search([('id', '=', self.env.context.get('stockds_op_id'))])
        mypurchaseno = mystockinrec.origin
        mypurchaseid = self.env['purchase.order'].search([('name', '=', mypurchaseno)])
        mypurline = self.env['neweb.pitem_list'].search(
            [('pitem_id', '=', mypurchaseid.id), ('pitem_stockin_complete', '=', False)])
        for line in mypurline:
            self.env.cr.execute("select genstockdsline(%s,%s,%s)" % (line.id, mystockid,myid.id))


class newebdsselectableline(models.TransientModel):
    _name = "neweb.dsselectableline"

    ds_id = fields.Many2one('neweb.dsselectable',required=True, ondelete='cascade')
    ds_machinetype = fields.Char(string="機種")
    ds_modeltype = fields.Char(string="機種-機型/料號")
    ds_prodno = fields.Char(string="料號")
    ds_spec = fields.Char(string="規格說明")
    ds_desc = fields.Char(string="備註")
    ds_num = fields.Float(digits=(10,0), string="收貨數量", required=True)
    ds_price = fields.Float(digits=(13,2), string="單價")
    ds_stockin_num = fields.Float(digits=(10,0), string="已收數量", default=0)
    sale_no = fields.Char(related='ds_id.name', string="銷售單號")
    origin_id = fields.Integer()


    def name_get(self):
        result = []
        for myrec in self:
            mytext1 = myrec.ds_machinetype
            if not mytext1:
                mytext1 = "-"
            mytext2 = myrec.ds_modeltype
            if not mytext2:
                mytext2 = "-"
            mytext3 = myrec.ds_prodno
            if not mytext3:
                mytext3 = "-"
            mytext4 = myrec.ds_spec
            if not mytext4:
                mytext4 = "-"
            mytext5 = myrec.ds_num
            if not mytext5:
                mytext5 = "1"
            else:
                mytext5 = str(myrec.ds_num)
            mytext6 = myrec.ds_stockin_num
            if not mytext6:
                mytext6 = mytext5
            else:
                mytext6 = str(myrec.ds_num - myrec.ds_stockin_num)

            mysaleitem = "[單號:%s][機種:%s][機型:%s][料號:%s][規格:%s][交貨量:%s][未交量:%s]" % (
                myrec.sale_no, mytext1, mytext2, mytext3, mytext4, mytext5, mytext6)
            result.append((myrec.id, mysaleitem))
        return result



class newebstockinlist(models.Model):
    _name = "neweb.stockin_list"
    _description = '進貨明細檔'
    _order = "stockin_item"

    stockin_id = fields.Many2one('stock.picking',required=True, ondelete='cascade')
    stockin_machinetype = fields.Char(string="機種")
    stockin_modeltype = fields.Char(string="機種-機型/料號")
    stockin_prodno = fields.Char(string="料號")
    stockin_spec = fields.Text(string="規格說明")
    stockin_serial = fields.Char(string="序號")
    stockin_num = fields.Float(digits=(10,0), string=u"允收數量",store=True,compute='_get_stockinnum')
    stockin_num1 = fields.Float(digits=(10,0),string=u"原始數量")
    stockin_check = fields.Selection([('1','OK'),('2','NG'),('3','NO')],string="測試狀況",default='3')
    stockin_desc = fields.Char(string="備註")
    stockin_sequence_id = fields.Integer(string="Pitem ID")
    stockin_sendemail = fields.Boolean(default=False)
    stockin_qcsendemail = fields.Boolean(default=False)
    stockin_qc = fields.Boolean(related='stockin_id.stockin_qc')
    prod_id = fields.Many2one('product.template', string="庫存料號")
    qc_man = fields.Many2one('res.users',string="檢驗工程師",compute='_get_qcman',store=True)
    stockin_item = fields.Float(digits=(4,1),string="項次")
    po_no = fields.Char(string="採購單號",compute='_get_pono')

    @api.depends('stockin_sequence_id')
    def _get_pono(self):
        for rec in self:
            self.env.cr.execute("""select getstockinpono(%d)""" % rec.stockin_sequence_id)
            rec.po_no = self.env.cr.fetchone()[0]


    @api.depends('stockin_id.stockin_checkman')
    def _get_qcman(self):
        for rec in self:
            rec.update({'qc_man': rec.stockin_id.stockin_checkman.id})


    @api.depends('stockin_num1')
    def _get_stockinnum(self):
        for rec in self:
            if rec.stockin_num == 0:
               rec.update({'stockin_num':rec.stockin_num1})


    @api.model
    def create(self, vals):
        if 'stockin_num1' in vals and vals['stockin_num1']:
            vals['stockin_num']=vals['stockin_num1']
            myprodid = self.prod_id
            mystockinnum = vals['stockin_num1']
            if myprodid:
                myrec = self.env['stock.pack.operation'].search(
                    [('picking_id', '=', self.stockin_id.id), ('product_id', '=', myprodid.id)])
                if myrec:
                    myrec.write({'qty_done': mystockinnum})
        rec = super(newebstockinlist, self).create(vals)
        # backorder check
        mystockinid = rec.stockin_id.id
        # myqcmanid = rec.qc_man.id
        # print "CREATE:%s,%s" % (mystockinid,myqcmanid)
        self.env.cr.execute("select checkbackorder(%s)" % mystockinid)
        self.env.cr.execute("commit")
        # self.env.cr.execute("select updateqcman(%s,%s)" % (mystockinid,myqcmanid))
        return rec


    def write(self, vals):
        #myid = self.id
        for rec in self:
            if 'stockin_num1' in vals and vals['stockin_num1']:
                vals['stockin_num'] = rec.stockin_num1
                myprodid = rec.prod_id
                mystockinnum = vals['stockin_num1']
                if myprodid:
                   myrec = self.env['stock.pack.operation'].search([('picking_id','=',rec.stockin_id.id),('product_id','=',myprodid.id)])
                   # print "%d" % mystockinnum
                   if myrec:
                      myrec.write({'qty_done':mystockinnum})


        rec = super(newebstockinlist, self).write(vals)
        return rec


    def unlink(self):
        for rec in self:
            self.env.cr.execute("""select unlinkstockinlist(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        res = super(newebstockinlist, self).unlink()
        return res


class newebstockoutlist(models.Model):
    _name = "neweb.stockout_list"
    _description = '出貨明細記錄-實際扣帳'

    stockout_id = fields.Many2one('stock.picking',required=True, ondelete='cascade')
    stockout_machinetype = fields.Char(string="機種")
    stockout_modeltype = fields.Char(string="機種-機型/料號")
    stockout_prodno = fields.Char(string="料號")
    stockout_spec = fields.Char(string="規格說明")
    stockout_num = fields.Float(digits=(10,0), string="數量")
    stockout_price = fields.Float(digits=(13,2), string="單價")
    stockout_desc = fields.Char(string="備註")
    stockout_sequence_id = fields.Integer(string="Sitem ID")
    line_item = fields.Integer(string="序")

    # 舊邏輯
    # @api.multi
    # def unlink(self):
    #     self.env.cr.execute("""select unlinkstockoutlist(%d)""" % self.id)
    #     res = super(newebstockoutlist,self).unlink()
    #     return res

    # @api.multi
    # def unlink(self):
    #     self.env.cr.execute("""select unlinkstockoutlist1(%d)""" % self.id)
    #     res = super(newebstockoutlist, self).unlink()
    #     return res


class newebstockshiplist(models.Model):
    _name = "neweb.stockship_list"
    _description = '出貨單出貨明細記錄'
    _order = "stockship_item"


    stockship_id = fields.Many2one('stock.picking', required=True, ondelete='cascade')
    stockship_machinetype = fields.Char(string="機種")
    stockship_modeltype = fields.Char(string="機種-機型/料號")
    stockship_prodno = fields.Char(string="料號")
    stockship_spec = fields.Text(string="規格說明")
    stockship_num = fields.Float(digits=(10,0), string="數量")
    stockship_price = fields.Float(digits=(13,2), string="單價")
    stockship_desc = fields.Text(string="備註")
    sequence = fields.Integer(default=10)
    stockship_item = fields.Float(digits=(4,1),string="項次")
    line_item = fields.Integer(string="序")

    # def unlink(self):
    #     self.env.cr.execute("""select unlinkstockoutlist1(%d)""" % self.id)
    #     res = super(newebstockshiplist, self).unlink()
    #     return res



class newebstockpickinginherit(models.Model):
    _inherit = "stock.picking"
    _description = '調撥主檔'

    @api.depends('name')
    def _get_pickname(self):
        for rec in self:
            if rec.name[:2] == 'DS':
                rec.update({'stockin_pickname': 'DS'})
            else:
                rec.update({'stockin_pickname': 'OTHER'})

    @api.depends('picking_type_id')
    def _get_picktype(self):
        for rec in self:
            rec.update({'stockin_picktype': rec.picking_type_id.code})

    @api.depends('stockin_line', 'stockin_qc')
    def _get_checkyn(self):
        for rec in self:
            if rec.stockin_qc:
                mycheckyn = False
            else:
                mycheckyn = True
            rec.update({'stockin_checkyn': mycheckyn})

    stockin_line = fields.One2many('neweb.stockin_list','stockin_id', copy=False, string="收貨明細資料")
    stockout_line = fields.One2many('neweb.stockout_list','stockout_id', copy=False, string="交貨明細資料")
    stockship_line = fields.One2many('neweb.stockship_list','stockship_id',copy=False, string="出貨單明細資料")
    stockin_type = fields.Selection([('1','銷貨'),('2','備品'),('3','歸還'),('4','其他')],string="進貨原因",default='1')
    stockout_type = fields.Selection([('1','銷售'),('3','借出'),('5','其它')],string="出貨原因",default='1')
    stockin_checkman = fields.Many2one('res.users',string="檢測工程師")
    stockin_desc = fields.Text(string="說明")
    stockin_sendmail = fields.Boolean(default=False,string="發信給檢驗者")
    stockin_qc = fields.Boolean(default=False, string="是否需工程檢驗？")
    stockin_checkyn = fields.Boolean(store=True,compute=_get_checkyn)
    stockin_picktype = fields.Char(compute=_get_picktype,store=False)
    stockin_pickname = fields.Char(compute=_get_pickname,store=False)
    stockds_origin = fields.Char(string="來源單據1")
    stockin_qc_status = fields.Selection([('1','[QC Waiting]'),('2','[QC Completed]'),('3','[Non QC]')],string="檢驗狀態",default=False)
    stockout_proj_no = fields.Char(string="專案編號")
    stockout_customer = fields.Char(string="聯絡人")
    stockout_custel = fields.Char(string="聯絡人電話")
    stockout_shipaddr = fields.Char(string="送貨地址")
    last_send_mail = fields.Datetime(string="最後發信時間")
    is_proj_main = fields.Boolean(string="是否為主出貨單?", default=False)
    is_pur_main = fields.Boolean(string="是否為主收貨單?", default=False)


    def stock_copy(self):
        if self.stockin_picktype=='outgoing':   # 出貨
            myrec=self.env['stock.picking'].search([('id','=',self.id)])
            self.env.cr.execute("""select chk_stockout(%d)""" % self.id)
            mycount = self.env.cr.fetchone()[0]
            if mycount > 0 :
                myres = myrec.copy()
                self.env.cr.execute("""select gen_copy_stockout2('%s',%d)""" % (self.stockout_proj_no, myres.id))
                self.env.cr.execute("""commit""")
                return {'view_name': 'Stock Picking',
                        'name': ('Stock Picking'),
                        'views': [[False, 'form'], [False, 'tree']],
                        'res_model': 'stock.picking',
                        'context': self._context,
                        'type': 'ir.actions.act_window',
                        'target': 'self',
                        'res_id': myres.id,
                        'view_mode': 'form',
                        'view_type': 'form',
                        'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                        }
            else:
                view = self.env.ref('sh_message.sh_message_wizard')
                view_id = view and view.id or False
                context = dict(self._context or {})
                context['message']='已無項目可以出貨了'
                return {
                    'name':'Success',
                    'type':'ir.actions.act_window',
                    'view_type':'form',
                    'view_mode':'form',
                    'res_model':'sh.message.wizard',
                    'views':[(view.id,'form')],
                    'view_id':view.id,
                    'target':'new',
                    'context':context,
                    }


    def stock_copy1(self):
        if self.stockin_picktype=='incoming': # 進貨
            myrec = self.env['stock.picking'].search([('id', '=', self.id)])
            self.env.cr.execute("""select chk_stockin(%d)""" % self.id)
            mycount = self.env.cr.fetchone()[0]
            if mycount > 0:
                myres = myrec.copy()
                self.env.cr.execute("""select gen_copy_stockin2('%s',%d)""" % (self.origin, myres.id))
                self.env.cr.execute("""commit""")
                return {'view_name': 'Stock Picking',
                        'name': ('Stock Picking'),
                        'views': [[False, 'form'], [False, 'tree']],
                        'res_model': 'stock.picking',
                        'context': self._context,
                        'type': 'ir.actions.act_window',
                        'target': 'self',
                        'res_id': myres.id,
                        'view_mode': 'form',
                        'view_type': 'form',
                        'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                        }
            else:
                view = self.env.ref('sh_message.sh_message_wizard')
                view_id = view and view.id or False
                context = dict(self._context or {})
                context['message'] = '已無項目可以收貨了'
                return {
                    'name': 'Success',
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'sh.message.wizard',
                    'views': [(view.id, 'form')],
                    'view_id': view.id,
                    'target': 'new',
                    'context': context,
                }

    def return_cancel(self):
        myid = self.env.context.get('stockin_op_id')
        myrec = self.env['stock.picking'].search([('id','=',myid)])
        myrec.update({'state':'assigned'})


    @api.onchange('origin')
    def stockoutget(self):
        for rec in self:
            myrec = self.env['neweb.project'].search([('sale_no','=',rec.origin)])
            if myrec:
               myprojno = myrec.name
               if myrec.proj_contact_ids[0].contact_name:
                  mycustomer = myrec.proj_contact_ids[0].contact_name
               else:
                  mycustomer = '-'
               if myrec.proj_contact_ids[0].contact_phone:
                  mycustel = myrec.proj_contact_ids[0].contact_phone
               else:
                  mycustel = '-'
               if myrec.proj_cus_ids[0].cus_address:
                  myshipaddr = myrec.proj_cus_ids[0].cus_address
               else:
                  myshipaddr = '-'
               rec.update({'stockout_proj_no':myprojno,'stockout_customer':mycustomer,
                           'stockout_custel':mycustel,'stockout_shipaddr':myshipaddr})




    @api.onchange('stockin_qc')
    def _client_qc_change(self):
        if self.stockin_qc :
            for rec in self.stockin_line:
                if rec.stockin_check == '3' :
                   rec.update({'stockin_check':'2'})
        else:
            for rec in self.stockin_line :
                if rec.stockin_check == '2' :
                   rec.update({'stockin_check':'3'})


    def name_get(self):
        result = []
        isacc =False
        isacc = self.env.context.get('isacc')
        for myrec in self:
            mytext1 = myrec.origin
            if not mytext1:
                mytext1 = "-"
            mytext2 = myrec.name
            if not mytext2:
                mytext2 = "-"
            if isacc==True:
                mypuritem = "%s" % myrec.name
            else:
                mypuritem = "[來源單號:%s][調撥單號:%s]" % (mytext1, mytext2)
            result.append((myrec.id, mypuritem))
        return result


    @api.model
    def create(self, vals):
        if 'stockin_qc' in vals :
            if vals.get('stockin_qc')==True:
               vals['stockin_qc_status']='1'
               if not vals.get('stockin_checkman'):
                   raise UserError("未選取QC 工程師,請確認")
            if vals.get('stockin_qc')==False:
               vals['stockin_qc_status']='3'
        rec = super(newebstockpickinginherit, self).create(vals)
        genprodid = self.env.ref('neweb_project.neweb_product_purchase_1')
        myprodid = genprodid.id
        for myrec in self.stockin_line:
            mystockinid = myrec.stockin_id.id
            self.env.cr.execute("select genpurstockcheck(%s,%s)" % (mystockinid,myprodid))
            self.env.cr.execute("commit")
        self.env.cr.execute("select updatepurchasenum('%s')" % rec.origin)
        self.env.cr.execute("""select check_stockout_origin(%d)""" % rec.id)
        # self.env.cr.execute("""select setstockitem(%d)""" % rec.id)
        return rec


    def write(self, vals):
        if 'stockin_qc' in vals :
            if vals.get('stockin_qc')==True:
               vals['stockin_qc_status']='1'
               if not vals.get('stockin_checkman'):
                   raise UserError("未選取QC 工程師,請確認")
            if vals.get('stockin_qc')==False:
               vals['stockin_qc_status']='3'
        issendmail = self.env.context.get('stockin_sendmail')
        myid = self.env.context.get('stockin_op_id')
        myrec = self.env['neweb.stockin_list'].search([('stockin_id', '=', myid)])
        myrec1 = self.env['stock.picking'].search([('id','=',myid)])
        if issendmail=='Y':
            myrec.write({'stockin_sendemail': True})
        else :
            myrec.write({'stockin_sendemail': False})
        rec = super(newebstockpickinginherit, self).write(vals)
        genprodid = self.env.ref('neweb_project.neweb_product_purchase_1')
        myprodid = genprodid.id
        for myreclist in self.stockin_line:
            mystockinid = myreclist.stockin_id.id
            self.env.cr.execute("select genpurstockcheck(%s,%s)" % (mystockinid, myprodid))
            self.env.cr.execute("commit")
        # print "%s" % myrec1.origin
        self.env.cr.execute("select updatepurchasenum('%s')" % myrec1.origin)
        self.env.cr.execute("""select check_stockout_origin(%d)""" % myrec1.id)
        self.env.cr.execute("""select setstockitem(%d)""" % self.id)
        return rec


    def get_stockin_selectable(self):
        #mystockinrec = self.env['stock.picking'].search([('id', '=', self.env.context.get('stockin_op_id'))])
        mystockinrec = self.env['stock.picking'].search([('id', '=', self.id)])
        mypurchaseno = mystockinrec.origin
        mypurchaseid = self.env['purchase.order'].search([('name', '=', mypurchaseno)])
        self.env.cr.execute("delete from neweb_purselectable")
        self.env.cr.execute("delete from neweb_purselectableline")
        self.env.cr.execute("commit")
        myselectablerec = self.env['neweb.purselectable'].search([])
        myselectablerec.create({'name':mypurchaseno})
        myrec=self.env['neweb.purselectable'].search([('name','=',mypurchaseno)])
        for rec in mypurchaseid.display_line :
            if rec.pitem_num - rec.pitem_stockin_num > 0 :
               myrec.write({'display_line':[(0,0,{'pitem_machine_type':rec.pitem_machine_type,
                                                  'pitem_model_type': rec.pitem_model_type,
                                                  'pitem_prod_no': rec.pitem_prod_no,
                                                  'pitem_spec': rec.pitem_spec ,
                                                  'pitem_num':rec.pitem_num ,
                                                  'pitem_stockin_num':rec.pitem_stockin_num,
                                                  'origin_id':rec.id})]})


        myrecid = self.env['neweb.purselectable'].search([('name','=',mypurchaseno)],limit=1)
        return {'view_name': 'newebstockpickinginherit',
                'name': ('採購明細選單'),
                'views': [[False, 'form'] ],
                'res_model': 'neweb.purselectable',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'current',
                'res_id': myrecid.id,
                'flags': {'action_buttons': False},
                'view_mode': 'form',
                'view_type': 'form',
                'context':{'stockin_op_id':self.id},
                }


    def del_stockship_list(self):
        # myid = self.env.context.get('stockout_op_id')
        myid = self.id
        # 刪除 stockship_line 不連動刪除 stockout_line
        # self.env.cr.execute("""select gendelstockout(%d)""" % myid)
        # self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from neweb_stockship_list where stockship_id=%d""" % myid)
        self.env.cr.execute("""commit""")


    def get_stockout_selectable(self):
        #mystockinrec = self.env['stock.picking'].search([('id', '=', self.env.context.get('stockout_op_id'))])
        mystockinrec = self.env['stock.picking'].search([('id', '=', self.id)])
        myprojno = mystockinrec.stockout_proj_no

        myprojid = self.env['neweb.project'].search([('name', '=', myprojno)])
        self.env.cr.execute("delete from neweb_saleselectable")
        self.env.cr.execute("delete from neweb_saleselectableline")
        self.env.cr.execute("commit")
        myselectablerec = self.env['neweb.saleselectable'].search([])
        myselectablerec.create({'name': myprojno})
        myrec = self.env['neweb.saleselectable'].search([('name', '=', myprojno)])

        for rec in myprojid.saleitem_line:
            if not rec.prod_num:
                myprodnum = 0
            else:
                myprodnum = rec.prod_num
            if not rec.prod_stockoutnum:
                myprodstockoutnum = 0
            else:
                myprodstockoutnum = rec.prod_stockoutnum
            if myprodnum - myprodstockoutnum > 0:
                myrec.write({'display_line': [(0, 0, {'sitem_modeltype': rec.prod_modeltype,
                                                      'sitem_spec': rec.prod_desc,
                                                      'sitem_desc': rec.prod_no,
                                                      'sitem_num': myprodnum,
                                                      'sitem_stockout_num': myprodstockoutnum,
                                                      # 'sitem_prodno': rec.sitem_prodno,
                                                      'origin_id': rec.id,
                                                      'line_item':rec.line_item,})]})

        myrecid = self.env['neweb.saleselectable'].search([('name', '=', myprojno)], limit=1)
        return {'view_name': 'newebstockpickinginherit',
                'name': ('交貨明細選單'),
                'views': [[False, 'form']],
                'res_model': 'neweb.saleselectable',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'current',
                # 'domain': mydomain,
                'res_id': myrecid.id,
                'flags': {'action_buttons': False},
                'view_mode': 'form',
                'view_type': 'form',
                'context':{'stockout_op_id':self.id},
                }

    def get_projsaleitem_serial(self):
        #mypickid = self.env.context.get('stockout_op_id')
        mypickid = self.id
        self.env.cr.execute("""select getprojserial(%d)""" % mypickid)
        self.env.cr.execute("""commit""")
    # 舊邏輯
    # @api.multi
    # def get_stockout_selectable(self):
    #     mystockinrec = self.env['stock.picking'].search([('id', '=', self.env.context.get('stockout_op_id'))])
    #     myprojno = mystockinrec.stockout_proj_no
    #     if not mystockinrec.origin and myprojno:
    #         myrec = self.env['neweb.project'].search([('name','=',myprojno)])
    #         mysaleorderno = myrec[0].sale_no
    #     else:
    #         mysaleorderno = mystockinrec.origin
    #     mysaleid = self.env['sale.order'].search([('name', '=', mysaleorderno)])
    #     self.env.cr.execute("delete from neweb_saleselectable")
    #     self.env.cr.execute("delete from neweb_saleselectableline")
    #     self.env.cr.execute("commit")
    #     myselectablerec = self.env['neweb.saleselectable'].search([])
    #     myselectablerec.create({'name':mysaleorderno})
    #     myrec = self.env['neweb.saleselectable'].search([('name','=',mysaleorderno)])
    #     for rec in mysaleid.display_line:
    #         if rec.sitem_num - rec.sitem_stockout_num > 0:
    #             myrec.write({'display_line': [(0, 0, {'sitem_modeltype': rec.sitem_modeltype,
    #                                                    'sitem_spec': rec.sitem_desc,
    #                                                    'sitem_desc': rec.sitem_desc,
    #                                                    'sitem_num': rec.sitem_num,
    #                                                    'sitem_stockout_num': rec.sitem_stockout_num,
    #                                                    # 'sitem_prodno': rec.sitem_prodno,
    #                                                    'origin_id': rec.id})]})
    #
    #     myrecid = self.env['neweb.saleselectable'].search([('name', '=', mysaleorderno)], limit=1)
    #     return {'view_name': 'newebstockpickinginherit',
    #             'name': (u'交貨明細選單'),
    #             'views': [[False, 'form']],
    #             'res_model': 'neweb.saleselectable',
    #             'context': self._context,
    #             'type': 'ir.actions.act_window',
    #             'target': 'current',
    #             # 'domain': mydomain,
    #             'res_id': myrecid.id,
    #             'flags': {'action_buttons': False},
    #             'view_mode': 'form',
    #             'view_type': 'form'
    #             }



    def get_stockds_selectable(self):
        mystockinrec = self.env['stock.picking'].search([('id', '=', self.env.context.get('stockds_op_id'))])
        mypurchaseno = mystockinrec.origin
        mypurchaseid = self.env['purchase.order'].search([('name', '=', mypurchaseno)])
        self.env.cr.execute("delete from neweb_dsselectable")
        self.env.cr.execute("delete from neweb_dsselectableline")
        myselectablerec = self.env['neweb.dsselectable'].search([])
        # print "%s" % mypurchaseno
        for rec in mypurchaseid.display_line:
            if rec.pitem_num - rec.pitem_stockin_num > 0:
                myselectablerec.create({'name': mypurchaseno,
                                        'display_line': [(0, 0, {'ds_machinetype': rec.pitem_machine_type,
                                                                 'ds_modeltype': rec.pitem_model_type,
                                                                 'ds_prodno': rec.pitem_prod_no,
                                                                 'ds_spec': rec.pitem_spec,
                                                                 'ds_num': rec.pitem_num,
                                                                 'ds_stockin_num': rec.pitem_stockin_num,
                                                                 'origin_id': rec.id})]})

        return {'view_name': 'newebstockpickinginherit',
                'name': ('直運明細選單'),
                'views': [[False, 'form']],
                'res_model': 'neweb.dsselectable',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'new',
                # 'domain': mydomain,
                # 'res_id': myrec.id,
                'flags': {'action_buttons': False},
                'view_mode': 'form',
                'view_type': 'form'
                }


    def get_stockin_email(self, myid):
        myids = self.env['stock.picking'].search([('id', '=', myid)])
        all_mails = []
        for item in myids:
            all_mails.append(item.stockin_checkman.login)
            for line in item.stockin_email:
                if line :
                    all_mails.append(line.work_email)
        # all_mails.append('annie.lee@newebinfo.com.tw')
        return ','.join(str(mail) for mail in all_mails)


    def stockin_sendmail(self):
        # import sys
        # reload(sys)
        # sys.setdefaultencoding('utf-8')
        '''
        This function opens a window to compose an email, with the edi purchase request template message loaded by default
        '''
        # mail_tmp_id = self.env['mail.template'].search([('name', '=', 'Repair-SLA_Warn_template')])
        # # _logger.info("mail tmp id is %s" % mail_tmp_id.id)
        # self.pool['mail.template'].send_mail(self.env.cr, self.env.uid, mail_tmp_id.id, self.id, force_send=True,
        #                                      context=self.env.context)

        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            # template_id = self.env['mail.template'].search([('name', '=', 'email_template_stockin_check1')])
            template_id = ir_model_data.get_object_reference('neweb_stockin', 'email_template_stockin_check1')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        # self.env['mail.template'].browse(template_id).sudo().send_mail(myid)
        # self.env['mail.template'].browse(template_id).sudo().send_mail(self.ids[0])
        self.env['mail.template'].browse(template_id).sudo().send_mail(self.id)
        myrec = self.env['stock.picking'].search([('id','=',self.id)])
        if myrec:
            myrec.update({'last_send_mail': datetime.now()})
        #ctx = dict()
        # ctx = self.env.context.copy()
        # ctx.update({
        #     'default_model': 'stock.picking',
        #     'default_res_id': self.ids[0],
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_composition_mode': 'mass_mail',
        #     # 'bin_raw' : True,
        #     # 'lang' : 'zh_TW',
        #     # 'auto_commit': True,
        #     # 'active_model': self._name,
        #     # 'active_ids':self._ids,
        #     # 'active_id':self._ids[0],
        #     # 'force_send':True,
        #     # 'mail_post_autofollow': True,
        #     # 'mark_so_as_sent': True,
        #     # 'sent_stockin_via_email':True,
        # })

        # return {
        #     'type': 'ir.actions.act_window',
        #     'view_type': 'form',
        #     'view_mode': 'form',
        #     'res_model': 'mail.compose.message',
        #     'views': [(compose_form_id, 'form')],
        #     'view_id': compose_form_id,
        #     'target': 'new',
        #     'context': ctx,
        # }


# class MailComposeMessage(models.TransientModel):
#     _inherit = 'mail.compose.message'
#
#     @api.multi
#     def send_mail(self, auto_commit=False):
#      context = self._context
#      #ctx = self.env.context.copy()
#      if context.get('default_model') == 'stock.picking' and \
#        context.get('default_res_id') and context.get('sent_stockin_via_email'):
#
#           stockin_order = self.env['stock.picking'].browse(context['default_res_id'])
#           #ctx.update({'default_composition_mode': 'mass_mail',})
#           # auto_commit = True
#       # stockin_order.sent_po_via_email = True
#      return super(MailComposeMessage, self).with_context({'default_composition_mode': 'mass_mail'}).send_mail(auto_commit=auto_commit)


