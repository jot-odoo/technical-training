# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Spaceship(models.Model):
    _name = 'space.spaceship'
    _description = 'Spaceship Info'

    name = fields.Char(string="name")
    shipType = fields.Selection(string='Type', selection=[
        ('shuttle', 'Shuttle'), ('rocket', 'Rocket'), ('cargo', 'Cargo')])
    numPassengers = fields.Integer(string='Number of Passengers')
    fuelType = fields.Selection(string='Fuel Type', selection=[(
        'gasoline', 'Gasoline'), ('jet_propellant', 'Jet Propellant')])
    dimensionsLength = fields.Float(string='Length')
    dimensionsWidth = fields.Float(string='Width')
    dimensionsHeight = fields.Float(string='Height')
    active = fields.Boolean(string='Active', default=False)
