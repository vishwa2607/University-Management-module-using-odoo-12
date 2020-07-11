from odoo import models, fields


class partner(models.Model):
    _inherit = 'res.partner'


    instructor = fields.Boolean("instructor", default=False)
    session_ids = fields.Many2many('student.student', String='Attended Session')
