# -*- coding: utf-8 -*-
import psycopg2 as pg
from globalVars import GlobalVars

name = 'odoo10_to_odoo13_data_transfer'

gv = GlobalVars()

# 忽略的特定開頭的資料表
ignore_doc = [
    'calendar',
    'ir',
    'res'
]

# 忽略特定的資料表
ignore_table = [
    'mail_tracking_value',
    'product_pricelist',
    'stock_picking_type',
    'mail_template',
    'zimo_acls3203', 
    'readers_group_logs', 
    'tags_collect', 
    'zimo_acls203'
]

# 指定要轉入的資料表
res_doc = [
    # 'res_partner',
    # 'res_users',
    # 'res_mqtt',
    # 'ir_attachment'
    'neweb_repair_questionnaire',
    'neweb_repair_question',
    'neweb_repair_repair',
    'neweb_repair_manager_note',
    'neweb_repair_repair_line',
    'neweb_repair_repair_part',
    'neweb_repair_repair_care_call_log',
    'neweb_repair_repair_questionnaire',
    'neweb_repair_parts_categ',
    'neweb_repair_repeat_call_report',
    'neweb_repair_repeatcall_excel_download',
    #
    'neweb_sale_analysis_team_targetgp',
    'neweb_sale_analysis_teammember_targetgp',
    'neweb_sale_analysis_teammember_utargetgp',
    'neweb_sale_analysis_sale_revemueq',
    'neweb_sale_analysis_sale_revenuem',
    'neweb_sale_analysis_sale_revenuel',
    'neweb_sale_analysis_expense_report',
    'neweb_sale_analysis_expense_line',
    'neweb_sale_analysis_expenseitem',
    'neweb_sale_analysis_expenseevent',
    'neweb_sale_analysis_expensedoc',
    'neweb_sale_analysis_cf_sumline',
    'neweb_sale_analysis_group_member',
    'neweb_sale_analysis_op_program',
    'neweb_sale_analysis_official_doc',
    'neweb_sale_analysis_saleanalysis_excel_dpwnload',
    'neweb_sale_analysis_travel_report',
    #
    'neweb_enhancement_security_download',
    'neweb_enhancement_security_category',
    'neweb_enhancement_security_group',
    #
    'neweb_invoice_invoiceopen',
    'neweb_invoice_invoiceopen_line',
    'neweb_invoice_invopen_list',
    'neweb_invoice_proj_inv_excel_download',
    'neweb_invoice_projectdata',
    'neweb_invoice_invoicedata',
    'neweb_invoice_purinvdata',
    #
    'neweb_emp_timesheet_inspection_alert_mail',
    'neweb_emp_timesheet_hrholiday',
    'neweb_emp_timesheet_hrholiday_line',
    'neweb_emp_timesheet_inspection_calendar',
    'neweb_emp_timesheet_repair_calendar',
    'neweb_emp_timesheet_timesheet_calendar',
    'neweb_emp_timesheet_timesheet_calendar_line',
    'neweb_emp_timesheet_timesheet_lock',
    'neweb_emp_timesheet_timesheet_adjustowner',
    'neweb_emp_timesheet_timesheet_download',
    'neweb_emp_timesheet_timesheet_worktype',
    'neweb_emp_timesheet_todo_calendar',
    'neweb_emp_timesheet_tolerance_setting',
    'neweb_emp_timesheet_workdate_check',
    #
    'neweb_chi_invoicing_excel_download',
    'neweb_chi_invoicing_purinv_excel_download',
    'neweb_chi_invoicing_invoiceopen_excel_download',
    'neweb_chi_invoicing_purchase_select',
    'neweb_chi_invoicing_purchase_select_line',
    'neweb_chi_invoicing_excelset_seq',
    'neweb_chi_invoicing_package_excel_download',
    'neweb_chi_invoicing_package_purinv_excel_download',
    'neweb_chi_invoicing_package_saleinv_excel_download',
    'neweb_chi_invoicing_package_project',
    'neweb_chi_invoicing_package_product',
    'neweb_chi_invoicing_package_purchase',
    'neweb_chi_invoicing_package_sales',
    'neweb_chi_invoicing_invoiceline',
    'neweb_chi_invoicing_un_export_invoiceopen',
    'neweb_chi_invoicing_un_export_invoiceopenline',
    'neweb_chi_invoicing_un_export_main_proj',
    'neweb_chi_invoicing_un_export_main_proj_line',
    'neweb_chi_invoicing_export_main_proj_log',
    'neweb_chi_invoicing_export_main_purchase_log',
    'neweb_chi_invoicing_export_main_sales_log',
    'neweb_chi_invoicing_productset_seq',
    'neweb_chi_invoicing_un_export_proj',
    'neweb_chi_invoicing_un_export_proj_line',
    'neweb_chi_invoicing_export_proj_log',
    'neweb_chi_invoicing_incomeoutcome_seq',
    'neweb_chi_invoicing_export_purchase_log',
    'neweb_chi_invoicing_export_sales_log',
    'neweb_chi_invoicing_un_export_purinv',
    'neweb_chi_invoicing_un_export_purinvline',
]

