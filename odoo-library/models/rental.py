# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Rental(models.Model):
    _name = 'library.rental'
    _description = 'Rental Info'
    
    customer_id = fields.Many2one(string='Customer', 
                                  comodel_name='res.partner', 
                                  ondelete='cascade')
    book_ids = fields.Many2many(string='Books',
                               comodel_name='library.book')