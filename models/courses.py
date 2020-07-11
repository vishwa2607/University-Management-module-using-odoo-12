from odoo import models,fields


class courses(models.Model):
    _name='course.course'

    _rec_name = 'course_name'
    course_name=fields.Char(String='Course Name')
    course_credit=fields.Integer(String='Course Credit')


