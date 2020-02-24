from django.conf.urls import url
from django.contrib import admin

from .views import employee_create, employee_detail, employee_list, employee_update
# from .import views
app_name = 'firm'

urlpatterns = [
	url(r'^$', employee_list, name='list'),
    url(r'^create/$', employee_create),
    url(r'^(?P<slug>[\w-]+)/$', employee_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', employee_update, name='update'),
]
