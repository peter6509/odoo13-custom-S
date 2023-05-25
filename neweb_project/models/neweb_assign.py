# -*- coding: utf-8 -*-
# Author: Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from datetime import datetime
from dateutil.relativedelta import relativedelta
# import odoo.addons.decimal_precision as dp

# class irattachmentsinherit(models.Model):
#     _inherit = 'ir.attachment'
#     def check(self, cr, context=None, values=None):
#         res_ids = {}
#         if self.ids:
#             if isinstance(self.ids, (int, long)):
#                 ids = [self.ids]
#             cr.execute('SELECT DISTINCT res_model, res_id, create_uid FROM ir_attachment WHERE id = ANY (%s)',
#                        (self.ids,))
#             for rmod, rid, create_uid in cr.fetchall():
#                 if not (rmod and rid):
#                     continue
#                 res_ids.setdefault(rmod, set()).add(rid)
#         if values:
#             if values.get('res_model') and values.get('res_id'):
#                 res_ids.setdefault(values['res_model'], set()).add(values['res_id'])
#         ima = self.pool.get('ir.model.access')
#         for model, mids in res_ids.items():
#             # ignore attachments that are not attached to a resource anymore when checking access rights
#             # (resource was deleted but attachment was not)
#             if not self.pool.get(model):
#                 continue
#             existing_ids = self.pool[model].exists(cr, self.env.uid, mids)
#             ima.check(cr, self.env.uid, model, self.mode)
#             self.pool[model].check_access_rule(cr, self.env.uid, existing_ids, self.mode, context=context)


class projsetupdescitem(models.Model):
    _name = "neweb.setup_desc_item"
    _description = '成本分析裝機及施工說明'

    name = fields.Char(string="裝機及施工說明")
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("裝機及施工方式不能為空值！"))
        if 'name' in vals and vals['name']:
            myname = vals['name']
            myrec = self.env['neweb.setup_desc_item'].search([('name', '=', myname)])
            if myrec:
                raise UserError(("裝機及施工方式 => ％s 重複建立了,請確認") % myname)
        rec = super(projsetupdescitem, self).create(vals)
        return rec


class projsetupattach(models.Model):
    _name = "neweb.setup_attach"
    _description = '成本分析附件名稱'

    name = fields.Char(string="附件")
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("附件名稱不能為空值！"))
        if 'name' in vals and vals['name']:
            myname = vals['name']
            myrec = self.env['neweb.setup_attach'].search([('name', '=', myname)])
            if myrec:
                raise UserError(("附件名稱 => ％s 重複建立了,請確認") % myname)
        rec = super(projsetupattach, self).create(vals)
        return rec


class projservicemode(models.Model):
    _name = "neweb.ass_service_mode"
    _description = '成本分析專服務名稱基礎配置'

    name = fields.Char(size=50,string="服務名稱")
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("服務名稱不能為空值！"))
        if 'name' in vals and vals['name']:
            myname = vals['name']
            myrec = self.env['neweb.ass_service_mode'].search([('name', '=', myname)])
            if myrec:
                raise UserError(("服務名稱 => ％s 重複建立了,請確認") % myname)
        rec = super(projservicemode, self).create(vals)
        return rec


class projservicetype(models.Model):
    _name = "neweb.ass_service_type"
    _description = '成本分析服務類別基礎配置'

    name = fields.Char(size=50, string="服務類別")
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError(("服務類別不能為空值！"))
        if 'name' in vals and vals['name']:
            myname = vals['name']
            myrec = self.env['neweb.ass_service_type'].search([('name', '=', myname)])
            if myrec:
                raise UserError(("服務類別 => ％s 重複建立了,請確認") % myname)
        rec = super(projservicetype, self).create(vals)
        return rec


class projsetupprod(models.Model):
    _name = "neweb.setup_prod"
    _description = '成本分析裝機明細內容'

    setup_id = fields.Many2one('neweb.proj_eng_assign',required=True, ondelete='cascade')
    prod_set = fields.Many2one('neweb.prodset', string="產品組別")
    prod_modeltype = fields.Char(string="機種-機型/料號")
    prod_serial = fields.Char(string="序號")
    prod_no = fields.Char(string="料號")
    prod_desc = fields.Char(string="規格說明")
    prod_num = fields.Integer(string="數量")
    software_ver = fields.Char(string="軟體版本")
    prod_memo = fields.Char(string="備註")



