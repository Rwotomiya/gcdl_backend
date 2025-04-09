from django.contrib import admin
from .models import Procurement, Stock, Produce
# Register your models here.
admin.site.register(Produce)
admin.site.register(Procurement)
admin.site.register(Stock)