from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
]
