from django.db import models

# Create your models here.
class Event(models.Model):
  event_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=150) 
  type = models.CharField(max_length=150) 
  details = models.CharField( max_length=255)
  date = models.DateField()  
  time = models.TimeField() 
  num_of_participants = models.IntegerField() 
  is_cancelled = models.BooleanField(default=False)  
  num_of_upvotes = models.IntegerField() 

  class Meta:
    db_table = 'event'

class Organizer(models.Model):
  org_id = models.AutoField(primary_key=True) 
  user = models.ForeignKey('user.User', on_delete=models.CASCADE)
  event = models.ForeignKey(Event, on_delete=models.CASCADE) 

  class Meta:
    db_table = 'organizer'

class Participant(models.Model):
  par_id = models.AutoField(primary_key=True) 
  user = models.ForeignKey('user.User', on_delete=models.CASCADE)
  event = models.ForeignKey(Event, on_delete=models.CASCADE) 

  class Meta:
    db_table = 'participant'