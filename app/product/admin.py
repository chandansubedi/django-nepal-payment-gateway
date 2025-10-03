from django.contrib import admin

# Register your models here.
from .models import Product, Transaction
# Register both models separately. The second argument to register() must be
# a ModelAdmin class, so register models individually or pass a tuple.
admin.site.register(Product)
admin.site.register(Transaction)
