
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings

import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    re_path('media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),
    path('',include('home.urls')),
    path('user/',include('user.urls')),
    path('video/',include('video.urls')),
    path('img/',include('img.urls')),
    path('newhot/',include('newhotsearch.urls')),
    # path('knowledge/',include('knowledge.urls')),
]








