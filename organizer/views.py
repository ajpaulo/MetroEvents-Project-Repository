from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect 
from .models import *
from datetime import datetime
from .forms import EventForm

# Create your views here.
class OrganizerDashboardView(View):
	def get(self, request):
		return render(request, 'organizerDashboard.html')
	def post(self, request):
		if request.method == 'POST':
			if 'btn_create_event' in request.POST:	
				form = EventForm(request.POST or None)
				title = request.POST.get("title_create")
				type = request.POST.get("type_create")
				details = request.POST.get("details_create")
				date = request.POST.get("date_create")
				time = request.POST.get("time_create")
				form = Event(title = title,
													type = type,
													details = details,
													date = date,
													time = time)
				form.save()
		return redirect('organizer:organizer_dashboard_view')