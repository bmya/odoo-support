# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
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
    "name": "ADHOC Modules",
    "version": "8.0.0.0.0",
    'author':  'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'adhoc_modules',
        'mass_editing',
        ],
    'external_dependencies': {
        'python': ['octuhub']
        },
    'data': [
        'views/adhoc_module_repository_view.xml',
        'views/adhoc_module_category_view.xml',
        'views/adhoc_module_view.xml',
        'security/ir.model.access.csv',
        'data/mass_editting_data.xml',
        ],
    'demo': [],
    'test': [],
    'installable': True,
    'active': False,
    'auto_install': True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
