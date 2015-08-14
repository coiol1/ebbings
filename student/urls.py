from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^classes/$', views.classes, name = 'classes'),
    url(r'^study/(\d+)/$', views.study_intro, name = 'study_intro'),
    url(r'^study/(\d+)/start/$', views.study_start, name = 'study_start'),
]