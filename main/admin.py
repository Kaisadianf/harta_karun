from django.contrib import admin
from .models import Item  # Import the Item model from your models.py file

# Register your models here.
admin.site.register(Item)  # Register the Item model with the admin panel
