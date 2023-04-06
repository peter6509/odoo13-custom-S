# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _


class Questionnaire(models.Model):
	_name = "neweb_base.questionnaire"
	_description = "Questionnaire"

	name = fields.Char(string="Questionnaire Category", required=True)
	#questionnaire_category = fields.Selection([('maintenance','Maintenance Questionnaire'),('annual','Annual Questionnaire')], string='Questionnaire Category')
	question_1 = fields.Char(string="Question 1", required=True)
	question_2 = fields.Char(string="Question 2")
	question_3 = fields.Char(string="Question 3")
	question_4 = fields.Char(string="Question 4")
	question_5 = fields.Char(string="Question 5")
	question_6 = fields.Char(string="Question 6")
	question_7 = fields.Char(string="Question 7")
	question_8 = fields.Char(string="Question 8")
	question_9 = fields.Char(string="Question 9")
	question_10 = fields.Char(string="Question 10")
	disabled = fields.Boolean(string="Disabled")

