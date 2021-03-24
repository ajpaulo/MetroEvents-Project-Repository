from django.urls import path
from . import views

app_name = 'organizer'
urlpatterns = [
	path('dashboard', views.OrganizerDashboardView.as_view(), name="organizer_dashboard_view"),
] 