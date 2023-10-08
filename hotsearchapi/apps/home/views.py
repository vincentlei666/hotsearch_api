# Create your views here.

from utils import models

from rest_framework.viewsets import ViewSetMixin, ViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from utils.response import APIResponse
from rest_framework.decorators import action
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .paginations import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter



from article import models
from . import serializer


class ShareView(ViewSet):
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    @action(methods=['post',],detail=False)
    def short(self,request,*args,**kwargs):
        ser = serializer.ShareShortSerializer(data=request.data,context={'request':request})
        if not ser.is_valid():
            return APIResponse(code=0,msg=ser.errors)
        ser.save()
        inner_link = ser.context.get('inner_link')
        return APIResponse(code=1,msg='分享成功',data={'inner_link':inner_link})

    @action(methods=['post',],detail=False)
    def img(self,request,*args,**kwargs):
        print(request.FILES)
        print(request.data)
        ser = serializer.ShareImgSerializer(data=request.data,context={'request':request})
        if not ser.is_valid():
            return APIResponse(code=0,msg=ser.errors)
        ser.save()
        return APIResponse(code=1,msg='分享成功')

    @action(methods=['post',],detail=False)
    def link(self,request,*args,**kwargs):
        ser = serializer.ShareLinkSerializer(data=request.data,context={'request':request})
        if not ser.is_valid():
            return APIResponse(code=0,msg=ser.errors)
        ser.save()
        return APIResponse(code=1,msg='分享成功')

class LinkView(GenericViewSet,ListModelMixin):
    queryset = models.Article.objects.filter(is_delete=False,is_show=True).order_by('-id')
    serializer_class = serializer.LinkSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_backends = [DjangoFilterBackend,]
    ordering_fields = ['up_num','pu_date']
    filter_fields = ['inner_link', 'user','area','topic','category']














