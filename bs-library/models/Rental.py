import re
from odoo import api, fields, models


class Rental(models.Model):
    _name = 'library.rental'
    _description = 'Single Rental of a Book'

    customer_id = fields.Many2one(string='Borrower',
                                  comodel_name='res.partner',
                                  required=True)
    book_id = fields.Many2one(string='Book',
                              comodel_name='library.bookcopy',
                              required=True)
    start_date = fields.Date(string='Start Date', required=True)
    due_date = fields.Date(string='Due Date', required=True)
    is_returned = fields.Boolean(string='Returned?', default=False)