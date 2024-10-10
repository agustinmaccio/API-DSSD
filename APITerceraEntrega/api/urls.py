from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
]
