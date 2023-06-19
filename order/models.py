from django.db import models

# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=32)
    order_total = models.CharField(max_length=32)
    date = models.DateField()
    location = models.CharField(max_length=32)
    delivery_options = models.CharField(max_length=32)
    delivery_date = models.DateField()
    
    def __str__(self):
        return self.order_number