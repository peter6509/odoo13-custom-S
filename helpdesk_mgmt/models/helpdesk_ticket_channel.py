from odoo import fields, models


class HelpdeskTicketChannel(models.Model):

    _name = "helpdesk.ticket.channel"
    _description = "客服單據管道"

    name = fields.Char(required=True,string="名稱")
    active = fields.Boolean(default=True,string="生效")
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="公司",
        default=lambda self: self.env.company,
    )
