from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect 
from .models import *
from user.models import *
from organizer.models import *
from django.contrib.auth.models import User

# Create your views here.
class AdministratorDashboardView(View):
  def get(self, request):
    return render(request, 'admin.html')

class AdministratorUsersView(View):
  def get(self, request):
    qs_users = User.objects.all()
    qs_organizers = Organizer.objects.all()
    qs_administrators = Administrator.objects.all()
    context = {
      'users' : qs_users,
      'organizers' : qs_organizers,
      'administrators': qs_administrators
    }
    return render(request, 'user.html', context)

class AdministratorEventsView(View):
  def get(self, request):
    return render(request, 'event.html')
    
class AdministratorManageView(View):
  def get(self, request):
    return render(request, 'manage.html')
  
