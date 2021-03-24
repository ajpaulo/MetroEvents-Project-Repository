from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect 
from .models import *
from user.models import *
from administrator.models import *
from datetime import datetime
from .forms import EventForm

# Create your views here.
class OrganizerDashboardView(View):
	def get(self, request):
		qs_events = Event.objects.filter(is_cancelled=False)
		qs_participants = Participant.objects.all()
		qs_reviews = Review.objects.all()
		qs_notifications = Notification.objects.all()
		qs_requests = Request.objects.filter(status='pending',request_type='join_event')
		context = {
			'events' : qs_events,
			'participants' : qs_participants,
			'reviews' : qs_reviews,
			'notifications' : qs_notifications,
			'requests' : qs_requests,
		}
		return render(request, 'organizerDashboard.html', context)
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
			elif 'btn_edit_details' in request.POST:
				id_num = request.POST.get("event_id_num")
				title = request.POST.get("title_edit")
				type = request.POST.get("type_edit")
				details = request.POST.get("details_edit")
				date = request.POST.get("date_edit")
				time = request.POST.get("time_edit")
				edit_event = Event.objects.filter(event_id = id_num).update(title = title,
																															type = type,
																															details = details,
																															date = date,
																															time = time)
			elif 'btn_yes' in request.POST:
				id_num = request.POST.get("event_id_num")
				delete_event = Event.objects.filter(event_id = id_num).update(is_cancelled = True)
		return redirect('organizer:organizer_dashboard_view')