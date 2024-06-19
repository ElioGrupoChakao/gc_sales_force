# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "gc_sales_force",
    'version': '0.1',
    'category' : 'Sales',
    'author': 'Grupo Chakao',
    'maintainer': 'Eliomar Alberto Rodríguez Castro',
    'description': "Módulo personalizado para Fuerza de Ventas",
    'images' : [],
    'depends' : [
        'base',
        'sale',

    ],
    'data': [
        'security/sales_force_access.xml',
        'views/sales.xml',

    ],
    
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'logo': 'gc_sales_force,static/img/sales_force.png',
    'default_action': 'sale.action_orders',
    'default_view': 'gc_sales_force.view_welcome'
}

