# -*- coding: utf-8 -*-
# Author: Peter Wu


from odoo import models, fields, api,_
from odoo.exceptions import UserError
import datetime




class requiremabackup(models.Model):
    _name = "neweb.ma_backup_type"
    _description = '資產類MA備機基礎配置'

    name = fields.Char(size=50,string="資產類 MA 備機")

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("MA備機類別不能為空值！"))
        if 'name' in vals and vals['name']:
            cname = vals['name']
            nrec = self.env['neweb.ma_backup_type'].search([('name', '=', cname)])
            if nrec:
                raise UserError(("MA備機類別 ％s 已重複") % cname)
        rec = super(requiremabackup, self).create(vals)
        return rec

class requiremaparts(models.Model):
    _name = "neweb.ma_parts_type"
    _description = '費用類MA零件基礎配置'

    name = fields.Char(size=50, string="費用類 MA 零件")

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("MA零件類別不能為空值！"))
        if 'name' in vals and vals['name']:
            cname = vals['name']
            nrec = self.env['neweb.ma_parts_type'].search([('name', '=', cname)])
            if nrec:
                raise UserError(("MA零件類別 ％s 已重複") % cname)
        rec = super(requiremaparts, self).create(vals)
        return rec


class requiregencode(models.Model):
    _name = "neweb.requiregencode"
    _description = '申購單號流水號記錄'

    name = fields.Char(size=6, string="民國年月日", required=True)
    gencode = fields.Integer(string="流水號")


class newebrequirepurchaseitem(models.Model):
    _name = "neweb.require_purchase_item"
    _order = "pitem_nid,id"
    _description = '申購單明細記錄'

    @api.depends('pitem_num', 'pitem_price')
    def _amount_budget(self):
        for require_purchase in self:
            totamount = 0
            totamount += (require_purchase.pitem_num * require_purchase.pitem_price)
            require_purchase.update({'pitem_budget': round(totamount), })

    @api.depends('pitem_pay')
    def _get_pitem_pay(self):
        for rec in self:
            if rec.pitem_pay == False:
                mycpitempay = '否'
            else:
                mycpitempay = '是'
            rec.cpitempay = mycpitempay
            return mycpitempay

    cpitempay = fields.Char(string="請款py3o", compute=_get_pitem_pay)
    pitem_seq = fields.Integer(string="項次")
    pitem_id = fields.Many2one('neweb.require_purchase',required=True, ondelete='cascade')
    pitem_nid = fields.Integer(size=2, string="項次", default=10)
    pitem_modeltype = fields.Char(string="機種-機型/料號")
    prod_id = fields.Many2one('product.template', string="庫存料號")
    pitem_serial = fields.Char(string="序號")
    pitem_no = fields.Char(string="料號")
    pitem_desc = fields.Text(string="規格說明")
    pitem_num = fields.Float(digits=(10,0), string="數量", default=1)
    pitem_purnum = fields.Float(digits=(10,0), string="已採購量", default=0)
    pitem_price = fields.Float(digits=(13,0), string="單價")
    supplier = fields.Many2one('res.partner', string="廠商")
    pitem_budget = fields.Float(digits=(13,0), string="預算", store=True,compute=_amount_budget)
    expense_custom = fields.Many2one('res.partner', string="更換客戶名稱")
    pitem_pay = fields.Boolean(string=u"請款", default=False)
    purchase_no = fields.Char(size=15, string="採購單號")
    require_no = fields.Char(related='pitem_id.name',string="申購單號")
    purok = fields.Boolean(string="已採購否?")
    pur_memo = fields.Text(string="申購備註")



    @api.onchange('prod_id')
    def onchangeprodid(self):
        self.pitem_modeltype = self.prod_id.name

    @api.onchange('pitem_modeltype')
    def onchange_client(self):
        self.env.cr.execute("select getcontractcus()")
        mylist = self.env.cr.fetchall()
        myids = self.env['res.partner'].search([('id','in',mylist)])
        ids = []
        for item in myids:
            ids.append(item.id)
        res={}
        res['domain']={'expense_custom':[('id','in',ids)]}
        return res




    def name_get(self):
        result = []
        for myrec in self:
            mytext1 = myrec.pitem_modeltype
            if not mytext1:
                mytext1 = "-"
            mytext2 = myrec.pitem_serial
            if not mytext2:
                mytext2 = "-"
            mytext3 = myrec.pitem_no
            if not mytext3:
                mytext3 = "-"
            mytext4 = myrec.pitem_desc
            if not mytext4:
                mytext4="-"
            mytext5 = myrec.pitem_num
            if not mytext5:
                mytext5 = "1"
            else :
                mytext5 = str(myrec.pitem_num)
            mytext6 = myrec.supplier.name
            if not mytext6:
                mytext6="-"
            else:
                mytext6 = myrec.supplier.name[:4]
            mytext7 = myrec.pitem_purnum
            if not mytext7:
                mytext7="0"

            myreqitem = u"[單號:%s][機種:%s][序號:%s][料號:%s][規格:%s][廠商:%s][數量:%s][已採購量:%s]" % (myrec.require_no,mytext1, mytext2, mytext3,mytext4,mytext6,mytext5,mytext7)
            result.append((myrec.id, myreqitem))
        return result


