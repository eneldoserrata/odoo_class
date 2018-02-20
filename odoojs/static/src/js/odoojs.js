odoo.define('odoojs.odoojs', function (require) {

    var Widget = require('web.Widget');
    var core = require('web.core');

    var Odoojs = Widget.extend({

        start: function() {
            console.log("pet store home page loaded");
            this.$el.append("<button id='get_advance_paper' class='btn btn-default btn-block'><div class='stat_button_icon fa fa-level-up'></div><div>Sacar papel</div></button>");

        }
    });


    core.action_registry.add('odoojs.ui', Odoojs);
});