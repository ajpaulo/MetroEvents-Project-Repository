from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('dashboard', views.UserDashboard.as_view(), name='user_dashboard'),
    path('login', views.UserLoginView.as_view(), name='user_login_view'),
    path('signup', views.UserSignupView.as_view(), name='user_signup_view'),
]

