from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from .models import EventInfo, Event
# admin.site.register(EventInfo)

class EventInfoAdmin(admin.ModelAdmin):
    def get_queryset(self,request):
        queryset = super(EventInfoAdmin ,self).get_queryset(request)
        queryset = queryset.order_by('date')
        return queryset
    list_display = ['title', 'date', 'By','Event_type']
    search_fields = ('title', 'Grand_Event', 'date','priority', )
admin.site.register(EventInfo , EventInfoAdmin)