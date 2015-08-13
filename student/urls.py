from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^classes/$', views.classes, name = 'classes'),
    url(r'^study/(\d+)/$', views.study_one, name = 'study_one'),
]