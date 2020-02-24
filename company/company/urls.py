# from django.urls import include, url
from django.conf.urls import include, url
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from accounts.views import login_view, register_view, logout_view, index
# from .views import *
from firm.views import *


router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


urlpatterns = [
	url('admin/', admin.site.urls),
    # url('', include(router.urls)),
    # url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', index, name='index'),
    url(r'^$^register/', register_view, name='register_view'),
    url(r'^$^login/', login_view, name='login_view'),
    url(r'^$^logout/', logout_view, name='logout_view'),
    url(r'^api/users/', include("accounts.api.urls", namespace='users-api')),
    url('^firm/', include('firm.urls', namespace='firm')),
    url(r'^api/firm/', include("firm.api.urls", namespace='firm-api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)