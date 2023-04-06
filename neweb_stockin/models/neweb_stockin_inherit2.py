# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
# import dateutil.parser
# b = "2015-10-28 16:09:59"
# d = dateutil.parser.parse(b).date()
# print d

class newebstockininherit1(models.Model):
    _inherit = "stock.picking"

    @api.depends('scheduled_date')
    def _get_scheduled_date(self):
        for rec in self:
            rec.scheduled_date1 = dateutil.parser.parse(scheduled_date).date()

    neweb_outmemo = fields.Text(string="NEWEB出貨備註")
    stockin_email = fields.Many2many('hr.employee', 'stock_picking_stockin_email_rel', 'pid', 'eid',
                                     string="進貨額外收信人")
    scheduled_date1 = fields.Date(string="預計出貨日",default=fields.Date.today())
    scheduled_date = fields.Date(string="預計出貨日",default=fields.Date.today())



# class newebstickshiplistinherit(models.Model):
#     _inherit = "neweb.stockship_list"
#
#     sequence = fields.Integer()