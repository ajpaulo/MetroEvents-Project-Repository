from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import Http404
from django.http import HttpResponse 
# from .forms import Customer_Form
from organizer.models import *
from django.contrib.auth.models import auth, User
from datetime import date
import time
from .models import *
from organizer.models import *
from django.contrib.auth import login, logout
from administrator.models import *
from organizer.models import *
from .forms import RequestForm

# Create your views here.
# user = User.objects.create_user('hotdog667', 'hotdog666@gmail.com', 'passwordnihotdog')

# Class to display all events to the user dashboard
class UserDashboard(View):
  def get(self, request):
    # if request.user.is_authenticated:

    now = date.today()
    current_date = now.strftime("%Y-%m-%d")

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    qs_compare_lt = Event.objects.filter(date__lt = current_date, is_cancelled = False)
    qs_compare_gt = Event.objects.filter(date__gt = current_date, is_cancelled = False)
    qs_cancelled_events = Event.objects.filter(is_cancelled=True)
    
    qs_users = User.objects.all()

    # eventID = Event.objects.filter(date__lt = current_date, is_cancelled = False)
    # userID = Event.objects.filter(date__lt = current_date, is_cancelled = False)

    # qs_requests = Request.objects.filter(request_type='join_event', event_id__in=events_organized)

    print(qs_users)
    print(qs_compare_lt)
    print(qs_compare_gt)
    print(qs_cancelled_events)
    

    context = {
        'filterdate_lt': qs_compare_lt,
        'filterdate_gt': qs_compare_gt,
        'cancelledevents' : qs_cancelled_events,
    }

    return render(request, 'userdashboard.html', context)

  def post(self, request):
    if request.method == 'POST':
      if 'reqJoinBtn' in request.POST:
        userID = request.POPST.get(request.User.id)
        form = RequestForm(request.POST)
        description = request.POST.get("req_description")
        type = request.POST.get("req_type")
        status = request.POST.get("req_status")
        eventID = request.POST.get("req_event_id")
        form = Request(description = description, type = type, status = status, event = eventID)

        form.save()

    return redirect('user:user_dashboard')
        
class UserLoginView(View):
  def get(self, request):
    return render(request, 'index.html')

  def post(self, request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = auth.authenticate(username = username, password = password)
    if user is not None:
      auth.login(request, user)
      is_admin = Administrator.objects.filter(user_id=request.user.id)
      is_organizer = Organizer.objects.filter(user_id=request.user.id)
      if is_organizer:
        return redirect('organizer:organizer_dashboard_view')
      elif is_admin:
        return redirect('administrator:administrator_dashboard_view')
      else:
        return redirect('user:user_dashboard')
    else:
      return HttpResponse("Wrong credentials. Please try again.")

class UserSignupView(View):
  def get(self, request):
    return render(request, 'signup.html')

  def post(self, request):
    if request.method == 'POST':
      if 'btn_signup' in request.POST:
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")
        if str(password) == str(confirmpassword):
          user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
        else:
          return HttpResponse("Passwords don't match. Please try again.")
        return redirect('user:user_login_view')
  
class UserLogoutView(View):
  def get(self,request):
    logout(request)
    return  redirect("user:user_login_view")
    
  def post(self,request):
    logout(request)
    return  redirect("user:user_login_view")
      

