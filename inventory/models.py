from django.db import models

# Create your models here.
from django.db import models
from users.models import User

class Dealer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    company = models.CharField(max_length=100, blank=True)

class Produce(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class Procurement(models.Model):
    produce = models.ForeignKey(Produce, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    tonnage = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    branch = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Stock(models.Model):
    produce = models.ForeignKey(Produce, on_delete=models.CASCADE)
    available_tonnage = models.DecimalField(max_digits=10, decimal_places=2)
