from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from .paginations import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter

from article import models
from . import serializer

class ImgView(GenericViewSet,ListModelMixin):
    queryset = models.Article.objects.filter(is_delete=False,is_show=True,category_id=2).all()
    serializer_class = serializer.ImgSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # filter_backends = [DjangoFilterBackend,]
    ordering_fields = ['order']
    # filter_fields = ['course_category', ]


