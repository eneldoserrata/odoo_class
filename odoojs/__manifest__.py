# -*- coding: utf-8 -*-
{
    'name': "odoojs",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "La clase",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/course_view.xml',
        'views/teacher_view.xml',
        'views/students_view.xml',
        'views/action_client_view.xml',
    ],
    # only loaded in demonstration mode
    'qweb': [
        'static/src/xml/odoojs.xml',
        'static/src/xml/jeff.xml',
        ],
    'demo': [
        'demo/demo.xml',
    ],
}