# -*- coding: utf-8 -*-
# Author: Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError,Warning
import datetime


class projengassignwizard(models.TransientModel):
    _name = "neweb.eng_assign_wizard"

    assign_type = fields.Selection([('1','未建檔新客戶'),('2','已建檔客戶')],string='客戶型態',default='2')
    proj_cus_name = fields.Many2one('res.partner', string="客戶名稱")
    proj_cus_name1 = fields.Char(string="客戶名稱")
    proj_branch = fields.Many2one('neweb.projbranch', string="工程成本分區", required=True)
    proj_sale = fields.Many2one('res.users', string='業務人員',default=lambda self:self.env.uid)

    @api.onchange('proj_sale')
    def onchange_proj_sale(self):
        myids = self.env['res.partner'].search(['|','|','|','|',('salesp1','=',self.proj_sale.id),('salesp2','=',self.proj_sale.id),('salesp3','=',self.proj_sale.id),('salesp4','=',self.proj_sale.id),('salesp5','=',self.proj_sale.id),('customer_rank', '=', 1),('is_company', '=', '1')])
        ids = []
        for item in myids:
            ids.append(item.id)
        res = {}
        res['domain'] = {'proj_cus_name': [('id', 'in', ids)]}
        return res


    def neweb_eng_assign_wizard(self):
        if self.assign_type == '2' and self.proj_cus_name == False:
            raise UserError("必須選擇客戶名稱")
        if self.assign_type == '1' and self.proj_cus_name1 == False:
            raise  UserError("必須手動輸入客戶名稱")
        if self.proj_cus_name != False:
            mycus_rec = self.env['res.partner'].search([('id', '=', self.proj_cus_name.id)])
            mycontact_rec = self.env['res.partner'].search([('parent_id','=',mycus_rec.id)])
            myaddress1 = mycus_rec.street
        else:
            myaddress1 = ' '
        mybranch = self.env['neweb.projbranch'].search([('id', '=', self.proj_branch.id)])
        myprefixcode = mybranch.prefixcode
        myprefixcode = 'X'
        mynow = datetime.datetime.now()
        myyy = str(mynow.year - 1911)
        myyear = myyy[1:]
        mymm = str(mynow.month)
        mymonth = mymm.zfill(2)
        myym = myyear + mymonth
        # print "%s  %s" % (myym,myprefixcode)
        gencode_rec = self.env['neweb.projgencode'].search([('name', '=', myym), ('prefixcode', '=', myprefixcode)])
        if gencode_rec:
            strcode = str(gencode_rec.gencode + 1)
            mycode = strcode.zfill(3)
            myassignno = "SUP%s-%s" % (myym, mycode)
            gencode_rec.gencode += 1
        else:
            myassignno = "SUP%s-001" % (myym)
            gencode_rec.create({'name': myym, 'prefixcode': 'X', 'gencode': 1})

        myeng_rec = self.env['neweb.proj_eng_assign']
        # print "%s" % myassignno
        mysaleid = 1
        if self.proj_sale:
            self.env.cr.execute("select id from resource_resource where user_id=%d " % self.proj_sale.id)
            resid = self.env.cr.fetchone()
            self.env.cr.execute("select id from hr_employee where resource_id=%d" % int(resid[0]))
            mysaleid = self.env.cr.fetchone()
        if mycontact_rec:
           # print "%s %s %s %s" % (mysaleid[0],mycontact_rec[0].phone,mycontact_rec[0].mobile,myaddress1)
           # raise Warning("message")
           if self.assign_type=='1':
               myengid = myeng_rec.sudo().create({'assign_no': myassignno, 'proj_cus_name1': self.proj_cus_name1,
                                                  'proj_sale': mysaleid[0],
                                                  'assign_type':self.assign_type})
           else:
               myengid = myeng_rec.sudo().create({'assign_no': myassignno, 'proj_cus_name': self.proj_cus_name.id,
                                                  'proj_sale': mysaleid[0], 'setup_contact': mycontact_rec[0].id,
                                                  'setup_contact_phone': mycontact_rec[0].phone,
                                                  'setup_contact_mobile': mycontact_rec[0].mobile,
                                                  'setup_address': myaddress1,'assign_type':self.assign_type})

        else:
           # print "%s %s %s %s" % (mysaleid[0], mycontact_rec[0].phone, mycontact_rec[0].mobile, myaddress1)
           if self.assign_type=='1':
               myengid = myeng_rec.sudo().create({'assign_no': myassignno, 'proj_cus_name1': self.proj_cus_name1,
                                                  'proj_sale': mysaleid, 'setup_contact': mycus_rec.id,
                                                  'setup_contact_phone': mycus_rec.phone,
                                                  'setup_contact_mobile': mycus_rec.mobile,
                                                  'setup_address': myaddress1,'assign_type':self.assign_type})
           else:
               myengid = myeng_rec.sudo().create({ 'assign_no': myassignno ,'proj_cus_name': self.proj_cus_name.id,
                                      'proj_sale': mysaleid,'setup_contact': mycus_rec.id,
                                      'setup_contact_phone': mycus_rec.phone,
                                      'setup_contact_mobile': mycus_rec.mobile ,'setup_address': myaddress1,'assign_type':self.assign_type})

        mydomain = []
        mydomain.append(('id', '=', myengid.id))
        return {'view_name': 'projengassignwizard',
                'name': ('人力支援派工維護'),
                'views': [[False, 'form'], ],
                'res_model': 'neweb.proj_eng_assign',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'current',
                # 'domain': mydomain,
                'res_id': myengid.id,
                'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }

    # def view_init(self, fields_list):
    #     super(projengassignwizard, self).view_init(fields_list)
