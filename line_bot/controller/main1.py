# -*- coding: utf-8 -*-
import logging
import re
from datetime import datetime as dt

from linebot import LineBotApi, WebhookHandler, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from odoo.http import request, route, Controller, Response
from odoo.modules.module import get_module_resource


def init_line_bot():
    global line_bot_api, handler
    # 若是chanel_secret 不存在則更新
    if not handler.parser.signature_validator.channel_secret:
        line_bot_api.__init__(params('access_token'))
        handler.parser = WebhookParser(params('channel_secret'))


def params(key):
    return request.env['line.setting'].sudo().get_value(key)


line_bot_api = LineBotApi('')
handler = WebhookHandler('')

_logger = logging.getLogger(__name__)


class LineBotController(Controller):
    @route('/api/callback', methods=['POST'], type='json', auth='public', csrf=False)
    def callback(self):
        init_line_bot()
        r = request
        if 'X-Line-Signature' not in r.httprequest.headers:
            Response.status = 400
            return 'Header "X-Line-Signature" not exist!'
        signature = r.httprequest.headers['X-Line-Signature']
        body = r.httprequest.data.decode('utf-8')

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            _logger.info('[line_bot][callback] Invalid Signature')

        return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    source, r, host, user_id = [
        event.source,
        request,
        request.httprequest.host_url,
        event.source.user_id
    ]

    user = verify_user_id(user_id)
    user_text = event.message.text.strip()

    if user:
        func = {
            '繳費通知': lambda: notify_paid(user),
            '查閱帳單': lambda: check_balance(user),
        }
        status = user.line_request_status

        if user_text in func:
            if status:
                user.line_request_status = ''
            msg = func[user_text]()
        elif status == 'notify':
            msg = notify_paid_create_record(user, user_text)
        else:
            set_main_rich_menu_2_user(user)
            func_name = "」、「".join(func.keys())
            msg = f'Hi, {display_name(user_id)},目前只有 「{func_name}」功能，請回覆功能名稱或是點擊主選單來操作'
    else:
        if re.match(r'^[A-Za-z]\d{9}$', user_text):
            msg = '驗證失敗，請重新輸入'
            if verify_pid(user_text):
                user = user.sudo().search([('member_pid', '=', user_text)], limit=1)
                if any(user):
                    user.line_user_id = user_id
                    set_main_rich_menu_2_user(user)
                    msg = '驗證成功'
        else:
            msg = '請輸入身分證字號，以進行住戶綁定'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg)
    )
    return 'OK'


def verify_user_id(user_id):
    """
    判斷使用者是否有綁定，有綁定則回傳 'res.user' object
    :param user_id:
    :return:
    """
    user = request.env['era.household_member'].sudo().search([('line_user_id', '=', user_id)], limit=1)
    return user


def set_main_rich_menu():
    """
    取得主要 rich menu id
    :return: str rich_menu_id
    """
    _logger.info('Init Main Menu')
    record = request.env['line.rich.menu'].sudo().search([('name', '=', '主選單')], limit=1)

    if not record:
        area_notify = RichMenuArea(
            bounds=RichMenuBounds(x=288, y=64, width=784, height=669),
            action=MessageAction(label='message', text='繳費通知')
        )

        area_balence = RichMenuArea(
            bounds=RichMenuBounds(x=1436, y=68, width=767, height=661),
            action=MessageAction(label='message', text='查閱帳單')
        )

        rich_menu_id = line_bot_api.create_rich_menu(RichMenu(
            size=RichMenuSize(width=2500, height=843),
            selected=True,
            name="主功能",
            chat_bar_text="功能選單",
            areas=[area_notify, area_balence]
        ))

        # set image
        png_path = get_module_resource('line_bot', 'static/img/line_bot/', 'rich_menu_Main.png')
        with open(png_path, 'rb') as f:
            line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)

        record = record.create({
            'name': 'main',
            'rich_menu_id': rich_menu_id,
            'remark': '主功能選單',
        })

    return record.rich_menu_id


def set_main_rich_menu_2_user(user):
    """
    判斷使用者的rich_menu是否有設定或是跑掉
    :param user: record
    :return: bool
    """
    if not user:
        return False

    main_menu_id = set_main_rich_menu()

    if main_menu_id is not user.line_rich_menu_id:
        line_bot_api.link_rich_menu_to_user(
            user.line_user_id,
            main_menu_id
        )

        user.update({
            'line_rich_menu_id': main_menu_id
        })
    return True


def delete_rich_menu(rich_menu_id):
    """刪除所有的 rich menu"""
    line_bot_api.delete_rich_menu(rich_menu_id)
    return True


