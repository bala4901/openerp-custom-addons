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
    'name': "Transaction Category",
    'version': "1.0",
    'depends': ['base', 'account', 'account_accountant', 'analytic', 'product',
                ],
    'author': "Ben Olsen",
    'description':  """
                    Adds financial transaction categories, which limit the real and analytic accounts that
                    a given transaction (invoice line, etc) can select. For situations when allowing any
                    transaction to be booked to any account/analytic combination isn't reasonable.
                    """,
    'category': "Uncategorized",
    'data': ['txn_category_view.xml',
             'account_invoice_view.xml',
            ],
	'css' : [
		"static/src/css/txn_category_style.css",
	],
    'installable': True,
    'auto_install': False,
}