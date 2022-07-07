from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path("index",views.index,name="index"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("tutor",views.tutor,name="tutor"),
    path("studentview",views.studentview,name="studentview"),
    path("student_details",views.student_details,name="student_details"),
    path("send_mail",views.send_mail,name='send_mail'),
    path("signout",views.signout,name='signout'),
    path('tutorview',views.tutorview,name='tutorview'),
]