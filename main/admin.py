from django.contrib import admin
from .models import Item  # Import the Item model from your models file

# Create an admin class for the Item model
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'description')  # Display these fields in the admin list view

# Register the Item model with the admin site
admin.site.register(Item, ItemAdmin)

