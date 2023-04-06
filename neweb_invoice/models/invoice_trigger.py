# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class newebinvoiceTrigger(models.Model):
    _name = "neweb_invoice.trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists insert_unitprice() cascade""")
        self._cr.execute("""create  or replace function insert_unitprice() returns trigger as $BODY$
          DECLARE
            cusname int ;
            invcontact1 int ;
            invpaymentdate date ;
            myprice float ; 
            openamttot float ;
            openamttot1 float ;
            myamount float ;
            mytax float ;
            senddate date ;
            senddate1 date ;
            ncount int ;
            ncount1 int ;
            mymaxid int ;
            projid int ;
            saleassist varchar ;
            projamounttot float ;
          BEGIN
             select getsaleassist() into saleassist ;
             select amount into myamount from account_tax where id=NEW.invoice_taxtype and active=True ;
             mytax = 1 + round((myamount::numeric/100::numeric),2) ;
             myprice = round((NEW.invoice_unit_price::numeric * mytax::numeric),2) ;
             NEW.invoice_unit_price1 = myprice ;
            /* update neweb_invoice_invoiceopen_line set invoice_unit_price1=myprice where id = NEW.id ; */
            if NEW.invoice_state='2' or NEW.invoice_state='3' then
                select sum(round(invoice_num * invoice_unit_price1,0)) into openamttot from neweb_invoice_invoiceopen_line 
                       where invoice_id = NEW.invoice_id and invoice_state in ('2','3'); 
                select sum(round(invoice_num * invoice_unit_price1,0)) into openamttot1 from neweb_invoice_invoiceopen_line 
                       where invoice_id = NEW.invoice_id and invoice_date=NEW.invoice_date and invoice_state in ('2','3') ;    
                update neweb_invoice_invoiceopen set open_complete_total=openamttot,open_amount_total=openamttot1 where id = NEW.invoice_id ; 
                select project_amount_total into projamounttot from neweb_invoice_invoiceopen where id = NEW.invoice_id ;    
                if abs(projamounttot - openamttot) <= 10 or (openamttot > projamounttot) then
                   update neweb_invoice_invoiceopen set is_completed=TRUE where id = NEW.invoice_id ;
                end if ;     
             end if ;
             /* 當發票狀態由 暫存 轉成 已生效,驗收 */
             if (NEW.invoice_state='3' or NEW.invoice_state='2') then                
                select project_no,invoice_contact1,invoice_paymentdate into projid,invcontact1,invpaymentdate 
                   from neweb_invoice_invoiceopen where id = NEW.invoice_id ;
                select cus_name into cusname from neweb_project where id = projid ;   
                if NEW.invoice_date is not null then   
                   select (NEW.invoice_date + interval '7 day')::DATE into senddate ; 
                else
                   senddate = null ;
                end if ;   
                if NEW.invoice_no is not null and projid is not null then /* 如果有發票號碼且有專案編號 */
                    select count(*) into ncount from neweb_invoice_invoice_sendmail where invoice_no=NEW.invoice_no and sendmail_type='1' ; 
                    if ncount = 0 then
                       if cusname is not null and NEW.invoice_no is not null then
                          insert into neweb_invoice_invoice_sendmail(invoice_date,send_date,partner_id,invoice_contact1,invoice_no,is_send,cando,invoice_taxtype,sale_assist,sendmail_type)
                           values (NEW.invoice_date,senddate,cusname,invcontact1,NEW.invoice_no,False,False,NEW.invoice_taxtype,saleassist,'1') ;
                       end if ;   
                    else
                       update neweb_invoice_invoice_sendmail set invoice_date=NEW.invoice_date,send_date=senddate,partner_id=cusname,invoice_contact1=invcontact1,invoice_no=NEW.invoice_no,
                              is_send=FALSE,cando=FALSE,invoice_taxtype=NEW.invoice_taxtype,sale_assist=saleassist,sendmail_type='1' where invoice_no=NEW.invoice_no and sendmail_type='1' ; 
                    end if ;
                    select max(id) into mymaxid from neweb_invoice_invoice_sendmail where invoice_no=NEW.invoice_no and sendmail_type='1' ;
                    select count(*) into ncount1 from neweb_invoice_invoice_sendmail_line where sendmail_id = mymaxid and inv_sequence_id = NEW.id ;
                    if ncount1 = 0  then
                       if cusname is not null and NEW.invoice_no is not null then
                          insert into neweb_invoice_invoice_sendmail_line(sendmail_id,invoice_spec,invoice_num,invoice_unit_price,invoice_unit_price1,invoice_taxtype,inv_sequence_id) values
                               (mymaxid,NEW.invoice_spec,NEW.invoice_num,NEW.invoice_unit_price,NEW.invoice_unit_price1,NEW.invoice_taxtype,NEW.id) ;
                       end if ; 
                    else
                       update neweb_invoice_invoice_sendmail_line set invoice_spec=NEW.invoice_spec,invoice_num=NEW.invoice_num,invoice_unit_price=NEW.invoice_unit_price,invoice_unit_price1=NEW.invoice_unit_price1,
                               invoice_taxtype=NEW.invoice_taxtype where sendmail_id = mymaxid and inv_sequence_id = NEW.id ;         
                    end if ;
                end if ;    
             end if ;
             return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists update_unitprice() cascade""")
        self._cr.execute("""create  or replace function update_unitprice() returns trigger as $BODY$
          DECLARE
            myprice float ; 
            myamount float ;
            mytax float ;
          BEGIN
             select amount into myamount from account_tax where id=NEW.invoice_taxtype and active=True ;
             mytax = 1 + round((myamount::numeric/100::numeric),2) ;
             NEW.invoice_unit_price1 = round((NEW.invoice_unit_price::numeric * mytax::numeric),2) ;   
             return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次新增 neweb_invoice_invoiceopen_line  作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_on_invoiceopen_line on neweb_invoice_invoiceopen_line ;""")
        self._cr.execute("""create trigger insert_on_invoiceopen_line before insert on neweb_invoice_invoiceopen_line
                                 for each row execute procedure insert_unitprice();""")

        # 針對每次更新 neweb_invoice_invoiceopen_line  作動一次 trigger
        self._cr.execute("""drop trigger if exists update_on_invoiceopen_line on neweb_invoice_invoiceopen_line ;""")
        self._cr.execute("""create trigger update_on_invoiceopen_line before update of invoice_unit_price on neweb_invoice_invoiceopen_line
                                         for each row execute procedure update_unitprice();""")

        self._cr.execute("""drop function if exists update_invoicetot() cascade""")
        self._cr.execute("""create  or replace function update_invoicetot() returns trigger as $BODY$
          DECLARE
            mydate date ; 
            mycompletetot float ;
            myamounttot float ;
            cusname int ;
            invcontact1 int ;
            invpaymentdate date ;
            senddate date ;
            senddate1 date ;
            ncount int ;
            ncount1 int ;
            mymaxid int ;
            projid int ;
            contractid int ;
            projamounttot float ;
          BEGIN
             if NEW.invoice_state='2' or NEW.invoice_state='3' then
                select max(invoice_date) into mydate from neweb_invoice_invoiceopen_line where invoice_state in ('2','3') and invoice_id = NEW.invoice_id ;
                select sum(round(invoice_num * invoice_unit_price1,0)) into mycompletetot from neweb_invoice_invoiceopen_line 
                       where invoice_id = NEW.invoice_id and invoice_state in ('2','3')  ; 
                select sum(round(invoice_num * invoice_unit_price1,0)) into myamounttot from neweb_invoice_invoiceopen_line 
                       where invoice_id = NEW.invoice_id and invoice_date=mydate and invoice_state in ('2','3')  ; 
                update neweb_invoice_invoiceopen set open_complete_total=mycompletetot,open_amount_total=myamounttot
                       where id = NEW.invoice_id ;    
                select project_amount_total into projamounttot from neweb_invoice_invoiceopen where id = NEW.invoice_id ;    
                if abs(projamounttot - mycompletetot) <= 10 or (mycompletetot > projamounttot) then
                   update neweb_invoice_invoiceopen set is_completed=TRUE where id = NEW.invoice_id ;
                end if ;      
             end if ;
             /* 當發票狀態由 暫存 轉成 已生效,驗收 */
             if (NEW.invoice_state='3' or NEW.invoice_state='2') then
                select project_no,invoice_contact1,invoice_paymentdate,contract_no into projid,invcontact1,invpaymentdate,contractid 
                   from neweb_invoice_invoiceopen where id = NEW.invoice_id ;
                select cus_name into cusname from neweb_project where id = projid ;   
                if NEW.invoice_date is not null then   
                   select (NEW.invoice_date + interval '7 day')::DATE into senddate ;  
                    /* 先產生開立7天後通知信 */    
                   select count(*) into ncount from neweb_invoice_invoice_sendmail where invoice_no=NEW.invoice_no and sendmail_type='1' ; 
                   if ncount = 0 then
                      if cusname is not null and NEW.invoice_no is not null then
                         insert into neweb_invoice_invoice_sendmail(project_no,contract_no,invoice_date,send_date,partner_id,invoice_contact1,invoice_no,is_send,cando,invoice_taxtype,sendmail_type)
                            values (projid,contractid,NEW.invoice_date,senddate,cusname,invcontact1,NEW.invoice_no,False,False,NEW.invoice_taxtype,'1') ;
                      end if ; 
                   else
                      update neweb_invoice_invoice_sendmail set project_no=projid,contract_no=contractid,invoice_date=NEW.invoice_date,send_date=senddate,partner_id=cusname,invoice_contact1=invcontact1,
                             invoice_no=NEW.invoice_no,is_send=FALSE,cando=FALSE,invoice_taxtype=NEW.invoice_taxtype where invoice_no=NEW.invoice_no and sendmail_type='1' ;       
                   end if ;
                else
                   senddate = null ;
                end if ;   
                
                /* 產生一般通知信明細 */
                select max(id) into mymaxid from neweb_invoice_invoice_sendmail where invoice_no=NEW.invoice_no and sendmail_type='1' ;
                if NEW.invoice_no is not null then
                    select count(*) into ncount1 from neweb_invoice_invoice_sendmail_line where sendmail_id = mymaxid and inv_sequence_id = NEW.id ;
                    if ncount1 = 0 then
                       if cusname is not null then
                         insert into neweb_invoice_invoice_sendmail_line(sendmail_id,invoice_spec,invoice_num,invoice_unit_price,invoice_unit_price1,invoice_taxtype,inv_sequence_id) values
                             (mymaxid,NEW.invoice_spec,NEW.invoice_num,NEW.invoice_unit_price,NEW.invoice_unit_price1,NEW.invoice_taxtype,NEW.id) ;     
                       end if ;  
                    else
                        update neweb_invoice_invoice_sendmail_line set invoice_spec=NEW.invoice_spec,invoice_num=NEW.invoice_num,invoice_unit_price=NEW.invoice_unit_price,invoice_unit_price1=NEW.invoice_unit_price1,
                               invoice_taxtype=NEW.invoice_taxtype where sendmail_id = mymaxid and inv_sequence_id = NEW.id ;     
                    end if ;
                end if ;    
             end if ;
             return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 變更 invoice_state on neweb_invoice_invoiceopen_line
        self._cr.execute("""drop trigger if exists update_invoice_state on neweb_invoice_invoiceopen_line ;""")
        self._cr.execute("""create trigger update_invoice_state after update of invoice_state on neweb_invoice_invoiceopen_line
                                                 for each row execute procedure update_invoicetot();""")

        self._cr.execute("""drop function if exists update_receivedate() cascade""")
        self._cr.execute("""drop trigger if exists update_receive_date on neweb_invoice_invoiceopen_line ;""")

        self._cr.execute("""drop function if exists update_invoice_no() cascade""")
        self._cr.execute("""create  or replace function update_invoice_no() returns trigger as $BODY$
          DECLARE
            mydate date ; 
            mycompletetot float ;
            myamounttot float ;
            cusname int ;
            invcontact1 int ;
            invpaymentdate date ;
            senddate date ;
            senddate1 date ;
            ncount int ;
            ncount1 int ;
            mymaxid int ;
            projid int ;
            contractid int ;
            projamounttot float ;
          BEGIN
             if NEW.invoice_state='2' or NEW.invoice_state='3' then
                select max(invoice_date) into mydate from neweb_invoice_invoiceopen_line where invoice_state in ('2','3') and invoice_id = NEW.invoice_id ;
                select sum(round(invoice_num * invoice_unit_price1,0)) into mycompletetot from neweb_invoice_invoiceopen_line 
                       where invoice_id = NEW.invoice_id and invoice_state in ('2','3')  ; 
                select sum(round(invoice_num * invoice_unit_price1,0)) into myamounttot from neweb_invoice_invoiceopen_line 
                       where invoice_id = NEW.invoice_id and invoice_date=mydate and invoice_state in ('2','3')  ; 
               update neweb_invoice_invoiceopen set open_complete_total=mycompletetot,open_amount_total=myamounttot
                       where id = NEW.invoice_id ;   
               select project_amount_total into projamounttot from neweb_invoice_invoiceopen where id = NEW.invoice_id ;    
                if abs(projamounttot - mycompletetot) <= 10 or (mycompletetot > projamounttot) then
                   update neweb_invoice_invoiceopen set is_completed=TRUE where id = NEW.invoice_id ;
                end if ;              
             end if ;
             /* 當發票狀態由 暫存 轉成 已生效,驗收 */
             if (NEW.invoice_state='3' or NEW.invoice_state='2') then
                select project_no,invoice_contact1,invoice_paymentdate,contract_no into projid,invcontact1,invpaymentdate,contractid 
                   from neweb_invoice_invoiceopen where id = NEW.invoice_id ;
                select cus_name into cusname from neweb_project where id = projid ;   
                if NEW.invoice_date is not null then   
                   select (NEW.invoice_date + interval '7 day')::DATE into senddate ;  
                    /* 先產生開立7天後通知信 */    
                   select count(*) into ncount from neweb_invoice_invoice_sendmail where invoice_no=NEW.invoice_no and sendmail_type='1' ; 
                   if ncount = 0 then
                      if cusname is not null and NEW.invoice_no is not null then
                         insert into neweb_invoice_invoice_sendmail(project_no,contract_no,invoice_date,send_date,partner_id,invoice_contact1,invoice_no,is_send,cando,invoice_taxtype,sendmail_type)
                            values (projid,contractid,NEW.invoice_date,senddate,cusname,invcontact1,NEW.invoice_no,False,False,NEW.invoice_taxtype,'1') ;
                      end if ;   
                   else
                         update neweb_invoice_invoice_sendmail set project_no=projid,contract_no=contractid,invoice_date=NEW.invoice_date,send_date=senddate,partner_id=cusname,
                                    invoice_contact1=invcontact1,is_send=False,cando=False,invoice_taxtype=NEW.invoice_taxtype where invoice_no=NEW.invoice_no and sendmail_type='1' ;
                   end if ;
                else
                   senddate = null ;
                end if ;   

                /* 產生一般通知信明細 */
                
                if NEW.invoice_no is not null then
                    select max(id) into mymaxid from neweb_invoice_invoice_sendmail where invoice_no=NEW.invoice_no and sendmail_type='1' ;
                    select count(*) into ncount1 from neweb_invoice_invoice_sendmail_line where sendmail_id = mymaxid and inv_sequence_id = NEW.id ;
                    if ncount1 = 0 then
                       if cusname is not null then
                          insert into neweb_invoice_invoice_sendmail_line(sendmail_id,invoice_spec,invoice_num,invoice_unit_price,invoice_unit_price1,invoice_taxtype,inv_sequence_id) values
                              (mymaxid,NEW.invoice_spec,NEW.invoice_num,NEW.invoice_unit_price,NEW.invoice_unit_price1,NEW.invoice_taxtype,NEW.id) ; 
                       end if ;  
                    else
                          update neweb_invoice_invoice_sendmail_line set invoice_spec=NEW.invoice_spec,invoice_num=NEW.invoice_num,invoice_unit_price=NEW.invoice_unit_price,invoice_unit_price1=NEW.invoice_unit_price1,
                               invoice_taxtype=NEW.invoice_taxtype where sendmail_id = mymaxid and inv_sequence_id = NEW.id ;             
                    end if ;
                end if ;    
             end if ;
             return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 變更 invoice_no on neweb_invoice_invoiceopen_line
        self._cr.execute("""drop trigger if exists update_invoice_no on neweb_invoice_invoiceopen_line ;""")
        self._cr.execute("""create trigger update_invoice_no after update of invoice_no on neweb_invoice_invoiceopen_line
                                                         for each row execute procedure update_invoice_no();""")

        self._cr.execute("""drop function if exists update_open_complete_total() cascade""")
        # self._cr.execute("""create  or replace function update_open_complete_total() returns trigger as $BODY$
        #   DECLARE
        #     projectamount float ;
        #     opencomplete float ;
        #   BEGIN
        #      select coalesce(project_amount_total,0),coalesce(open_complete_total,0) into projectamount,opencomplete from neweb_invoice_invoiceopen
        #          where id = NEW.id ;
        #      if abs(projectamount - opencomplete) <= 10 or (opencomplete > projectamount) then
        #         update neweb_invoice_invoiceopen set is_completed=TRUE where id = NEW.id ;
        #      end if ;
        #      return NEW ;
        #   END;$BODY$
        #   LANGUAGE plpgsql;""")

        # 變更 open_complete_total on neweb_invoice_invoiceopen
        self._cr.execute("""drop trigger if exists update_open_complete_total on neweb_invoice_invoiceopen ;""")
        # self._cr.execute("""create trigger update_invoice_no after update of open_complete_total on neweb_invoice_invoiceopen
        #                                                          for each row execute procedure update_open_complete_total();""")





