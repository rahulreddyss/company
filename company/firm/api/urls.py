from django.conf.urls import url
from django.contrib import admin

app_name = 'firm'

from .views import EmployeeCreateAPIView,EmployeeListAPIView,EmployeeDetailAPIView,EmployeeUpdateAPIView

urlpatterns = [
    url(r'^$', EmployeeListAPIView.as_view(), name='list'),
    url(r'^create-employee/$', EmployeeCreateAPIView.as_view(), name='create-employee'),
    url(r'^(?P<slug>[\w-]+)/$', EmployeeDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', EmployeeUpdateAPIView.as_view(), name='update'),
]
