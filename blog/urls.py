from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.about_me, name='about_me'),
    url(r'^about_group$', views.about_group, name='about_group'),
    url(r'^about_univer$', views.about_univer, name='about_univer'),
]
