# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api
from odoo import exceptions


class mesqcstoreproc(models.Model):
    _name = "mixmes_qc_config.storeproc"
    _description = u"MES_QC STORE_PROCEURE"

    def init(self):
        self.env.cr.execute("""DROP FUNCTION IF EXISTS setqcconfigitem(qcid int) cascade;""")
        self.env.cr.execute("""create or replace function setqcconfigitem(qcid int) returns void as $BODY$
          DECLARE
             myitem int := 1 ;
             qc_cur refcursor ;
             qc_rec record ;
          BEGIN
             open qc_cur for select id from barcode_line where qc_id=qcid order by sequence,id ;
             loop
                fetch qc_cur into qc_rec ;
                exit when not found ;
                update barcode_line set barcode_seq=myitem where id=qc_rec.id ;
                myitem=myitem + 1 ;
             end loop ;
             close qc_cur ;
             myitem := 1 ;
             open qc_cur for select id from pic_line where qc_id=qcid order by sequence,id ;
             loop
                fetch qc_cur into qc_rec ;
                exit when not found ;
                update pic_line set pic_seq=myitem where id=qc_rec.id ;
                myitem=myitem + 1 ;
             end loop ;
             close qc_cur ;
          END;$BODY$
          LANGUAGE plpgsql ;""")
