from django.db import models

# Create your models here.
class Notifications(models.Model):
    message = models.CharField(max_length=32)
    time = models.TimeField()
    date = models.DateField()
    customer = models.CharField(max_length=30)
    identifcation_num = models.CharField(max_length=32)
    
    def __str__(self):
        return self.message
    
