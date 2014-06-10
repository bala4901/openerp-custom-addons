# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 IMSAR
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': "IMSAR Accounting",
    'version': "1.0",
    'depends': ['base', 'web_m2x_options',
                'imsar_default_data',
                'l10n_us', 'account_chart', 'account_accountant', 'analytic',
                ],
    'author': "Ben Olsen",
    'description': "Customized IMSAR chart of accounts",
    'category': "Uncategorized",
    'data': ['accounting_data.xml',
             'imsar_account_type.xml',
             'account.account.template.csv',
             'account.analytic.account.csv',
             'accounting_data_after.xml',
            ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: