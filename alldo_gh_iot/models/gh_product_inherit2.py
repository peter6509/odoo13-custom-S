# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class producttemplateinherit2(models.Model):
    _inherit = "product.template"

    avgdata_line = fields.One2many('alldo_gh_iot.workorder_avgdata', 'prod_id', copy=False)
    pdf_preview = fields.Binary(string="PDF文件", attachment=True)

    def run_tot_avg_data(self):  # cron job 每日執行一次 (夜間執行)
        self.env.cr.execute("""select geniotseq()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select genallavgdata()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gentotavgdata1()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gentotavgdata()""")
        self.env.cr.execute("""commit""")



class ghproductinherit2(models.Model):
    _name = "alldo_gh_iot.workorder_avgdata"
    _order = "sequence,id"

    @api.depends('prod_id','eng_type')
    def _compute_prodrealnum(self):
        for rec in self:
            self.env.cr.execute("""select getprodrealnum(%d,'%s')""" % (rec.prod_id.id,rec.eng_type))
            rec.prod_real_num = self.env.cr.fetchone()[0]

    @api.depends('prod_id','eng_type')
    def _compute_reprealtime(self):
        for rec in self:
            self.env.cr.execute("""select getreprealtime(%d,'%s')""" % (rec.prod_id.id,rec.eng_type))
            rec.replace_real_time = self.env.cr.fetchone()[0]

    sequence = fields.Integer(string="SEQ", default=10)
    prod_id = fields.Many2one('product.template', ondelete='cascade')
    eng_type = fields.Char(string="工程別名稱")
    iot_machine = fields.Char(string="加工機器")
    iot_single_avg = fields.Float(digits=(10,1),string="單件總平均時間(分)")
    iot_min_avg = fields.Float(digits=(10,1),string="最快前五件時間(分)")
    is_combine = fields.Boolean(string="有中暫停", default=False)
    prod_real_num = fields.Integer(string="近三月實際量(H)",compute=_compute_prodrealnum)
    replace_real_time = fields.Integer(string="架機均值(H)",compute=_compute_reprealtime)


