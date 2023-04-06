from odoo import fields, models


class HelpdeskTicketTag(models.Model):
    _name = "helpdesk.ticket.tag"
    _description = "客服單據標簽"

    name = fields.Char(string="單號")
    color = fields.Integer(string="顏色編號")
    active = fields.Boolean(default=True,string="生效")
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="公司",
        default=lambda self: self.env.company,
    )
