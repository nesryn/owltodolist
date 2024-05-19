# -*- coding: utf-8 -*-
{
    'name': "owl_todo_list",

    'summary': """
        Todo list """,
    'sequence': -1,

    'description': """
      
    """,

    'author': "Nesrine Essaies",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'assets': {
        'web.assets_backend': [
            'owl_todo_list/static/src/components/*/*.xml',
            'owl_todo_list/static/src/components/*/*.js',
            'owl_todo_list/static/src/components/*/*.scss',

        ],
    },

    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/views.xml',
    ],

}
