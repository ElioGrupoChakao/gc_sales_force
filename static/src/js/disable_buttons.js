odoo.define('your_module.disable_buttons', function (require) {
    "use strict";

    var core = require('web.core');
    var ListRenderer = require('web.ListRenderer');

    var _t = core._t;

    ListRenderer.include({
        _renderRow: function (record) {
            var $row = this._super.apply(this, arguments);

            // Revisa si el usuario pertenece al grupo 'gc_sales_force.group_hide_button'
            var user_groups = odoo.session_info.groups;
            var isInGroup = _.contains(user_groups, 'gc_sales_force.group_hide_button');

            // Deshabilitar todos los botones si el usuario no está en el grupo
            if (!isInGroup) {
                $row.find('.o_list_button').prop('disabled', true);
            }

            return $row;
        },
    });

});
