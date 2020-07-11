from odoo import models, fields, api
from datetime import date, datetime
from odoo.exceptions import UserError

_sql_constraints = [('identity_unique', 'UNIQUE(student_identity), '
                                        '"Identity of the student must be Unique!!!"')]

class studentstudent(models.Model):
    _name = 'student.student'
    name = fields.Char(String='Name', required=True)
    student_identity = fields.Char(String='Student ID', required=True)

    gender = fields.Selection([('male', 'Male'),('female', 'Female'),('others', 'Others')],String='Gender',
                              required=True)
    birthdate = fields.Date(String='BirthDate', required=True)
    department = fields.Many2one('department.department', 'Department')
    college = fields.Many2one('college.college', 'College')
    age = fields.Integer(String='Age')
    nationality = fields.Many2one('res.country',String='Nationality')

    @api.onchange('age')
    def check_age(self):
        if (self.age < 18):
            raise UserError("You are not eligible to apply for Degree")

    @api.multi
    def get_report(self):
        data={
            'model': self._name,
            'ids' : self.ids,
            'form' : {
                'name' : self.name,
                'student_id' : self.student_identity,
                'gender' : self.gender,
                'birthdate' : self.birthdate,
                'department': self.department,
                'college' : self.college,
                'age' : self.age,
                'nationality': self.nationality
            },

        }
        return self.env.reference('student.student').report_action(self,data=data)

    # #using _constraints
    # @api.constrains('age')
    # def check_age(self):
    #     if(self.age<18):
    #         raise UserError("You are not eligible to apply for Degree")