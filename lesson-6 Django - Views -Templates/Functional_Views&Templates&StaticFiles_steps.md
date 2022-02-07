# Django Class Notes
Functional Views & Templates, Static Files

### Nice to have VSCode Extentions:
- Djaneiro - Django Snippets

### Needs
- Python, add the path environment variable
- pip
- virtualenv

## Summary
- Intro to Views&Templates with additional note
- Create project and app
- Views
  - Request object
  - Interview Question
  - Create a template view
- Templates
  - Variables
  - Tags
  - Filters
  - Comments
  - Advenced examples
  - Interview Question
- Static Files


## Create project and app:
## project and app oluşturma:

- Create a working directory, name it as you wish, cd to new directory
- Create virtual environment as a best practice:
```py
python3 -m venv env # for Windows or
python -m venv env # for Windows
virtualenv env # for Mac/Linux or;
virtualenv yourenv -p python3 # for Mac/Linux
```
- Activate scripts:
```bash
.\env\Scripts\activate  # for Windows
source env/bin/activate  # for MAC/Linux
```
- See the (env) sign before your command prompt.
- Install django:
```bash
pip install django
```
(python -m pip install --upgrade pip  (for pip upgrate))

- See installed packages:
```sh
pip freeze

# you will see:
asgiref==3.3.4
Django==3.2.4
pytz==2021.1
sqlparse==0.4.1

# If you see lots of things here, that means there is a problem with your virtual env activation. 
# Activate scripts again
```
- Create requirements.txt same level with working directory, send your installed packages to this file, requirements file must be up to date:
```py
pip freeze > requirements.txt

pip install -r .\requirements.txt
```

- Create project:
```py
django-admin startproject project
django-admin startproject project . 
# With . it creates a single project folder.
# Avoiding nested folders
# Alternative naming:
django-admin startproject main . 
```
- Various files has been created!
- Check your project if it's installed correctly:
```py
python3 manage.py runserver  # or,
python manage.py runserver  # or,
py -m manage.py runserver  # or,
py manage.py runserver
```
- (Optional) If you have nested project folders with the same name; change the name of the project main (parent) directory as src to distinguish from subfolder with the same name!
  Aynı isimde iç içe proje klasörleriniz varsa; Aynı isimli alt klasörden ayırt etmek için proje ana (ana) dizininin adını src olarak değiştirin! 
```bash
# optional
mv .\project\ src
```
- Lets create first application:
  ilk application ınımızı oluşturalım.
- Go to the same level with manage.py file:
  manage.py ile aynı seviyeye gelmeliz.
```bash
cd .\src\
```
- Start app
```py
python manage.py startapp app

# Alternative naming:
python manage.py startapp home
```

VSCode' da
Ctrl + Shift + P ile İnterpreter seçimi yapabiliyoruz.(env interpreterini seçmaliyiz.)



# Views

- Go to views.py in app directory
  app dizininde views.py'ye gidin
- Check your interpreter on VSCode, and choose the one with virtual env
  VSCode'da interpreterı kontrol edin ve sanal env ile olanı seçin
- Create first view by adding:
  ilk view ünüzü oluşturarak ekleyin 
```py
from django.http import HttpResponse

def home_view(request):
    html = "<html><body>Hello World!</body></html>"
    return HttpResponse(html)
```
- Must include URL path of new app to the project url list.
  Proje URL listesine yeni app in URL yolu eklenmelidir, içermelidir.

