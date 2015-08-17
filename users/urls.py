from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'u_index'),
    url(r'^register_teacher/$', views.register_teacher, name = 'u_register_teacher'),
    url(r'^register_teacher/check/$', views.register_teacher_check, name = 'u_register_teacher_check'),
    url(r'^register_teacher/success/$', views.register_teacher_success, name = 'u_register_teacher_success'),
    url(r'^register_student/$', views.register_student, name = 'u_register_student'),
    url(r'^register_student/check/$', views.register_student_check, name = 'u_register_student_check'),
    url(r'^register_student/success/$', views.register_student_success, name = 'u_register_student_success'),
    url(r'^login/$', views.login, name = 'u_login'),
    url(r'^login/try/$', views.login_try, name = 'u_login_try'),
    url(r'^login/success/$', views.login_success, name = 'u_login_success'),
    url(r'^logout/$', views.logout, name = 'u_logout'),
    url(r'^logout/try/$', views.logout_try, name = 'u_logout_try'),
    url(r'^logout/success/$', views.logout_success, name = 'u_logout_success'),
]