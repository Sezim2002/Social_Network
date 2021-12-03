from django.urls import path
from .views import (RegistrationView, ActivationView, LogoutView, LoginView)


urlpatterns = [
    path('regist/', RegistrationView.as_view()),
    path('activate/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]