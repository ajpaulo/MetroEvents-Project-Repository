from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import Http404
from django.http import HttpResponse 
# from .forms import Customer_Form
from organizer.models import *
from django.contrib.auth.models import auth, User
from datetime import date
import time
from django.db.models import Q
from administrator.models import *
from organizer.models import *
from django.contrib.auth import login, logout

# Create your views here.
# user = User.objects.create_user('hotdog667', 'hotdog666@gmail.com', 'passwordnihotdog')

# Class to display all events to the user dashboard
class UserDashboard(View):
    def get(self, request):

        now = date.today()
        current_date = now.strftime("%Y-%m-%d")

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S")

        qs_compare_lt = Event.objects.filter(date__lt = current_date, time__lt = current_time, is_cancelled = False)
        qs_compare_gt = Event.objects.filter(date__gt = current_date, time__gt = current_time, is_cancelled = False)
        qs_cancelled_events = Event.objects.filter(is_cancelled=True)

        # eventID = Event.objects.exclude(date__gt = current_date, time__gt = current_time, is_cancelled = False).values("event_id")

        # # qs_organizer = Organizer.objects.filter(event = eventID).values('user')

        # qs_org = User.objects.filter(id = eventID).values('first_name')

        # org = User.objects.filter(id=qs)
        # print(eventID)    

        print(qs_compare_lt)
        print(qs_compare_gt)

        # print(org)
        
        

        context = {
            'filterdate_lt': qs_compare_lt,
            'filterdate_gt': qs_compare_gt,
            'cancelledevents' : qs_cancelled_events,
            # 'organizer' : org,
        }

        return render(request, 'userdashboard.html', context)

    # def post(self, request):

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
      # elif is_admin:
      #   return redirect('')
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
        

