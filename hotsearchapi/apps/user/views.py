from django.shortcuts import render

# Create your views here.

import re

from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.core.cache import cache

from . import serializer
from hotsearchapi.utils.response import APIResponse
from . import models
from hotsearchapi.libs.tx_sms import get_code, send_message
from django.conf import settings
from .throttlings import SMSThrottling


class LoginView(ViewSet):
    @action(methods=['post'], detail=False)
    def login(self, request, *args, **kwargs):
        ser = serializer.UserSerilaizer(data=request.data)
        if not ser.is_valid():
            return APIResponse(code=0, msg=ser.errors)
        token = ser.context.get('token')
        username = ser.context.get('user').username
        return APIResponse(token=token, username=username)

    @action(methods=['get'], detail=False)
    def check_telephone(self, request, *args, **kwargs):
        # telephone = request.GET.get('telephone')
        telephone = request.query_params.get('telephone')
        if not re.match('^1[3-9][0-9]{9}$', telephone):
            return APIResponse(code=0, msg='手机号不合法')
        try:
            models.User.objects.get(telephone=telephone)
            return APIResponse(code=1)
        except Exception as e:
            return APIResponse(code=0, msg='手机号不存在')

    @action(methods=['post'],detail=False)
    def code_login(self,request,*args,**kwargs):
        telephone = request.data.get('telephone')
        user = models.User.objects.filter(telephone=telephone).first()
        ser = serializer.CodeUserSerializer(instance=user,data = request.data,partial=True)
        if not ser.is_valid():
            return  APIResponse(code=0,msg=ser.errors)
        username = ser.context.get('user').username
        token = ser.context.get('token')
        return APIResponse(username=username,token=token)

class SendSMSView(ViewSet):
    throttle_classes = [SMSThrottling, ]

    @action(methods=['get'], detail=False)
    def send(self, request, *args, **kwargs):
        telephone = request.GET.get('telephone')
        if not re.match('^1[3-9][0-9]{9}$', telephone):
            return APIResponse(code=0, msg='手机号不合法')
        code = get_code()
        result = send_message(telephone, code)
        # sms_cache_%s
        cache.set(settings.PHONE_CACHE_KEY % telephone, code, 180)
        if not result:
            return APIResponse(code=0, msg='验证码发送失败')
        return APIResponse(code=1, msg='验证码发送成功')

class RegisterView(ViewSet):
    @action(methods=['post'],detail=False)
    def register(self,request,*args,**kwargs):
        ser = serializer.UserRegisterSerializer(data=request.data)
        if not ser.is_valid():
            return APIResponse(code=0,msg=ser.errors)
        ser.save()
        return APIResponse(code=1,msg='注册成功',username=ser.data.get('username'))
















