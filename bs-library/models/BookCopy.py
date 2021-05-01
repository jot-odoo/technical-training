from odoo import api, fields, models


class ModuleName(models.Model):
    _name = 'library.bookcopy'
    _description = 'Copy of a Book'
    _inherits = {'library.book': 'book_id'}

    name = fields.Char(string='Name')
    book_id = fields.Many2one(comodel_name='library.book',
                              required=True,
                              ondelete='cascade')
    rental_ids = fields.One2many(comodel_name='library.rental',
                                 inverse_name='book_id')
