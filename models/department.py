from odoo import models, fields

class departmentdepartment(models.Model):
    _name='department.department'
    _rec_name = 'dept_name'
    dept_name = fields.Char(String='Department')