- Go to urls.py and add:
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls")),
]
```

- Create urls.py under app, and add:
  app in altında urls.py oluşturun ve ekleyin
```py
from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view, name="home"),
]
```
- Go to settings.py and add under INSTALLED_APPS:
  settings.py'ye gidin ve INSTALLED_APPS altına oluşturduğumuz app i ekleyin:
```py
'app.apps.FirstappConfig'  # or
'app'
```
- Run our project:
  runserver yaptığımızda terminalde çıkan kırmızı uyarıyı settings de yaptığımız değişiklikten dolayı veriyor. eğer migrate komutunu çalıştırırsak bunu engelleriz.
```py
python manage.py runserver
```
- Go to http://localhost:8000/home/ in your browser, and you should see the text “Hello, world.”, which you defined in the index view.

### Some experimentation about request object:
### request object hakkında bazı deneyler:


- Go to the views.py, try adding these lines and interact with the web page:
  views.py'ye gidin, bu satırları eklemeyi deneyin ve web sayfasıyla etkileşime geçin
```py
def home_view(request):
    # print(request)
    # <WSGIRequest: GET '/'>
    # gives info about the request object

    # print(request.GET)
    # <QueryDict: {}> an empty dict
    # but after some querry on browser like /?q=abc
    # <QueryDict: {'a': ['3']}>
    # returns values brought by GET method

    # print(request.GET.get("q"))
    # returns the value of q

    # print(request.COOKIES)
    # COOKIES: HTTP cookies are small blocks of data created by a web server while a user is browsing a website and placed on the user's computer or other device by the user’s web browser. 
    # 
    # When you visit a website that uses cookies, a cookie file is saved to your PC, Mac, phone or tablet. It stores the website's name, and also a unique ID that represents you as a user. That way, if you go back to that website again, the website knows you've already been there before.
    #
    # {'csrftoken': '8RR6TAZe8rBtyQl1H1tbb3umLijiQBAT5QhtTsDOPseM4letTnixfnYryrPcb1ZS'}
    #
    # A CSRF token is a unique, secret, unpredictable value that is generated by the server-side application and transmitted to the client in such a way that it is included in a subsequent HTTP request made by the client.
    # Session id if you login the page

    # print(request.user)
    # AnonymousUser

    # print(request.path)
    # /

    # print(request.method)
    # GET

    # print(request.META)

    # if request.method == "GET":
    #     print("This is a GET method")

    # if request.method == "GET":
    #     print(f"This is a {request.method} method")

    # print(request.META) 


    return HttpResponse("Hello, Jane")
```

Django uses request and response objects to pass state through the system.

Django, durumu sistemden geçirmek için istek ve yanıt nesnelerini kullanır.

When a page is requested, Django creates an HttpRequest object that contains metadata about the request. Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function. Each view is responsible for returning an HttpResponse object.

Bir sayfa istendiğinde (request), Django, istekle ilgili meta verileri içeren bir HttpRequest nesnesi oluşturur. Sonra Django uygun görünümü yükler ve HttpRequest'i görünüm işlevine (view function) ilk argüman olarak iletir. Her görünüm (view), bir HttpResponse nesnesinin döndürülmesinden sorumludur.


### Interview Question:

**What are views in Django?**

A view function, or “view” for short, is simply a Python function that takes a web request and returns a web response. This response can be HTML contents of a web page, or a redirect, or a 404 error, or an XML document, or an image, etc. 

Bir view function veya kısaca “view”, yalnızca bir web isteği (request) alan ve bir web yanıtı (response) döndüren bir Python işlevidir. Bu yanıt (response), bir web sayfasının HTML içeriği veya bir yönlendirme, bir 404 hatası veya bir XML belgesi veya bir resim vb. olabilir.

Example:
```py
from django.http import HttpResponse
def sample_function(request):
 return HttpResponse(“Welcome to Django”)
``` 
There are two types of views:
İki tür görünüm vardır:
- Function-Based Views: We import our view as a function.
  Function Tabanlı Views: Views ümüzü bir Function olarak import ediyoruz.
- Class-based Views: It’s an object-oriented approach.
- Class Tabanlı Views: Nesneye yönelik bir yaklaşımdır.

## Create a template view
## Bir template view oluşturma

- Create app/templates/app directory and create a home.html file under it:
  app/templates/app dizini oluşturun ve altında bir home.html dosyası oluşturun:
```html
<h1>Hello World!</h1>

