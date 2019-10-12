from django.shortcuts import render
def index(request):
    mydict  = {
        'insert_me':"Hello I am from views.py!"
    }
    return render(request, 'index/index.html', context=mydict)
