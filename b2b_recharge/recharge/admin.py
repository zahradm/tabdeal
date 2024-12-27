from django.contrib import admin
from .models import PhoneNumber


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'seller')
    search_fields = ('number',)
    list_filter = ('seller',)
