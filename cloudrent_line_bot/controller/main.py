# -*- coding: utf-8 -*-

import logging
import re
import base64
from datetime import datetime as dt
from odoo import models,fields,api
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


#@handler.add(MessageEvent, message=TextMessage)
@handler.add(MessageEvent)
def handle_message(event):
    source, r, host, user_id = [
        event.source,
        request,
        request.httprequest.host_url,
        event.source.user_id
    ]

    user = verify_user_id(user_id)

    if event.message.type == 'text' :
       user_text = event.message.text.strip()
    else :
       user_text = ''
    # user_text = event.message.text.strip()
    # print(event.message.text)
    if user:
        # print(user.member_no)
        func = {
            '繳費通知': lambda: notify_paid(user),
            '查閱帳單': lambda: check_balance(user),
            '修繕通知': lambda: call_service(user),
            '照片上傳': lambda: upload_photo(user),
            '查閱案件': lambda: check_case(user),
        }
        status = user.line_request_status

        if user_text in func:
            if status:
                user.line_request_status = ''
            msg = func[user_text]()
        elif status == 'notify':
            if event.message.type == 'text' :
                request.env['cloudrent.paymentlog'].sudo().create({
                    'line_id': event.source.user_id,
                    'date': dt.now(),
                    'content_text': event.message.text,
                })
                user.line_request_status = ''
                msg = '已上傳公司電腦管理系統,等待相關人員做後續之處理'
            elif event.message.type == 'image':
                image_content = line_bot_api.get_message_content(event.message.id)
                image_f = get_module_resource('cloudrent_line_bot', './static/img/line_bot/', 'tmp_image.jpg')
                with open(image_f, 'wb') as fd:
                     for chunk in image_content.iter_content():
                         fd.write(chunk)
                with open(image_f, 'rb') as file:
                      img_buffer = file.read()
                if img_buffer :
                   img_buf = base64.b64encode(img_buffer)
                   request.env['cloudrent.paymentlog'].sudo().create({
                        'line_id': event.source.user_id,
                         'date': dt.now(),
                     'content_img': img_buf,})
                   user.line_request_status = ''
                   msg = '已上傳公司電腦管理系統,等待相關人員做後續之處理'
                else:
                   msg =  '錯誤，請傳送匯款作業之照片!'
        elif status == 'service':
            if event.message.type == 'text':
                user_text = event.message.text.strip()
                request.env['cloudrent.maintenancelog'].sudo().create({
                    'line_id': event.source.user_id,
                    'date': dt.now(),
                    'content_text': user_text,
                })
                user.line_request_status = ''
                msg = '已上傳公司電腦管理系統,等待相關人員做後續之處理'
            else:
                msg = '錯誤，請依照範例輸入文字描述!'
        else:
            userl = request.env['cloudrent.member_line_user'].search([('line_user_id','=',user_id)],limit=1)
            set_main_rich_menu_user(userl)
            func_name = "」、「".join(func.keys())
            msg = f'Hi, {display_name(user_id)},目前只有 「{func_name}」功能，請回覆功能名稱或是點擊主選單來操作'
    else:
        if verify_pid(user_text):
            userl = request.env['cloudrent.member_line_user'].sudo().search([('member_pid', '=', user_text),('active','=',True)],limit=1)
            user = request.env['cloudrent.household_member'].sudo().search([('id', '=', userl.member_id.id), ('active', '=', True)], limit=1)
            if any(userl):
                userl.sudo().line_user_id = user_id
                set_main_rich_menu_user(userl)
                msg = '驗證成功'
        else:
            msg = '請輸入身分證字號，以進行使用者綁定'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg)
    )

    """
    將使用者全部的訊息存入資料庫中
    Insert into line message to cloudrent_linelog table
    """

    if event.message.type == 'text' :
       user_text = event.message.text.strip()
       request.env['cloudrent.linelog'].sudo().create({
            'line_id': user_id,
            'date': dt.now(),
            'content_text': event.message.text.strip(),
       })
    elif event.message.type == 'image' :
       image_content = line_bot_api.get_message_content(event.message.id)
       image_f = get_module_resource('cloudrent_line_bot', './static/img/line_bot/', 'tmp_image.jpg')
 
       with open(image_f, 'wb') as fd:
            for chunk in image_content.iter_content():
                fd.write(chunk)
       with open(image_f, 'rb') as file:
            img_buffer = file.read()
       if img_buffer :
          img_buf = base64.b64encode(img_buffer)
          request.env['cloudrent.linelog'].sudo().create({
            'line_id': user_id,
            'date': dt.now(),
            'content_img': img_buf,
            })
    return 'OK'


