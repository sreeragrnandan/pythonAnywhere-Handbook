from django.shortcuts import render

# Create your views here.
def syllabus(request):
    return render(request, 'syllabus/index.html')
