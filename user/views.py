from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import Http404
from django.http import HttpResponse 
# from .forms import Customer_Form
from organizer.models import *
from django.contrib.auth.models import User
from datetime import date
import time
from django.db.models import Q

# Create your views here.
# user = User.objects.create_user('hotdog667', 'hotdog666@gmail.com', 'passwordnihotdog')

# Class to display all events to the user dashboard
class UserDashboard(View):
    def get(self, request):

        now = date.today()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)

        qs_events = Event.objects.all()
        qs_compare = Event.objects.filter(Q(date_gt = now) | Q(time_gt = current_time))
        print(qs_events)
        print(qs_compare)

        context = {
            'events': qs_events,
            'filterdate': qs_compare
        }

        return render(request, 'userdashboard.html', context)

    # def post(self, request):