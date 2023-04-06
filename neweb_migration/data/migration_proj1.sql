create extension dblink;
select dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
delete from neweb_setup_desc_item ;
alter table neweb_setup_desc_itemdisable trigger all ;
insert into neweb_setup_desc_item (id,create_uid,create_date,name,write_uid,write_date,sequence)
select id,create_uid,create_date,name,write_uid,write_date,sequence from
dblink('hostaddr=localhost port=5432 dbname=NEWEB user=odoo password=odoo','select id,create_uid,create_date,name,write_uid,write_date,sequence from neweb_setup_desc_item')
 as fields(id integer,create_uid integer,create_date timestamp without time zone,name character varying,write_uid integer,write_date timestamp without time zone,sequence integer) ;
