# -*- coding: utf-8 -*-
from openerp import models, fields, api


class StockPackOperation(models.Model):

    _inherit = 'stock.pack.operation'

    @api.one
    def _get_running_number(self):
        '''Assigns a running number to the invoice3 line, starting from 1 onwards '''

        '''Get all lines related to the current Invoice. '''
        pack_operation_lines = self.search(args=[('picking_id', '=', self.picking_id.id)])

        i = 1
        for line in pack_operation_lines:
            if line.id == self.id:
                self.running_number = i
                break
            i += 1

    running_number = fields.Integer('Running Number', compute=_get_running_number)
