from django.contrib import admin
from .models import  Contact, Users

# Register your models here.


# admin.site.register(Users)
@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'division', 'image']
    
@admin.register(Users)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password', 'image']
    
