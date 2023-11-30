from django.contrib import admin

from .models import ScheduleRegister

class ScheduleRegisterAdmin(admin.ModelAdmin):
    
    
    list_display = ('id', 'event')
    
    list_display_links = ('id', 'event')
    
admin.site.register(ScheduleRegister, ScheduleRegisterAdmin)