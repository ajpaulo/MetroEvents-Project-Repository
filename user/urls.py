from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('dashboard', views.UserDashboard.as_view(), name='user_dashboard'),
]

