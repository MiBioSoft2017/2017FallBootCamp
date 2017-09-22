from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.submit_login, name='login'),
    url(r'^logout/$', views.submit_logout, name='logout'),
]