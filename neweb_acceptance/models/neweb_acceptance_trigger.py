# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class NewebAcceptanceTrigger(models.Model):
    _name = "neweb.acceptance_trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists update_projsaleitem_status() cascade""")
        self._cr.execute("""create  or replace function update_projsaleitem_status() returns trigger as $BODY$
          DECLARE
            prodid int ;
            mynowdate date ;
          BEGIN
            select current_timestamp::DATE into mynowdate ;
            update neweb_project set projsaleitem_status = NEW.projsaleitem_status where id=NEW.project_no ;
            if NEW.projsaleitem_status is not null then
               update neweb_acceptance set keyin_date=mynowdate where id=NEW.id ;
               update neweb_acceptance_line set projsaleitem_status=NEW.projsaleitem_status,keyin_date=mynowdate where acceptance_id=NEW.id and active=True;
            end if ;
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次變更 neweb_acceptance=> projsaleitem_status  作動一次 trigger
        self._cr.execute("""drop trigger if exists update_projsaleitem_status on neweb_acceptance;""")
        self._cr.execute("""create trigger update_projsaleitem_status after update of projsaleitem_status on neweb_acceptance
                                 for each row execute procedure update_projsaleitem_status();""")

        self._cr.execute("""drop function if exists insert_neweb_project_acceptance() cascade""")
        self._cr.execute("""create  or replace function insert_neweb_project_acceptance() returns trigger as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            select count(*) into ncount from neweb_acceptance where project_no=NEW.id ;
            if ncount = 0 then
               insert into neweb_acceptance(project_no,acceptance_status,proj_sale,active) values (NEW.id,'1',NEW.proj_sale,TRUE) ;
            end if ;
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        # 針對每次新增 neweb_project => neweb_acceptance 新增一筆
        self._cr.execute("""drop trigger if exists insert_neweb_project_acceptance on neweb_project ;""")
        self._cr.execute("""create trigger insert_neweb_project_acceptance after insert on neweb_project
                                 for each row execute procedure insert_neweb_project_acceptance();""")

        self._cr.execute("""drop function if exists insert_acceptance_assist() cascade""")
        self._cr.execute("""create  or replace function insert_acceptance_assist() returns trigger as $BODY$
          DECLARE
            workemail varchar ;
          BEGIN
            if NEW.sale_assist is not null then
               select work_email into workemail from hr_employee where id=NEW.sale_assist and active=True ;
               NEW.assist_email = workemail ;
            end if ;
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        # 針對每次新增 neweb_acceptance.assist Trigger 動作
        self._cr.execute("""drop trigger if exists insert_acceptance_assist on neweb_acceptance_assist ;""")
        self._cr.execute("""create trigger insert_acceptance_assist before insert on neweb_acceptance_assist
                                 for each row execute procedure insert_acceptance_assist();""")

        self._cr.execute("""drop function if exists update_acc_sale_close() cascade""")
        self._cr.execute("""create  or replace function update_acc_sale_close() returns trigger as $BODY$
          DECLARE
            workemail varchar ;
          BEGIN
            if NEW.acc_sale_close = TRUE then
               update neweb_acceptance set active=FALSE,acceptance_status='2' where project_no = NEW.project_no ;
            end if ;
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        # 針對每次變更 neweb_invoice_invoiceopen => acc_sale_close  作動一次 trigger
        self._cr.execute("""drop trigger if exists update_acc_sale_close on neweb_invoice_invoiceopen;""")
        self._cr.execute("""create trigger update_acc_sale_close after update of acc_sale_close on neweb_invoice_invoiceopen
                                         for each row execute procedure update_acc_sale_close();""")


        self._cr.execute("""drop function if exists update_acceptanced_date2() cascade""")
        self._cr.execute("""create  or replace function update_acceptanced_date2() returns trigger as $BODY$
         DECLARE
           mynowdate date ;
         BEGIN
           select current_timestamp::DATE into mynowdate ;
           if NEW.acceptanced_date2 is not null  then
              update neweb_acceptance set active=FALSE,acceptanced_date2=NEW.acceptanced_date2,acceptance_status='2' where project_no = NEW.id ;
           end if ;
           return NEW ;
         END;$BODY$
         LANGUAGE plpgsql;""")


        # 針對每次變更 neweb_project ＝> acceptanced_date2 時 作動一次 trigger
        self._cr.execute("""drop trigger if exists update_acceptanced_date2 on neweb_project ;""")
        self._cr.execute("""create trigger update_acceptanced_date2 after update of acceptanced_date2 on neweb_project
                                                 for each row execute procedure update_acceptanced_date2();""")

        # self._cr.execute("""drop function if exists update_projsaleitem_status() cascade""")
        # self._cr.execute("""create  or replace function update_projsaleitem_status() returns trigger as $BODY$
        #   DECLARE
        #     prodid int ;
        #     mynowdate date ;
        #     projid  int ;
        #   BEGIN
        #     select project_no into projid from neweb_acceptance where id = NEW.acceptance_id ;
        #     select current_timestamp::DATE into mynowdate ;
        #     if NEW.projsaleitem_status is not null then
        #        update neweb_project set projsaleitem_status = NEW.projsaleitem_status where id=projid ;
        #        update neweb_acceptance set keyin_date=mynowdate,projsaleitem_status=NEW.projsaleitem_status where id=NEW.acceptance_id and active=TRUE ;
        #        update neweb_acceptance_line set keyin_date=mynowdate where id=NEW.id ;
        #     end if ;
        #     return NEW ;
        #   END;$BODY$
        #   LANGUAGE plpgsql;""")

        # 針對每次變更 neweb_acceptance_line => projsaleitem_status  作動一次 trigger
        self._cr.execute("""drop trigger if exists update_projsaleitem_status on neweb_acceptance_line;""")
        # self._cr.execute("""create trigger update_projsaleitem_status after update of projsaleitem_status on neweb_acceptance_line
        #                                  for each row execute procedure update_projsaleitem_status();""")

        self._cr.execute("""drop function if exists update_proj_acceptanced_date1() cascade""")
        self._cr.execute("""create  or replace function update_proj_acceptanced_date1() returns trigger as $BODY$
          DECLARE
            prodid int ;
            mynowdate date ;
            projid  int ;
          BEGIN
            update neweb_acceptance set acceptanced_date1=NEW.acceptanced_date1 where project_no=NEW.id and active=TRUE ;
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次變更 neweb_project => acceptanced_date1  作動一次 trigger
        self._cr.execute("""drop trigger if exists update_proj_acceptanced_date1 on neweb_project;""")
        self._cr.execute("""create trigger update_proj_acceptanced_date1 after update of acceptanced_date1 on neweb_project
                                                 for each row execute procedure update_proj_acceptanced_date1();""")
