from django import forms
from .models import *
from organizer.models import *

class RequestForm(forms.ModelForm):
	
	class Meta:
		model = Request
		fields = ('user', 'event', 'description', 'request_type', 'status')