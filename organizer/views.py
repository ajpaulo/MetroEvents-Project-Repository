from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect 
from .models import *
from datetime import datetime

# Create your views here.
class OrganizerDashboardView(View):
	def get(self, request):
		# qs_conferences = Conference.objects.filter(is_deleted = False, is_created = True, date__gte=datetime.now()).order_by('-date')
		# context = {
		# 	'conferences' : qs_conferences
		# }
		return render(request, 'organizerDashboard.html')
