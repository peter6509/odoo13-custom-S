from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval


class HelpdeskTeam(models.Model):

    _name = "helpdesk.ticket.team"
    _description = "客服單據群組"
    _inherit = ["mail.thread", "mail.alias.mixin"]

    name = fields.Char(string="單號", required=True)
    user_ids = fields.Many2many(comodel_name="res.users", string="人員")
    active = fields.Boolean(default=True,string="生效")
    category_ids = fields.Many2many(
        comodel_name="helpdesk.ticket.category", string="類別"
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="公司",
        default=lambda self: self.env.company,
    )
    user_id = fields.Many2one(
        comodel_name="res.users", string="成員領導", check_company=True,
    )
    alias_id = fields.Many2one(
        comodel_name="mail.alias",
        string="Email",
        ondelete="restrict",
        required=True,
        help="The email address associated with \
                               this channel. New emails received will \
                               automatically create new tickets assigned \
                               to the channel.",
    )
    color = fields.Integer(string="顏色編號", default=0)
    ticket_ids = fields.One2many(
        comodel_name="helpdesk.ticket", inverse_name="team_id", string="單據",
    )

    todo_ticket_count = fields.Integer(
        string="單據數量", compute="_compute_todo_tickets"
    )
    todo_ticket_count_unassigned = fields.Integer(
        string="未指派單據數量", compute="_compute_todo_tickets"
    )
    todo_ticket_count_unattended = fields.Integer(
        string="尚未關注單據數量", compute="_compute_todo_tickets"
    )
    todo_ticket_count_high_priority = fields.Integer(
        string="高優先等級單據數量", compute="_compute_todo_tickets"
    )

    @api.depends("ticket_ids", "ticket_ids.stage_id")
    def _compute_todo_tickets(self):
        ticket_model = self.env["helpdesk.ticket"]
        fetch_data = ticket_model.read_group(
            [("team_id", "in", self.ids), ("closed", "=", False)],
            ["team_id", "user_id", "unattended", "priority"],
            ["team_id", "user_id", "unattended", "priority"],
            lazy=False,
        )
        result = [
            [
                data["team_id"][0],
                data["user_id"] and data["user_id"][0],
                data["unattended"],
                data["priority"],
                data["__count"],
            ]
            for data in fetch_data
        ]
        for team in self:
            team.todo_ticket_count = sum([r[4] for r in result if r[0] == team.id])
            team.todo_ticket_count_unassigned = sum(
                [r[4] for r in result if r[0] == team.id and not r[1]]
            )
            team.todo_ticket_count_unattended = sum(
                [r[4] for r in result if r[0] == team.id and r[2]]
            )
            team.todo_ticket_count_high_priority = sum(
                [r[4] for r in result if r[0] == team.id and r[3] == "3"]
            )

    def get_alias_model_name(self, vals):
        return "helpdesk.ticket"

    def get_alias_values(self):
        values = super().get_alias_values()
        values["alias_defaults"] = defaults = safe_eval(self.alias_defaults or "{}")
        defaults["team_id"] = self.id
        return values