class newebrequirepurchase(models.Model):
    _name = "neweb.require_purchase"
    _order = "state asc,name desc"
    _description = "申購單"

    @api.onchange('emp_name')
    def onchangeempname(self):
        self.department_no = self.emp_name.employee_ids[0].department_id.id

    @api.depends('emp_name')
    def _get_department(self):
        for rec in self:
            if rec.emp_name.employee_ids:
                mydept = False
                for rec1 in rec.emp_name.employee_ids:
                    mydept = rec1.department_id.id
                rec.department_no = mydept
                rec.update({'department_no': mydept})
                return mydept


    @api.depends('require_line.pitem_num', 'require_line.pitem_price')
    def _amount_all(self):
        for require in self:
            totamount = 0
            for line in require.require_line:
                totamount += (line.pitem_num * line.pitem_price)
            require.update({
                'tot_pitem_sum': totamount,
            })

    @api.depends('asset_expense_categ')
    def _get_asset(self):
        for rec in self:
            if rec.asset_expense_categ=='1':
                rec.asset_type1=True
            else:
                rec.asset_type1=False

    @api.depends('asset_expense_categ')
    def _get_expense(self):
        for rec in self:
            if rec.asset_expense_categ == '2':
                rec.expense_type1 = True
            else:
                rec.expense_type1 = False

    name = fields.Char(size=12, string="申購單編號")
    emp_name = fields.Many2one('res.users', string=u"申請人", require=True, default=lambda self: self.env.uid)
    ext_no = fields.Char(size=10, string=u"分機")
    department_no = fields.Many2one("hr.department", string="部門代號",default=lambda self:self._get_department)
    asset_expense_categ = fields.Selection([('1','資產類'),('2','費用類')],string="申購類別",default='1')
    asset_type = fields.Selection([('1', '辦公器材'), ('2', '研發/測試設備'), ('3', 'MA備機'), ('4', '未來轉銷貨'), ('5', '其他')],string=u"資產類")
    asset_machine_type = fields.Many2many('neweb.ma_backup_type',string="MA備機類別")
    asset_custom = fields.Many2one('res.partner', string="客戶名稱")
    asset_desc = fields.Text(string="說明")
    expense_type = fields.Selection([('1', 'MA零件'), ('2', '其他')], string="費用類")
    expense_machine_type = fields.Many2many('neweb.ma_parts_type',string="MA零件類別")
    expense_desc = fields.Text(string="說明")
    catalog_attach_yn = fields.Selection([('1', '是'), ('2', '否')], string="請購型錄或廠商報價:")
    catalog_attach = fields.Many2many('ir.attachment', string="專案附件")
    require_desc = fields.Text(string="申購內容說明")
    pay_type = fields.Char(size=20, string="付款方式")
    require_line = fields.One2many('neweb.require_purchase_item', 'pitem_id', copy=True, string="專案相關地址")
    tot_pitem_sum = fields.Float(digits=(13, 0), string="預估總金額", compute=_amount_all)
    state = fields.Selection([('1', '新單'), ('2', '採購'), ('3', '結案')], string="狀態", default='1')
    purchase_yn = fields.Boolean(string="是否已採購",default=False)
    is_signed = fields.Boolean(string="是否授信",default=False)
    asset_type1 = fields.Boolean('ASSET TYPE',compute=_get_asset)
    expense_type1 = fields.Boolean('EXPENSE TYPE',compute=_get_expense)



    ### WKF SEND MAIL PROCEDURE
    ###   type='1' 所有簽核人員    type='2' 送件者
    ###


    # @api.model
    def get_approve_emails(self):
        self.env.cr.execute("select wkfsendmail('%s',%d,'%s')" % (self.name,self.id,'1'))
        mylist = self.env.cr.fetchall()
        myids = self.env['res.users'].search([('id','in',mylist)])
        all_mails = []
        for item in myids:
            all_mails.append(item.employee_ids.work_email)
        return ','.join(str(mail) for mail in all_mails)

    # @api.model
    def get_reject_emails(self):
        self.env.cr.execute("select wkfsendmail('%s',%d,'%s')" % (self.name, self.id, '2'))
        mylist = self.env.cr.fetchall()
        myids = self.env['res.users'].search([('id', 'in', mylist)])
        all_mails = []
        for item in myids:
            all_mails.append(item.employee_ids.work_email)
        return ','.join(str(mail) for mail in all_mails)


    def send_approve_mail(self):
        myrec = self.env['neweb.require_purchase'].search([('id', '=', self.id)])
        myid = myrec.id
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_purchase', 'mail_template_rfq_wkf_approve')[1]
        except ValueError:
            template_id = False
        # ctx = self.env.context.copy()
        # ctx.update({
        #     'default_model': 'neweb.require_purchase',
        #     'default_res_id': self.ids[0],
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_composition_mode': 'comment',
        #     'mark_so_as_sent': True,
        #     'mail_post_autofollow': True,
        #     'custom_layout': "neweb_purchase.mail_template_rfq_wkf_approve"
        # })
        self.env['mail.template'].browse(template_id).send_mail(myid)
        # template_id = ir_model_data.get_object_reference('neweb_purchase', 'mail_template_rfq_wkf_approve')[1]
        # self.pool['mail.template'].send_mail(self.env.cr, self.env.uid, template_id, self.id, force_send=True,context=self.with_context(ctx))


    def send_reject_mail(self):
        myrec = self.env['neweb.require_purchase'].search([('id', '=', self.id)])
        myid = myrec.id
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_purchase', 'mail_template_rfq_wkf_reject')[1]
        except ValueError:
            template_id = False
        # ctx = self.env.context.copy()
        # ctx.update({
        #     'default_model': 'neweb.require_purchase',
        #     'default_res_id': self.ids[0],
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_composition_mode': 'comment',
        #     'mark_so_as_sent': True,
        #     'mail_post_autofollow': True,
        #     'custom_layout': "neweb_purchase.mail_template_rfq_wkf_reject"
        # })
        self.env['mail.template'].browse(template_id).send_mail(myid)
        #template_id = ir_model_data.get_object_reference('neweb_purchase', 'mail_template_rfq_wkf_reject')[1]
        #myrec.write({'state': 'sent'})
        #self.pool['mail.template'].send_mail(self.env.cr, self.env.uid, template_id, self.id, force_send=True,context=self.with_context(ctx))



    # def set_signed(self):
    #     myrec = self.env['neweb_purchase.require_purchase'].search([('id','=',self.id)])
    # 	for rec in myrec:
    # 		rec.update({'is_signed':True})
    #     myrec.send_approve_mail()

    is_closed = fields.Boolean(string="是否結案",default=False)


    def set_closed(self):
        for rec in self:
            rec.update({'is_closed':True,'state':'3'})

    def set_reject(self):
        myrec = self.env['neweb_purchase.require_purchase'].search([('id','=',self.id)])
        for rec in self:
            rec.update({'is_closed':False , 'is_signed':False,'state':'1'})
        myrec.send_reject_mail()



    @api.model
    def create(self, vals):
        mynow = datetime.datetime.now()
        myyy = str(mynow.year - 1911)
        myyear = myyy[1:]
        mymm = str(mynow.month)
        mydd = str(mynow.day)
        mymonth = mymm.zfill(2)
        myday = mydd.zfill(2)
        myym = myyear + mymonth + myday
        gencode_rec = self.env['neweb.requiregencode'].search([('name', '=', myym)])
        if gencode_rec:
            strcode = str(gencode_rec.gencode + 1)
            mycode = strcode.zfill(2)
            myrequire_no = "SVC%s%s" % (myym, mycode)
            gencode_rec.gencode += 1
        else:
            myrequire_no = "SVC%s01" % myym
            gencode_rec.create({'name': myym, 'gencode': 1})
        vals['name'] = myrequire_no
        rec = super(newebrequirepurchase, self).create(vals)
        self.env.cr.execute("""select genpitemseq(%d)""" % rec.id)
        self.env.cr.execute("""commit""")

        return rec

    def write(self, vals):

        res = super(newebrequirepurchase, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select genpitemseq(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res

    # def unlink(self):
    #     self.env.cr.execute("select wkfisstart(%d)" % int(self.x_wkf_state))
    #     isstart = self.env.cr.fetchone()
    #     if not isstart[0]:
    #         raise UserError("表單已送簽核,不能刪除")
    #     res = super(newebrequirepurchase,self).unlink()
    #     return res