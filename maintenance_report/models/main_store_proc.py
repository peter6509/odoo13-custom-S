# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class mainstoreproc(models.Model):
    _name = "maintenance.storeproc"

    @api.model_cr
    def init(self):
        """ DAN_PROD Get stageid mytype='1' go_back  mytype='2' go_next """
        self._cr.execute("""DROP FUNCTION IF EXISTS get_stageid(mystageid int,mytype int) cascade;""")
        self._cr.execute("""DROP FUNCTION IF EXISTS get_stageid(mystageid int,mytype char) cascade;""")
        self._cr.execute("""create or replace function get_stageid(mystageid int,mytype int) returns INTEGER as $BODY$
                      DECLARE 
                        nextstageid INT ;
                        backstageid INT ;
                        maxstageid INT ;
                        minstageid INT ;
                        maxsequenceid int ;
                        minsequenceid int ;
                        nowsequenceid int ;
                        retstageid INT ;
                      BEGIN
                        select sequence into nowsequenceid from maintenance_stage where id=mystageid ;
                        select min(id),max(id),min(sequence),max(sequence) into minstageid,maxstageid,minsequenceid,maxsequenceid from maintenance_stage ;
                        select id into maxstageid from maintenance_stage where sequence=maxsequenceid ;
                        select id into minstageid from maintenance_stage where sequence=minsequenceid ;
                        select COALESCE(id,maxstageid) into nextstageid from maintenance_stage 
                            where sequence > nowsequenceid and sequence = (select min(sequence) from maintenance_stage where sequence > nowsequenceid) ;
                        select COALESCE(id,minstageid) into backstageid from maintenance_stage 
                            where sequence < nowsequenceid and sequence = (select max(sequence) from maintenance_stage where sequence < nowsequenceid) ;   
                        if mytype = 1 THEN 
                           if nowsequenceid <= minsequenceid THEN 
                             retstageid := minstageid ;
                           ELSE 
                             retstageid := backstageid ;
                           end if ;  
                        ELSE 
                           if nowsequenceid >= maxsequenceid THEN 
                              retstageid := maxstageid ;
                           ELSE 
                              retstageid := nextstageid ;
                           end if ;   
                        end if ;   
                        return retstageid ;
                      END;$BODY$
                      LANGUAGE plpgsql;""")