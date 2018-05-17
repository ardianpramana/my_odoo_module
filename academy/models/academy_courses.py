# -*- coding: utf-8 -*-

from openerp import models, fields, api


class AcademyCourses(models.Model):
    _name = 'academy.courses'
    _description = 'Academy Courses'
    _inherit = ['mail.thread']

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string='Teachers')
