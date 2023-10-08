
from django.urls import path, include
from . import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('',views.ImgView,'share')

urlpatterns = [
    path('',include(router.urls))
]

# urlpatterns += router.urls