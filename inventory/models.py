from django.db import models
class Products(models.Model):
    name = models.CharField(max_length=32)
    descrption = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

