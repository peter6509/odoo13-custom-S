odoo.define('web_export_view', function (require) {
"use strict";

    var core = require('web.core');
    var Sidebar = require('web.Sidebar');
    var QWeb = core.qweb;

    var _t = core._t;
    var ListView = require('web.ListView')
    ListView.include({

        redraw: function () {
            var self = this;
            this._super.apply(this, arguments);
            if (this.$buttons){
                var btn = this.$buttons.find('#tahu').on('click',self.on_export_require_item);
            }

        },

        on_export_require_item: function () {
            // Select the first list of the current (form) view
            // or assume the main view is a list view and use that
            var self = this,
                view = this.getParent(),
                children = view.getChildren();


            var export_columns_keys = [];
            var export_columns_names = [];
            $.each(view.visible_columns, function () {
                if (this.tag == 'field' && (this.widget === undefined || this.widget != 'handle')) {
                    // non-fields like `_group` or buttons
                    export_columns_keys.push(this.id);
                    export_columns_names.push(this.string);
                }
            });
            var context = {}
             context = {
                        'req_op_ids': export_columns_keys
                    };
            var action = ({
            context: context
        })
            self.do_action(action)
        }

    });
});
