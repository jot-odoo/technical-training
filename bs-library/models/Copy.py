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

    location = fields.Char(string='Location')

    is_available = fields.Boolean(string='Is Available',
                                  compute='_compute_availability',
                                  store=True)

    @api.depends('rental_ids.is_returned')
    def _compute_availability(self):
        for record in self:
            for rental in record.rental_ids:
                if (not rental.is_returned):
                    record.is_available = False
                    return
            record.is_available = True
