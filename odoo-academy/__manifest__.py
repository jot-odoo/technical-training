# -*- coding: utf-8 -*-
{
    'name':
    "Odoo Academy",
    'summary':
    """
        Manage trainings""",
    'description':
    """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,
    'author':
    "My Company",
    'website':
    "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':
    'Training',
    'version':
    '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sales_views_inherit.xml',
        'views/products_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
