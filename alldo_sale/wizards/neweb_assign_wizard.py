# -*- coding: utf-8 -*-
# Author: Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError,Warning
import datetime


class projengassignwizard(models.TransientModel):
    _name = "neweb.eng_assign_wizard"

    assign_type = fields.Selection([('1',u'未建檔新客戶'),('2',u'已建檔客戶')],string=u'客戶型態',default='2')
    proj_cus_name = fields.Many2one('res.partner', string=u"客戶名稱",
                              domain=[ ('customer', '=', '1'), ('is_company', '=', '1')])
    proj_branch = fields.Many2one('neweb.projbranch', string=u"工程成本分區", required=True)
    proj_sale = fields.Many2one('res.users', string=u'業務人員',default=lambda self:self.env.uid)

    @api.multi
    def neweb_eng_assign_wizard(self):
        if self.assign_type == '2' and self.proj_cus_name == False:
            raise UserError(u"必須選擇客戶名稱")
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
           myengid = myeng_rec.create({'assign_no': myassignno, 'proj_cus_name': self.proj_cus_name.id,
                                        'proj_sale': mysaleid[0], 'setup_contact': mycontact_rec[0].id,
                                        'setup_contact_phone': mycontact_rec[0].phone,
                                        'setup_contact_mobile': mycontact_rec[0].mobile, 'setup_address': myaddress1})
        else:
           # print "%s %s %s %s" % (mysaleid[0], mycontact_rec[0].phone, mycontact_rec[0].mobile, myaddress1)
           myengid = myeng_rec.create({ 'assign_no': myassignno ,'proj_cus_name': self.proj_cus_name.id,
                                      'proj_sale': mysaleid,'setup_contact': mycus_rec.id,
                                      'setup_contact_phone': mycus_rec.phone,
                                      'setup_contact_mobile': mycus_rec.mobile ,'setup_address': myaddress1})

        mydomain = []
        mydomain.append(('id', '=', myengid.id))
        return {'view_name': 'projengassignwizard',
                'name': (u'人力支援派工維護'),
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
