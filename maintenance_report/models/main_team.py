# _*_ coding: utf-8 _*_
# Author: Peter Wu

from odoo import models, fields, api
from odoo.osv.orm import except_orm


class user_main_team(models.Model):
    _inherit = "res.users"

    main_team_id = fields.Integer(string=u'維護團隊代號')


class main_req_team(models.Model):
    _inherit = "maintenance.request"

    main_team_id = fields.Integer(string=u'維護團隊代號')

    @api.multi
    def write(self, vals):
        if 'technician_user_id' in vals and vals['technician_user_id']:
            mytechid = vals['technician_user_id']
            myteamid = self.env['res.users'].search([('id', '=', mytechid)]).main_team_id
            # myteamid = self.env['main_team.group'].search([(mytechid,'in','main_team_member')])
            if myteamid:
                vals['main_team_id'] = myteamid
        rec = super(main_req_team, self).write(vals)
        return rec


class main_team_group(models.Model):
    _name = "main_team.group"

    name = fields.Char(size=2, string=u'組名')
    main_team_member = fields.Many2many('res.users', string=u'組員')

    @api.model_cr
    def init(self):
        self._cr.execute("""DROP FUNCTION IF EXISTS updatemainreq(techid int,teamid int) cascade;""")
        self._cr.execute("""create or replace function updatemainreq(techid int,teamid int) returns CHAR as $BODY$
DECLARE
   ncount integer;
   ncount1 integer;
   group_cur refcursor;
   group_rec record;
BEGIN
  select count(*) into ncount from main_team_group_res_users_rel ;
  select count(DISTINCT res_users_id) into ncount1 from main_team_group_res_users_rel ;
  if ncount = ncount1 then
    update maintenance_request set main_team_id=null ;
    open group_cur for select * from main_team_group_res_users_rel ;
    loop
      fetch group_cur into group_rec;
      exit when not found;
      update maintenance_request set main_team_id=group_rec.main_team_group_id where
           technician_user_id=group_rec.res_users_id ;
    end loop;
    close group_cur;
    return 'T' ;
  else
    return 'F' ;
  end if;
end;$BODY$
LANGUAGE plpgsql;""")


    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise except_orm(u"资料不完整", u"必须輸入組名")
        if 'name' in vals and vals['name']:
            myname = vals['name']
            hasval = self.env['main_team.group'].search([('name', '=', myname)])
            if hasval:
                raise except_orm(u"資料錯誤", u"組名重複,請確認..")
        if 'main_team_member' in vals and not vals['main_team_member']:
            raise except_orm(u"资料不完整", u"必须輸入組員")
        rec = super(main_team_group, self).create(vals)
        myid = rec.id
        mainteammember = self.env['main_team.group'].search([('id', '=', myid)])
        for memberrec in mainteammember.main_team_member:
            # print "%d" % memberrec.id
            resusers_rec = self.env['res.users'].search([('id', '=', memberrec.id)])
            resusers_rec.write({'main_team_id': myid})
            self.env.cr.execute("select updatemainreq(%s,%s)" % (memberrec.id,myid))
            runstate = self.env.cr.fetchone()
            if runstate[0] == 'F':
               raise except_orm(u"組員重複", u"分組中有組員重複")

        return rec

    @api.multi
    def write(self, vals):
        myid = self.id
        if 'name' in vals and not vals['name']:
            raise except_orm(u"资料不完整", u"必须輸入組名")

        if 'main_team_member' in vals and not vals['main_team_member']:
            raise except_orm(u"资料不完整", u"必须輸入組員")
        rec = super(main_team_group, self).write(vals)
        # myid = rec.id
        mainteammember = self.env['main_team.group'].search([('id', '=', myid)])

        for memberrec in mainteammember.main_team_member:
            # print "%d" % memberrec.id
            resusers_rec = self.env['res.users'].search([('id', '=', memberrec.id)])
            resusers_rec.write({'main_team_id': myid})
            # print "UID:%s TEAMID:%s" % (memberrec.id,myid)
            self.env.cr.execute("select updatemainreq(%s,%s)" % (memberrec.id, myid))
            runstate = self.env.cr.fetchone()
            # print "runstate: %s" % runstate[0]
            if runstate[0] == 'F' :
               raise except_orm(u"組員重複", u"分組中有組員重複")

        return rec
