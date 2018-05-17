# -*- coding: utf-8 -*-

from openerp import models, fields, api


class AcademyCourses(models.Model):
    _inherit = 'product.template'
    _description = 'Academy Courses'
    # _inherit = ['product.template','mail.thread']

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string='Teachers')
