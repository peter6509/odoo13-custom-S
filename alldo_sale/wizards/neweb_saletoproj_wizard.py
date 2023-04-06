# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import datetime


class newebsaletoprojwizard(models.TransientModel):
    _name = "neweb.saletoproj"

    proj_branch = fields.Many2one('neweb.projbranch', string=u"專案成本分區", required=True)
    proj_sale = fields.Many2one('hr.employee', string=u'專案業務', required=True)
    cost_type = fields.Many2one('neweb.costtype', string=u"專案成本類型",default='1')


    @api.onchange("proj_branch")
    def onchange_proj_id(self):
        res = {}
        mysaleid = self.env.context.get("sale_op_id")
        myrec = self.env['sale.order'].search([('id', '=', mysaleid)])
        myid = myrec.user_id.id
        myemprec = self.env['hr.employee'].search([('user_id', '=', myid)])
        ids = []
        for item in myemprec:
            ids.append(item.id)
        if myid:
           res['domain'] = {'proj_sale': [('id', 'in', ids)]}
        else:
           res['domain'] = {'proj_sale': [(1,'=',1)]}
        self.proj_sale = myemprec[0].id
        return res


    @api.multi
    def saletoproj_wizard(self):
        mysaleorderid = self.env.context.get('sale_op_id')
        mysaleorder = self.env['sale.order'].search([('id', '=', self.env.context.get('sale_op_id'))])
        mysaleno = mysaleorder.name
        self.env.cr.execute("""select hasdisamount(%d)""" % self.env.context.get('sale_op_id'))
        myres = self.env.cr.fetchone()
        if not myres[0]:
            raise UserError("給予最優惠總價不能為0,請確認")
        # raise UserError("%s" % mysaleno)
        mysalenocheck = self.env['neweb.salenocheck'].search([('sale_no', '=', mysaleno[:10])])
        # if mysalenocheck:
        #     mytransyn = mysalenocheck.trans_proj
        #     if mytransyn:
        #         raise UserError("已經轉專案成本分析了...")
        # print "mysaleorderid :%s" % mysaleorderid
        mysalerec = self.env['sale.order'].search([('id','=',mysaleorderid)])
        mybranch = self.env['neweb.projbranch'].search([('id', '=', self.proj_branch.id)])
        myprefixcode = mybranch.prefixcode
        mynow = datetime.datetime.now()
        myyy = str(mynow.year - 1911)
        myyear = myyy[1:]
        mymm = str(mynow.month)
        mymonth = mymm.zfill(2)
        myym = myyear + mymonth
        gencode_rec = self.env['neweb.projgencode'].search([('name', '=', myym), ('prefixcode', '=', myprefixcode)])
        if gencode_rec:
            strcode = str(gencode_rec.gencode + 1)
            mycode = strcode.zfill(3)
            myprojname = "%sSVC%s-%s" % (myprefixcode, myym, mycode)
            gencode_rec.gencode += 1
        else:
            myprojname = "%sSVC%s-001" % (myprefixcode, myym)
            gencode_rec.create({'name': myym, 'prefixcode': myprefixcode, 'gencode': 1})
        mycount = self.env['neweb.project'].search_count([('name', '=', myprojname)])
        if mycount > 0:
            raise UserError("專案編號 (％s) 已重複,請連絡系統管理員" % myprojname)
        myrec = self.env['neweb.project']
        mycus = self.env['res.partner'].search([('id', '=', mysalerec.partner_id.id)])
        mytransationtypeid=2
        if self.cost_type.id==2:
           mytransationtypeid=10
        if self.cost_type.id==3:
           mytransationtypeid=6
        if self.cost_type.id==4:
           mytransationtypeid=7
        if self.cost_type.id==5 :
           mytransationtypeid=4
        if self.cost_type.id==7:
           mytransationtypeid=9
        if mycus.acc_receivable == '1' or not mycus.acc_receivable :
           myaccreceivable = '2'
        else:
           myaccreceivable = mycus.acc_receivable

        self.env.cr.execute("select get_partnercloseday(%d)" % mysalerec.partner_id.id)
        mycloseday = self.env.cr.fetchone()

        myactive_id = myrec.create(
            {'name': myprojname, 'cus_name': mysalerec.partner_id.id, 'proj_branch': self.proj_branch.id,
             'main_cus_name': mysalerec.partner_id.id, 'proj_sale': self.proj_sale.id,
             'sno': mycus.vat, 'comp_cname': mycus.name, 'comp_sname': mycus.comp_sname,
             'comp_ename': mycus.comp_ename, 'cate_type': mycus.cate_type.id,
             'group_name': mycus.group_name, 'proj_pay_type': mycus.proj_pay_type,
             'acc_close_day': mycus.acc_close_day,
             'pay_term': mycus.pay_term, 'payto_date': mycus.payto_date,
             'other_date': mycus.other_date, 'acc_receivable': myaccreceivable,
             'post_date': mycus.post_date, 'post_term': mycus.post_term,
             'post_envelop': mycus.post_envelop, 'tt_date': mycus.tt_date,'self_receive_type': mycus.self_receive_type,
             'self_receive_date': mycus.self_receive_date, 'self_rece_stamp': mycus.self_rece_stamp,
             'description': mycus.description, 'memo': mycus.memo,'sale_no': mysalerec.name,'open_account_day':mysalerec.open_account_day,
             'cus_project':mysalerec.project_name,'acc_close_day1':mycloseday[0]})

        #print "myactive_id:%s" % myactive_id.id
        newrec = self.env['neweb.project'].search([('id', '=', myactive_id.id)])
        # if mycus.cus_payment:
        #     newrec.write({'proj_pay':mycus.cus_payment})
        # newrec.write({'transation_type':[(6,0,[mytransationtypeid])]})
        # for saleitemrec in mysalerec.display_line:
        #     if not saleitemrec.sitem_modeltype:
        #         sitemmodeltype='-'
        #     else:
        #         sitemmodeltype=saleitemrec.sitem_modeltype.replace("'","''")
        #
        #     if not saleitemrec.sitem_desc:
        #         sitemdesc='-'
        #     else:
        #         sitemdesc=saleitemrec.sitem_desc.replace("'","''")
        #     if not saleitemrec.sitem_num:
        #         sitemnum = 1
        #     else:
        #         sitemnum=saleitemrec.sitem_num
        #     if not saleitemrec.sitem_cost:
        #         sitemcost=0
        #     else:
        #         sitemcost=saleitemrec.sitem_cost
        #     if not saleitemrec.sitem_price:
        #         sitemprice=0
        #     else:
        #         sitemprice=saleitemrec.sitem_price
        #     if not self.cost_type.id:
        #         costtypeid=1
        #     else:
        #         costtypeid=self.cost_type.id
        #
        #     if not saleitemrec.sitem_item:
        #         sitemitem = '-'
        #     else:
        #         sitemitem=saleitemrec.sitem_item
        #
        #     if not saleitemrec.sitem_serial:
        #         sitemserial = '-'
        #     else:
        #         sitemserial=saleitemrec.sitem_serial.replace("'","''")

            # if not saleitemrec.sitem_brand.id:
            #     self.env.cr.execute("""insert into neweb_projsaleitem(saleitem_id,prod_modeltype,prod_desc,prod_num,
            #                                     prod_price,prod_revenue,cost_type,saleitem_item,prod_serial) values (%s,'%s','%s',%s,%s,%s,%s,'%s','%s')""" %
            #                         (myactive_id.id, sitemmodeltype,sitemdesc, sitemnum, sitemcost,
            #                          sitemprice, costtypeid, sitemitem, sitemserial))
            # else:
            #     sitembrandid=saleitemrec.sitem_brand.id
            #     self.env.cr.execute("""insert into neweb_projsaleitem(saleitem_id,prod_modeltype,prod_brand,prod_desc,prod_num,
            #                     prod_price,prod_revenue,cost_type,saleitem_item,prod_serial) values (%s,'%s',%s,'%s',%s,%s,%s,%s,'%s','%s')""" %
            #                     (myactive_id.id,sitemmodeltype,sitembrandid,sitemdesc,sitemnum,sitemcost,sitemprice,costtypeid,sitemitem,sitemserial))

        if not mycus.street:
            cstreet='-'
        else:
            cstreet=mycus.street.replace("'","''")
        if not mycus.phone:
            cphone='-'
        else:
            cphone=mycus.phone
        if not mycus.fax:
            cfax='-'
        else:
            cfax=mycus.fax
        if not mycus.memo:
            cmemo='-'
        else:
            cmemo=mycus.memo.replace("'","''")

        self.env.cr.execute("""insert into neweb_projcustom(cus_id,cus_type,cus_address,cus_phone,cus_fax,cus_memo) VALUES (%s,%s,'%s','%s','%s','%s')""" % (myactive_id.id,1,cstreet,cphone,cfax,cmemo))

        #print "parent_id:%s" % mysalerec.partner_id.id
        contact_rec = self.env['res.partner'].search([('parent_id', '=', mysalerec.partner_id.id)])
        for child_rec in contact_rec:
            if not child_rec.function:
                cfunction='-'
            else:
                cfunction=child_rec.function
            if not child_rec.phone:
                cphone='-'
            else:
                cphone=child_rec.phone
            if not child_rec.mobile:
                cmobile='-'
            else:
                cmobile=child_rec.mobile
            if not child_rec.email:
                cemail='-'
            else:
                cemail=child_rec.email
            if not child_rec.fax:
                cfax='-'
            else:
                cfax=child_rec.fax
            if not child_rec.street :
                caddress = '-'
            else:
                caddress = child_rec.street
            if not child_rec.comment:
                cmemo = '-'
            else:
                cmemo = child_rec.comment
            if not child_rec.contact_type.id:
                self.env.cr.execute("""insert into neweb_projcontact(contact_id,contact_name,contact_function,contact_phone,
                                    contact_mobile,contact_email,contact_fax) values (%s,%s,'%s','%s','%s','%s','%s')""" %
                                    (myactive_id.id,child_rec.id,cfunction, cphone, cmobile, cemail, cfax))
            else:
                contacttypeid=child_rec.contact_type.id
                self.env.cr.execute("""insert into neweb_projcontact(contact_id,contact_type,contact_name,contact_function,contact_phone,
                                contact_mobile,contact_email,contact_fax) values (%s,%s,%s,'%s','%s','%s','%s','%s')""" %
                                (myactive_id.id,contacttypeid,child_rec.id,cfunction,cphone, cmobile,cemail,cfax))
            self.env.cr.execute("""insert into neweb_projcustom(cus_id,cus_address,cus_phone,cus_fax,cus_memo) VALUES (%s,'%s','%s','%s','%s')""" % (
                myactive_id.id, caddress, cphone, cfax, cmemo))
        #   將轉到專案的銷單號碼鎖定
        mysalenorec = self.env['neweb.salenocheck'].search([('sale_no','=',mysalerec.name[:10])])
        if mysalenorec :
           mysalenorec.write({'trans_proj':True})

        # 自動轉成確認訂單
        #self.env.cr.execute("select proj_cal_cost(%d)" % newrec.id)
        mysalerec.action_confirm()
        mysalerec.action_done()

        mydomain = []
        mydomain.append(('id', '=', myactive_id.id))
        return {'view_name': 'newebprojwizard',
                'name': (u'專案維護'),
                'views': [[False, 'form'], ],
                'res_model': 'neweb.project',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': myactive_id.id,
                'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }
