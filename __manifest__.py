# -*- coding: utf-8 -*-
{
    'name': u'Studio customizations',
    'version': '1.0',
    'category': 'Studio',
    'description': u"""
This module has been generated by Odoo Studio.
It contains the apps created with Studio and the customizations of existing apps.
""",
    'author': u'PWTCBookingSystem1',
    'depends': [
        u'base',
        'website',
#         u'hr',
#         u'hr_holidays',
    ],
    'data': [
#         'data/res_groups.xml',
#         'data/ir_model.xml',
#         'data/ir_model_fields.xml',
#         'data/ir_ui_view.xml',
#         'data/ir_actions_act_window.xml',
#         'data/ir_ui_menu.xml',
#         'data/ir_model_access.xml',

        'views/booking_website_views.xml',
    ],
    'application': False,
    'license': u'OPL-1',
}
