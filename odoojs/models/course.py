

from odoo import models, fields, api


class Course(models.Model):
    _name = "odoojs.course"

    name = fields.Char("Curso")
    course_date = fields.Datetime("Fecha del curso")
    student_ids = fields.One2many("odoojs.student", "course_id", string="Estudiante")
    teacher_id = fields.Many2one("odoojs.teacher", string="Profesor")
    tags_ids = fields.Many2many("odoojs.course.tags", string="Etiquetas")


    @api.model
    def create(self, vals):

        return super(Course, self).create(vals)


    @api.multi
    def open_ui(self):
        """ open the pos interface """
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'url':   '/pos/web/',
            'target': 'self',
        }



class CourseTags(models.Model):
    _name = "odoojs.course.tags"

    name = fields.Char("Etiquetas")