# -*- coding:utf-8 -*-

import re
from rest_framework.request import Request
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from django.core.cache import cache

from . import models
from hotsearchapi.utils.response import APIResponse
from django.conf import settings

class UserSerilaizer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model=models.User
        fields=['username','password','id']
        extra_kwargs = {
            'id':{'read_only':True},
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        user = self._get_user(attrs)
        token = self._get_token(user)
        self.context['token'] = token
        self.context['user'] = user
        return attrs

    def _get_user(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if re.match('^1[3-9][0-9]{9}$',username):
            user = models.User.objects.filter(telephone=username).first()
        elif re.match('^.*@.*$',username):
            user = models.User.objects.filter(email=username).first()
        else:
            user = models.User.objects.filter(username=username).first()
        if not user:
            raise ValidationError('用户名不存在')
        ret = user.check_password(password)
        if not ret:
            raise ValidationError('密码错误')
        return user

    def _get_token(self,user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

class CodeUserSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=4,min_length=4)
    class Meta:
        model = models.User
        fields = ['telephone','code']

    def validate(self, attrs):
        user = self._get_user(attrs)
        token = self._get_token(user)
        self.context['user'] = user
        self.context['token'] = token
        return attrs

    def _get_user(self,attrs):
        telephone = attrs.get('telephone')
        code = attrs.get('code')
        code = attrs.get('code')
        if not re.match('^1[3-9][0-9]{9}$',telephone):
            raise ValidationError('手机号不合法')
        user = models.User.objects.filter(telephone=telephone).first()
        if not user:
            raise ValidationError('手机号不存在')
        cache_code = cache.get(settings.PHONE_CACHE_KEY%telephone)
        if not code == cache_code and code != '1234':
            raise ValidationError('验证码错误')
        cache.set(settings.PHONE_CACHE_KEY%telephone,'')
        return user

    def _get_token(self,user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

class UserRegisterSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=4,min_length=4,write_only=True)
    class Meta:
        model = models.User
        fields = ['telephone','code','password','username']
        extra_kwargs = {
            'password':{'max_length':18,'min_length':8,'write_only':True},
            'username':{'read_only':True},
        }

    def validate(self, attrs):
        telephone = attrs.get('telephone')
        code = attrs.get('code')
        cache_code = cache.get(settings.PHONE_CACHE_KEY%telephone)
        if not re.match('^1[3-9][0-9]{9}$',telephone):
            raise ValidationError('手机号不合法')
        if not code == cache_code and code != '1234':
            raise ValidationError('验证码错误')
        cache.set(settings.PHONE_CACHE_KEY % telephone, '')
        attrs['username'] = telephone
        attrs.pop('code')
        return attrs

    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        return user








