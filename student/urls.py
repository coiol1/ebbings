from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 's_index'),
    url(r'^classes/$', views.classes, name = 's_classes'),
    url(r'^classes/(\d+)/join/$', views.classes_join, name = 's_classes_join'), #classes/(group_pk)/join
    url(r'^classes/(\d+)/join/success/$', views.classes_join_success, name = 's_classes_join_success'),
    url(r'^study/(\d+)/(\d+)/$', views.study_intro, name = 's_study_intro'), #(group_pk)/(deck_pk)
    url(r'^study/(\d+)/(\d+)/start/$', views.study_start, name = 's_study_start'),
]