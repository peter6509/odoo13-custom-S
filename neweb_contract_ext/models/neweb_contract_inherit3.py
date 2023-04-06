# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import logging
import datetime, pytz
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

_logger = logging.getLogger(__name__)

class newebcontractinherit3(models.Model):
    _inherit = "neweb_contract.contract"

    contract_newold = fields.Selection([('1','新合約'),('2','續約')],string="維護合約類型",default='1')
    satisfaction_person = fields.Many2many('res.partner','neweb_contract_satisfaction_partner_rel','contract_id','partner_id',string="寄送滿意度調查人員")
    is_warranty_contract = fields.Boolean(string="保固支援合約")
    hasbackuphw = fields.Boolean(string="備品置客戶端?", default=False)
    isduedate = fields.Boolean(string="是否30天到期歸還期?",default=False)

    def get_hasbackuphw_emails(self,myid):
        mymail=''
        mymaillist=[]
        myrec = self.env['neweb_contract.contract'].search([('id','=',myid)])
        for rec in myrec:
            if rec.sales and rec.sales.work_email not in mymaillist:
               mymaillist.append(str(rec.sales.work_email))
            if rec.sales.partner_id and rec.sales.partner_id.work_email not in mymaillist:
               mymaillist.append(str(rec.sales.partnet_id.work_email))
            for line in rec.ae1:
                if line.work_email not in mymaillist:
                   mymaillist.append(str(line.work_email))
                if line.parent_id and line.parent_id.work_email not in mymaillist:
                   mymaillist.append(str(line.partner_id.work_email))
        if 'evan.dai@newebinfo.com.tw' not in mymaillist:
            mymaillist.append('evan.dai@newebinfo.com.tw')
        if 'leno.wu@newebinfo.com.tw' not in mymaillist:
            mymaillist.append('leon.wu@newebinfo.com.tw')
        if 'alice.fu@newebinfo.com.tw' not in mymaillist:
            mymaillist.append('alice.fu@newebinfo.com.tw')
        if 'wayne.hsieh@newebinfo.com.tw' not in mymaillist:
            mymaillist.append('wayne.hsieh@newebinfo.com.tw')
        for rec in mymaillist:
            if mymail =='':
                mymail = rec
            else:
                mymail = mymail + ','.join(rec)
        return mymail


    def run_check_hasbackuphw(self):
        _logger.info("process_return_backuphw")
        # Contract-Special_Warn_template
        self.env.cr.execute("""select runcheckduedate()""")
        self.env.cr.execute("commit")
        mail_tmp_id = self.env['mail.template'].search([('name', '=', 'Contract-hasbackuphw-email')])
        _logger.info("mail tmp id is %s" % mail_tmp_id.id)
        now = datetime.datetime.now()
        contract_rec= self.env['neweb_contract.contract'].search([('hasbackuphw', '=', True), ('isduedate','=',True)])
        for contract in contract_rec:
            self.pool['mail.template'].send_mail(self.env.cr, self.env.uid, mail_tmp_id.id, contract.id,force_send=True, context=self.env.context)


    def write(self, vals):

        res = super(newebcontractinherit3, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select check_subscribebuild(%d)""" % rec.id)
            self.env.cr.execute("""commit""")

        return res


    def subscribe_reset(self):
        # print "start step"
        mycontractid = self.env.context.get('contract_id', False)
        mycontractrec = self.env['neweb_contract.contract'].search([('id', '=', mycontractid)])
        if mycontractrec.maintenance_start_date == False or mycontractrec.maintenance_end_date == False :
            raise UserError("起迄時間不完整,請確認!!")
        mystartdate = mycontractrec.maintenance_start_date
        myenddate = mycontractrec.maintenance_end_date
        if mystartdate >= myenddate:
            raise UserError("輸入的維護的起迄日期有問題,請確認!!")

        if mycontractrec.routine_maintenance_new.id == '1':
            inspectionmode = '1'
        elif mycontractrec.routine_maintenance_new.id == '2':
            inspectionmode = '3'
        elif mycontractrec.routine_maintenance_new.id == '3':
            inspectionmode = '2'
        elif mycontractrec.routine_maintenance_new.id == '4':
            inspectionmode = '4'
        else:
            inspectionmode = '5'
        # print "step 1"
        myuid = self.env.uid
        self._cr.execute("""select delinspectionlist(%d,%d)""" % (mycontractid,myuid))
        self._cr.execute("""commit;""")

        self._cr.execute("select gen_contract_list(%s,%s,%d)" % (mycontractid, inspectionmode,myuid))
        self._cr.execute("commit;")
        # print "step 2"
        mycontractrec.write({'subscribe_build': True})
        return {'view_name': 'contractinherit',
                'name': ('合約維護作業'),
                'views': [[False, 'form'], [False, 'tree']],
                'res_model': 'neweb_contract.contract',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'main',
                'res_id': mycontractid,
                'view_mode': 'form',
                'view_type': 'tree,form',
                'flags': {'action_buttons': True, 'initial_mode': 'edit'},
                }
