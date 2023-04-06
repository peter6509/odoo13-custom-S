# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.tools.misc import formatLang, get_lang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare


class newebinvoiceopen(models.Model):
    _name = 'neweb_invoice.invoiceopen'
    _description = "發票開立申請"

    @api.depends('project_no')
    def _get_projno(self):
        for rec in self:
            if rec.project_no == False:
                rec.projectno = ' '
            else:
                rec.projectno = rec.project_no.name

    @api.depends('project_no')
    def _get_amounttot(self):
        for rec in self:
            myid = rec.id
            if myid:
                self.env.cr.execute("""select getsalediscountamount(%s)""" % myid)
                myamounttot = self.env.cr.fetchone()[0]
                rec.project_amount_total = myamounttot
        # myid = self.id
        # if myid :
        #     self.env.cr.execute("""select getsalediscountamount(%d)""" % self.id)
        #     myamounttot = self.env.cr.fetchone()[0]
        #
        # else:
        #     myamounttot = 0
        # self.project_amount_total = myamounttot
        # return myamounttot

        # myamounttot = 0
        # for mainrec in self:
        #     for rec in mainrec.invoice_open_lines:
        #         myamounttot = myamounttot + round(rec.invoice_tax_amount1)
        #     mainrec.project_amount_total = myamounttot
        #     return myamounttot


    @api.depends('invoice_open_lines.invoice_untax_amount')
    def _get_amountuntot(self):
        myamounttot = 0
        for mainrec in self:
            for rec in mainrec.invoice_open_lines:
                myamounttot = myamounttot + round(rec.invoice_untax_amount)
            mainrec.update({'project_untax_amount': myamounttot})

    @api.depends('invoice_open_lines.invoice_costtype', 'invoice_open_lines.invoice_untax_amount')
    def _get_revenue1(self):
        myrevenue1 = 0
        for rec in self.invoice_open_lines:
            # print "%d" % rec.invoice_costtype.id
            # print "%d" % rec.invoice_untax_amount
            if rec.invoice_costtype.id == 1:
                myrevenue1 = myrevenue1 + round(rec.invoice_untax_amount)
        # print "%d" % myrevenue1
        self.revenue_1 = myrevenue1

    @api.depends('invoice_open_lines.invoice_costtype', 'invoice_open_lines.invoice_untax_amount')
    def _get_revenue2(self):
        myrevenue2 = 0
        for rec in self.invoice_open_lines:
            if rec.invoice_costtype.id == 2:
                myrevenue2 = myrevenue2 + round(rec.invoice_untax_amount)
        self.revenue_2 = myrevenue2

    @api.depends('invoice_open_lines.invoice_costtype', 'invoice_open_lines.invoice_untax_amount')
    def _get_revenue3(self):
        myrevenue3 = 0
        for rec in self.invoice_open_lines:
            if rec.invoice_costtype.id == 3:
                myrevenue3 = myrevenue3 + round(rec.invoice_untax_amount)
        self.revenue_3 = myrevenue3

    @api.depends('invoice_open_lines.invoice_costtype', 'invoice_open_lines.invoice_untax_amount')
    def _get_revenue4(self):
        myrevenue4 = 0
        for rec in self.invoice_open_lines:
            if rec.invoice_costtype.id == 4 or rec.invoice_costtype.id == 9:
                myrevenue4 = myrevenue4 + round(rec.invoice_untax_amount)
        self.revenue_4 = myrevenue4

    @api.depends('invoice_open_lines.invoice_costtype', 'invoice_open_lines.invoice_untax_amount')
    def _get_revenue5(self):
        myrevenue5 = 0
        for rec in self.invoice_open_lines:
            if rec.invoice_costtype.id == 5:
                myrevenue5 = myrevenue5 + round(rec.invoice_untax_amount)
        self.revenue_5 = myrevenue5

    @api.depends('invoice_open_lines.invoice_costtype', 'invoice_open_lines.invoice_untax_amount')
    def _get_revenue6(self):
        myrevenue6 = 0
        for rec in self.invoice_open_lines:
            if rec.invoice_costtype.id == 6:
                myrevenue6 = myrevenue6 + round(rec.invoice_untax_amount)
        self.revenue_6 = myrevenue6

    @api.depends('invoice_open_lines.invoice_costtype', 'invoice_open_lines.invoice_untax_amount')
    def _get_revenue7(self):
        myrevenue7 = 0
        for rec in self.invoice_open_lines:
            if rec.invoice_costtype.id == 7:
                myrevenue7 = myrevenue7 + rec.invoice_untax_amount
        self.revenue_7 = round(myrevenue7)

    @api.depends('invoice_open_lines.invoice_costtype', 'invoice_open_lines.invoice_untax_amount')
    def _get_revenue8(self):
        myrevenue8 = 0
        for rec in self.invoice_open_lines:
            if rec.invoice_costtype.id == 8:
                myrevenue8 = myrevenue8 + round(rec.invoice_untax_amount)
        self.revenue_8 = myrevenue8

    @api.depends('invoice_open_lines.invoice_tax_amount1','invoice_open_lines.invoice_date')
    def _get_openamount(self):
        for myrec in self:
            myamounttot = 0

            self.env.cr.execute("""select getlastinvdate(%d)""" % myrec.id)
            myinvdate = self.env.cr.fetchone()[0]
            for myrec1 in myrec.invoice_open_lines:
                if (myrec1.invoice_state == '2' or myrec1.invoice_state=='3') and myrec1.invoice_date==myinvdate:
                    # myamounttot = myamounttot + myrec1.invoice_untax_amount + myrec1.invoice_tax
                    myamounttot = myamounttot + round(myrec1.invoice_tax_amount)
            # myrec.open_amount_total=int(myamounttot)
            myrec.update({'open_amount_total':myamounttot})
            return myamounttot

    @api.depends('invoice_open_lines.invoice_tax_amount1')
    def _get_completeamount(self):
        for myrec in self:
            myamounttot=0
            for myrec1 in myrec.invoice_open_lines:
                if myrec1.invoice_state == '2' or myrec1.invoice_state=='3' :
                    # myamounttot = myamounttot + myrec1.invoice_untax_amount + myrec1.invoice_tax
                    myamounttot = myamounttot + round(myrec1.invoice_tax_amount)
            # myrec.open_complete_total=int(myamounttot)
            myrec.update({'open_complete_total':myamounttot})
            return myamounttot


    @api.depends('project_amount_total','open_complete_total')
    def _get_completed(self):
        for rec in self:
            if abs(rec.project_amount_total - rec.open_complete_total) <= 5 or rec.project_amount_total==0 :
                iscompleted = True
                rec.update({'is_completed':True})
            else:
                iscompleted = False
                rec.update({'is_completed':False})
            return iscompleted


    @api.depends('invoice_open_lines')
    def _get_invoicever(self):
        for rec in self:
            myver=0
            for rec1 in rec.invoice_open_lines:
                if not rec1.invoice_ver:
                    myver=0
                else:
                    myver = rec1.invoice_ver
            rec.invoice_ver=myver
            return myver

    application_date = fields.Date(string="申請日期")
    project_no = fields.Many2one('neweb.project', string="專案編號", index=True)
    project_name = fields.Text(string='申案名稱')
    contract_no = fields.Many2one('neweb_contract.contract', string="合約編號")
    contract_main_start = fields.Date(string="維護啟始日")
    contract_main_end = fields.Date(string="維護截止日")
    invoice_title = fields.Text(string='發票抬頭')
    payment_type = fields.Selection(
        [('1', '一次付清'), ('2', '月初'), ('3', '月末'), ('4', '雙月初'), ('5', '雙月末'), ('6', '季初'),
         ('7', '季末'), ('8', '半年初'), ('9', '半年末'), ('10', '年初'), ('11', '年末'),
         ('12', '分期付款'),('13','其他')], string="付款方式", default='1')
    payment_memo = fields.Text(string="備註")
    sno = fields.Char(string="統一編號")
    #project_amount_total = fields.Float(digits=(12, 0), string="合計金額(含税)")
    project_amount_total = fields.Float(digits=(12, 0), string="合計金額(含税)",store=True, compute=_get_amounttot,track_visibility="always")
    project_untax_amount = fields.Float(digits=(12, 0), string="合計金額(未税)",store=True,compute=_get_amountuntot,track_visibility="always")
    open_complete_total = fields.Float(digits=(12, 0), string="已開金額(含税)")
    # open_complete_total = fields.Float(digits=(12, 0), string="已開金額(含税)", compute=_get_completeamount, store=True,track_visibility="onchange")
    open_amount_total = fields.Float(digits=(12, 0), string="本次金額(含税)")
    # open_amount_total = fields.Float(digits=(12, 0), string="本次金額(含税)", compute=_get_openamount, store=True,track_visibility="onchange")
    revenue_1 = fields.Float(digits=(9, 0), string="銷貨收入(未税)", default=0,store=True,compute=_get_revenue1,track_visibility="onchange")
    revenue_2 = fields.Float(digits=(9, 0), string="專案收入(未税)", default=0,store=True,compute=_get_revenue2,track_visibility="onchange")
    revenue_3 = fields.Float(digits=(9, 0), string="建置收入(未税)", default=0,store=True,compute=_get_revenue3,track_visibility="onchange")
    revenue_4 = fields.Float(digits=(9, 0), string="維護收入(未税)", default=0,store=True,compute=_get_revenue4,track_visibility="onchange")
    revenue_5 = fields.Float(digits=(9, 0), string="維護人力收入(未税)", default=0,store=True,compute=_get_revenue5,track_visibility="onchange")
    revenue_6 = fields.Float(digits=(9, 0), string="利息收入(未税)", default=0,store=True,compute=_get_revenue6,track_visibility="onchange")
    revenue_7 = fields.Float(digits=(9, 0), string="租賃收入(未税)", default=0,store=True,compute=_get_revenue7,track_visibility="onchange")
    revenue_8 = fields.Float(digits=(9, 0), string="其他收入(未税)", default=0,store=True,compute=_get_revenue8,track_visibility="onchange")
    invoice_open_lines = fields.One2many('neweb_invoice.invoiceopen_line', 'invoice_id', string="發票開立",track_visibility="onchange")
    delivery_type = fields.Selection([('1', '郵寄'), ('2', '業務派送')], default='1', string="寄送方式")
    invoice_contact = fields.Char(string="收件人")
    invoice_phone = fields.Char(string="電話")
    invoice_address = fields.Text(string="收件地址")
    invoice_return_envelope = fields.Selection([('1', '需附回郵'), ('2', '不需附回郵')], default='1', string="回郵註記")
    other_memo = fields.Text(string="其他備註")
    name = fields.Char(string="發票開立序號", default='New')  ## INV年月日流水號
    have_inherit = fields.Boolean(string="有展單?", default=False)
    is_completed = fields.Boolean(string="結案")
    invoice_ver = fields.Integer(string="最後版次",compute=_get_invoicever,track_visibility="onchange")
    is_signed = fields.Boolean(string="是否授權", default=False)
    cus_name = fields.Many2one('res.partner',string="專案客戶")
    main_cus_name = fields.Many2one('res.partner',string="終端客戶")
    tax_type = fields.Selection([('1', '未税金額'), ('2', '含稅金額')])
    projectno = fields.Char(string="專案編號", store=True, compute=_get_projno)

    def format_amount(env, amount, currency, lang_code=False):
        fmt = "%.{0}f".format(currency.decimal_places)
        lang = get_lang(env, lang_code)

        formatted_amount = lang.format(fmt, currency.round(amount), grouping=True, monetary=True) \
            .replace(r' ', u'\N{NO-BREAK SPACE}').replace(r'-', u'-\N{ZERO WIDTH NO-BREAK SPACE}')

        pre = post = u''
        if currency.position == 'before':
            pre = u'{symbol}\N{NO-BREAK SPACE}'.format(symbol=currency.symbol or '')
        else:
            post = u'\N{NO-BREAK SPACE}{symbol}'.format(symbol=currency.symbol or '')

        return u'{pre}{0}{post}'.format(formatted_amount, pre=pre, post=post)

    def getsaletot(self):
        self.env.cr.execute("""select geninvprojamount(%d)""" % self.id)
        self.env.cr.execute("""commit""")
        # self.project_amount_total = self.env.cr.fetchone()[0]

    def run_delinvoiceopenline(self):
        # myid = self.env.context.get('invoiceopen_id')
        myid = self.id
        self.env.cr.execute("""delete from neweb_invoice_invoiceopen_line where invoice_id=%d""" % myid)
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select calinvoiceamount(%d)""" % myid)
        self.env.cr.execute("""commit""")

        return {'view_name': 'invoiceopencopywizard',
                'name': ('開立發票複製作業'),
                'views': [[False, 'form'], [False, 'tree'], ],
                'res_model': 'neweb_invoice.invoiceopen',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'self',
                # 'domain': mydomain,
                'res_id': myid,
                'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }


    def invoiceopen_copy(self):
        default = {}
        invoice_copy = super(newebinvoiceopen, self).copy(default=default)

        return {'view_name': 'invoiceopencopywizard',
                'name': ('開立發票複製作業'),
                'views': [[False, 'form'], [False, 'tree'], ],
                'res_model': 'neweb_invoice.invoiceopen',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'self',
                # 'domain': mydomain,
                'res_id': invoice_copy.id,
                'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }


    def calinvoiceamount(self):
        invoiceid = self.env.context.get("invoiceid")
        self.env.cr.execute("""select calinvoiceamount(%d)""" % invoiceid)
        return {'view_name': 'newebinvoiceopen',
                'name': ('發票開立重新計算'),
                'views': [[False, 'form'], ],
                'res_model': 'neweb_invoice.invoiceopen',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                # 'domain': mydomain,
                'res_id': invoiceid,
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                'view_mode': 'form',
                'view_type': 'form'
                }


    def neweb_invoiceopen_copy(self):
        default = {}
        # myprojid = self.env.context.get('proj_op_id')
        myinvoiceopen = self.env['neweb_invoice.invoiceopen'].search(
            [('id', '=', self.env.context.get('invoiceopen_id'))])
        myinvoiceopen.write({'is_completed': True})
        default['invoice_ver'] = myinvoiceopen.invoice_ver + 1
        myinvoiceno = myinvoiceopen.name
        if myinvoiceopen.have_inherit:
            default['name'] = myinvoiceno[:-1] + str(default['invoice_ver'])
        else:
            default['name'] = myinvoiceno + '_1'
        default['open_amount_total'] = 0
        default['is_completed'] = False
        invoiceopen_copy = super(newebinvoiceopen, self).copy(default=default)
        myinvoiceopen.write({'have_inherit': True})
        return {'view_name': 'newebinvoiceopen',
                'name': ('發票開立作業'),
                'views': [[False, 'form'], [False, 'tree'], ],
                'res_model': 'neweb_invoice.invoiceopen',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                # 'domain': mydomain,
                'res_id': invoiceopen_copy.id,
                'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }


    def set_signed(self):
        myrec = self.env['neweb_invoice.invoiceopen'].search([('id', '=', self.id)])
        for rec in self:
            rec.update({'is_signed': True})
        # self.env.cr.execute("select update_invoice_record(%d)" % self.id)
        # self.env.cr.execute("select cal_invoice_complete(%d)" % self.id)
        myrec.send_approve_mail()

    is_closed = fields.Boolean(string="是否結案", default=False)


    def set_closed(self):
        for rec in self:
            rec.update({'is_closed': True})
        self.env.cr.execute("select set_invoice_complete(%d)" % self.id)


    def set_reject(self):
        myrec = self.env['neweb_invoice.invoiceopen'].search([('id', '=', self.id)])
        for rec in self:
            rec.update({'is_closed': False, 'is_signed': False})
        myrec.send_reject_mail()

    ### WKF SEND MAIL PROCEDURE
    ###   type='1' 所有簽核人員    type='2' 送件者
    ###


    def get_approve_emails(self):
        self.env.cr.execute("select wkfsendmail('%s',%d,'%s')" % (self.name, self.id, '1'))
        mylist = self.env.cr.fetchall()
        myids = self.env['res.users'].search([('id', 'in', mylist)])
        all_mails = []
        for item in myids:
            all_mails.append(item.employee_ids.work_email)
        return ','.join(str(mail) for mail in all_mails)


    def get_reject_emails(self):
        self.env.cr.execute("select wkfsendmail('%s',%d,'%s')" % (self.name, self.id, '2'))
        mylist = self.env.cr.fetchall()
        myids = self.env['res.users'].search([('id', 'in', mylist)])
        all_mails = []
        for item in myids:
            all_mails.append(item.employee_ids.work_email)
        return ','.join(str(mail) for mail in all_mails)


    def send_approve_mail(self):
        myrec = self.env['neweb_invoice.invoiceopen'].search([('id', '=', self.id)])
        myid = myrec.id
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_invoice', 'mail_neweb_invoiceopen_wkf_approve')[1]
        except ValueError:
            template_id = False
        # ctx = self.env.context.copy()
        # ctx.update({
        #     'default_model': 'neweb_invoice.invoiceopen',
        #     'default_res_id': self.ids[0],
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_composition_mode': 'comment',
        #     'mark_so_as_sent': True,
        #     'mail_post_autofollow': True,
        #     'custom_layout': "neweb_invoice.mail_neweb_invoiceopen_wkf_approve"
        #     })
        self.env['mail.template'].browse(template_id).send_mail(myid)
        # template_id = ir_model_data.get_object_reference('neweb_invoice', 'mail_neweb_invoiceopen_wkf_approve')[1]
        # self.pool['mail.template'].send_mail(self.env.cr, self.env.uid, template_id, self.id, force_send=True,
        #                                          context=self.with_context(ctx))


    def send_reject_mail(self):
        myrec = self.env['neweb_invoice.invoiceopen'].search([('id', '=', self.id)])
        myid = myrec.id
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('neweb_invoice', 'mail_neweb_invoiceopen_wkf_reject')[1]
        except ValueError:
            template_id = False
        # ctx = self.env.context.copy()
        # ctx.update({
        #     'default_model': 'neweb_invoice.invoiceopen',
        #     'default_res_id': self.ids[0],
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_composition_mode': 'comment',
        #     'mark_so_as_sent': True,
        #     'mail_post_autofollow': True,
        #     'custom_layout': "neweb_invoice.mail_neweb_invoiceopen_wkf_reject"
        #     })
        self.env['mail.template'].browse(template_id).send_mail(myid)
        # template_id = ir_model_data.get_object_reference('neweb_invoice', 'mail_neweb_invoiceopen_wkf_reject')[1]
        # myrec.write({'state': 'sent'})
        # self.pool['mail.template'].send_mail(self.env.cr, self.env.uid, template_id, self.id, force_send=True,
        #                                         context=self.with_context(ctx))


    def name_get(self):
        result = []
        for myrec in self:
            myinvoiceitem = "(%s) => 合計金額 NT$:%s / 已開金額 NT$:%s" % (
            myrec.invoice_title, int(round(myrec.project_amount_total,0)), int(round(myrec.open_complete_total,0)))
            result.append((myrec.id, myinvoiceitem))
        return result



    @api.model
    def create(self, vals):
        if 'project_name' in vals and not vals['project_name']:
            raise UserError("申案名稱不能空值,請確認....")
        # if 'sno' in vals and not vals['sno']:
        #     raise UserError("統編空白,請確認...")
        if 'invoice_title' in vals and not vals['invoice_title']:
            raise UserError("發票抬頭空白,請確認....")

        vals['name'] = self.env['ir.sequence'].next_by_code('neweb_invoice.invoiceopen')
        rec = super(newebinvoiceopen, self).create(vals)

        # self.env.cr.execute("select update_invoice_record(%d)" % rec.id)
        # self.env.cr.execute("""select calinvoiceamount(%d)""" % rec.id)
        return rec


    def write(self, vals):
        if 'project_name' in vals and not vals['project_name']:
            raise UserError("申案名稱不能空值,請確認....")
        if 'sno' in vals and not vals['sno']:
            raise UserError("統編空白,請確認...")
        if 'invoice_title' in vals and not vals['invoice_title']:
            raise UserError("發票抬頭空白,請確認....")
        res = super(newebinvoiceopen, self).write(vals)
        for rec in self:
            if rec.have_inherit == True:
                raise UserError("已有餘額開立,不能異動")
            self.env.cr.execute("select gentaxprice1(%d)" % rec.id)
            self.env.cr.execute("""commit""")
            myid = rec.id
            # self.env.cr.execute("select check_invoice_amount(%d)" % self.id)
            # invstatus = self.env.cr.fetchone()
            # if not invstatus[0] :
            #     raise UserError("累計開立金額已超出專案總金額,請確認！")
            self.env.cr.execute("select update_warrantydate(%d)" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select setinvoicesales(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select geninvprojamount(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            return res


    def unlink(self):
        if self.open_amount_total > 0:
            raise UserError("已有開立發票明細資料了,不能刪除資料了")
        myprojectno = self.project_no.name
        myrec = self.env['neweb.project'].search([('name', '=', myprojectno)])
        if myrec:
            myrec.write({'invoice_mark': False,'invoice_complete':False})
        # self.env.cr.execute("select wkfisstart(%d)" % int(self.x_wkf_state))
        # isstart = self.env.cr.fetchone()
        # if not isstart[0]:
        #     raise UserError("表單已送簽核,不能刪除")
        return super(newebinvoiceopen, self).unlink()

    # @api.multi
    # def name_get(self):
    #     result = []
    #     for myrec in self:
    #         myinvoicename = "%s - %s (%s)" % (myrec.project_no,myrec.contract_no,myrec.invoice_title)
    #         result.append((myrec.id, myinvoicename))
    #     return result


class newebinvoiceopenline(models.Model):
    _name = "neweb_invoice.invoiceopen_line"
    _description = '發票開立申請明細檔'

    @api.depends('invoice_num', 'invoice_unit_price', 'invoice_unit_price1')
    def _get_untaxamount(self):
        for rec in self:
            rec.invoice_untax_amount = rec.invoice_num * rec.invoice_unit_price
        # for rec in self:
        #     if rec.invoice_unit_price1 > 0:  # 含稅單價
        #         myuntax_price = round(rec.invoice_unit_price1 / 1.05, 2)
        #         myamount = rec.invoice_num * myuntax_price
        #         rec.update({'invoice_unit_price': myuntax_price, 'invoice_untax_amount': myamount})
        #     else:
        #         myamount = rec.invoice_num * rec.invoice_unit_price
        #         rec.update({'invoice_untax_amount': myamount})

    @api.depends('invoicetype', 'invoice_num', 'invoice_unit_price', 'invoice_unit_price1')
    def _get_tax(self):
        for rec in self:
            if rec.invoicetype == '2':
                myamount = rec.invoice_num * rec.invoice_unit_price
                mytax = (myamount * 0.05)
            elif rec.invoicetype == '1':
                if rec.invoice_unit_price1 > 0:
                    myamount = rec.invoice_num * rec.invoice_unit_price1
                    myuntaxamount = (myamount / 1.05)
                    mytax = myamount - myuntaxamount
                else:
                    myamount = rec.invoice_num * rec.invoice_unit_price
                    mytax= (myamount * 0.05)
                    # mytax = myamount - myuntaxamount

            else:
                mytax = 0

            rec.update({'invoice_tax': mytax})

    @api.depends( 'invoice_num', 'invoice_unit_price1')
    def _get_taxamount(self):
        for rec in self:
            # mytaxamount = round((rec.invoice_num * rec.invoice_unit_price) * 1.05 ,0)
            mytaxamount = (rec.invoice_num * rec.invoice_unit_price1)
            rec.update({'invoice_tax_amount': mytaxamount})
            return mytaxamount



    @api.depends('invoice_num', 'invoice_unit_price')
    def _get_invoiceamount(self):
        for myrec in self:
            myinvoiceamount = myrec.invoice_num * myrec.invoice_unit_price
            myrec.update({'invoice_untax_amount': myinvoiceamount})
            return myinvoiceamount

    @api.depends('invoice_unit_price')
    def _get_unitnprice(self):
        for rec in self:
            myunitnprice = round(rec.invoice_unit_price)
            rec.invoice_unit_nprice = myunitnprice
            return myunitnprice

    @api.depends('invoice_unit_price1')
    def _get_unitnprice1(self):
        for rec in self:
            myunitnprice1 = round(rec.invoice_unit_price1)
            rec.invoice_unit_nprice1 = myunitnprice1
            return myunitnprice1

    @api.depends('invoice_untax_amount')
    def _get_untaxamount1(self):
        for rec in self:
            myuntaxamount1 = round(rec.invoice_untax_amount)
            rec.invoice_untax_amount1 = myuntaxamount1
            return myuntaxamount1

    @api.depends('invoice_tax_amount')
    def _get_taxamount1(self):
        mytaxamount1 = 0
        for rec in self:
            mytaxamount1 = round(rec.invoice_tax_amount)
            rec.invoice_tax_amount1 = mytaxamount1
            return mytaxamount1

    invoice_id = fields.Many2one('neweb_invoice.invoiceopen', required=True,ondelete='cascade')
    invoice_costtype = fields.Many2one('neweb.costtype', string="發票類型")
    invoice_spec = fields.Text(string="品名")
    invoice_num = fields.Integer(size=5, string="數量",default=1)
    invoice_unit_price = fields.Float(digits=(11, 2), string="單價",default=0)
    invoice_unit_nprice = fields.Float(digits=(11,0),string="BF單價",compute=_get_unitnprice)
    invoice_unit_price1 = fields.Float(digits=(11, 0), string="含稅價", default=0)
    invoice_unit_nprice1 = fields.Float(digits=(11, 0), string="BF含稅價", compute=_get_unitnprice1)
    invoice_untax_amount = fields.Float(digits=(13, 0), store=False, string="未稅合計",compute=_get_untaxamount)
    invoice_untax_amount1 = fields.Float(digits=(13, 0), string="BF未稅合計", compute=_get_untaxamount1)
    # invoice_untax_amount1 = fields.Float(digits=(9, 0), store=True, string="未稅合計",compute='_get_untaxamount1')
    invoice_taxtype = fields.Many2one('account.tax', string='Taxes',
                                      domain=['|', ('active', '=', False), ('active', '=', True),('type_tax_use', '=', 'sale')], default='1')
    invoicetype = fields.Selection([('1', '二聯式'), ('2', '三聯式'), ('3', '零税率')], string="税別", default='2')
    invoice_tax = fields.Float(digits=(7, 0), string="税金", store=False,compute=_get_tax)
    # invoice_tax1 = fields.Float(digits=(7, 0), string="税金", store=True,compute='_get_tax1')
    invoice_tax_amount = fields.Float(digits=(13, 0), store=False, string="含稅合計",compute=_get_taxamount)
    invoice_tax_amount1 = fields.Float(digits=(13, 0), store=False, string="BF含稅合計", compute=_get_taxamount1)
    # invoice_tax_amount1 = fields.Float(digits=(10, 0), store=True, string="含稅合計", compute='_get_taxamount1')
    invoice_no = fields.Char(size=10, string="發票號碼")
    invoice_date = fields.Date(string="開立日期")
    invoice_state = fields.Selection([('1', '暫存'), ('2', '已生效'), ('3', '驗收'), ('4', '作廢')], default='1',
                                     string="發票狀態")
    purchase_no = fields.Char(string="PO單號")
    invoice_ver = fields.Integer(string="次", default=0)
    sequence = fields.Integer(default=10)

    @api.onchange('invoice_unit_price')
    def onchangeunitprice(self):
        self.invoice_unit_price1 = round((self.invoice_unit_price * 1.05),2)
        # for rec in self:
        #     rec.invoice_unit_price1=round(rec.invoice_unit_price * 1.05)

    @api.onchange('invoice_unit_price1')
    def onchangeunitprice1(self):
        self.invoice_unit_price = round((self.invoice_unit_price1 / 1.05),2)
        # for rec in self:
        #     rec.invoice_unit_price = round(rec.invoice_unit_price1/1.05)


    def write(self, vals):
        res = super(newebinvoiceopenline, self).write(vals)
        for rec in self:
            if rec.invoice_no and rec.invoice_date :
               self.env.cr.execute("""select chk_invno_dup('%s','%s','%s')""" % (rec.invoice_no,rec.invoice_date,rec.invoice_id.sno))
               myres = self.env.cr.fetchone()[0]
               if myres:
                    raise UserError("""發票號碼 %s 有重複,請確認""" % rec.invoice_no)
        return res


    # def unlink(self):
    #     if self.invoice_no != False:
    #         raise UserError("已登錄發票號碼無法刪除,請用作廢模式")
    #     res = super(newebinvoiceopenline, self).unlink()
    #     return res


    ########## 20180926 update

    # @api.onchange('invoicetype')
    # def onclienttypechange(self):
    #     if self.invoicetype == '1' or self.invoicetype == '2':
    #         self.invoice_taxtype = '1'
    #         self.invoice_tax = self.invoice_num * self.invoice_unit_price * (self.invoice_taxtype.amount / 100)
    #         self.invoice_tax_amount = self.invoice_num * self.invoice_unit_price * (
    #                 1 + (self.invoice_taxtype.amount / 100))
    #     else:
    #         self.invoice_tax = 0
    #         self.invoice_tax_amount = self.invoice_num * self.invoice_unit_price

    # @api.depends('invoice_num', 'invoice_taxtype', 'invoice_unit_price')
    # def _get_tax(self):
    #     for myrec in self:
    #         if myrec.invoice_taxtype=='2':
    #             myrec.update(
    #                 {'invoice_tax': (myrec.invoice_num * myrec.invoice_unit_price * (myrec.invoice_taxtype.amount / 100))})

            ###############

    # @api.depends('invoice_num', 'invoice_taxtype', 'invoice_unit_price')
    # def _get_taxinvoiceamount(self):
    #     for myrec in self:
    #         if myrec.invoice_taxtype.include_base_amount:
    #             myrec.update({'invoice_tax_amount': (myrec.invoice_num * myrec.invoice_unit_price )})
    #         else:
    #             myrec.update({'invoice_tax_amount': (myrec.invoice_num * myrec.invoice_unit_price * ( 1 + (myrec.invoice_taxtype.amount/100)))})




class newebinvoiceproject(models.Model):
    _inherit = ["neweb.project"]

    invoice_mark = fields.Boolean(string="已開立發票", default=False)
    invoice_complete = fields.Boolean(string="發票已開完", default=False)
    invoice_openamount = fields.Float(digits=(10, 0), store=True, string="已開金額")
    invoice_record = fields.Many2many("neweb_invoice.invoiceopen", "neweb_project_invoice_rel", "pid", "iid",
                                      string="已開立發票記錄")
