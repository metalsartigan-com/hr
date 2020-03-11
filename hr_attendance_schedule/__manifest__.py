##############################################################################
#
#    Copyright (C) 2017 Métal Sartigan <jtheriault@metalsartigan.com>
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
    'name': "Attendance Schedule",
    'version': '12.0.1.0.0',
    'author': "Métal Sartigan, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    'website': "https://github.com/OCA/hr",
    'category': 'Human Resources',
    'depends': ['hr_attendance'],
    'data': [
        'views/hr_attendance.xml',
        'views/hr_attendance_schedule_assets.xml',
        'views/res_calendar_attendance.xml',
    ],
    'demo': [
        'demo/hr_attendance_schedule.xml',
    ],
    'installable': True,
}