def verify_user_id(user_id):
    """
    判斷使用者是否有綁定，有綁定則回傳 'res.user' object
    :param user_id:
    :return:
    """
    line_user = request.env['cloudrent.member_line_user'].sudo().search([('line_user_id', '=', user_id), ('active', '=', True)], limit=1)
    user = request.env['cloudrent.household_member'].sudo().search([('id', '=', line_user.member_id.id), ('active', '=', True)], limit=1)
    return user


def set_main_rich_menu(user):
    """
    取得主要 rich menu id
    :return: str rich_menu_id
    """
    _logger.info('Init Main Menu')
    record = request.env['line.rich.menu'].sudo().search([('name', '=', '主選單')], limit=1)

    if not record:
       if user.member_position == '3':
          area_notify = RichMenuArea(
              bounds=RichMenuBounds(x=15, y=15, width=820, height=820),
              action=MessageAction(label='message', text='繳費通知')
          )

          area_balence = RichMenuArea(
              bounds=RichMenuBounds(x=850, y=15, width=820, height=820),
              action=MessageAction(label='message', text='查閱帳單')
          )

          area_service = RichMenuArea(
              bounds=RichMenuBounds(x=1680, y=15, width=820, height=820),
              action=MessageAction(label='message', text='修繕通知')
          )

          rich_menu_id = line_bot_api.create_rich_menu(RichMenu(
              size=RichMenuSize(width=2500, height=843),
              selected=True,
              name="主功能",
              chat_bar_text="功能選單",
              areas=[area_notify, area_balence]
          ))

        # set image
          png_path = get_module_resource('line_bot', 'static/img/line_bot/', 'rich_menu_Main1.png')
          with open(png_path, 'rb') as f:
              line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)

#      elif user.member_position == '2'
#      elif user.member_position == '3':
#         area_notify = RichMenuArea(
#             bounds=RichMenuBounds(x=20, y=20, width=820, height=820),
#             action=MessageAction(label='message', text='繳費通知')
#         )

#         area_balence = RichMenuArea(
#             bounds=RichMenuBounds(x=841, y=20, width=820, height=820),
#             action=MessageAction(label='message', text='查閱帳單')
#         )

#         area_service = RichMenuArea(
#             bounds=RichMenuBounds(x=1674, y=20, width=820, height=820),
#             action=MessageAction(label='message', text='修繕通知')
#         )

#         rich_menu_id = line_bot_api.create_rich_menu(RichMenu(
#             size=RichMenuSize(width=2500, height=843),
#             selected=True,
#             name="主功能",
#             chat_bar_text="功能選單",
#             areas=[area_notify, area_balence]
#         ))

