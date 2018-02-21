odoo.define('odoojs.jorge', function (require) {

    var Widget = require('web.Widget');
    var core = require('web.core');

    Jorge = Widget.extend({

        template: "dropdown_teacher",
        start: function () {
            var self = this.$el;
                 this._rpc({
                "model": "odoojs.teacher",
                "method": "search_read",
                "fields": ['name'],
                "args": [
                    []
                ]
            }).then(function (lista_profesores) {

                var lista = ""
                lista_profesores.forEach(element => {
                    lista =+ "<li class=\"teacher \">" + element.name + "</li>"
                });

                console.log(self.find(".dropdown-menu").append(lista));
                self.find(".teacher").on("click", function (elm) {

                    self.find("#selected_teacher").val(elm.target.innerHTML);

                })
            });

        }


    });



    core.action_registry.add('jorge.ui', Jorge);

});