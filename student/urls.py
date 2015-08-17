from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 's_index'),
    url(r'^classes/$', views.classes, name = 's_classes'),
    url(r'^study/(\d+)/$', views.study_intro, name = 's_study_intro'),
    url(r'^study/(\d+)/start/$', views.study_start, name = 's_study_start'),
]