#       # set image
#         png_path = get_module_resource('line_bot', 'static/img/line_bot/', 'rich_menu_Main1.png')
#         with open(png_path, 'rb') as f:
#             line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)
       elif user.member_position == '4':
          area_upload = RichMenuArea(
              bounds=RichMenuBounds(x=288, y=64, width=784, height=669),
              action=MessageAction(label='message', text='照片上傳')
          )

          area_case = RichMenuArea(
              bounds=RichMenuBounds(x=1436, y=68, width=767, height=661),
              action=MessageAction(label='message', text='查閱案件')
          )

          rich_menu_id = line_bot_api.create_rich_menu(RichMenu(
              size=RichMenuSize(width=2500, height=843),
              selected=True,
              name="主功能",
              chat_bar_text="功能選單",
              areas=[area_upload, area_case]
          ))
          png_path = get_module_resource('line_bot', 'static/img/line_bot/', 'rich_menu_Main.png')
          with open(png_path, 'rb') as f:
              line_bot_api.set_rich_menu_image(rich_menu_id, 'image/png', f)

       record = record.create({
            'name': 'main',
            'rich_menu_id': rich_menu_id,
            'remark': '主功能選單',
        })

    return record.rich_menu_id


def set_main_rich_menu_user(user):
    """
    判斷使用者的rich_menu是否有設定或是跑掉
    :param user: record
    :return: bool
    """
    if not user:
        return False

    main_menu_id = set_main_rich_menu(user)

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
    msg = '請上傳轉帳水單憑證！'
    # msg = '請輸入銀行帳號後五碼與金額\n 範例:"12345 300"'
    user.line_request_status = 'notify'
    return msg

def call_service(user):
    msg = '請輸入維修項目、聯絡方式、方便聯絡時段\n 範例:"冷氣故障 0919123456 上班時段"'
    user.line_request_status = 'service'
    return msg

def upload_photo(user):
    msg = '請依序上傳處理前、處理中、處理後之照片"'
    user.line_request_status = 'upload'
    return msg


def call_service_create_record(user, event):
    if event.message.type == 'text':
       user_text = event.message.text.strip()
       request.env['cloudrent.maintenancelog'].sudo().create({
            'line_id': event.source.user_id,
            'date': dt.now(),
            'content_text': user_text,
       })
       user.line_request_status = ''
       return '已上傳公司電腦管理系統,等待相關人員做後續之處理'
    else:
       return '錯誤，請依照範例輸入文字描述!'


def notify_paid_create_record(self,user, event):
    if event.message.type == 'image' :
       img_buffer,img_buf = ''
       image_content = line_bot_api.get_message_content(event.message.id)
       # image_name = 'tmp_image.jpg'
       # image_f='/odoo/custom/addons/cloudrent_line_bot/static/img/line_bot/'+image_name
       image_f = get_module_resource('cloudrent_line_bot', 'static/img/line_bot/', 'tmp_image.jpg')
       with open(image_f, 'wb') as fd:
            for chunk in image_content.iter_content():
                fd.write(chunk)
       with open(image_f, 'rb') as file:
            img_buffer = file.read()
       if img_buffer :
          img_buf = base64.b64encode(img_buffer)
       request.env['cloudrent.paymentlog'].sudo().create({
            'line_id': event.source.user_id,
            'date': dt.now(),
            'content_img': img_buffer}),
       user.line_request_status = ''
       return '已上傳公司電腦管理系統,等待相關人員做後續之處理'
    else:
       return '錯誤，請傳送匯款作業之照片!'

def display_name(user_id):
    user = line_bot_api.get_profile(user_id)
    return user.display_name


def check_balance(user):

    amount = [
        user.period_start if user.period_start else ' ',
        user.period_end if user.period_end else ' ',
        user.now_ym if user.now_ym else ' ',
        user.period_subtot if user.period_subtot else 0,
        user.period_totrent if user.period_totrent else 0,
        user.period_totrentpay if user.period_totrentpay else 0,
        user.now_totrent_balance if user.now_totrent_balance else 0,
        user.period_totscale if user.period_totscale else 0,
        user.period_totscalepay if user.period_totscalepay else 0,
        user.now_totscalebalance if user.now_totscalebalance else 0,
        user.now_totbalance if user.now_totbalance else 0,


    ]


    msg = f'起租日: {amount[0]:}\n' \
          f'退租日: {amount[1]:}\n' \
          f'目前應結帳年月: {amount[2]:}\n' \
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
