# -*- coding: utf-8 -*-
from openerp import http


class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public', website=True)
    # @http.route('/academy/academy/', auth='public')
    def index(self, **kw):
        # return "Hello, world"
        Teachers = http.request.env['academy.teachers']
        return http.request.render('academy.index', {
            'teachers': Teachers.search([]),
            'list_teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
        })
    
    @http.route('/academy/<name>/', auth='public', website=True)
    def teacher(self, name):
        return '<h1>{}</h1>'.format(name)

    @http.route('/academy/list/<int:id>', auth='public', website=True)
    def teacher_list(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

# class Academy(http.Controller):
#     @http.route('/academy/academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy/academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy.listing', {
#             'root': '/academy/academy',
#             'objects': http.request.env['academy.academy'].search([]),
#         })

#     @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy.object', {
#             'object': obj
#         })