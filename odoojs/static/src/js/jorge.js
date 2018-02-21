odoo.define('odoojs.jorge', function (require) {

    var Widget = require('web.Widget');
    var core = require('web.core');

    Jorge = Widget.extend({

        template: "dropdown_teacher",
        start: function () {
            var self  = this.$el;
            console.log("Widget arriba");
            // var def_account = this._rpc({
            //     model: 'account.account',
            //     method: 'search_read',
            //     fields: ['code'],
            // })
            // .then(function (accounts) {
            //     self.accounts = _.object(_.pluck(accounts, 'id'), _.pluck(accounts, 'code'));
            // });

            this._rpc({
                "model": "odoojs.teacher",
                "method": "search_read",
                "fields": ['name'],
                "args": [[]]
            }).then(function (lista_profesores) {
                console.log(lista_profesores);
                var lista= ""
                lista_profesores.forEach(element => {
                    lista = lista +"<li class=\"teacher \">"+element.name+"</li>"
                });

                console.log(self.find(".dropdown-menu").append(lista));
                // this.$el.find("dropdown-menu").append(lista);
                self.find(".teacher").on("click",function(elm){
                    console.log(elm.target.innerHTML);
                    // self.find("#selected_teacher").innerHTML = elm.target.innerHTML;
                    self.find("#selected_teacher").val(elm.target.innerHTML);
                    // console.log(self.find("#selected_teacher"));
                })
            });

        }


    });



    core.action_registry.add('odoojs.jorge', Jorge);

});