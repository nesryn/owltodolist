# -*- coding: utf-8 -*-

from odoo import models, fields, api


class owlTodo(models.Model):
    _name = 'owl.todo.list'

    name = fields.Char('Task name')
    done = fields.Boolean()
    color = fields.Char()

