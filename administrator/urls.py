from django.urls import path
from . import views

app_name = 'administrator'
urlpatterns = [
	path('dashboard', views.AdministratorDashboardView.as_view(), name="administrator_dashboard_view"),
  path('users', views.AdministratorUsersView.as_view(), name="administrator_users_view"),
  path('events', views.AdministratorEventsView.as_view(), name="administrator_events_view"),
  path('manage', views.AdministratorEventsView.as_view(), name="administrator_manage_view"),
] 