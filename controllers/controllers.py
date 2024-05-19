# -*- coding: utf-8 -*-
# from odoo import http


# class OwlTodoList(http.Controller):
#     @http.route('/owl_todo_list/owl_todo_list', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/owl_todo_list/owl_todo_list/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('owl_todo_list.listing', {
#             'root': '/owl_todo_list/owl_todo_list',
#             'objects': http.request.env['owl_todo_list.owl_todo_list'].search([]),
#         })

#     @http.route('/owl_todo_list/owl_todo_list/objects/<model("owl_todo_list.owl_todo_list"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('owl_todo_list.object', {
#             'object': obj
#         })
