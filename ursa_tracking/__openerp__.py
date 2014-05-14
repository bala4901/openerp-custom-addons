# -*- coding: utf-8 -*-
##############################################################################
#
#    Ursa Information Systems
#    Author: Adam O'Connor, Balaji Kannan
#    Copyright (C) 2013 (<http://www.ursainfosystems.com>).
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
############################################################################################################################################################

{
    "name" : "Tracking Numbers",
    "version" : "1.0",
    "author" : ["Ursa Information Systems, USA"],
    "category": 'Delivery Management',
    'complexity': "normal",
    "description": """
    Tracking Numbers: adds a new model to store multiple tracking numbers for one delivery order. 
    """,
    'website': 'http://www.ursainfosystems.com',
    "depends" : ['base', 'delivery'],
    "data" : ['security/ir.model.access.csv',],
    'init_xml': [],
    'update_xml': ['tracking_view.xml'],
    'demo_xml': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
