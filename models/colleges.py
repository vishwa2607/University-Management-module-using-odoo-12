from odoo import models, fields


class collegecollege(models.Model):
    _name ='college.college'

    _rec_name = 'college_name'
    college_name = fields.Char(String='College Name')
    department=fields.Many2one('college.college', 'College')


