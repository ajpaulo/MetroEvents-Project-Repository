from django.db import models

# Create your models here.
class User(models.Model):
  user_id = models.AutoField(primary_key=True) 
  username = models.CharField(max_length=50) 
  password = models.CharField(max_length=50) 
  first_name = models.CharField(max_length=50) 
  last_name = models.CharField(max_length=50)  

  class Meta:
    db_table = 'user'

class Request(models.Model):
  request_id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE) 
  event = models.ForeignKey('organizer.Event', on_delete=models.CASCADE, blank=True, null=True)  
  description = models.CharField(max_length=255)  
  request_type = models.CharField(max_length=50)
  status = models.CharField(max_length=50)

  class Meta:
    db_table = 'request'

class Review(models.Model):
  review_id = models.AutoField(primary_key=True)
  event = models.ForeignKey('organizer.Event', on_delete=models.CASCADE)
  par = models.ForeignKey('organizer.Participant', on_delete=models.CASCADE)
  rating = models.IntegerField()  
  description = models.CharField(max_length=255) 

  class Meta:
    db_table = 'review'