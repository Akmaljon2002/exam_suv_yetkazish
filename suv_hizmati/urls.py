from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenRefreshView, TokenObtainPairView,)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from asosiy.views import *

schema_view = get_schema_view(
   openapi.Info(
      title="Suv Yetkazish",
      default_version='v1',
      description="Test description",
      # terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact("AkmaljonFayzullayev, <akmaljonfayzullayev07@gmail.com>"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('suvlar', SuvViewSet)
router.register('mijozlar', MijozViewSet)
router.register('adminlar', AdminViewSet)
router.register('haydovchiar', HaydovchiViewSet)
router.register('buyurtmalar', BuyurtmaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token_ber/', TokenObtainPairView.as_view()),
    path('token_yangila/', TokenRefreshView.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('', include(router.urls)),
]