# 特殊欄位
special_field = [
    # 'references',
    # 'default',
    # 'N4_relieve',
    # 'N5_relieve',
    # 'N6_relieve',
    # 'FReplace',
    # 'FJYnum'
]

# 沒有id欄位的資料表
without_id_table = [
    # 'jg',
    # 'stock_route_product',
    # 'stock_route_warehouse'
]


def init_db_connect(res_info, target_info):
    target = pg.connect(target_info)
    cursor = target.cursor()

    #  開啟 dblink 功能
    cursor.execute("SELECT * FROM pg_extension WHERE extname='dblink'")
    if not cursor.rowcount:
        cursor.execute('CREATE EXTENSION dblink')

    cursor.execute(f"""
        SELECT dblink_connect('resource', '{res_info}');
    """)
    print('* Already connect Resource & target database')
    return target


def reconnect_resource(cursor, res_info):
    print('* Reconnect resource database', end='\r')
    cursor.execute(f"""
        SELECT dblink_disconnect('resource');
        SELECT dblink_connect('resource', '{res_info}');
    """)


def run():
    res_info = gv.getVar('resource')['connection']
    target_info = gv.getVar('target')['connection']
    conn = init_db_connect(res_info, target_info)
    cursor = conn.cursor()

    # jg 這是一張獨立資料表要轉入的, 這裡先建立好
    # print('* Create table "jg"')
    # cursor.execute("""
    #     DROP TABLE IF EXISTS jg;
    #     CREATE TABLE jg (
    #         name varchar(255),
    #         jg varchar(255)
    #     );
    # """)

    # 因有存在空值，因此先移除幾個欄位的必填屬性
    # print('* Remove many column not null')
    # cursor.execute("""
    #     ALTER TABLE mrp_bom ALTER consumption DROP NOT NULL;
    #     ALTER TABLE mrp_production ALTER consumption DROP NOT NULL;
    #     ALTER TABLE stock_move_line ALTER company_id DROP NOT NULL;
    #     ALTER TABLE stock_production_lot ALTER company_id DROP NOT NULL;
    # """)

    # 取得資料表交集
    print('* Get database intersection')
    cursor.execute(f"""
        SELECT 
		    a.table_name
        FROM (
            SELECT table_name 
                FROM dblink('resource', 'SELECT table_name FROM information_schema.columns WHERE table_schema = ''public''') AS t1(table_name varchar)	
            INTERSECT
            SELECT table_name 
                FROM information_schema.columns 
                WHERE table_schema='public'
        ) AS a
        LEFT JOIN (
            SELECT relname, reltuples FROM dblink('resource', 'SELECT relname, reltuples FROM pg_class r JOIN pg_namespace n ON (relnamespace = n.oid) WHERE relkind = ''r'' AND n.nspname = ''public''') AS t1(relname varchar, reltuples numeric)
        ) AS b ON a.table_name = b.relname
        WHERE b.reltuples <> 0 GROUP BY a.table_name ORDER BY a.table_name;
    """)

    # 過濾table
    result = filter(lambda x: x[0] not in ignore_table, cursor.fetchall())
    table_doc = []
    for index, value in enumerate(result):
        table_name = value[0]
        if table_name in table_doc:
            continue

        print(f'* Process {table_name}', end='\r')
        # 先忽略ir, res開頭的資料表, 往後要忽略的資料表也可寫在 ignore_doc
        # 而 res_doc 是可搬移資料的例外表
        if table_name.split('_')[0] in ignore_doc and table_name not in res_doc:
            print(f'* Skip {table_name}                               ', end='\r')
            continue

        if index:
            reconnect_resource(cursor, res_info)

        # 關閉觸發器
        print(f'* Process {table_name} => Disable trigger', end='\r')
        cursor.execute(f"ALTER TABLE {table_name} DISABLE TRIGGER ALL;")

        # 取得欄位名稱及型別, 後面組合字串會用
        print(f'* Process {table_name} => Get column information', end='\r')
        cursor.execute(f"""
            SELECT 
                t1.column_name, t1.data_type 
            FROM
                (SELECT
                    table_name, column_name, data_type 
                FROM information_schema.columns WHERE table_schema='public') AS t1
                INNER JOIN (
                    SELECT * FROM dblink('resource', 'select table_name, column_name, data_type from information_schema.columns where table_schema = ''public''') AS t1(table_name varchar, column_name varchar, data_type varchar)
                ) AS t2 ON t1.table_name=t2.table_name AND t1.column_name=t2.column_name
            WHERE t1.table_name = '{table_name}';
        """)
        field_name, field_type = [], []
        for l in cursor.fetchall():
            col_name, col_type = l[0], l[1]
            if col_name in special_field:
                field_name.append(f'"{col_name}"')
                field_type.append(f'"{col_name}" {col_type}')
            else:
                field_name.append(f'{col_name.lower()}')
                field_type.append(f'{col_name.lower()} {col_type}')
        field_name, field_type = ",".join(field_name), ",".join(field_type)

        if table_name == 'res_partner':
            print(f'* Process {table_name} => Delete id=7 user        ', end='\r')
            cursor.execute(f"""
                DELETE FROM {table_name} WHERE id = 7;
                UPDATE {table_name} 
                SET partner_share = 't', type = 'private' 
                WHERE id = 3;
            """)

            print(f'* Process {table_name} => Insert data             ', end='\r')
            cursor.execute(f"""
                INSERT INTO {table_name} ({field_name})
                SELECT {field_name}
                FROM dblink('resource', 'SELECT {field_name} FROM {table_name} WHERE id > 6')
                AS fields({field_type});
            """)

            print(f'* Process {table_name} => Update data             ', end='\r')
            cursor.execute(f"""
                UPDATE {table_name} SET type = 'private' WHERE id > 6;
            """)
        elif table_name == 'res_users':
            print(f'* Process {table_name} => Insert data             ', end='\r')
            cursor.execute(f"""
                INSERT INTO {table_name} ({field_name})
                SELECT {field_name}
                FROM dblink('resource', 'SELECT {field_name} FROM {table_name} WHERE id > 5')
                AS fields({field_type});
            """)
        else:
            print(f'* Process {table_name} => Check exist data        ', end='\r')
            cursor.execute(f"SELECT * FROM {table_name}")

            if cursor.rowcount:
                print(f'* Process {table_name} => Clear exist data    ', end='\r')
                cursor.execute(f"DELETE FROM {table_name}")

            print(f'* Process {table_name} => Insert data             ', end='\r')
            cursor.execute(f"""
                INSERT INTO {table_name} ({field_name})
                SELECT {field_name}
                FROM dblink('resource', 'SELECT {field_name} FROM {table_name}')
                AS fields({field_type});
            """)
            # print(cursor.query)

        if table_name[-3:] != 'rel' and table_name not in without_id_table:
            print(f'* Process {table_name} => Update sequence         ', end='\r')
            cursor.execute(f'SELECT MAX(id) + 1 FROM {table_name}')
            max_id = cursor.fetchone()

            if max_id[0]:
                cursor.execute(f'ALTER SEQUENCE {table_name}_id_seq RESTART WITH {max_id[0]}')

        # 開啟觸發器
        print(f'* Process {table_name} => Enable trigger              ', end='\r')
        cursor.execute(f"ALTER TABLE {table_name} ENABLE TRIGGER ALL;")

        print(f'* Process {table_name} => Commit                      ', end='\r')
        conn.commit()
        table_doc.append(table_name)
        print(f'* Done {table_name}                                   ')

    # 公司別只有1個, 所以就直接更新
    print(f'* Update company')
    cursor.execute("""
        UPDATE stock_move_line SET company_id = 1;
        UPDATE stock_production_lot SET company_id = 1;
        UPDATE mrp_bom SET consumption='warning' WHERE consumption IS NULL;
        UPDATE mrp_production SET consumption='flexible' WHERE consumption IS NULL;
    """)

    print('* Set many column not null')
    cursor.execute("""
        ALTER TABLE stock_move_line ALTER company_id SET NOT NULL;
        ALTER TABLE stock_production_lot ALTER company_id SET NOT NULL;
        ALTER TABLE mrp_bom ALTER consumption SET NOT NULL;
        ALTER TABLE mrp_production ALTER consumption SET NOT NULL;
    """)

    print('* Search cf_report_define relation')
    sub_sql = """
        SELECT a.id, b.model FROM 
        (SELECT id, name, model_id FROM cf_report_define) AS a
        LEFT JOIN (SELECT id, model FROM ir_model) AS b ON a.model_id = b.id
        ORDER BY a.id;
    """
    cursor.execute(f"""
        SELECT id, model
        FROM dblink('resource', '{sub_sql}')
        AS fields(id INTEGER, model VARCHAR);
    """)

    print('* Update cf_report_define relation')
    for line in cursor.fetchall():
        cursor.execute(f"""
            UPDATE cf_report_define SET model_id = a.id FROM ir_model a 
            WHERE a.model = '{line[1]}' AND cf_report_define.id = {line[0]};
        """)

    print('* Disable cf_report_define trigger and constraint')
    cursor.execute("""
        ALTER TABLE cf_report_define_field DISABLE TRIGGER ALL;
        ALTER TABLE cf_report_define_field DROP CONSTRAINT cf_report_define_field_uniq_repoer_model_field;
    """)

    print('* Update cf_report_define model_id')
    cursor.execute("""
        UPDATE cf_report_define_field SET model_id = a.model_id FROM cf_report_define a 
        WHERE a.id = cf_report_define_field.report_id;
    """)

    print('* Search cf_report_define model_name and name')
    sub_sql = """
        SELECT a.id, c.model AS model_name, b.name FROM 
        (SELECT id, model_id, field_id FROM cf_report_define_field) AS a
        LEFT JOIN (SELECT id, name, model_id FROM ir_model_fields) AS b ON a.model_id = b.model_id AND a.field_id = b.id
        LEFT JOIN (SELECT id, model FROM ir_model) AS c ON a.model_id = c.id
        ORDER BY c.model;
    """
    cursor.execute(f"""
        SELECT id, model_name, name
        FROM dblink('resource', '{sub_sql}')
        AS fields(id INTEGER, model_name VARCHAR, name VARCHAR);
    """)

    print('* Update cf_report_define model_name and name')
    for line in cursor.fetchall():
        cursor.execute(f"""
            UPDATE cf_report_define_field SET field_id = a.id FROM
            (
                SELECT id, model, name FROM ir_model_fields 
                WHERE model = '{line[1]}' AND name = '{line[2]}'
            ) AS a
            WHERE cf_report_define_field.id = {line[0]};
        """)

    print('* Enable cf_report_define trigger and constraint')
    cursor.execute("""
        ALTER TABLE cf_report_define_field ENABLE TRIGGER ALL;
        ALTER TABLE cf_report_define_field ADD CONSTRAINT cf_report_define_field_uniq_repoer_model_field UNIQUE (report_id, model_id, related_field_id, field_id);
    """)

    print('* Commit change')
    conn.commit()

    print('* Close cursor')
    cursor.close()

    print('* Close connection')
    conn.close()
    print('*** ALL TRANSFER IS DONE ***')
