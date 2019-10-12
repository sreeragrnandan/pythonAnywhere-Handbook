from django.shortcuts import render

# Create your views here.
def administration(request):
    return render(request, 'administration/index.html')
