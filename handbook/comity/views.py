from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from comity.models import comity , Member
# from contacts.models import contact
def index(request):
    com_id = comity.objects.order_by('id')
    con = Member.objects.order_by('id')
    date_dict = {'comity': com_id ,'member': con}
    return render(request, 'comity/index.html', context=date_dict)