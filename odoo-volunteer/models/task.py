# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Task(models.Model):
    _name = 'volunteer.task'
    _description = 'Task Info'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    taskType = fields.Selection(string='Type', selection=[(
        'manual_labor', 'Manual Labor'), ('technical', 'Technical')])

    startTime = fields.Datetime(string='Start Time')
    endTime = fields.Datetime(string='End Time')
    repeating = fields.Boolean(string='Repeats', default=False)
    frequency = fields.Integer(string='Frequency')
    frequencyUnits = fields.Selection(string='Frequency Units', selection=[
                                      ('day', 'Day'), ('week', 'Week'), ('month', 'Month')])
    
    leader_id = fields.Many2one(string='Leader', comodel_name='res.partner')
    state = fields.Selection(string='State', selection=[('draft','Draft'),('ready','Ready'),('inprogress','In-progress'),('done','Done')], default='draft')
    
    volunteer_ids = fields.Many2many(string='Volunteers', comodel_name='res.partner')
    
    @api.onchange('leader_id')
    def _onchange_leader(self):
        if(self.state == 'draft' and self.leader_id): 
            self.state = 'ready'
