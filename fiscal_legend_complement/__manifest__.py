# -*- encoding: utf-8 -*-
{
    'name': 'Fiscal legend complement biooni',
    'author': '',
    'category': 'Account',
    'sequence': 50,
    'summary': 'Fiscal legend complement biooni',
    'version': '1.0',
    'description': """
Fiscal legend complement for bioni
=====================================================
This module add the LeyendaFiscal in CFDI for biooni.
""",
    'depends': [
        'base',
        'account',
        'account_accountant',
        'l10n_mx',
        'l10n_mx_edi',
    ],
    'data': [
        'data/fiscal_legend_complement.xml',
        'views/inherit_partner_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
}
