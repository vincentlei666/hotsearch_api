# -*- coding:utf-8 -*-
from django.urls import path,include
from . import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('', views.NewHotView, 'free')
urlpatterns = [
    path('', include(router.urls)),
]
