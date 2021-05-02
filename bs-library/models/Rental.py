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

    return_date = fields.Date(string='Date Returned', readonly=True)

    status = fields.Selection(string='Status',
                              selection=[
                                  ('on_hold', 'On Hold'),
                                  ('checked_out', 'Checked Out'),
                                  ('overdue', 'Overdue'),
                                  ('returned', 'Returned'),
                              ],
                              default='checked_out')

    gantt_date_end = fields.Date(string='End Date',
                                 compute='_compute_end_date',
                                 store=False)
    gantt_color = fields.Char(string='Color',
                              compute='_compute_color',
                              store=False)

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

    @api.onchange('status')
    def _onchange_status(self):
        if (self.status == 'checked_out'):
            self.book_id.status = 'checked_out'
        if (self.status == 'on_hold'):
            self.book_id.status = 'on_hold'
        if (self.status == 'returned'):
            self.return_date = date.today()
            self.book_id.status = 'circulation'

    @api.depends('return_date', 'due_date')
    def _compute_end_date(self):
        for record in self:
            record.gantt_date_end = record.return_date if (
                (record.return_date) and
                (record.return_date < record.due_date)) else record.due_date

    @api.depends('status')
    def _compute_color(self):
        colors = {'on_hold': 0, 'checked_out': 6, 'returned': 1, 'overdue': 4}
        for record in self:
            record.gantt_color = colors[record.status]

    @api.model
    def create(self, values):
        res = super(Rental, self).create(values)
        if res.status in ['checked_out', 'on_hold']:
            res.book_id.status = res.status
        return res