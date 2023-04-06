# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _


class Problem(models.Model):
	_name = 'neweb_base.problem'
	_description = "Problem"
	_sql_constraints = [('name_maintenance_category_uniq', 'unique(name, maintenance_category_id)', 'Problem Name + Maintenance Category must be unique!!')]

	name = fields.Char(string='Problem Name', required=True)
	disabled = fields.Boolean(string='Disabled')
	memo = fields.Text(string='Remark')
	description = fields.Text(string='Problem Description', required=True)
	# problem_representation = fields.One2many('neweb_base.problem_representation', 'problem_id', string="Problem Representation")
	problem_solution = fields.One2many('neweb_base.problem_solution', 'problem_id', string="Problem Solution")
	maintenance_category_id = fields.Many2one('neweb_base.maintenance_category', string="Maintenance Category", required=True, default=lambda self: self.env.context.get('maintenance_category', self.env['neweb_base.maintenance_category']))

	# 2016/01/05 SP6新增需求欄位
	problem_category = fields.Char(string='Problem Category')
	err_code = fields.Char(string='Error Code')
	err_log = fields.Char(string='Error Log')
	event_log = fields.Char(string='Event Log')

# class ProblemRepresentation(models.Model):
# 	_name = 'neweb_base.problem_representation'
# 	_description = "Problem Representation"
# 	_sql_constraints = [('name_uniq', 'unique(name)', 'Problem Representation must be unique!!')]
#
# 	name = fields.Char(string="Problem Representation", required=True, translate=True)
# 	disabled = fields.Boolean(string='Disabled')
# 	memo = fields.Text(string='Remark')
#
# 	problem_id = fields.Many2one('neweb_base.problem', string="Problem", required=True, default=lambda self: self.env.context.get('problem', self.env['neweb_base.problem']))


class ProblemSolution(models.Model):
	_name = 'neweb_base.problem_solution'
	_description = "Problem Solution"
	_sql_constraints = [('name_uniq', 'unique(name)', 'Problem Solution must be unique!!')]

	name = fields.Char(string="Problem Solution", required=True, translate=True)
	disabled = fields.Boolean(string='Disabled')
	memo = fields.Text(string='Remark')
	problem_id = fields.Many2one('neweb_base.problem', string="Problem", required=True, default=lambda self: self.env.context.get('problem', self.env['neweb_base.problem']))
