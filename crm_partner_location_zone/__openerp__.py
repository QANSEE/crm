# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jacques-Etienne Baudoux <je@bcim.be>
#    Copyright 2015 BCIM sprl
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
    'name': 'Segment ZIP/Cities by zone',
    'version': '0.1',
    'author': "BCIM,Odoo Community Association (OCA)",
    'maintainer': 'BCIM',
    'category': 'Customer Relationship Management',
    'complexity': 'easy',
    'depends': ['crm','base_location'],
    'website': 'http://www.bcim.be',
    'data': [
        'view/better_zip_view.xml',
        'view/lead_view.xml',
        'view/partner_view.xml',
        'view/zone_view.xml',
    ],
    'demo': [],
#    'test': ['test/test_street3.yml'],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
    'application': False,
}
