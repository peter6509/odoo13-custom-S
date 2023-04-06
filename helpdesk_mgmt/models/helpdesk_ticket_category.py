from odoo import fields, models


class HelpdeskCategory(models.Model):

    _name = "helpdesk.ticket.category"
    _description = "客服單據分類"

    active = fields.Boolean(string="生效", default=True,)
    name = fields.Char(string="名稱", required=True,)
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="公司",
        default=lambda self: self.env.company,
    )
