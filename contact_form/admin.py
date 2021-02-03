from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]
    list_filter = ['phone', 'email', ]
    search_fields = ['name', 'email', 'phone', ]

