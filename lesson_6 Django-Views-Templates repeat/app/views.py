'''

# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # print(request)
    """ <WSGIRequest: GET '/'> """
    # print(request.GET)   
    """ (<QueryDict: {}>) """
    # print(request.GET)   
    """ (<QueryDict: {'q': ['abc']}>) """
    # print(request.GET)
    """ <QueryDict: {'q': ['5']}> """
    # print(request.GET.get('q'))
    """ 5 """
    # print(request.COOKIES)
    """ {'csrftoken': 'eTfgjAYmjFf3vExsM50ZQkljEiY1PDXMiTSbTzxo9OFxMsJk0SZogpP26TxxcHuO', 'sessionid': 'zy9ai4tsn8zuh8wtpkiogtwx330h052x'} """
    # print(request.path)
    """ / """
    # print(request.user)
    """ error """
    # print(request.method)
    """ GET """
    # if request.method == 'GET':
        # print('You are using GET method!')
    """ You are using GET method! """
    # if request.method == 'GET':
        # print(f'You are using {request.method} method!')
    """ You are using GET method! """
    print(request.META)
    """ metadata olarak birçok şey var. """
    return HttpResponse("<h2>Hello World!</h2>")
    
'''

from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request, 'app/home.html', context)
