from django.urls import path
from . import views
urlpatterns=[
    path("signup/",views.LmsSignupUser.as_view()),
    path("getAllUser/",views.LmsGetUserDetail.as_view()),
    path("updateEmail/",views.LmsUpdateEmail.as_view()),
    path("deleteUser/<number>/",views.LmsDeleteuser.as_view())
]