from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from article.models import Article, ArticleImg
from .models import NewHotArticle
from . import serializer
from .paginations import PageNumberPagination

class NewHotView(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    queryset = NewHotArticle.objects.filter(is_delete=False,is_show=True).order_by('-id')
    serializer_class = serializer.NewHotSerializer
    pagination_class = PageNumberPagination

