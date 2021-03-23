from django.db import models

# Create your models here.
class Administrator(models.Model):
  admin_id = models.AutoField(primary_key=True) 
  user = models.ForeignKey('user.User', on_delete=models.CASCADE)

  class Meta:
    db_table = 'administrator'

class Notification(models.Model):
  notif_id = models.AutoField(primary_key=True) 
  user = models.ForeignKey('user.User', on_delete=models.CASCADE) 
  description = models.CharField(max_length=255)  

  class Meta:
    db_table = 'notification'