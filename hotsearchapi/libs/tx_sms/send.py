# -*- coding:utf-8 -*-

import random

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

from . import settings
from hotsearchapi.utils.logging import logger

def  get_code():
    s_code = ''
    for i in range(4):
        s_code += str(random.randint(1,9))
    return s_code

def send_message(phone,code):
    ssender = SmsSingleSender(settings.appid, settings.appkey)
    params = [code, 3]  # 当模板没有参数时，`params = []`
    try:
        result = ssender.send_with_param(86,phone,settings.template_id, params, sign=settings.sms_sign, extend="", ext="")
        if result.get('result') == 0:
            return True
        else:
            return False
    except Exception as e:
        logger.error('手机号：%s，短信发送失败，错误为：%s'%(phone,str(e)))




















