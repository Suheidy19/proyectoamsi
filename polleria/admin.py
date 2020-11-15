from django.contrib import admin
from .models import Clients, Provider, Products,Sales, Invoices


# Register your models here.
admin.site.register(Provider)
admin.site.register(Clients)
admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(Invoices)
