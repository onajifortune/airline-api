from django.urls import path

from . import views

# from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name="register"),
    path('login', views.LoginAPIView.as_view(), name="login"),
    path('me', views.AuthUserAPIView.as_view(), name="user"),
]
