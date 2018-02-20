

from odoo import models, fields


class Course(models.Model):
    _name = "odoojs.course"

    name = fields.Char("Curso")
    course_date = fields.Datetime("Fecha del curso")

    student_ids = fields.One2many("odoojs.student","course_id")
    