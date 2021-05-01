from odoo import api, fields, models


class Genre(models.Model):
    _name = 'library.genre'
    _description = 'Book Genre'

    name = fields.Char(string='Name', required=True)