# -*- coding: utf-8 -*-
#
#    Author: Jacques-Etienne Baudoux <je@bcim.be>. BCIM sprl
#    Contributor: 
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


from openerp import models, fields


class ResCountryZone(models.Model):
    '''Commercial Zone to group cities/zip for segmentation'''

    _name = 'res.country.zone'
    _description = __doc__

    name = fields.Char('Commercial Zone', requried=True)
    zip_ids = fields.One2many('res.better.zip', 'state_id', 'Cities')
