# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class NewebempTimesheetTrigger(models.Model):
    _name = "neweb_emp_timesheet.trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists updatetodo() cascade""")
        self._cr.execute("""create  or replace function updatetodo() returns trigger as $BODY$
          DECLARE
          maxid int ;
          ncount int ;
          BEGIN
             if NEW.todo_completed='1' and OLD.todo_completed='2' then 
               execute update_todocalendar(NEW.id,NEW.write_uid);
             end if ;        
           return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists update_on_todo_calendar on neweb_emp_timesheet_todo_calendar;""")
        self._cr.execute("""create trigger update_on_todo_calendar after update of todo_completed on neweb_emp_timesheet_todo_calendar
                                 for each row execute procedure updatetodo();""")

        self._cr.execute("""drop function if exists insert_timesheet_calline() cascade""")
        self._cr.execute("""create  or replace function insert_timesheet_calline() returns trigger as $BODY$
          DECLARE
          maxid int ;
          ncount int ;
          myhour float ;
          myminute float ;
          mytime  float ;
          BEGIN
             select abs(date_part('hour',age(NEW.timesheet_end_date,NEW.timesheet_start_date))) into myhour;
             select abs(date_part('minute',age(NEW.timesheet_end_date,NEW.timesheet_start_date))) into myminute ;
             mytime = myhour + (myminute/60) ;   
             update neweb_emp_timesheet_timesheet_calendar_line set timesheet_duration=mytime,duration=mytime where id=NEW.id ;   
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists insert_timesheet_calline on neweb_emp_timesheet_timesheet_calendar_line;""")
        self._cr.execute("""create trigger insert_timesheet_calline after insert on neweb_emp_timesheet_timesheet_calendar_line
                                for each row execute procedure insert_timesheet_calline(); """)

        self._cr.execute("""drop function if exists update_timesheet_calline() cascade""")
        self._cr.execute("""create  or replace function update_timesheet_calline() returns trigger as $BODY$
          DECLARE
          maxid int ;
          ncount int ;
          myhour float ;
          myminute float ;
          mytime  float ;
          BEGIN
             select abs(date_part('hour',age(NEW.timesheet_end_date,NEW.timesheet_start_date))) into myhour;
             select abs(date_part('minute',age(NEW.timesheet_end_date,NEW.timesheet_start_date))) into myminute ;
             mytime = myhour + (myminute/60) ;   
             update neweb_emp_timesheet_timesheet_calendar_line set timesheet_duration=mytime,duration=mytime where id=NEW.id ; 
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists update_timesheet_calline_s on neweb_emp_timesheet_timesheet_calendar_line ;""")
        self._cr.execute("""create trigger update_timesheet_calline_s after update of timesheet_start_date on neweb_emp_timesheet_timesheet_calendar_line
                                        for each row execute procedure update_timesheet_calline(); """)

        self._cr.execute("""drop trigger if exists update_timesheet_calline_e on neweb_emp_timesheet_timesheet_calendar_line ;""")
        self._cr.execute("""create trigger update_timesheet_calline_e after update of timesheet_end_date on neweb_emp_timesheet_timesheet_calendar_line
                                                for each row execute procedure update_timesheet_calline(); """)

        self._cr.execute("""drop function if exists update_empid_inspection_cal() cascade""")
        self._cr.execute("""create  or replace function update_empid_inspection_cal() returns trigger as $BODY$
          DECLARE
            ncount int ;
            todoid int ;
          BEGIN
             select count(*) into ncount from neweb_emp_timesheet_todo_calendar where 
                  emp_id=OLD.emp_id and contract_no=OLD.contract_no and todo_origin='1' 
                  and todo_completed='2' and todo_datetime::DATE = OLD.inspection_datetime::DATE ;
             if ncount > 0 then
                select min(id) into todoid from neweb_emp_timesheet_todo_calendar where 
                  emp_id=OLD.emp_id and contract_no=OLD.contract_no and todo_origin='1' 
                  and todo_completed='2' and todo_datetime::DATE = OLD.inspection_datetime::DATE ;
                update neweb_emp_timesheet_todo_calendar set emp_id=NEW.emp_id where id = todoid ;  
             end if ;     
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists udate_empid_inspection_calendar on neweb_emp_timesheet_inspection_calendar ;""")
        self._cr.execute("""create trigger udate_empid_inspection_calendar after update of emp_id  on neweb_emp_timesheet_inspection_calendar
                                                        for each row execute procedure update_empid_inspection_cal(); """)