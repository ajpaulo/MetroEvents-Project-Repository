from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect 
from .models import *
from user.models import *
from administrator.models import *
from datetime import datetime
from .forms import EventForm
from django.db.models import F

# Create your views here.
class OrganizerDashboardView(View):
	def get(self, request):
		if request.user.is_authenticated:
			events_organized = Organizer.objects.filter(user_id=request.user.id).values_list('event_id', flat=True)
			qs_events = Event.objects.filter(is_cancelled=False, event_id__in=events_organized)
			qs_participants = Participant.objects.all()
			qs_reviews = Review.objects.all()
			qs_notifications = Notification.objects.filter(user_id=request.user.id)
			qs_requests = Request.objects.filter(status='pending',request_type='join_event', event_id__in=events_organized)
			context = {
				'events' : qs_events,
				'participants' : qs_participants,
				'reviews' : qs_reviews,
				'notifications' : qs_notifications,
				'requests' : qs_requests,
			}
			return render(request, 'organizerDashboard.html', context)
		else:
			return redirect('user:user_login_view')
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
				new_organizer = Organizer(event_id = form.event_id, user_id=request.user.id)
				new_organizer.save()
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
				event_to_be_cancelled = Event.objects.filter(event_id = id_num)
				cancel_event = event_to_be_cancelled.update(is_cancelled = True)
				description = "We regret to inform you that the organizer of " + event_to_be_cancelled[0].title + " has decided to cancel the said event."
				participants = Participant.objects.filter(event_id=event_to_be_cancelled[0]).values_list('user_id', flat=True)
				for participant in participants:
					new_notification = Notification(description=description, user_id=participant)
					new_notification.save()
			elif 'btn_accept' in request.POST:
				id_num = request.POST.get("request_id_num")
				current_request = Request.objects.filter(request_id = id_num)
				accept_request = current_request.update(status = 'accepted')
				new_participant = Participant(event_id=current_request[0].event_id, user_id=current_request[0].user_id)
				new_participant.save()
				current_event = Event.objects.filter(event_id = current_request[0].event_id)
				if current_event[0].num_of_participants is None:
					update_num_of_par = Event.objects.filter(event_id = current_request[0].event_id).update(num_of_participants = 1)
				else:
					update_num_of_par = Event.objects.filter(event_id = current_request[0].event_id).update(num_of_participants=F('num_of_participants') + 1)
				description = "Your request to join " + current_event[0].title + " has been accepted by the organizer!"
				new_notification = Notification(description=description, user_id=current_request[0].user_id)
				new_notification.save()
			elif 'btn_decline' in request.POST:
				id_num = request.POST.get("request_id_num")
				current_request = Request.objects.filter(request_id = id_num)
				current_event = Event.objects.filter(event_id = current_request[0].event_id)
				decline_request = Request.objects.filter(request_id = id_num).update(status = 'declined')
				description = "Unfortunately, your request to join " + current_event[0].title + " has been declined by the organizer."
				new_notification = Notification(description=description, user_id=current_request[0].user_id)
				new_notification.save()
		return redirect('organizer:organizer_dashboard_view')