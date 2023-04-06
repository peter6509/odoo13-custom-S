# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class AcmePivotRefresh(models.Model):
    _name = "alldo_acme_iot.material_refresh"

    @api.model
    def run_material_refresh(self):
        self._cr.execute("""refresh materialized view alldo_acme_iot_cnc_performance_report""")
        self._cr.execute("""refresh materialized view alldo_acme_iot_cnc_performance_report2""")
        self._cr.execute("""refresh materialized view alldo_acme_iot_scale_performance_report""")
        self._cr.execute("""refresh materialized view alldo_acme_iot_shipping_kpi_report""")
        self._cr.execute("""refresh materialized view alldo_acme_iot_outorderqc_kpi_report""")
        self._cr.execute("""refresh materialized view alldo_acme_iot_wkorderqc_kpi_report""")
        self._cr.execute("""refresh materialized view alldo_acme_iot_outsourcing_kpi_report""")
        self._cr.execute("""commit""")