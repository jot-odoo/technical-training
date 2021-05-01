from datetime import date, timedelta
from odoo import api, fields, models


class Rental(models.Model):
    _name = 'library.rental'
    _description = 'Single Rental of a Book'

    customer_id = fields.Many2one(string='Borrower',
                                  comodel_name='res.partner',
                                  required=True)
    book_id = fields.Many2one(string='Book',
                              comodel_name='library.copy',
                              required=True)
    start_date = fields.Date(string='Start Date',
                             required=True,
                             default=fields.Date.today)
    duration = fields.Integer(string='Loan Duration', required=True,
                              default=7)  # In days

    due_date = fields.Date(string='Due Date',
                           required=True,
                           compute='_compute_due_date',
                           inverse='_inverse_due_date')
    is_returned = fields.Boolean(string='Returned?', default=False)

    @api.depends('start_date', 'duration')
    def _compute_due_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.due_date = record.start_date
            else:
                duration = timedelta(days=record.duration)
                record.due_date = record.start_date + duration

    def _inverse_due_date(self):
        for record in self:
            if record.start_date and record.due_date:
                record.duration = (record.due_date - record.start_date).days

    @api.onchange('is_returned')
    def _onchange_is_returned(self):
        if (self.is_returned):
            self.due_date = date.today()