<p>This is our first paragraph...</p>
```

- Change your views to comply with the template:
  template e uymak için views değiştirin
```py
# from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):    
    return render(request, "app/home.html")
```
- Add a context:
```py
def home_view(request):
    
    context = {
        'first_name': 'Rafe',
        'last_name': 'Stefano',
    }    
    
    return render(request, "app/home.html", context)
```
- Keep going wiht the examples below.

# Templates

### Variables: {{ variable }}
https://docs.djangoproject.com/en/3.2/topics/templates/#variables

```html
My first name is {{ first_name }}. My last name is {{ last_name }}.
```
- With a context of {'first_name': 'John', 'last_name': 'Doe'}, this template renders to:
My first name is John. My last name is Doe.

- Add a context:
  Bir context ekleyelim
```py
def home_view(request):
    context = {
        'first_name': 'Rafe',
        'last_name': 'Stefano',
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request, "app/home.html", context)
```

### Tags: {% tag %}
- Some tags require beginning and ending tags:
  Bazı etiketler için başlangıç ve bitiş etiketleri gerekir:
```html
{% if %}
{% endif %}


{% if my_list %}
    print("List is not empty")
{% endif %}


{% for num in my_list %}
    <li>{{ num }}</li>
{% endfor %}
```
### Filters
```
- Filters transform the values of variables and tag arguments: {{ variable|filter }}

```html
{{ dict1.django|title }}
```

