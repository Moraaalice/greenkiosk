from django.db import models
class Customer(models.Model):
    name = models.CharField(max_length=32)
    phone_number = models.IntegerField()
    email_address = models.EmailField()
    address = models.CharField(max_length=32)
    
    def __str__(self):
        return self.name 
