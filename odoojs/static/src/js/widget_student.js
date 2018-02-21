odoo.define('odoojs.widget_student', function (require) {

    var Widget = require('web.Widget');
    var core = require('web.core');

    var WidgetStudent = Widget.extend({
        //template: "odoojs_main_widget",
        tagName: 'div',
        id: "grd_student",
        start: function () {
            var grd = $("<table width='100%' border='1' cellpadding='4' cellspacing='4'></table>");

            grd.append("<thead style='background-color: lightgrey'><tr><th>Nombre</th><th>Matricula</th></tr></thead>");

            this.$el.append("<h1>Estudiantes</h1>");
            this.$el.append(grd);

            this._rpc({
                "model": "odoojs.student",
                "method": "search_read",
                "fields": ["name", "matricula"],
                "args": [[]]
            }).then(function (data) {
                $.each(data, (i, e) => {
                       grd.append("<tr><td>" + e.name + "</td><td>" + e.matricula + "</td></tr>");
                    });

                //console.log(JSON.stringify(data));
            });
        }
    });

    core.action_registry.add('widget_student.ui', WidgetStudent);
});