# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, api


class AlldoGhIotTrigger(models.Model):
    _name = "alldo_gh_iot.trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists insert_mvl_powk() cascade""")
        # self._cr.execute("""create  or replace function insert_mvl_powk() returns trigger as $BODY$
        #   DECLARE
        #     prodid int ;
        #     pickingdate date ;
        #     prodqty float ;
        #     pickingid int ;
        #     ncount int ;
        #     ncount1 int;
        #     ref1 varchar ;
        #     qtydone float ;
        #     moveid int ;
        #     locid int ;
        #     locdestid int ;
        #   BEGIN
        #     select product_id,date,qty_done,move_id,reference,location_id,location_dest_id into prodid,pickingdate,prodqty,moveid,ref1,locid,locdestid from stock_move_line where id = NEW.move_id ;
        #     select id into pickingid from stock_picking where name = ref1 ;
        #     if coalesce(prodqty,0)=0 then
        #        select product_qty into prodqty from stock_move where id = moveid ;
        #        select date_done::DATE into pickingdate from stock_picking where id = pickingid ;
        #     end if ;
        #     select count(*) into ncount from alldo_gh_iot_picking_line where picking_id=pickingid and po_id=NEW.po_id ;
        #     if ncount = 0 then
        #         if locid=8 and locdestid=5 then  /* 出貨 */
        #             insert into alldo_gh_iot_picking_line(po_id,picking_id,picking_type_id,picking_date,picking_num) values
        #                   (NEW.po_id,pickingid,2,pickingdate,prodqty) ;
        #         elsif locid=5 and locdestid=8 then  /* 退貨 */
        #             select date_done::DATE into pickingdate from stock_picking where id = pickingid ;
        #             insert into alldo_gh_iot_picking_line(po_id,picking_id,picking_type_id,picking_date,picking_num) values
        #                   (NEW.po_id,pickingid,1,pickingdate,prodqty * -1) ;
        #         end if ;
        #     end if ;
        #     return NEW ;
        #   END;$BODY$
        #   LANGUAGE plpgsql;""")

        # 針對每次新增 ghiot_moveline_powk_rel move_id/po_id 作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_moveline_powk_rel on ghiot_moveline_powk_rel ;""")
        # self._cr.execute("""create trigger insert_moveline_powk_rel after insert on ghiot_moveline_powk_rel
        #                          for each row execute procedure insert_mvl_powk();""")

        self._cr.execute("""drop function if exists del_mvl_powk() cascade""")
        self._cr.execute("""create  or replace function del_mvl_powk() returns trigger as $BODY$
          DECLARE
            prodid int ;
            pickingdate date ;
            prodqty float ;
            pickingid int ;
            ncount1 int ;
            moveid int ;
          BEGIN
            select product_no into prodid from alldo_gh_iot_po_wkorder where id = OLD.po_id ;
            select move_id into moveid from stock_move_line where id = OLD.move_id ;
            select picking_id into pickingid from stock_move where id = moveid ;
            select count(*) into ncount1 from alldo_gh_iot_picking_line where po_id = OLD.po_id and picking_id = pickingid ;    
            if ncount1 > 0 then
               delete from alldo_gh_iot_picking_line where po_id = OLD.po_id and picking_id = pickingid ; 
            end if ;          
            return OLD ; 
          END;$BODY$
          LANGUAGE plpgsql;""")


        # 針對每次刪除 ghiot_moveline_powk_rel move_id/po_id 作動一次 trigger
        self._cr.execute("""drop trigger if exists del_moveline_powk_rel on ghiot_moveline_powk_rel ;""")
        self._cr.execute("""create trigger del_moveline_powk_rel before delete on ghiot_moveline_powk_rel
                                         for each row execute procedure del_mvl_powk();""")
        self._cr.execute("""drop function if exists return_stock_picking() cascade""")
        self._cr.execute("""create  or replace function return_stock_picking() returns trigger as $BODY$
          DECLARE
            prodid int ;
            pickingdate date ;
            prodqty float ;
            pickingid int ;
            ncount int ;
            ncount1 int ;
            stockno varchar ;
            mv_cur refcursor ;
            mv_rec record ;
            newmvid int ;
            poid int ;
          BEGIN
            if NEW.state='done' then
               select count(*) into ncount from stock_picking where NEW.origin like '%退回%' ;
               if ncount > 0 then   /* 退貨 */
                  select id,product_id into newmvid,prodid from stock_move_line where picking_id=NEW.id ;
                  select substring(NEW.origin,4,12) into stockno ;
                  select id into pickingid from stock_picking where name = stockno ;
                  open mv_cur for select * from stock_move_line where picking_id=pickingid and state='done' and product_id=prodid ;
                  loop
                    fetch mv_cur into mv_rec ;
                    exit when not found ;
                    select po_id into poid from ghiot_moveline_powk_rel where move_id=mv_rec.id ;
                    if poid is not null then
                       select count(*) into ncount1 from ghiot_moveline_powk_rel where move_id=newmvid and po_id=poid ;
                       if ncount1 = 0 then
                          insert into ghiot_moveline_powk_rel(move_id,po_id) values (newmvid,poid) ;
                       end if ;
                    end if ;
                  end loop ;
                  close mv_cur ;
               end if ;
            end if ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists return_stock_picking on stock_picking ;""")
        self._cr.execute("""create trigger return_stock_picking after update of state on stock_picking
                           for each row execute procedure return_stock_picking();""")

        self._cr.execute("""drop function if exists afterins_stockmoveline() cascade""")
        # self._cr.execute("""create  or replace function afterins_stockmoveline() returns trigger as $BODY$
        #   DECLARE
        #     prodid int ;
        #     pickingdate date ;
        #     prodqty float ;
        #     pickingid int ;
        #     ncount int ;
        #     ncount1 int;
        #     ref1 varchar ;
        #     qtydone float ;
        #     moveid int ;
        #     locid int ;
        #     locdestid int ;
        #     poid int ;
        #   BEGIN
        #     select count(*) into ncount from ghiot_moveline_powk_rel where move_id = NEW.id ;
        #     if ncount > 0 then  /* 有訂單 */
        #        select picking_id into pickingid from stock_move where move_id = NEW.id ;
        #        select max(po_id) into poid from ghiot_moveline_powk_rel where move_id = NEW.id ;
        #        select count(*) into ncount from alldo_gh_iot_picking_line where picking_id=pickingid and po_id=NEW.po_id ;
        #         if ncount = 0 then
        #            if NEW.location_id=8 and NEW.location_dest_id=5 then  /* 出貨 */
        #               insert into alldo_gh_iot_picking_line(po_id,picking_id,picking_type_id,picking_date,picking_num) values
        #                   (poid,pickingid,2,NEW.date::DATE,NEW.qty_done) ;
        #            elsif NEW.location_id=5 and NEW.location_dest_id=8 then  /* 退貨 */
        #               insert into alldo_gh_iot_picking_line(po_id,picking_id,picking_type_id,picking_date,picking_num) values
        #                   (poid,pickingid,1,NEW.date::DATE,NEW.qty_done * -1) ;
        #            end if ;
        #         end if ;
        #     end if ;
        #     return NEW ;
        #   END;$BODY$
        #   LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists afterins_stockmoveline on stock_move_line ;""")
        # self._cr.execute("""create trigger afterins_stockmoveline after insert on stock_move_line
        #                            for each row execute procedure afterins_stockmoveline();""")

        self._cr.execute("""drop function if exists afupdate_stockmoveline() cascade""")
        self._cr.execute("""create  or replace function afupdate_stockmoveline() returns trigger as $BODY$
          DECLARE
            prodid int ;
            pickingdate date ;
            prodqty float ;
            pickingid int ;
            ncount int ;
            ncount1 int;
            ref1 varchar ;
            qtydone float ;
            moveid int ; 
            locid int ;
            locdestid int ;
            poid int ;
          BEGIN
            if NEW.state='done' and OLD.state != 'done' then
               select count(*) into ncount from ghiot_moveline_powk_rel where move_id = NEW.id ;
                if ncount > 0 then  /* 有訂單 */
                   select picking_id into pickingid from stock_move where id = NEW.move_id ;
                   select origin into ref1 from stock_picking where id =pickingid ;
                   select max(po_id) into poid from ghiot_moveline_powk_rel where move_id = NEW.id ;
                   select count(*) into ncount from alldo_gh_iot_picking_line where picking_id=pickingid and po_id=poid ;
                    if ncount = 0 then
                       if NEW.location_id=8 and NEW.location_dest_id=5 then  /* 出貨 */
                          insert into alldo_gh_iot_picking_line(po_id,picking_id,picking_type_id,picking_date,picking_num,origin) values 
                              (poid,pickingid,2,NEW.date::DATE,NEW.qty_done,ref1) ;  
                       elsif NEW.location_id=5 and NEW.location_dest_id=8 then  /* 退貨 */ 
                          insert into alldo_gh_iot_picking_line(po_id,picking_id,picking_type_id,picking_date,picking_num,origin) values 
                              (poid,pickingid,1,NEW.date::DATE,NEW.qty_done * -1,ref1) ;  
                       end if ;          
                    end if ;    
                end if ;
            end if ;
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists afupdate_stockmoveline on stock_move_line ;""")
        self._cr.execute("""create trigger afupdate_stockmoveline after update of state on stock_move_line
                                   for each row execute procedure afupdate_stockmoveline();""")

        self._cr.execute("""drop function if exists insert_powkorder_iotwkorder_rel() cascade""")
        self._cr.execute("""create  or replace function insert_powkorder_iotwkorder_rel() returns trigger as $BODY$
          DECLARE
             rel_cur refcursor ;
             rel_rec record ;
             pono varchar ;
             pono1 varchar ;
          BEGIN
             pono = '';
             open rel_cur for select * from powkorder_iotwkorder_rel where wk_id=NEW.wk_id ;
             loop
                fetch rel_cur into rel_rec ;
                exit when not found ;
                select po_no into pono1 from alldo_gh_iot_po_wkorder where id = rel_rec.po_id ;
                if pono='' then
                   pono = pono1 ;
                else
                   pono = concat(pono,',',pono1) ;
                end if ;
             end loop ;
             close rel_cur ;
             update alldo_gh_iot_workorder set po_no=pono where id = NEW.wk_id ;
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次新增 powkorder_iotwkorder_rel wk_id/po_id 作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_powkorder_iotwkorder_rel on powkorder_iotwkorder_rel ;""")
        self._cr.execute("""create trigger insert_powkorder_iotwkorder_rel after insert on powkorder_iotwkorder_rel
                                 for each row execute procedure insert_powkorder_iotwkorder_rel();""")

        self._cr.execute("""drop function if exists del_powkorder_iotwkorder_rel() cascade""")
        self._cr.execute("""create  or replace function del_powkorder_iotwkorder_rel() returns trigger as $BODY$
          DECLARE
             rel_cur refcursor ;
             rel_rec record ;
             pono varchar ;
             pono1 varchar ;
          BEGIN
             pono = '';
             open rel_cur for select * from powkorder_iotwkorder_rel where wk_id=OLD.wk_id ;
             loop
                fetch rel_cur into rel_rec ;
                exit when not found ;
                select po_no into pono1 from alldo_gh_iot_po_wkorder where id = rel_rec.po_id ;
                if pono='' then
                   pono = pono1 ;
                else
                   pono = concat(pono,',',pono1) ;
                end if ;
             end loop ;
             close rel_cur ;
             update alldo_gh_iot_workorder set po_no=pono where id = OLD.wk_id ;
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次刪除 powkorder_iotwkorder_rel wk_id/po_id 作動一次 trigger
        self._cr.execute("""drop trigger if exists del_powkorder_iotwkorder_rel on powkorder_iotwkorder_rel ;""")
        self._cr.execute("""create trigger del_powkorder_iotwkorder_rel after delete on powkorder_iotwkorder_rel
                                         for each row execute procedure del_powkorder_iotwkorder_rel();""")

        # self._cr.execute("""drop function if exists update_wkorder_shippingnum() cascade""")
        # self._cr.execute("""create  or replace function update_wkorder_shippingnum() returns trigger as $BODY$
        #   DECLARE
        #     ncount int ;
        #   BEGIN
        #     if NEW.order_num <= NEW.shipping_num then
        #        NEW.state = '4' ;
        #     end if ;
        #     return NEW ;
        #   END;$BODY$
        #   LANGUAGE plpgsql;""")
        #
        # self._cr.execute("""drop trigger if exists update_wkorder_shippingnum on alldo_gh_iot_workorder ;""")
        # self._cr.execute("""create trigger update_wkorder_shippingnum before update of shipping_num on alldo_gh_iot_workorder
        #                                  for each row execute procedure update_wkorder_shippingnum();""")
        #
        #

        self._cr.execute("""drop function if exists update_state_purchase_order() cascade""")
        self._cr.execute("""create  or replace function update_state_purchase_order() returns trigger as $BODY$
          DECLARE
             pl_cur refcursor ;
             pl_rec record ;
             rel_cur refcursor ;
             rel_rec record ;
             ncount int ;
             powkid int ;
          BEGIN
             if NEW.state = 'purchase' then  /* 確認成正式採購訂單 */
                open pl_cur for select * from purchase_order_line where order_id = NEW.id ;
                loop
                   fetch pl_cur into pl_rec ;
                   exit when not found ;
                   select count(*) into ncount from po_wkorder_purchase_order_rel1 where po_line_id=pl_rec.id ;
                   if ncount = 1 then
                      select powk_id into powkid from po_wkorder_purchase_order_rel1 where po_line_id=pl_rec.id ;
                      update alldo_gh_iot_po_wkorder set booking_blank_num=pl_rec.product_qty,booking_blank=TRUE,po_id=pl_rec.order_id 
                          where id = powkid ;
                   elsif ncount > 1 then
                       open rel_cur for select * from po_wkorder_purchase_order_rel1 where po_line_id=pl_rec.id ;
                       loop
                          fetch rel_cur into rel_rec ;
                          exit when not found ;
                          update alldo_gh_iot_po_wkorder set booking_blank_num=po_num,booking_blank=TRUE,po_id=pl_rec.order_id 
                             where id = rel_rec.powk_id ; 
                       end loop ;
                       close rel_cur ;
                   end if ;    
                end loop ;
                close pl_cur ;
             end if ;
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次確認採購訂單 purchase_order state='purchase' 作動一次 trigger
        self._cr.execute("""drop trigger if exists update_state_purchase_order on purchase_order ;""")
        self._cr.execute("""create trigger update_state_purchase_order after update of state on purchase_order
                                 for each row execute procedure update_state_purchase_order();""")

        self._cr.execute("""drop function if exists ins_stock_move_line() cascade""")
        self._cr.execute("""create  or replace function ins_stock_move_line() returns trigger as $BODY$
          DECLARE
            ptid int ;
            ncount int ;
            stockno varchar ;
          BEGIN
             if NEW.picking_id is not null and NEW.picking_type_id in (select id from stock_picking_type where sequence_code='IN') then   /* 收貨 */
                update stock_picking set location_dest_id=6 where id = NEW.picking_id ;  /* 入 Inter Company Trans  */
                update stock_move set location_dest_id=6 where id=NEW.id ;
                select name into stockno from stock_picking where id = NEW.picking_id ;
                select count(*) into ncount from stock_move_line where move_id=NEW.id ;
                if ncount = 0 then
                   insert into stock_move_line(move_id,company_id,product_id,product_uom_id,product_qty,product_uom_qty,location_id,location_dest_id,state,reference,picking_id) values
                    (NEW.id,NEW.company_id,NEW.product_id,NEW.product_uom,NEW.product_uom_qty,NEW.product_uom_qty,NEW.location_id,6,'assigned',stockno,NEW.picking_id) ;
                else
                   update stock_move_line set product_qty=NEW.product_uom_qty,product_uom_qty=NEW.product_uom_qty,location_id=NEW.location_id,location_dest_id=6,picking_id=NEW.picking_id,
                       state='assigned',reference=stockno where move_id=NEW.id and product_id=NEW.product_id ;
                end if ;
             end if ;
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists ins_stock_move_line on stock_move ;""")
        self._cr.execute("""create trigger ins_stock_move_line after insert on stock_move
                                for each row execute procedure ins_stock_move_line()""")

        self._cr.execute("""drop function if exists update_state_workorder() cascade""")
        self._cr.execute("""create  or replace function update_state_workorder() returns trigger as $BODY$
          DECLARE
             mogid int ;
             ncount int ;
             powkid int ;
          BEGIN
             if NEW.state='4' and OLD.state='3' then
                update alldo_gh_iot_schedule_line set active=False where mo_no=NEW.id ;
             end if ;   
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次工單狀態變更 alldo_gh_iot_workorder state 作動一次 trigger
        self._cr.execute("""drop trigger if exists update_state_workorder on alldo_gh_iot_workorder ;""")
        self._cr.execute("""create trigger update_state_workorder after update of state on alldo_gh_iot_workorder
                                         for each row execute procedure update_state_workorder();""")


        self._cr.execute("""drop function if exists update_repdate_stockpicking_report() cascade""")
        self._cr.execute("""create  or replace function update_repdate_stockpicking_report() returns trigger as $BODY$
          DECLARE
             spid int ;
             ncount int ;
             powkid int ;
          BEGIN
             select count(*) into ncount from stock_picking where report_no=NEW.name ;
             if ncount > 0 then
                select id into spid from stock_picking where report_no=NEW.name ;
                update stock_picking set schedule_date=NEW.report_date,date_done=NEW.report_date,date=NEW.report_date where id = spid ;
             end if ; 
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")



        # 針對每次工單狀態變更 alldo_gh_iot_stockpicking_report report_date 作動一次 trigger
        self._cr.execute("""drop trigger if exists update_repdate_stockpicking_report on alldo_gh_iot_stockpicking_report ;""")
        self._cr.execute("""create trigger update_repdate_stockpicking_report after update of report_date on alldo_gh_iot_stockpicking_report
                                                 for each row execute procedure update_repdate_stockpicking_report();""")

        self._cr.execute("""drop function if exists update_date_done() cascade""")
        self._cr.execute("""create  or replace function update_date_done() returns trigger as $BODY$
          DECLARE
             ncount int ;
          BEGIN
             update stock_picking set date=NEW.scheduled_date,date_done=NEW.scheduled_date where id = NEW.id ;
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists update_date_done on stock_picking ;""")
        self._cr.execute("""create trigger update_date_done after update of scheduled_date on stock_picking
                                                    for each row execute procedure update_date_done();""")

        self._cr.execute("""update stock_picking set date=date_done where date_done is not null and picking_type_id = 2 ;""")



