openerp.neweb_purchase = function(instance){

    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;

    instance.web.ListView.include({

        load_list: function(data) {
            if (this.$buttons) {
                this.$buttons.find('import_require_button').click(this.proxy('action')) ;
            }
        },

        action: function () {
            var model_obj = new instance.web.Model('ir.model.data');
            view_id = model_obj.call('get_object_reference', ["neweb_purchase", "neweb_unpurchase_item_tree"]);

            this.do_action(
                name=_t('Require Purchase'),
                type='ir.actions.act_window',
                res_model='neweb_purchase.require_purchase_item',
                view_type='form',
                view_mode='form',
                view_id=(view_id),
                target='new'
                );
        }
    });
}
