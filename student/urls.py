from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^classes/$', views.classes, name = 'classes'),
    url(r'^classes/(\d+)/join/$', views.classes_join, name = 'classes_join'), #classes/(group_pk)/join
    url(r'^classes/(\d+)/join/success/$', views.classes_join_success, name = 'classes_join_success'),
    url(r'^study/(\d+)/(\d+)/$', views.study_intro, name = 'study_intro'), #(group_pk)/(deck_pk)
    url(r'^study/(\d+)/(\d+)/start/$', views.study_start, name = 'study_start'),
]