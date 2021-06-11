# -*- coding: utf-8 -*-
{
    'name': 'Customer credit limit',
    'version': '13.0.0',
    'summary': 'This module allows to limit the sales to a customer without invoicing',
    'description': 'This module allows to limit the sales to a customer without invoicing',
    'author': 'Second Episode',
    'maintainer': '',
    'website': 'https://www.2ndepisode.com',
    'license': '',
    'contributors': [
    ],
    'depends': [
         'base',
        'product',
        'sale'
    ],
    'data': [
         'views/res_partner.xml',
    ],
    'images': ['static/description/banner.png'],
    'price': 9.99,
    'license': 'LGPL-3',
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
}
