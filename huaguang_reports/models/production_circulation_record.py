# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools,_


class ProductionCirculationRecord(models.Model):
    _inherit = 'production.circulation.record'

    child_ids = fields.One2many('production.circulation.record',compute='_compute_child_ids',string='分单列表')
    all_record_line_ids = fields.One2many('production.circulation.record.line', compute='_compute_prc_line')
    top_parent = fields.Many2one('production.circulation.record',  string='母单')
    is_finished = fields.Boolean('完工',compute='_compute_finished', store=True)

    @api.depends('record_line_ids', 'record_line_ids.last_completed', 'record_line_ids.state')
    def _compute_finished(self):
        for pcr in self:
            # if not pcr.record_line_ids.filtered(lambda r: r.workorder_id.name in ('47检成', '24机检', '25盘丝', '49挑棒')):
            #     pcr.is_finished = False
            # elif pcr.record_line_ids.filtered(lambda r: r.workorder_id.name in ('47检成', '24机检', '25盘丝', '49挑棒')
            #                                   and r.last_completed == False):
            #     pcr.is_finished = False
            # else:
            #     pcr.is_finished = True

            ##2021年03月04日15:33:25 逻辑修改为:只要有一条最后一批完成的记录,则表达为已完成
            find_finished = self.env['production.circulation.record.line'].search([
                ('line_id','=',pcr.id),
                ('workorder_id.name','in',('47检成', '24机检', '25盘丝', '49挑棒')) ,
                ('last_completed','=',True) ,
                ('state','=','completed'),
            ],limit=1)
            if find_finished :
                pcr.is_finished = True #
            else :
                pcr.is_finished = False #
        return



    def _compute_child_ids(self):
        for pcr in self:
            child_ids = self.env['production.circulation.record'].search([('top_parent', '=', pcr.id)])
            pcr.child_ids = child_ids

    @api.depends('child_ids', 'record_line_ids')
    def _compute_prc_line(self):
        for pcr in self:
            child_ids = pcr.child_ids.filtered(lambda c: c.record_line_ids)
            record_line_ids = pcr.record_line_ids
            if child_ids:
                for child in child_ids:
                    record_line_ids += child.record_line_ids
            pcr.all_record_line_ids = record_line_ids


    def _compute_parent_id(self):
        for pcr in self:
            if pcr.parent_id:
                parent = pcr.parent_id
                pcr_ids = self.env['production.circulation.record']
                while parent:
                    pcr_ids += parent
                    parent = parent.parent_id
                pcr.top_parent = pcr_ids.sorted('id')[0]

    @api.model
    def top_parent_write(self):
        pcr = self.env['production.circulation.record'].search([('parent_id', '!=', False)])
        if pcr:
            pcr._compute_parent_id()
        return True

    @api.model
    def create(self, vals):
        res = super(ProductionCirculationRecord, self).create(vals)
        if res.parent_id:
            res._compute_parent_id()
        return res
