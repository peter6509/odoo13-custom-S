# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iotstoreproc2(models.Model):
    _name ="alldo_gh_iot.storeproc2"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists getwkonepcstime(pono varchar,engtype varchar) cascade""")
        self._cr.execute("""create or replace function getwkonepcstime(pono varchar,engtype varchar) returns float as $BODY$
        DECLARE
          wkid int ;
          myres float ;
          iotdur float ;
          ncount int ;
        BEGIN
          select id into wkid from alldo_gh_iot_workorder where po_no=pono and eng_type=engtype ;
          if wkid is not null then
             select count(*) into ncount from alldo_gh_iot_workorder_iot_data where order_id=wkid ;
             select sum(iot_duration) into iotdur from alldo_gh_iot_workorder_iot_data where order_id=wkid ;
             if ncount > 0 then
                myres = round((iotdur::numeric/ncount::numeric),2)
             else
                myres = 0 ;
             end if ;
          else
             myres =0 ;
          end if ;
          return myres ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genpiprodanalysis(pono varchar) cascade""")
        self._cr.execute("""create or replace function genpiprodanalysis(pono varchar) returns void as $BODY$
        DECLARE
            e_cur refcursor ;
            e_rec record ;
            wk_cur refcursor ;
            wk_rec record ;
            iot_cur refcursor ;
            iot_rec record ;
            prodid int ;
            prodtmplid int ;
            defcode varchar ; /* 產品名稱 */
            prodstd varchar ; /* 產能標準量 */
            onepcsstd1 float ;
            onepcsstd varchar ; /* 單件標準時間 */
            onepcscomplete varchar ; /* 單件完成時間 */
            onepcscomplete1 float ;
            totcomplete float /* 單件產品總時間 */
            analysisid it ;
            iotowner int ;
            iottotnum int ;
            iottotdur float ;
            wktottime float ;
            stdtotdur float ;
        BEGIN  
            totcomplete = 0 ;
            delete from alldo_gh_iot_piprod_analysis_line ; 
            delete from alldo_gh_iot_piprod_analysis ; 
            select product_no into prodid from alldo_gh_iot_po_wkorder where po_no=pono ;
            if prodid is not null then
               select default_code into defcode from product_product where id=prodid ; 
               select product_tmpl_id into prodtmplid from product_product where id=prodid ; 
               open e_cur for select * from alldo_gh_iot_eng_order where prod_id=prodtmplid and is_outsourcing=False order by sequence,id ;
               loop
                 fetch e_cur into e_rec ;
                 exit when not found ;
                 if prodstd is null then
                    prodstd = concat(e_rec.eng_type,e_rec.standard_num::TEXT) ;
                 else
                    prodstd = concat(prodstd,' ',e_rec.eng_type,e_rec.standard_num::TEXT) ;
                 end if ;  
                 if e_rec.standard_num > 0  then
                       onepcsstd1 = round((60::numeric / e_rec.standard_num::numeric),2) ;
                    else
                       onepcsstd1 = 0 ; 
                    end if ; 
                 if onepcsstd is null then
                    onepcsstd = concat(e_rec.eng_type,onepcsstd1::TEXT) ;
                 else
                    onepcsstd = concat(onepcsstd,' ',e_rec.eng_type,onepcsstd1::TEXT) ;
                 end if ;
                 if onepcscomplete is null then
                    select getwkonepcstime(pono,e_rec.eng_type) into onepcscomplete1 ;
                    onepcscomplete = concat(e_rec.eng_type,onepcscomplete1::TEXT) ;
                 else
                    select getwkonepcstime(pono,e_rec.eng_type) into onepcscomplete1 ;
                    onepcscomplete = concat(onepcscomplete,' ',e_rec.eng_type,onepcscomplete1::TEXT) ;
                 end if ;
                 totcomplete = totcomplete + onepcscomplete1 ;
               end loop ;
               close e_cur ; 
               insert into alldo_gh_iot_piprod_analysis(po_no,product_no,prod_std,onepcs_std,onepcs_complete,onepcs_time_total) values 
                  (pono,defcode,prodstd,onepcsstd,onepcscomplete,totcomplete::TEXT) ;
               select max(id) into analysisid from alldo_gh_iot_piprod_analysis ;   
               open wk_cur for select * from alldo_gh_iot_workorder where po_no=pono order by eng_seq ;
               loop
                  fetch wk_cur into wk_rec ;
                  exit when not found ;
                  open iot_cur for select * from alldo_gh_iot_workorder_iot_data where order_id=wk_rec.id order by iot_owner ;
                  loop
                     fetch iot_cur into iot_rec ;
                     exit when not fouund ;
                     if iotowner != iot_rec.iot_owner then
                        select sum(iot_num),sum(iot_duration),sum(std_duration) into iottotnum,iottotdur,stdtotdur from alldo_gh_iot_workorder_iot_data where order_id=wk_rec.id and iot_owner=iot_rec.iot_owner ; 
                        wktottime = round((iottotdur::numeric/3600::numeric),2) ; /* 工時(H) */
                        stdtotdur = round((iottotdur::numeric/iot_rec.std_duration::numeric),0) ; /* 標準生產總量 */
                        insert into alldo_gh_iot_piprod_analysis_line(piprod_id,eng_type,iot_node,iot_owner,prod_num,std_num,wk_time) values 
                          (analysisid,wk_rec.eng_type,iot_rec.iot_node,iot_rec.iot_owner,iottotnum,stdtotdur,wktottime) ;
                        iotowner = iot_rec.iot_owner ;
                     end if ;
                  end loop ;
                  close iot_cur ;
               end loop ;
               close wk_cur ;   
            end if ;
        END;$BODY$
        LANGUAGE plpgsql;""")
