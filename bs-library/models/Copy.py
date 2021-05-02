import uuid
from odoo import api, fields, models


class Copy(models.Model):
    _name = 'library.copy'
    _description = 'Copy of a Book'
    _inherits = {'library.book': 'book_id'}
    _rec_name = 'title'

    def _generate_random_serial(self):
        return str(uuid.uuid4()).upper().replace('-', '')[0:10]

    book_id = fields.Many2one(comodel_name='library.book',
                              required=True,
                              ondelete='cascade')
    rental_ids = fields.One2many(comodel_name='library.rental',
                                 inverse_name='book_id')
    serial_number = fields.Char(
        string='Serial Number',
        required=True,
        default=lambda self: self._generate_random_serial(),
        index=True,
        readonly=True)

    # TODO: make Location model and make this a many2one
    location = fields.Char(string='Location')

    status = fields.Selection(string='Status',
                              selection=[('circulation', 'In Circulation'),
                                         ('on_hold', 'On Hold'),
                                         ('checked_out', 'Checked Out'),
                                         ('archived', 'Archived')],
                              default='circulation')

    @api.constrains('rental_ids.status, status')
    def _constrain_status(self):
        for record in self:
            for rental in record.rental_ids:
                if (rental.status in ['on_hold', 'checked_out', 'overdue']
                        and record.status not in ['checked_out', 'on_hold']):
                    return False
