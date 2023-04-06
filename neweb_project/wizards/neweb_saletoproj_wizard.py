# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import datetime


class newebsaletoprojwizard(models.TransientModel):
    _name = "neweb.saletoproj"

    proj_branch = fields.Many2one('neweb.projbranch', string="專案成本分區", required=True)
    proj_sale = fields.Many2one('hr.employee', string='專案業務', required=True)
    cost_type = fields.Many2one('neweb.costtype', string="專案成本類型",default='1')


    @api.onchange("proj_branch")
    def onchange_proj_id(self):
        res = {}
        mysaleid = self.env.context.get("sale_op_id")
        myrec = self.env['sale.order'].search([('id', '=', mysaleid)])
        myid = myrec.user_id.id
        myemprec = self.env['hr.employee'].search([('user_id', '=', myid)])
        if myemprec:
            self.proj_sale = myemprec[0].id
        ids = []
        for item in myemprec:
            ids.append(item.id)
        if myid:
           res['domain'] = {'proj_sale': [('id', 'in', ids)]}
        else:
           res['domain'] = {'proj_sale': [(1,'=',1)]}

        return res


    # @api.multi
    def saletoproj_wizard(self):
        mysaleorderid = self.env.context.get('sale_op_id')
        mysaleorder = self.env['sale.order'].search([('id', '=', self.env.context.get('sale_op_id'))])
        mysaleno = mysaleorder.name
        self.env.cr.execute("""select hasdisamount(%d)""" % self.env.context.get('sale_op_id'))
        myres = self.env.cr.fetchone()
        if not myres[0]:
            raise UserError("給予最優惠總價不能為0,請確認")
        # raise UserError("%s" % mysaleno)
        self.env.cr.execute("""select chksalenotoproj('%s')""" % mysaleno)
        myres = self.env.cr.fetchone()[0]
        if myres:
            raise UserError("已經轉專案成本分析了...")
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
        myprojname=''
        if gencode_rec:
            strcode = str(gencode_rec.gencode + 1)
            mygencode = gencode_rec.gencode + 1
            mycode = strcode.zfill(3)
            myprojname = "%sSVC%s-%s" % (myprefixcode, myym, mycode)
            # gencode_rec.write({'gencode':mygencode})
            gencode_rec.gencode = mygencode
        else:
            myprojname = "%sSVC%s-001" % (myprefixcode, myym)
            gencode_rec.create({'name': myym, 'prefixcode': myprefixcode, 'gencode': 2})
        mycount = self.env['neweb.project'].search_count([('name', '=', myprojname)])
        if mycount > 0:
            self.env.cr.execute("""select genovergencode('%s')""" % myprojname)
            myprojname = self.env.cr.fetchone()[0]
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
             'description': mycus.description, 'memo': mycus.memo,'sale_no': mysalerec.name,
             'open_account_day':mysalerec.open_account_day,
             'open_account_day1':mysalerec.open_account_day1.id,'open_account_day2':mysalerec.open_account_day2.id,
             'cus_project':mysalerec.project_name,'acc_close_day1':mycloseday[0]})

        #print "myactive_id:%s" % myactive_id.id
        self.env.cr.execute("""select gensaletoprojdata(%d,%d)""" % (mysaleorderid, myactive_id.id))
        self.env.cr.execute("""commit""")
        myitemrec = self.env['neweb.projsaleitem'].search([('saleitem_id','=',myactive_id.id)])
        for line in myitemrec:
            self.env.cr.execute("""select genprojchiprodno1(%d)""" % line.id)
            self.env.cr.execute("""commit""")
        newrec = self.env['neweb.project'].search([('id', '=', myactive_id.id)])


        if not mycus.street:
            cstreet='-'
        else:
            cstreet=mycus.street.replace("'","''")
        if not mycus.phone:
            cphone='-'
        else:
            cphone=mycus.phone
        # if not mycus.fax:
        cfax='-'
        # else:
        #     cfax=mycus.fax
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
            cfax='-'
            # if not child_rec.fax:
            #     cfax='-'
            # else:
            #     cfax=child_rec.fax
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

        newrec.env.cr.commit()
        mydomain = []
        mydomain.append(('id', '=', myactive_id.id))
        self.env.context = dict(self.env.context)
        self.env.context.update({'proj_op_id':myactive_id.id})
        print("SALE ID:%d" % myactive_id.id)
        # mytag_rec = self.env['neweb.projtag'].search([])
        # mytag_count = self.env['neweb_projtag'].search_count([])
        # if mytag_count==0:
        #     mytag_rec.create({'proj_id':myactive_id.id})
        # else:
        #     mytag_rec.write({'proj_id':myactive_id.id})
        self.env.cr.execute("""delete from neweb_projanalysis where analysis_id=%d""" % myactive_id.id)
        self.env.cr.execute("""commit""")
        self.env.cr.execute("select proj_cal_cost(%s)" % myactive_id.id)

        self.env.cr.execute("""delete from neweb_setupcost_line where project_id=%d ;""" % myactive_id.id)
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""delete from neweb_maincost_line where project_id=%d ;""" % myactive_id.id)
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gencostdeptdata(%d)""" % myactive_id.id)
        self.env.cr.execute("""commit""")

        self.env.cr.execute("""select getsetupanalysistotrev(%d)""" % myactive_id.id)
        mysetupanalysisrev = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getsetupanalysistotcost(%d)""" % myactive_id.id)
        # mysetupanalysiscost = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getmainanalysistotrev(%d)""" % myactive_id.id)
        mymainanalysisrev = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getmainanalysistotcost(%d)""" % myactive_id.id)
        mymainanalysiscost = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getsetupdeptrev(%d)""" % myactive_id.id)
        mysetupdeptrev = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select getsetupdeptcost(%d)""" % myactive_id.id)
        # mysetupdeptcost = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getmaindeptrev(%d)""" % myactive_id.id)
        mymaindeptrev = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getmaindeptcost(%d)""" % myactive_id.id)
        mymaindeptcost = self.env.cr.fetchone()[0]
        mystatus1=''
        if abs(mysetupanalysisrev - mysetupdeptrev) > 10:
            mystatus1 = mystatus1 + '(建置)成本分析收入:%s ,(建置)歸戶收入:%s 不合！' % (mysetupanalysisrev, mysetupdeptrev)
        elif abs(mymainanalysisrev - mymaindeptrev) > 10:
            mystatus1 = mystatus1 + '(維護)成本分析收入:%s ,(維護)歸戶收入:%s 不合！' % (mymainanalysisrev, mymaindeptrev)
        # elif abs(mysetupanalysiscost - mysetupdeptcost) > 10:
        #     mystatus = mystatus + '(建置)成本分析成本:%s ,(建置)歸戶成本:%s 不合！' % (mysetupanalysiscost, mysetupdeptcost)
        elif abs(mymainanalysiscost - mymaindeptcost) > 10:
            mystatus1 = mystatus1 + '(維護)成本分析成本:%s ,(維護)歸戶成本:%s 不合！' % (mymainanalysiscost, mymaindeptcost)
        else:
            mystatus1 = 'Balance'
        if mystatus1 == 'Balance':
            self.env.cr.execute("""update neweb_project set proj_status='Balance',proj_write_num=1 where id=%d""" % myactive_id.id)

        else:
            self.env.cr.execute("""update neweb_project set proj_status='%s',proj_write_num=1 where id=%d""" % (mystatus1, myactive_id.id))

        self.env.cr.execute("""commit""")
        self.proj_status1 = mystatus1
        return {'view_name': 'newebprojwizard',
                'name': ('專案維護'),
                'views': [[False, 'form'], ],
                'res_model': 'neweb.project',
                'domain':mydomain,
                "context": {'proj_op_id':myactive_id.id},
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': myactive_id.id,
                'flags': {'action_buttons': True},
                'view_mode': 'form',
                'view_type': 'form'
                }
