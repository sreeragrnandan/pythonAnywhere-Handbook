from django.contrib import admin
from .models import Time_table,department
# Register your models here.
class TimeTableAdmin(admin.ModelAdmin):
    def get_queryset(self,request):
        queryset = super(TimeTableAdmin ,self).get_queryset(request)
        queryset = queryset.order_by('-id')
        return queryset
    list_display = ['Department_name', 'semester']
    search_fields = ('Department_name', 'semester' )
admin.site.register(Time_table , TimeTableAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    def get_queryset(self,request):
        queryset = super(DepartmentAdmin ,self).get_queryset(request)
        queryset = queryset.order_by('department_name')
        return queryset
    list_display = ['department_name']
    search_fields = ('department_name', 'id' )
admin.site.register(department , DepartmentAdmin)