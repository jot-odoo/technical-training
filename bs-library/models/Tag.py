from odoo import api, fields, models


class Tag(models.Model):
    _name = 'library.tag'
    _description = 'Tag'

    name = fields.Char(string='Name', required=True)