'''
# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # print(request)
    # print(request.GET.get("q"))
    # print(request.COOKIES)
    # print(request.user)
    # print(request.path)
    # print(request.method)
    # if request.method == "GET":
    #     print(f"You are using {request.method} method!")
    # print(request.META)
    return HttpResponse("<h2>Hello World!</h2>")
    
'''


from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request, "app/home.html", context)