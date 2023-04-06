# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, api


class EraContractTrigger(models.Model):
    _name = "era.contract_trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists insert_era_contract() cascade""")
        self._cr.execute("""create  or replace function insert_era_contract() returns trigger as $BODY$
          DECLARE
            ncount int ;
            seqid int ;
            conseq int ;
            conno varchar ;
            houseno varchar ;
            memberno varchar ;
            ncount1 int ;
          BEGIN           
           if NEW.name is null then 
                select house_no into houseno from era_household_house_line where id = NEW.house_id ;
                memberno = concat(houseno,'-',NEW.member_pid) ;
                select count(*) into ncount from era_contract_seq where name=memberno ;
                if ncount > 0 then
                   select id,coalesce(seq,0) into seqid,conseq from era_contract_seq where name=memberno ;
                   conseq = conseq + 1 ;
                   conno = concat(memberno,'-',conseq::TEXT) ;
                   update era_contract_seq set seq=conseq where id = seqid ;
                else
                   if memberno is not null then
                       insert into era_contract_seq(name,seq) values (memberno,0) ;  
                   end if ;     
                   conno = memberno;
                end if ;
                update era_contract set name=conno where id=NEW.id ;
            end if ;                           
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次新增 era_contract NEW Contract  作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_era_contract on era_contract ;""")
        self._cr.execute("""create trigger insert_era_contract after insert on era_contract
                                 for each row execute procedure insert_era_contract();""")

        self._cr.execute("""drop function if exists insert_era_contract_emeter() cascade""")
        self._cr.execute("""create  or replace function insert_era_contract_emeter() returns trigger as $BODY$
          DECLARE
            ncount int ;
          BEGIN           
            select count(*) into ncount from era_contract_close where contract_id = NEW.contract_id ;
            if ncount = 0 then
               insert into era_contract_close(contract_id,household_clean_fee) values (NEW.contract_id,0) ;
            end if ;               
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists insert_era_contract_emeter on era_contract_emeter ;""")
        self._cr.execute("""create trigger insert_era_contract_emeter after insert on era_contract_emeter
                                 for each row execute procedure insert_era_contract_emeter()""")
