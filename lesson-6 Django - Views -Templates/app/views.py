# from django.http import HttpResponse

# Create your views here.

# def home(request): 
#     return HttpResponse("<h1>Hello World!</h1>")



from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'first_name': 'Rafe',
        'last_name': 'Stefano',
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request, "app/home.html", context)
