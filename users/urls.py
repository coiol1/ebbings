from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^register_teacher/$', views.register_teacher, name = 'register_teacher'),
    url(r'^register_teacher/check/$', views.register_teacher_check, name = 'register_teacher_check'),
    url(r'^register_student/$', views.register_student, name = 'register_student'),
    url(r'^register_student/check/$', views.register_student_check, name = 'register_student_check'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^login/try/$', views.login_try, name = 'login_try'),
    url(r'^login/success/$', views.login_success, name = 'login_success'),
    url(r'^logout/$', views.logout, name = 'logout'),
    url(r'^logout/try/$', views.logout_try, name = 'logout_try'),
    url(r'^logout/success/$', views.logout_success, name = 'logout_success'),
]