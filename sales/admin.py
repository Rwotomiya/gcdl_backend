from django.contrib import admin
from .models import Buyer, Sale, CreditSale
# Register your models here.
admin.site.register(Buyer)
admin.site.register(Sale)
admin.site.register(CreditSale)