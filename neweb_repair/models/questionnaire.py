# -*- coding:utf-8 -*-

from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)


class Questionnaire(models.Model):
    _name = 'neweb_repair.questionnaire'
    _description = "Questionnaire"
    _sql_constraints = [('questionnaire_no_uniq', 'unique(name)', 'Questionnaire Name must be unique!!')]

    name = fields.Char(string="Questionnaire Category", required=True)
    code = fields.Char(string="Code")
    disabled = fields.Boolean(string='Disabled')
    question_ids = fields.One2many('neweb_repair.question', 'questionnaire_id', string="Questions", required=True)

    _defaults = {
        'disabled': False
    }


class Question(models.Model):
    _name = 'neweb_repair.question'
    _description = "Question"
    _sql_constraints = [('question_no_uniq', 'unique(name)', 'Question must be unique!!')]

    name = fields.Char(string="Question", required=True)
    disabled = fields.Boolean(string='Disabled')
    questionnaire_id = fields.Many2one('neweb_repair.questionnaire', ondelete='cascade', string="Questionnaire Category")

    _defaults = {
        'disabled': False
    }
