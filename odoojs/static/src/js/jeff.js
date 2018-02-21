odoo.define('odoojs.jeff', function (require) {

    var Widget = require('web.Widget');
    var core = require('web.core');

    var Jeffjs = Widget.extend({
        template: "odoojs_jeff_widget",
    //    start: function () {
      //      this.$el.find(".mybutton").on("click", function () {
        //        alert("Hello")

        //    });

      //      this._rpc({
      //          "model": "odoojs.course",
      //          "method": "search",
      //          "args": [[]]
      //      }).then(function (value) {
      //          console.log(value)
      //      })
        //}
    });


    core.action_registry.add('jeff.ui', Jeffjs);
});