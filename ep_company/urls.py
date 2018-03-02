from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^company/$', views.list_company, name='list_company'),
    url(r'^division/$', views.list_division, name='list_division'),
    url(r'^division/(?P<pk>\d+)/$', views.division_detail, name='division_detail'),
]