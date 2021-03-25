from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect 
from .models import *
from user.models import *
from organizer.models import *

# Create your views here.
class AdministratorDashboardView(View):
  def get(self, request):
    return render(request, 'admin.html')

class AdministratorUsersView(View):
  def get(self, request):
    return render(request, 'user.html')

class AdministratorEventsView(View):
  def get(self, request):
    return render(request, 'event.html')
    
class AdministratorManageView(View):
  def get(self, request):
    return render(request, 'manage.html')
  