### Comments: 
  - Single line: {# this won't be rendered #}

{# This is a single line comment #}

  - Multi line: {% comment %}

{% comment %}
    This is a multi line comment,
    you can't see it on the page!
{% endcomment %}

Examples: 

```html
<h3>Hello, this is home page</h3>
{{ title }} <br>
{{ dict1 }} <br>
{{ dict1.django }} <br>
{% for i in my_list %}
{{ i }} <br>
{% endfor %}
{{ my_list }}
<h2>{{ request.method }}</h2>
<h2>{{ request.COOKIES }}</h2>
<h2>{{ first_name }}</h2>
<p>My first name is {{ first_name }}.</p>
```

- A different div example:
  Farklı bir örnek; 
```html
<a href="{% url 'pet_detail' pet.id %}">
```

### Advenced examples:
```html
{% extends "base.html" %}

{% load static %}

{% block blockname %}
{% endblock blockname %}

<script src="{% static 'main.js' %}"></script>
```

```html
{% extends "base.html" %}
{% block content %}
<div>
    {% for pet in pets %}

        <div>
            <a href="{% url 'pet_detail' pet.id %}">
            <h3>{{ pet.name | capfirst }}</h3>
            </a>
            <p>{{ pet.species }}</p>
            {% if pet.breed %}
            <p>Breed: {{ pet.breed }}</p>
            {% endif %}
            <p class="hidden">{{ pet.description }}</p>
        </div>

    {% endfor %}
</div>
{% endblock %}
```


### Interview Question

**What are templates in Django or Django template language?**
**Django veya Django şablon dilindeki şablonlar nelerdir?**

Templates are an integral part of the Django MVT architecture. They generally comprise HTML, CSS, and js in which dynamic variables and information are embedded with the help of views. Some constructs are recognized and interpreted by the template engine. The main ones are variables and tags.

(Templates, Django MVT mimarisinin ayrılmaz bir parçasıdır. Genellikle dinamik değişkenlerin ve bilgilerin views ler yardımıyla gömülü olduğu HTML, CSS ve js'yi içerirler. Bazı yapılar, templates engine tarafından tanınır ve yorumlanır. Başlıcaları variables, değişkenler ve tags, etiketlerdir.)

A template is rendered with a context. Rendering just replaces variables with their values, present in the context, and processes tags. Everything else remains as it is.

(Bir template, bir bağlamla işlenir. Oluşturma, değişkenleri yalnızca bağlam içinde bulunan değerleriyle değiştirir ve etiketleri işler. Diğer her şey olduğu gibi kalır.)

The syntax of the Django template language includes the following four constructs :
(Django template language sözdizimi aşağıdaki dört yapıyı içerir:)
- Variables
- Tags
- Filters
- Comments

# Static Files (images, JavaScript, CSS)

[Static Files reference](https://docs.djangoproject.com/en/3.2/howto/static-files/#managing-static-files-e-g-images-javascript-css)

Static files ları kullanmak için django diyor ki;
1. INSTALLED_APPS de bu 'django.contrib.staticfiles' var mı?
2. INSTALLED_APPS de STATIC_URL = 'static/' var mı?
3. Bir template te static file göstermek istiyorsak bunun önünde mutlaka {% load static %} tag ini kullanmamız gerekiyor. img src içine aşağıdakini yazmalıyız.
``` 
{% load static %}
<img src="{% static 'my_app/example.jpg' %}" alt="My image">
```
4. Statik dosyalarınızı app inizde static adlı bir klasörde saklayın. For example my_app/static/my_app/example.jpg.
5. Unutmayın static files larda değişiklik yapıldığında server yeniden başlatılmalı.
6. Ayrıca proje kasörünün bulunduğu yere de bir static klasörü oluşturulup buradada genel, evrensel static files ların depolandığı yer olabilir. Bunun için INSTALLED_APPS e aşağıdaki kodu eklemelisiniz.
```
STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/var/www/static/',
]
```

Websites generally need to serve additional files such as images, JavaScript, or CSS. In Django, we refer to these files as “static files”. Clients download static files as they are from the server.

(Web sitelerinin genellikle resimler, JavaScript veya CSS gibi ek dosyalar sunması gerekir. Django'da bu dosyalara "statik dosyalar" diyoruz. İstemciler, statik dosyaları sunucudan oldukları gibi indirirler.)


Django provides ```django.contrib.staticfiles``` to help you manage them, this collects static files from each of your applications (and any other places you specify) into a single location that can easily be served in production.

(Django, onları yönetmenize yardımcı olmak için "django.contrib.staticfiles" sağlar; bu, uygulamalarınızın her birinden (ve belirttiğiniz diğer yerlerden) statik dosyaları üretimde kolayca sunulabilecek tek bir konumda toplar.)


Using the ```collectstatic``` command, Django looks for all static files in your apps and collects them wherever you told it to, i.e. the ```STATIC_ROOT``` .

(Django, "collectstatic" komutunu kullanarak, uygulamalarınızdaki tüm statik dosyaları arar ve siz istediğiniz yerde, yani "STATIC_ROOT" olarak toplar.)


- Create a folder named ```static```. 
  ("static" isimli bir klasör oluştur.)
- Need to tell Django that this is the folder to look when a static folder is used.
  (Statik bir klasör kullanıldığında bakılacak klasörün bu olduğunu Django'ya söylemeniz gerekiyor.)
- Open settings.py, under STATIC_URL variable add;
  (STATIC_URL değişkeni eklentisi altında settings.py'yi açın;)

```py
STATICFILES_LIST = [ BASE_DIR / 'static', ]
```

- Create a folder under static named ```css```, this will be the place for our css files.

- Create a ```style.css``` file and add some css to test.

- Check the differences from home page.

- A basic example for a template using static files is:
```html
{% load static %}

<head>
    <link rel="stylesheet" href="{% static 'app/style.css' %}">
</head>

<h1>Hello World!</h1>
<img src="{% static 'app/example.jpg' %}" width="300" alt="Example">

<video width="400" controls>
    <source src="{% static 'app\kittens.mp4' %}" type="video/mp4">
    Your browser does not support HTML video.
  </video>

```


$ pip freeze
$ pip freeze > requirements.txt