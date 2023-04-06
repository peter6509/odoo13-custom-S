from odoo import fields, models


class HelpdeskTicketStage(models.Model):
    _name = "helpdesk.ticket.stage"
    _description = "客服單據階段"
    _order = "sequence, id"

    name = fields.Char(string="階段名稱", required=True, translate=True)
    description = fields.Html(translate=True, sanitize_style=True,string="說明")
    sequence = fields.Integer(default=1,string="序")
    active = fields.Boolean(default=True,string="生效")
    unattended = fields.Boolean(string="無人")
    closed = fields.Boolean(string="結束")
    mail_template_id = fields.Many2one(
        comodel_name="mail.template",
        string="Email樣板",
        domain=[("model", "=", "helpdesk.ticket")],
        help="If set an email will be sent to the "
        "customer when the ticket"
        "reaches this step.",
    )
    fold = fields.Boolean(
        string="在看板中收隴",
        help="This stage is folded in the kanban view "
        "when there are no records in that stage "
        "to display.",
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="公司",
        default=lambda self: self.env.company,
    )
