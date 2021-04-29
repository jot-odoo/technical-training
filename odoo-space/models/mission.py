# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class Mission(models.Model):
    _name = 'space.mission'
    _description = 'Mission Info'

    name = fields.Char(string='Name')
    ship_id = fields.Many2one(comodel_name='space.spaceship',
                              string='Assigned Ship')

    crew_ids = fields.Many2many(comodel_name='res.partner',
                                string='Crew Members')

    launchDate = fields.Date(string='Launch Date')
    returnDate = fields.Date(string='Return Date')

    # Metrics
    fuelUsed = fields.Float(string='Fuel Used', default=0.0)
    numberOfEngines = fields.Integer(string='Number of Engines', default=1)
    distanceTraveled = fields.Float(string='Distance Traveled', default=0.0)
