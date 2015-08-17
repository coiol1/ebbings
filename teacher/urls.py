from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 't_index'),
    url(r'^decks/$', views.decks, name = 't_decks'),
    url(r'^decks/review/$', views.decks_review, name = 't_decks_review'),
    url(r'^decks/review/(\d+)/$', views.decks_review_one, name = 't_decks_review_one'),
    url(r'^classes/$', views.classes, name = 't_classes'),
    url(r'^classes/(\d+)/$', views.classes_one, name = 't_classes_one'),
    url(r'^classes/new/$', views.classes_new, name = 't_classes_new'),
    url(r'^classes/new/create/$', views.classes_new_create, name = 't_classes_new_create'),
]