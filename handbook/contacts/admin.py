from django.contrib import admin

# Register your models here.
from .models import contact,department
# admin.site.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ['Name', 'departments', 'jecc_code']
    def get_queryset(self,request):
        queryset = super(contactAdmin ,self).get_queryset(request)
        queryset = queryset.order_by('departments')
        return queryset
    search_fields = ('departments', 'Designation', 'Name','Qualification','jecc_code','Phone_Number' )
admin.site.register(contact, contactAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    department_name = [' ', 'department_name']
    def get_queryset(self,request):
        queryset = super(DepartmentAdmin ,self).get_queryset(request)
        queryset = queryset.order_by('department_name')
        return queryset
    search_fields = ('department_name','id')
admin.site.register(department, DepartmentAdmin)