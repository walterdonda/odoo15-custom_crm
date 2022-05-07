# -*- coding: utf-8 -*-
{
    'name': "custom_crm",

    'summary': """
        Módulo personalizado para la gestión de visitas a clientes, probando inotify""",

    'description': """
        El módulo se crea por la necesidad de poder registrar distintas formas de visitas
        y registrar los costos relacionados.
    """,

    'author': "Walter Donda",
    'website': "http://www.nombreadeterminar.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/visit.xml',
        'views/templates.xml',
        'reports/visit_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
