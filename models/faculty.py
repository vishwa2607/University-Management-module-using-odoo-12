from odoo import models,fields


class facultyfaculty(models.Model):
    _name = 'faculty_new.faculty_new'

    _rec_name ='faculty_name'
    faculty_name = fields.Char(String='Faculty Name')
    designation = fields.Char(String='designation')
    courses = fields.Many2many('course.course', 'courses')
