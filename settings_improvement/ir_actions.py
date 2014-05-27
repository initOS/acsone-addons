# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2014 Acsone SA/NV (http://www.acsone.eu)
# All Rights Reserved
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsibility of assessing all potential
# consequences resulting from its eventual inadequacies and bugs.
# End users who are looking for a ready-to-use solution with commercial
# guarantees and support are strongly advised to contact a Free Software
# Service Company.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from openerp.osv import orm

class act_window(orm.Model):
    _inherit = 'ir.actions.act_window'

    def button_goto_action(self, cr, uid, act_id, context=None):
        if isinstance(act_id, (int, long)):
            act_id = [act_id]
        action = self.read(cr, uid, act_id, [], context)[0]
        action.update({'groups_id': False,
                       'search_view': False,
                      })
        return action

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
