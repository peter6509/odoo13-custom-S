# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class newebsaleanalysisTrigger(models.Model):
    _name = "neweb_sale_analysis.trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists chk_cfsumline() cascade""")
        self._cr.execute("""create  or replace function chk_cfsumline() returns trigger as $BODY$
          DECLARE
            ncount int ;
          BEGIN
             execute runcfsumline(NEW.exp_id) ;
             return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists chk_cfsumline1() cascade""")
        self._cr.execute("""create  or replace function chk_cfsumline1() returns trigger as $BODY$
          DECLARE
            ncount int ;
          BEGIN
             execute runcfsumline(OLD.exp_id) ;
             return OLD ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次更新 neweb_sale_analysis_expense_line  作動一次 trigger
        self._cr.execute("""drop trigger if exists update_on_expense_report on neweb_sale_analysis_expense_line ;""")
        self._cr.execute("""create trigger update_on_expense_report after update on neweb_sale_analysis_expense_line
                                 for each row execute procedure chk_cfsumline1();""")

        # 針對每次新增 neweb_sale_analysis_expense_line  作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_on_expense_report on neweb_sale_analysis_expense_line ;""")
        self._cr.execute("""create trigger insert_on_expense_report after insert on neweb_sale_analysis_expense_line
                                         for each row execute procedure chk_cfsumline();""")

        # 針對每次更新 neweb_sale_analysis_expense  作動一次 trigger
        # self._cr.execute("""drop trigger if exists update_on_expense_report on neweb_sale_analysis_expense_line ;""")
        # self._cr.execute("""create trigger update_on_expense_report after update on neweb_sale_analysis_expense_line
        #                                  for each row execute procedure chk_cfsumline1();""")

        self._cr.execute("""drop function if exists insert_traverl_cowork() cascade""")
        self._cr.execute("""create  or replace function insert_traverl_cowork() returns trigger as $BODY$
          DECLARE
            emp_cur refcursor ;
            emp_rec record ;
            nnum int ;
          BEGIN
             update neweb_sale_analysis_travel_report set co_man1=null,co_man2=null,co_man3=null,co_man4=null,co_man5=null where id=NEW.neweb_sale_analysis_travel_report_id ;
             nnum = 1 ;
             open emp_cur for select * from hr_employee_neweb_sale_analysis_travel_report_rel where neweb_sale_analysis_travel_report_id=NEW.neweb_sale_analysis_travel_report_id ;
             loop
                fetch emp_cur into emp_rec ;
                exit when not found ;
                if nnum=1 then
                   update neweb_sale_analysis_travel_report set co_man1=emp_rec.hr_employee_id where id=NEW.neweb_sale_analysis_travel_report_id ;
                elsif nnum=2 then
                   update neweb_sale_analysis_travel_report set co_man2=emp_rec.hr_employee_id where id=NEW.neweb_sale_analysis_travel_report_id ;
                elsif nnum=3 then
                   update neweb_sale_analysis_travel_report set co_man3=emp_rec.hr_employee_id where id=NEW.neweb_sale_analysis_travel_report_id ;
                elsif nnum=4 then
                   update neweb_sale_analysis_travel_report set co_man4=emp_rec.hr_employee_id where id=NEW.neweb_sale_analysis_travel_report_id ;
                else
                   update neweb_sale_analysis_travel_report set co_man5=emp_rec.hr_employee_id where id=NEW.neweb_sale_analysis_travel_report_id ;
                end if ;
                nnum = nnum + 1 ;
             end loop ;
             close emp_cur ; 
             return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次更新 hr_employee_neweb_sale_analysis_travel_report_rel  作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_traverl_co_work on hr_employee_neweb_sale_analysis_travel_report_rel ;""")
        self._cr.execute("""create trigger insert_traverl_co_work after insert on hr_employee_neweb_sale_analysis_travel_report_rel
                                         for each row execute procedure insert_traverl_cowork();""")