class projengcomplete(models.Model):
    _name = "neweb.assign_complete"

    complete_id = fields.Many2one('neweb.proj_eng_assign',required=True,ondelete='cascade')
    man_id = fields.Many2one('res.users',string='工程人員')
    man_day = fields.Float(digits=(5,1),string='天數')
    man_hour = fields.Float(digits=(4,1),string='時數')
    man_memo = fields.Text(string="備註")



class projengassign(models.Model):
    _name = "neweb.proj_eng_assign"  ## 裝機＆派工
    _description = "工程派工單/人力支援派工單"
    _inherit = ['mail.thread']
    _order = "assign_no desc"

    @api.depends('proj_complete_line')
    def _get_completed_man(self):
        man_num = 0
        for rec in self.proj_complete_line:
            man_num += 1
        self.update({'completed_man': man_num})

    @api.depends('proj_complete_line')
    def _get_completed_day(self):
        man_day = 0
        for rec in self.proj_complete_line:
            man_day += rec.man_day
        # man_day = self.completed_man * man_day
        self.update({'completed_day': man_day})

    @api.depends('proj_complete_line')
    def _get_completed_hour(self):
        man_hour = 0
        man_day = 0
        for rec in self.proj_complete_line:
            man_day += rec.man_day
            man_hour += rec.man_hour
        allmandayhr = man_day * 8
        man_hour = man_hour + allmandayhr
        self.update({'completed_hour': man_hour})

    @api.depends('assign_man')
    def _get_display(self):
        mydisplay_yn = False
        for rec in self.assign_man:
            if rec.id == self.env.uid:
                mydisplay_yn = True
        self.display_yn = mydisplay_yn
        return self.display_yn

    @api.depends('assign_no')
    def _get_assignno(self):
        for rec in self:
            rec.update({'name': rec.assign_no})

    @api.depends('assign_man_num')
    def _get_mannum(self):
        for rec in self:
            if rec.assign_man_num==0:
               mymannum = ' '
            else:
               mymannum = str(rec.assign_man_num)
            rec.assign_man_num1 = mymannum
            return mymannum

    @api.depends('assign_man_day')
    def _get_manday(self):
        for rec in self:
            if rec.assign_man_day == 0:
                mymanday = ' '
            else:
                mymanday = str(rec.assign_man_day)
            rec.assign_man_day1 = mymanday
            return mymanday

    @api.depends('assign_man_hour')
    def _get_manhour(self):
        for rec in self:
            if rec.assign_man_hour == 0:
                mymanhour = ' '
            else:
                mymanhour = str(rec.assign_man_hour)
            rec.assign_man_hour1 = mymanhour
            return mymanhour

    @api.depends('completed_man')
    def _get_compman(self):
        for rec in self:
            if rec.completed_man == 0:
                mycompman = ' '
            else:
                mycompman = str(rec.completed_man)
            rec.completed_man1 = mycompman
            return mycompman

    @api.depends('completed_day')
    def _get_compday(self):
        for rec in self:
            if rec.completed_day == 0:
                mycompday = ' '
            else:
                mycompday = str(rec.completed_day)
            rec.completed_day1 = mycompday
            return mycompday

    @api.depends('completed_hour')
    def _get_comphour(self):
        for rec in self:
            if rec.completed_hour == 0:
                mycomphour = ' '
            else:
                mycomphour = str(rec.completed_hour)
            rec.completed_hour1 = mycomphour
            return mycomphour


    # name = fields.Char(string="裝機單號")
    require_date = fields.Date(string="申請日期",default =  lambda *a:datetime.today().strftime('%Y-%m-%d'))
    proj_no = fields.Many2one('neweb.project', string="專案編號")
    assign_no = fields.Char(size=20,string="派工單號")
    proj_cus_name = fields.Many2one('res.partner', string="專案客戶")
    proj_sale = fields.Many2one('hr.employee', string="專案業務")
    setup_address = fields.Char(string="裝機地址")
    setup_contact = fields.Many2one('res.partner', string="裝機連絡人")
    setup_contact1 = fields.Char(string="裝機連絡人")
    setup_contact_phone = fields.Char(string="連絡人電話")
    setup_contact_mobile = fields.Char(string="連絡人手機")
    setup_date = fields.Date(string="預定裝機日",required=True,default=datetime.today())
    proj_manager = fields.Char(string="專案經理")
    service_name = fields.Many2one('neweb.ass_service_mode',string="服務名稱",required=True,default='1')
    setup_desc = fields.Many2many('neweb.engmaintype', string="裝機及施工方式",required=True)
    setup_other_desc = fields.Text(string="其他裝機說明")
    setup_attach = fields.Many2many('ir.attachment','ir_setup_attach_rel1','ir_id','eng_id', string="專案附件",public=True,attachment=False)
    setup_other_attach = fields.Text(string="其他說明")
    task_desc = fields.Text(string="工作說明")
    service_type = fields.Many2one('neweb.ass_service_type',string="服務類別")
    assign_man_num = fields.Float(digits=(4,1) , string="預估人力需求",required=True,default=0)
    assign_man_num1 = fields.Char(string="預估人力需求bf",compute=_get_mannum)
    assign_man_day = fields.Float(digita=(5,1) , string="預估工作天",required=True,default=0)
    assign_man_day1 = fields.Char(string="預估工作天bf",compute=_get_manday)
    assign_man_hour = fields.Float(digits=(4,1), string="預估工作小時",required=True,default=0)
    assign_man_hour1 = fields.Char(string="預估工作小時bf", compute=_get_manhour)
    assign_man_desc = fields.Text(string="派工需求說明")
    assign_man = fields.Many2many('res.users',string="指派工程人員")
    eng_man_desc = fields.Text(string="工程師完工說明")
    eng_attach = fields.Many2many('ir.attachment','ir_setup_attach_rel2','ir_id','eng_id', string="完工附件",public=True,attachment=False)
    proj_setup_line = fields.One2many('neweb.setup_prod', 'setup_id', copy=True, string="裝機內容",ondelete='cascade')
    state = fields.Selection([('1','新單'),('2','人力指派'),('3','完工')],string="狀態",default='1')
    proj_complete_line = fields.One2many('neweb.assign_complete','complete_id',copy=True,string="工程師工時明細",ondelete='cascade')
    display_yn = fields.Boolean(string="是否顯示",store=False,compute=_get_display)
    name = fields.Char(default=_get_assignno,store=True,string='單號')
    is_signed = fields.Boolean(string="是否授信",default=False)
    completed_man = fields.Integer(string="實際人數",store=False,compute=_get_completed_man)
    completed_day = fields.Integer(string="實際天數",store=False,compute=_get_completed_day)
    completed_hour = fields.Integer(string="實際時數",store=False,compute=_get_completed_hour)
    completed_man1 = fields.Char(string="實際人數bf",  compute=_get_compman)
    completed_day1 = fields.Char(string="實際天數bf",  compute=_get_compday)
    completed_hour1 = fields.Char(string="實際時數bf",  compute=_get_comphour)
    proj_cus_name1 = fields.Char(string="專案客戶")
    assign_type = fields.Selection([('1', '未建檔新客戶'), ('2', '已建檔客戶')], string='客戶型態', default='2')
    sendmail_dt = fields.Datetime(string="寄信時間")


    @api.model
    def create(self, vals):
        # if 'assign_man_desc' in vals and not vals['assign_man_desc']:
        #     raise UserError("未輸入派工需求說明,請確認...")
        rec = super(projengassign, self).create(vals)
        return rec

    def write(self, vals):
        # if 'setup_date' in vals and not vals['setup_date']:
        #     raise UserError("未輸入預定裝幾日,請確認...")
        # if 'service_name' in vals and not vals['service_name']:
        #     raise UserError("未輸入服務名稱,請確認...")
        # if 'service_type' in vals and not vals['service_type']:
        #     raise UserError("未輸入服務類別,請確認...")
        # if 'setup_desc' in vals and not vals['setup_desc']:
        #     raise UserError("未輸入裝機及施工方式,請確認...")
        # if 'assign_man_num' in vals and not vals['assign_man_num']:
        #     raise UserError("未輸入預估人力需求,請確認...")
        # if 'assign_man_day' in vals and not vals['assign_man_day']:
        #     raise UserError("未輸入預估人力天數,請確認...")
        # if 'assign_man_hour' in vals and not vals['assign_man_hour']:
        #     raise UserError("未輸入預估人力小時,請確認...")
        #
        # if 'assign_man_desc' in vals and not vals['assign_man_desc']:
        #     raise UserError("未輸入派工需求說明,請確認...")
        rec = super(projengassign, self).write(vals)
        return rec

    def unlink(self):
        # self.env.cr.execute("select wkfisstart(%d)" % int(self.x_wkf_state))
        # isstart = self.env.cr.fetchone()
        # if not isstart[0]:
        #     raise UserError("表單已送簽核,不能刪除")
        res = super(projengassign,self).unlink()
        return res


    def set_signed(self):
    	for rec in self:
    		rec.update({'is_signed':True,'state':'2'})

    is_closed = fields.Boolean(string="是否結案",default=False)


    def set_closed(self):
        for rec in self:
            rec.update({'is_closed':True,'state': '3'})

    def set_reject(self):
        for rec in self:
            rec.update({'is_closed':False , 'is_signed':False})



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
        myrec = self.env['neweb.proj_eng_assign'].search([('id', '=', self.id)])
        myid = myrec.id
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            if myrec.proj_no:
               ##  專案人力派工
               template_id = ir_model_data.get_object_reference('neweb_project', 'mail_neweb_neg_assign_wkf_approve')[1]
            else:
               ##  非專案人力支援派工
               template_id = ir_model_data.get_object_reference('neweb_project', 'mail_neweb_neg_assign_wkf_approve1')[1]
        except ValueError:
            template_id = False
        # ctx = self.env.context.copy()
        # ctx.update({
        #     'default_model': 'neweb.proj_eng_assign',
        #     'default_res_id': self.ids[0],
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_composition_mode': 'comment',
        #     'mark_so_as_sent': True,
        #     'mail_post_autofollow': True,
        #     'custom_layout': "neweb_project.mail_neweb_eng_assign_wkf_approve"
        # })

        self.env['mail.template'].browse(template_id).send_mail(myid)
        #template_id = ir_model_data.get_object_reference('neweb_project', 'mail_neweb_eng_assign_wkf_approve')[1]
        #self.pool['mail.template'].send_mail(self.env.cr, self.env.uid, template_id, self.id, force_send=True,
        #                                     context=self.with_context(ctx))


    def send_reject_mail(self):
        myrec = self.env['neweb.proj_eng_assign'].search([('id', '=', self.id)])
        myid = myrec.id
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            if myrec.proj_no:
               template_id = ir_model_data.get_object_reference('neweb_project', 'mail_neweb_eng_assign_wkf_reject')[1]
            else:
               template_id = ir_model_data.get_object_reference('neweb_project', 'mail_neweb_eng_assign_wkf_reject1')[1]
        except ValueError:
            template_id = False
        # ctx = self.env.context.copy()
        # ctx.update({
        #     'default_model': 'neweb.proj_eng_assign',
        #     'default_res_id': self.ids[0],
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_composition_mode': 'comment',
        #     'mark_so_as_sent': True,
        #     'mail_post_autofollow': True,
        #     'custom_layout': "neweb_project.mail_neweb_eng_assign_wkf_reject"
        # })
        self.env['mail.template'].browse(template_id).send_mail(myid)
        #template_id = ir_model_data.get_object_reference('neweb_project', 'mail_neweb_eng_assign_wkf_reject')[1]
        # myrec.write({'state': 'sent'})
        #self.pool['mail.template'].send_mail(self.env.cr, self.env.uid, template_id, self.id, force_send=True,
        #                                     context=self.with_context(ctx))


    def get_assignemail_ids(self,assign_man):
        # myemail = str([assign.partner_id.email for assign in assign_man]).replace('[','').replace(']','').replace("'",'').replace('','')
        # myprojsale = self.proj_sale.work_email
        # allemail = myemail + ',' + myprojsale

        self.env.cr.execute("""select genengmaillist(%d)""" %self.id)
        myids = self.env.cr.fetchall()
        allemail = self.proj_sale.work_email
        myrec = self.env['hr.employee'].search([('id','in',myids)])
        for rec in myrec:
            if allemail == '' :
                allemail = rec.work_email
            else:
                allemail = allemail + ',' + rec.work_email
        # print "%s" % allemail
        return allemail
        # return str(assign_man.ids).replace('[','').replace(']','')


    def get_assignname_ids(self, assign_man):
        return str([assign.login for assign in assign_man]).replace('[','').replace(']','').replace('','').replace("'",'')

    @api.onchange('setup_date')
    def _onchange_client(self):
        # myprojid = self.env.context.get('proj_op_id')
        self._cr.execute("select projsale_custom(%d)" % self.proj_no.id)
        mylist = self._cr.fetchall()
        myids = self.env['res.partner'].search([('id', 'in', mylist)])
        # print myids
        ids = []
        for item in myids:
            ids.append(item.id)
        res = {}
        res['domain']={'setup_contact':[('id','in',ids)]}
        return res


    def name_get(self):
        result = []
        for myrec in self:
            myprojitem = "(%s)" % (myrec.assign_no)
            result.append((myrec.id, myprojitem))
        return result


    @api.onchange('setup_contact')
    def _onchange_setup_contact(self):
        mycontact = self.env['res.partner'].search([('id', '=', self.setup_contact.id)])
        self.setup_contact_phone = mycontact.phone
        self.setup_contact_mobile = mycontact.mobile

    def gen_projsaleitem1(self):
        myengid = self.env.context.get('proj_assign_id')
        self.env.cr.execute("""select regenengsetupprod(%d)""" % (myengid))
        self.env.cr.execute("""commit""")

    def gen_projsaleitem(self):
        self.env.cr.execute("delete from neweb_proj_saleitem_select")
        self.env.cr.execute("delete from neweb_proj_select")
        self.env.cr.execute("delete from neweb_proj_item_select")
        # raise UserError("%s" % self.env.context.get('proj_assign_id'))
        myassignrec = self.env['neweb.proj_eng_assign'].search([('id', '=', self.env.context.get('proj_assign_id'))])
        # raise UserError("%s" % myassignrec.proj_no.name)
        myprojid = self.env['neweb.project'].search([('name', '=', myassignrec.proj_no.name)])
        myselect_rec = self.env['neweb.proj_select']
        myselectid = myselect_rec.create({'name': myassignrec.proj_no.name})
        myselect_rec = self.env['neweb.proj_select'].search([('id', '=', myselectid.id)])
        for rec in myprojid.saleitem_line:
            myselect_rec.write({'saleitem_line': [(0, 0,
                                                   {'prod_set': rec.prod_set.id, 'prod_modeltype': rec.prod_modeltype,
                                                    'prod_serial': rec.prod_serial,
                                                    'prod_no': rec.prod_no, 'prod_desc': rec.prod_desc,
                                                    'prod_num': rec.prod_num})]})

        return {'view_name': 'projengassign',
                'name': ('專案進貨明細選單'),
                'views': [[False, 'form'], [False, 'tree'], ],
                'res_model': 'neweb.proj_item_select',
                'context': self._context,
                'type': 'ir.actions.act_window',
                # 'res_id': myselectid.id,
                'target': 'new',
                'flags': {'action_buttons': False},
                'view_mode': 'form',
                'view_type': 'form'
                }


    def assign_sendmail(self):
        '''
          This function opens a window to compose an email, with the edi purchase request template message loaded by default
        '''
        self.ensure_one()
        myid = self.id
        ir_model_data = self.env['ir.model.data']
        try:
           template_id =  ir_model_data.get_object_reference('neweb_project', 'email_template_assign_message')[1]
        except ValueError:
           template_id = False
        try:
           compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
           compose_form_id = False

        ctx = dict()
        ctx.update({
            'default_model': 'neweb.proj_eng_assign',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'mail_post_autofollow': True,

            # 'custom_layout': "sale.mail_template_data_notification_email_sale_order"
            })
        self.env.cr.execute("""update neweb_proj_eng_assign set sendmail_dt = current_timestamp where id = %d""" % myid)
        self.env.cr.execute("""commit""")
        ir_model_data.get_object_reference('neweb_project', 'email_template_assign_message')[1]

        self.env['mail.template'].browse(template_id).sudo().send_mail(myid)
        # self.pool['mail.template'].sudo().send_mail(self.env.cr, self.env.uid, template_id, myid, force_send=True,context=self.env.context)

        # return {
        #     'type': 'ir.actions.act_window',
        #     'view_type': 'form',
        #     'view_mode': 'form',
        #     'res_model': 'mail.compose.message',
        #     'views': [(compose_form_id, 'form')],
        #     'view_id': compose_form_id,
        #     'target': 'new',
        #     'context': ctx,
        #     }