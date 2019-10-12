from django.shortcuts import render

# Create your views here.
from TimeTable.models import Time_table, department
# from contacts.models import department

def TimeTable(request):
    departments = department.objects.order_by('department_name')
    time_table = Time_table.objects.order_by('Department_name_id')    
    date_dict = {'departments': departments ,'timeTables': time_table}
    return render(request, 'TimeTable/index.html', context=date_dict)