def get_rich_menu_list():
    """更新 rich menu 清單"""
    _logger.info('Update rich menu list')
    for menu in line_bot_api.get_rich_menu_list():
        result = request.env['line.rich.menu'].sudo().search([('rich_menu_id', '=', menu.rich_menu_id)])
        print(menu)
        if not result:
            result.create({
                'rich_menu_id': menu.rich_menu_id,
                'setting': menu
            })
        else:
            result.update({
                'setting': menu
            })


def verify_pid(pid):
    """
    驗證身分證號
    :param str pid: 身分證
    :return bool:
    """
    id_map = {
        'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14',
        'F': '15', 'G': '16', 'H': '17', 'J': '18', 'K': '19',
        'L': '20', 'M': '21', 'N': '22', 'P': '23', 'Q': '24',
        'R': '25', 'S': '26', 'T': '27', 'U': '28', 'V': '29',
        'X': '30', 'Y': '31', 'W': '32', 'Z': '33', 'I': '34',
        'O': '35'
    }

    weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    new_uid = id_map[pid[0].upper()] + pid[1:]
    return sum([weight[i] * int(v) for i, v in enumerate(new_uid)]) % 10 == 0


def notify_paid(user):
    msg = '請輸入銀行帳號後五碼與金額\n 範例:"12345 300"'
    user.line_request_status = 'notify'
    return msg


def notify_paid_create_record(user, user_text):
    if re.match(r'^\d{5}\s(.+)\d{1,5}$', user_text):
        input_list = re.split(r'\s(.+)', user_text)
        input_list.pop()
        request.env['era.household_member.history'].sudo().create({
            'household_member_id': user.id,
            'bank_last_5_digit': input_list[0].strip(),
            'amount': int(input_list[1]),
            'notify_datetime': dt.now(),
        })
        user.line_request_status = ''
        return '已上傳ERA公司系統繳費訊息,等待財務人員後台核銷費用'
    else:
        return '錯誤的輸入，請再輸入一次!'


def display_name(user_id):
    user = line_bot_api.get_profile(user_id)
    return user.display_name


def check_balance(user):

    now_totbalance = fields.Integer(string="結算總應繳餘額")
    amount = [
        user.period_start if user.period_start else ' ',
        user.period_end if user.period_end else ' ',
        user.now_ym if user.now_ym else ' ',
        user.period_subtot if user.period_subtot else 0,
        user.period_totrent if user.period_totrent else 0,
        user.period_totrentpay if user.period_totrentpay else 0,
        user.now_totrent_balance if user.now_totrent_balance else 0,
        user.period_totescale if user.period_totescale else 0,
        user.period_totscalepay if user.period_totscalepay else 0,
        user.now_totscalebalance if user.now_totscalebalance else 0,
        user.now_totbalance if user.now_totbalance else 0,

        # user.previous_arrears if user.previous_arrears else 0,
        # user.period_addition if user.period_addition else 0,
        # user.period_electric if user.period_electric else 0,
        # user.period_house_rent if user.period_house_rent else 0,
        # user.period_house_manage if user.period_house_manage else 0,
        # user.period_park_rent if user.period_park_rent else 0,
        # user.period_park_manage if user.period_park_manage else 0,
        # user.period_moto_park_manage if user.period_moto_park_manage else 0,
        # user.period_total if user.period_total else 0,
        # user.period_complete_total if user.period_complete_total else 0,
        # user.period_water_fee if user.period_water_fee else 0,
    ]

    # msg = f'上期欠款: {amount[0]:,}\n' \
    #       f'本期增加: {amount[1]:,}\n' \
    #       f'本期電費: {amount[2]:,}\n' \
    #       f'本期房屋租金: {amount[3]:,}\n' \
    #       f'本期房屋管理費: {amount[4]:,}\n' \
    #       f'本期車位租金: {amount[5]:,}\n' \
    #       f'本期車位管理費: {amount[6]:,}\n' \
    #       f'本期機車位管理費: {amount[7]:,}\n' \
    #       f'本期水費: {amount[10]:,}\n' \
    #       f'本期應繳總金額: {amount[8]:,}\n' \
    #       f'本期已核銷金額: {amount[9]:,}\n' \
    #       f'如有任何疑問，請洽詢管理員。'
    msg = f'起租日: {amount[0]:,}\n' \
          f'退租日: {amount[1]:,}\n' \
          f'目前應結帳年月: {amount[2]:,}\n' \
          f'每月固定租金/管理費: {amount[3]:,}\n' \
          f'合計應繳房租/管理費總金額: {amount[4]:,}\n' \
          f'合計已繳房租/管理費總金額: {amount[5]:,}\n' \
          f'結算房租/管理費應繳餘額: {amount[6]:,}\n' \
          f'合計應繳總電費: {amount[7]:,}\n' \
          f'合計已繳總電費: {amount[8]:,}\n' \
          f'結算電費應繳餘額: {amount[9]:,}\n' \
          f'結算總應繳餘額: {amount[10]:,}\n' \
          f'如有任何疑問，請洽詢管理員。'
    return msg
