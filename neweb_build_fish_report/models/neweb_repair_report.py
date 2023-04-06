# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request

class newebrepairreport(models.Model):
    _inherit = "neweb_repair.repair"

    def action_repair_print(self):
        self.ensure_one()
        # base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_repair_print_report/%s" % (bf_url,self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }

    def action_repair_work(self):
        self.ensure_one()
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/neweb_repair_work_report/%s" % (base_url,self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }

    @api.depends('repair_lines')
    def _get_repair_parts(self):
        mycrepairparts = ' '
        for rec in self.repair_lines:
            for rec1 in rec.repair_parts:
                if mycrepairparts == ' ':
                    mycrepairparts = rec1.prod.name
                else:
                    mycrepairparts = mycrepairparts + ' , ' + rec1.prod.name
        self.crepairparts = mycrepairparts
        return mycrepairparts

    @api.depends('repair_lines')
    def _get_problem_desc(self):
        myproblemdesc = ' '
        for rec in self.repair_lines:
            myproblemdesc = myproblemdesc + rec.problem_desc
        self.cproblemdesc = myproblemdesc
        return myproblemdesc

    @api.depends('repair_work_logs')
    def _get_work_date(self):
        mycworkdate = ' '
        for rec in self.repair_work_logs:
            if mycworkdate == ' ':
                mycworkdate = fields.Date.from_string(rec.work_date).strftime('%Y-%m-%d')
            # else:
            #     mycworkdate = mycworkdate + ', ' + fields.Date.from_string(rec.work_date).strftime('%Y%m%d')
        self.cworkdate = mycworkdate
        return mycworkdate

    @api.depends('repair_work_logs')
    def _get_work_log(self):
        for rec1 in self:
            mycworklog = ' '
            for rec in rec1.repair_work_logs:
                if mycworklog == ' ':
                    if rec.work_log:
                       mycworklog = rec.work_log
                else:
                    if rec.work_log:
                       mycworklog = mycworklog + '\r\n'+'<br>' + '@' + rec.work_log
            rec1.cworklog = mycworklog
            return mycworklog

    @api.depends('repair_care_call_logs')
    def _get_care_call(self):
        for rec1 in self:
            myccarecall= ' '
            for rec in rec1.repair_care_call_logs:
                if myccarecall == ' ':
                    if rec.care_call_log:
                       myccarecall = rec.care_call_log
                else:
                    if rec.care_call_log:
                       myccarecall = myccarecall + ', '+rec.care_call_log
            rec1.ccarecalllog = myccarecall
            return myccarecall

    @api.depends('repair_lines')
    def _get_defaultcode(self):
        for rec2 in self:
            mydefcode = ' '
            for rec in rec2.repair_lines:
                for rec1 in rec.repair_parts:
                    if mydefcode==' ':
                        if rec1.prod.name:
                           mydefcode = rec1.prod.name
                    else:
                        if rec1.prod.name:
                           mydefcode = mydefcode + ', ' + rec1.prod.name
            rec2.pproddefcode = mydefcode
            return mydefcode

    @api.depends('repair_lines')
    def _get_modeltype(self):
        for rec1 in self:
            mymodeltype = ' '
            for rec in rec1.repair_lines:
                if mymodeltype==' ':
                    if rec.contract_line.prod_modeltype:
                       mymodeltype = rec.contract_line.prod_modeltype
                else:
                    if rec.contract_line.prod_modeltype:
                        mymodeltype = mymodeltype + ', ' + rec.contract_line.prod_modeltype
            rec1.cmodeltype = mymodeltype
            return mymodeltype

    @api.depends('repair_lines')
    def _get_machineno(self):
        for rec1 in self:
            mymachineno = ' '
            for rec in rec1.repair_lines:
                if mymachineno == ' ':
                    if rec.contract_line.machine_serial_no:
                        mymachineno = rec.contract_line.machine_serial_no
                else:
                    if rec.contract_line.machine_serial_no:
                        mymachineno = mymachineno + ', ' + rec.contract_line.machine_serial_no
            rec1.cmachineno = mymachineno
            return mymachineno

    @api.depends('repair_lines')
    def _get_spec(self):
        for rec1 in self:
            cspec = ' '
            for rec in rec1.repair_lines:
                for rec2 in rec.repair_parts:
                    if cspec == ' ':
                        if rec2.prod.specification:
                          cspec = rec2.prod.specification
                    else:
                        if rec2.prod.specification:
                            cspec = cspec + ', ' + rec2.prod.specification
            rec1.cspec = cspec
            return cspec

    @api.depends('end_customer')
    def _get_endcustomer(self):
        for rec in self:
            cendcustomer=' '
            for rec1 in rec.end_customer:
                if rec1.name :
                   cendcustomer=rec1.name
            rec.cendcustomer = cendcustomer
            return cendcustomer

    @api.depends('contact_user')
    def _get_contactuser(self):
        for rec1 in self:
            ccontactuser = ' '
            for rec in rec1.contact_user:
                if rec.parent_id.name :
                    ccontactuser = rec.parent_id.name
            rec1.ccontactuser = ccontactuser
            return ccontactuser

    @api.depends('contact_user')
    def _get_contactuser1(self):
        ccontactuser1 = ' '
        for rec in self.contact_user:
            if rec.name != False:
                ccontactuser1 = rec.name
        self.ccontactuser1 = ccontactuser1
        return ccontactuser1

    @api.depends('contract_id')
    def _get_saleman(self):
        csaleman = ' '
        for rec in self.contract_id:
            if rec.sales.name != False:
                csaleman = rec.sales.name
        self.csaleman = csaleman
        return csaleman

    @api.depends('ae_id')
    def _get_aeman(self):
        caeman = ' '
        for rec in self.ae_id:
            if rec.name != False:
                caeman = rec.name
        self.caeman = caeman
        return caeman

    @api.depends('repair_lines')
    def _get_brandname(self):
        cbrandname = ' '
        for rec in self.repair_lines:
            for rec1 in rec.contract_line:
                for rec2 in rec1.prod_brand:
                    if cbrandname == ' ':
                        cbrandname = rec2.name
                    else:
                        cbrandname = cbrandname + ', ' + rec2.name
        self.cbrandname = cbrandname
        return cbrandname

    @api.depends('repair_lines')
    def _get_prodnum(self):
        mynum = 0
        for rec in self.repair_lines:
            for rec1 in rec.repair_parts:
                # if mydefcode == ' ':
                #     mydefcode = rec1.prod.default_code
                # else:
                #     mydefcode = mydefcode + ', ' + rec1.prod.default_code
                mynum = mynum + rec1.used_parts_qty
        self.pprodnum = mynum
        return mynum

    @api.depends('repair_datetime')
    def _get_repairdate(self):
        for rec in self:
            myrepairdate = rec.repair_datetime.strftime('%Y-%m-%d')
            rec.repairdate = myrepairdate
            return myrepairdate


    crepairparts = fields.Char(string="報修用料new", compute=_get_repair_parts)
    cworkdate = fields.Char(string="處理日期new", compute=_get_work_date)
    cworklog = fields.Char(string="處理內容new", compute=_get_work_log)
    cproblemdesc = fields.Char(string="問題描述",compute=_get_problem_desc)
    ccarecalllog = fields.Char(string="CARE CALL",compute=_get_care_call)
    pproddefcode = fields.Char(string="料號",compute=_get_defaultcode)
    cmodeltype = fields.Char(string="機種/機型",compute=_get_modeltype)
    cmachineno = fields.Char(string="序號",compute=_get_machineno)
    cspec = fields.Char(string="規格",compute=_get_spec)
    cendcustomer = fields.Char(string="終端客戶",compute=_get_endcustomer)
    ccontactuser = fields.Char(string="聯絡客戶",compute=_get_contactuser)
    ccontactuser1 = fields.Char(string="聯絡人",compute=_get_contactuser1)
    csaleman = fields.Char(string="業務員",compute=_get_saleman)
    caeman = fields.Char(string="工程師",compute=_get_aeman)
    cbrandname = fields.Char(string="廠牌",compute=_get_brandname)
    pprodnum = fields.Integer(string="數量",compute=_get_prodnum)
    repairdate = fields.Date(string="報修日期", compute=_get_repairdate)



class NewebRepairLineInherit(models.Model):
    _inherit = "neweb_repair.repair"

    bfrepair_line = fields.One2many('neweb_repair.bfrepair_line','repair_id',copy=False)

    @api.model
    def create(self, vals):
        res = super(NewebRepairLineInherit, self).create(vals)
        self.env.cr.execute("""select insert_bfrepair_line(%d)""" % self.id)
        self.env.cr.execute("""commit""")
        return res

    def write(self, vals):
        res = super(NewebRepairLineInherit, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select update_bfrepair_line(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res


class NewebBFRepairline(models.Model):
    _name = 'neweb_repair.bfrepair_line'

    repair_id = fields.Many2one('neweb_repair.repair',ondelete='cascade')
    prod_modeltype = fields.Char(string="機種/機型")
    machine_serial_no = fields.Char(string="序號")
    prodname = fields.Char(string="料號")
    prodspec = fields.Char(string="規格")
    usedqty = fields.Char(string="數量")
    requiredqty = fields.Char(string="需求數量")
    update_tag = fields.Boolean(string="變更記號")
