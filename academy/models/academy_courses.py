# -*- coding: utf-8 -*-

from openerp import models, fields, api


class AcademyCourses(models.Model):
    _name = 'academy.courses'

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string='Teachers')
