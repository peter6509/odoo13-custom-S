# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class EraTrigger1(models.Model):
    _name = "era.trigger1"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists update_house_priceunit () cascade""")
        self._cr.execute("""create  or replace function update_house_priceunit () returns trigger as $BODY$
          DECLARE
            ncount int ;
            memberid int ;
            m_cur refcursor ;
            m_rec record ;
          BEGIN
            open m_cur for select id from era_household_member where house_id = NEW.id and active=TRUE ; 
            loop
               fetch m_cur into m_rec ;
                exit when not found ;
                update era_member_income_emeter set emeter_unit=NEW.price_unit where member_id=m_rec.id ;
            end loop ;
            close m_cur ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")


        # 針對每次新增 era_member_income_emeter  作動一次 trigger
        self._cr.execute("""drop trigger if exists update_house_priceunit on era_household_house_line ;""")
        self._cr.execute("""create trigger update_house_priceunit after update of price_unit on era_household_house_line
                                                 for each row execute procedure update_house_priceunit ();""")

