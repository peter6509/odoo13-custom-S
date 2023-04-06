# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebPivotRefresh(models.Model):
    _name = "neweb_pivot.materialized_refresh"

    @api.model
    def run_materialized_refresh(self):
        self._cr.execute("""refresh materialized view neweb_pivot_project_report""")
        self._cr.execute("""refresh materialized view neweb_pivot_project_report1""")
        self._cr.execute("""refresh materialized view neweb_pivot_repairpivotreport""")
        self._cr.execute("""commit""")
