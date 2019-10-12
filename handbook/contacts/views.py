# Create your views here.
from django.shortcuts import render
from contacts.models import contact,department
def contacts(request):
    depts = department.objects.order_by('department_name')
    con = contact.objects.order_by('departments_id')
    date_dict = {'contact': con ,'departments':depts}
    return render(request, 'contacts/contacts.html', context=date_dict)

def newTemp(request):
    depts = department.objects.order_by('department_name')
    con = contact.objects.order_by('departments_id')
    date_dict = {'contact': con ,'departments':depts}
    return render(request, 'contacts/contacts.html', context=date_dict)