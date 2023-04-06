# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api

class wkfstoreproc(models.Model):
    _name = "wkf.storeproc"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists genwkfstate(model_name varchar) cascade""")
        self._cr.execute("""create or replace function genwkfstate(model_name varchar) returns void as $BODY$
            BEGIN
               execute 'ALTER TABLE '|| model_name ||' ADD COLUMN  x_wkf_state character varying';
            EXCEPTION
                WHEN duplicate_column THEN RAISE NOTICE 'column x_wkg_state already exists in Model' ;
            END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists transiscomplete(resid int,transid int) cascade""")
        self._cr.execute("""create or replace function transiscomplete(resid int,transid int) returns Boolean as $BODY$
         DECLARE
          myres Boolean ;
          ncount int ;
          wkfid int ;
          endnode int ;
          endtrans int ;
         BEGIN
           select wkf_id into wkfid from wkf_trans where id = transid ;
           select max(id) into endnode from wkf_node where wkf_id= wkfid and is_stop=True ;
           select id into endtrans from wkf_trans where wkf_id=wkfid and node_to = endnode ;
           select count(*) into ncount from log_wkf_trans where res_id=resid and trans_id = endtrans ;
           if ncount > 0 then
              myres = True ;
           else
              myres = False ;
           end if ;
           return myres ;      
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getwkfsecurity()""")

        self._cr.execute("""drop function if exists checksecurity(mytable varchar,recid int,transid int,myuid int) cascade""")
        self._cr.execute("""create or replace function checksecurity(mytable varchar,recid int,transid int,myuid int) returns Boolean as $BODY$
          DECLARE
            t_cur refcursor ;
            t_rec record ;
            flowowner int ;
            flowman1 int ;
            flowman2 int ;
            flowman3 int ;
            flowman4 int ;
            nitem int ;
            wkfid int ;
            resourceid int ;
            empid int ;
            myres Boolean ;
            SQL varchar ;
          BEGIN
             nitem = 0 ;
             select id into resourceid from resource_resource where user_id=myuid ;
             select id into empid from hr_employee where resource_id=resourceid ;
             SQL = "'select flow_owner,flow_man1,flow_man2,flow_man3,flow_man4 into flowowner,flowman1,flowman2,flowman3,flowman4 from '|| mytable ||' where id = '|| recid ||" ;
             perform SQL ;
             select wkf_id into wkfid from wkf_trans where id = transid ;
             open t_cur for select * from wkf_trans where wkf_id=wkfid order by sequence ;
             loop
              fetch t_cur into t_rec ;
              exit when not found ;
              nitem = nitem + 1 ;
              if t_rec.id = transid then
                 exit ;
              end if ;
             end loop ;
             close t_cur ;
             if nitem = 1 then
               if empid = flowowner or empid = flowman1 or empid = flowman2 or empid = flowman3 or empid = flowman4 then
                  myres = True ;
               else
                  myres = False ;
               end if ;  
            elsif nitem = 2 then
               if empid = flowman1 or empid = flowman2 or empid = flowman3 or empid = flowman4 then
                  myres = True ;
               else
                  myres = False ;
               end if ;  
            elsif nitem = 3 then
               if empid = flowman2 or empid = flowman3 or empid = flowman4 then
                  myres = True ;
               else
                  myres = False ;
               end if ;  
            elsif nitem=4 then
               if empid = flowman3 or empid = flowman4 then
                  myres = True ;
               else
                  myres = False ;
               end if ;   
            elsif nitem=5 then
               if empid = flowman4 then
                  myres = True ; 
               else   
                  myres = False ;
               end if ;  
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")
