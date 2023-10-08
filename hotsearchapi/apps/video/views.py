from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,UpdateModelMixin
from .paginations import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter

from article import models
from . import serializer

class VideoView(GenericViewSet,ListModelMixin):
    queryset = models.Article.objects.filter(is_delete=False,is_show=True,category_id=1).all()
    serializer_class = serializer.VideoSerializer
    # pagination_class = PageNumberPagination
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    # ordering_fields = ['id', 'up_num','created_time']
    # filter_fields = ['course_category', ]


