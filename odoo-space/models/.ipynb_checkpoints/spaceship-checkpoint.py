# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class Spaceship(models.Model):
    _name = 'space.spaceship'
    _description = 'Spaceship Info'

    name = fields.Char(string="name")
    shipType = fields.Selection(string='Type', selection=[
        ('shuttle', 'Shuttle'), ('rocket', 'Rocket'), ('cargo', 'Cargo')])
    numPassengers = fields.Integer(string='Number of Passengers')
    fuelType = fields.Selection(string='Fuel Type', selection=[(
        'gasoline', 'Gasoline'), ('jet_propellant', 'Jet Propellant')])
    length = fields.Float(string='Length')
    width = fields.Float(string='Width')
    height = fields.Float(string='Height')
    active = fields.Boolean(string='Active', default=False)

    @api.constrains('length', 'width')
    def _check_dimensions(self):
        for record in self:
            if(record.length < record.width):
                raise UserError("Ship's length must be larger than its width!")