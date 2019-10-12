from django.contrib import admin

# Register your models here.
from .models import comity , Member
admin.site.register(comity)
# admin.site.register(Member)

class MemberAdmin(admin.ModelAdmin):
    def get_queryset(self,request):
        queryset = super(MemberAdmin ,self).get_queryset(request)
        queryset = queryset.order_by('comity_id')
        return queryset
    search_fields = ('comity__comity_name', 'Member_name', 'department','designation','jecc_code', )
admin.site.register(Member , MemberAdmin)