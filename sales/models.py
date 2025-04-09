from django.db import models

# Create your models here.
from django.db import models
from users.models import User
from inventory.models import Produce

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    national_id = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)

class Sale(models.Model):
    produce = models.ForeignKey(Produce, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    tonnage = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    sales_agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

class CreditSale(models.Model):
    produce = models.ForeignKey(Produce, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
