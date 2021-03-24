from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
  event_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=150) 
  type = models.CharField(max_length=150) 
  details = models.CharField( max_length=255)
  date = models.DateField()  
  time = models.TimeField() 
  num_of_participants = models.IntegerField(blank=True, null=True) 
  is_cancelled = models.BooleanField(default=False)  
  num_of_upvotes = models.IntegerField(blank=True, null=True) 

  class Meta:
    db_table = 'event'

class Organizer(models.Model):
  org_id = models.AutoField(primary_key=True) 
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  event = models.ForeignKey(Event, on_delete=models.CASCADE) 

  class Meta:
    db_table = 'organizer'

class Participant(models.Model):
  par_id = models.AutoField(primary_key=True) 
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  event = models.ForeignKey(Event, on_delete=models.CASCADE) 

  class Meta:
    db_table = 'participant'