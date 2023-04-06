# -*- coding: utf-8 -*-
# Author: Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import datetime


class newebprojwizard(models.TransientModel):
    _name = "neweb.projwizard"

    name = fields.Char(string=u"專案編號")
    comp_name1 = fields.Many2one('res.partner', string=u'專案客戶',
                                 domain=[('is_company', '=', 'True'), ('customer', '=', 'True'),
                                         ('parent_id', '=', False)], required=True)
    comp_name2 = fields.Many2one('res.partner', string=u'維護客戶',
                                 domain=[('is_company', '=', 'True'), ('customer', '=', 'True'),
                                         ('parent_id', '=', False)])
    proj_branch = fields.Many2one('neweb.projbranch', string=u"專案成本分區", required=True)
    proj_sale = fields.Many2one('hr.employee', string=u'專案業務', required=True,track_visibility='always',default=lambda self:self.get_projsale)




    @api.multi
    def neweb_proj_wizard(self):
        self.comp_name2 = self.comp_name1.id
        mybranch = self.env['neweb.projbranch'].search([('id', '=', self.proj_branch.id)])
        myprefixcode = mybranch.prefixcode
        mynow = datetime.datetime.now()
        myyy = str(mynow.year - 1911)
        myyear = myyy[1:]
        mymm = str(mynow.month)
        mymonth = mymm.zfill(2)
        myym = myyear + mymonth

        ##################   同步上線 成本分析編號 先採用業務輸入方式
        # gencode_rec = self.env['neweb.projgencode'].search([('name', '=', myym), ('prefixcode', '=', myprefixcode)])
        # if gencode_rec:
        #     strcode = str(gencode_rec.gencode + 1)
        #     mycode = strcode.zfill(3)
        #     self.name = "%sSVC%s-%s" % (myprefixcode, myym, mycode)
        #     gencode_rec.gencode += 1
        # else:
        #     self.name = "%sSVC%s-001" % (myprefixcode, myym)
        #     gencode_rec.create({'name': myym, 'prefixcode': myprefixcode, 'gencode': 1})
        # myprojname = self.name
        # mycount = self.env['neweb.project'].search_count([('name', '=', myprojname)])
        # if mycount > 0:
        #     raise UserError("專案編號 (％s) 已重複,請連絡系統管理員" % myprojname)
        ##################
        myrec = self.env['neweb.project']
        mycus = self.env['res.partner'].search([('id', '=', self.comp_name1.id)])
        myactive_id = myrec.create(
            {'name': self.name, 'cus_name': self.comp_name1.id, 'proj_branch': self.proj_branch.id,
             'main_cus_name': self.comp_name2.id, 'proj_sale': self.proj_sale.id,
             'sno': mycus.sno, 'comp_cname': mycus.name, 'comp_sname': mycus.comp_sname,
             'comp_ename': mycus.comp_ename, 'cate_type': mycus.cate_type.id,
             'group_name': mycus.group_name, 'proj_pay_type': mycus.proj_pay_type,
             'proj_pay': mycus.proj_pay, 'acc_close_day': mycus.acc_close_day,
             'pay_term': mycus.pay_term, 'payto_date': mycus.payto_date,
             'other_date': mycus.other_date, 'acc_receivable': mycus.acc_receivable,
             'post_date': mycus.post_date, 'post_term': mycus.post_term,
             'post_envelop': mycus.post_envelop, 'tt_date': mycus.tt_date,
             'self_receive_date': mycus.self_receive_date, 'self_rece_stamp': mycus.self_rece_stamp,
             'description': mycus.description, 'memo': mycus.memo})
        newrec = self.env['neweb.project'].search([('id', '=', myactive_id.id)])
        newrec.write({'firstgen':0,'proj_cus_ids': [(0, 0, {'cus_type': '1', 'cus_address': mycus.street, 'cus_phone': mycus.phone,
                                               'cus_fax': mycus.fax, 'cus_memo': mycus.memo})]})
        contract_rec = self.env['res.partner'].search([('parent_id', '=', self.comp_name1.id)])
        for child_rec in contract_rec:
            newrec.write({'firstgen':0,'proj_contact_ids': [(0, 0, {'contact_type': child_rec.contact_type.id,
                                                       'contact_name': child_rec.id,
                                                       'contact_function': child_rec.function,
                                                       'contact_phone': child_rec.phone,
                                                       'contact_mobile': child_rec.mobile,
                                                       'contact_email': child_rec.email,
                                                       'contact_fax': child_rec.fax})]})
        if self.comp_name1.id != self.comp_name2.id:
            mycus1 = self.env['res.partner'].search([('id', '=', self.comp_name2.id)])
            newrec.write({'firstgen':0,'proj_cus_ids': [(0, 0,
                                            {'cus_type': '2', 'cus_address': mycus1.street, 'cus_phone': mycus1.phone,
                                             'cus_fax': mycus1.fax, 'cus_memo': mycus1.memo})]})
            contract_rec1 = self.env['res.partner'].search([('parent_id', '=', self.comp_name2.id)])
            for child_rec in contract_rec1:
                newrec.write(
                    {'firstgen':0,'proj_contact_ids': [(0, 0,
                                           {'contact_type': child_rec.contact_type.id, 'contact_name': child_rec.id,
                                            'contact_function': child_rec.function,
                                            'contact_phone': child_rec.phone, 'contact_mobile': child_rec.mobile,
                                            'contact_email': child_rec.email, 'contact_fax': child_rec.fax})]})

        # mytotcosttype_rec = self.env['neweb.costtype'].search([])
        # for costrec in mytotcosttype_rec :
        #     newrec.write({'analysis_line':[(0,0,{'analysis_costtype': costrec.id , 'analysis_sequence': costrec.costtype_sequence})]})

        mydomain = []
        mydomain.append(('id', '=', myactive_id.id))
        return {'view_name': 'newebprojwizard',
                'name': (u'專案維護'),
                'views': [[False, 'form'], ],
                'res_model': 'neweb.project',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                # 'domain': mydomain,
                'res_id': myactive_id.id,
                'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }
