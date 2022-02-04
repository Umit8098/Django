### Todo App

## PRECLASS SETUP

```bash
# CREATING VIRTUAL ENVIRONMENT
(Önce virtual environment oluşturuyoruz.)

# windows
$ py -m venv env
# windows other option
$ python -m venv env
# linux / Mac OS
vitualenv env

# ACTIVATING ENVIRONMENT
(environment i active ediyoruz.)

# windows
$ .\env\Scripts\activate
# linux / Mac OS
source env/bin/activate

# django PACKAGE INSTALLATION
(django paketini kuruyoruz.)

# if pip does not work try pip3 in linux/Mac OS
$ pip install django

(windows power shell i yönetici modda çalıştırıp, "python.exe -m pip install --upgrade pip" komutu yazınca artık upgrade hatası vermeyecek ta ki yeni version çıkana kadar. Ancak bir önceki projede yapmama rağmen yine de warning mesajı aldım.)

$ python -m pip install --upgrade pip  (for pip upgrate)  or
$ py -m pip install --upgrade pip      (for pip upgrate)

# alternatively python -m pip install django


# decouple PACKAGE INSTALLATION
(djangonun decouple paketini kuruyoruz. API Key i gizlemek için <SECRET_KEY>)

$ pip install python-decouple

# pillow PACKAGE INSTALLATION
(Burada dosya, upload işlemleri yapacağımız için terminale gidip pillow kütüphanesini kurmamız gerekiyor.(pillow: dosya yükleme işlemlerini yapabilmemizi sağlayan bir kütüphane.))

$ pip install pillow
$ pip freeze > requirements.txt

$ pip install -r .\requirements.txt


(şimdi bakalım django muz kurulmuş mu, versionumuz neymiş)
$ django-admin --version


# create project
(şimdi proje oluşturuyoruz. boşluk nokta ile oluşturursak iç içe dosya oluşturmaz.)

$ django-admin startproject main .
```


##### .gitignore ve .env için ->

- add a gitignore file at same level as env folder
- create a new file and name as .env at same level as env folder
- copy your SECRET_KEY from settings.py into this .env file . Don't forget to remove quotation marks from SECRET_KEY

(env folderla aynı seviyede <.env> diye bir dosya oluşturuyoruz, <settings.py> daki <SECRET_KEY> i gizlememiz lazım. şimdi <SECRET_KEY> i olduğu gibi kopyalıyoruz ve .env dosyasına yapıştırıp tırnakları siliyoruz. Daha sonra <settings.py> daki <SECRET_KEY> i silip yerine aşağıdaki code u yazıyoruz. Sonra yine aynı seviyede bir <.gitignore> dosyası daha oluşturup <toptal.com dan django gitignore diye oluşturabiliyoruz.> içinde <.env>  ve <env> dosyalarının isimlerinin ilgili kısımda yazılı olduğunu görüyoruz.)

.env-> (örnek: tırnakları sil, tırnaksız olacak!)
```
SECRET_KEY = django-insecure-)=b-%-w+0_^slb(exmy*mfiaj&wz6_fb4m&s=az-zs!#1^ui7j
```

- go to settings.py, make amendments below

(settings.py dosyasına git aşağıdaki code ları SECRET_KEY'in yerine yaz ve SECRET_KEY'i sil.)

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

- go to terminal

(terminale git; biz default olarak gelen <settings.py> da değişiklikler yaptığımız için migrate hatasının önüne geçmek için önce migrate yapıp sonra runserver yapıyoruz.)

```bash
$ py manage.py migrate
$ py manage.py runserver
```

click the link with CTRL key pressed in the terminal and see django rocket.
(link i tıkla ve roketi gör!)


THEN ->


- go to terminal, stop project, add app

(terminale gidip durduruyoruz ve bir app <fscohort> oluşturuyoruz.)

```bash
$ py manage.py startapp todo
```

- go to settings.py and add 'todo' app to installed apps and add below lines

(<settings.py> dosyasına gidip app kısmına ekliyoruz.)

```python
INSTALLED_APPS = [
    .....
    .....
    'django.contrib.staticfiles',
    # apps
    'todo',
]
```




todo app views.py ında home view ü ile home.htm template inde  ekranda bir yazı çıkartmak istiyoruz.

proje <urls.py> ına gidip, todo app inin olmayan <urls.py> ını "include" ediyoruz, path ini ekliyoruz ->

<main/views.py> ->

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]

```



todo app inde bir <urls.py> dosyası oluşturup ve içine app imizin <views.py> ında oluşturduğumuz home view ini import edip aşağıdaki kodları yazıyoruz.->

<todo/urls.py> ->

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```



(Artık templates lerimize geliyoruz...)

- create templates folder in our app as todo/templates/todo

(todo app klasörünün içine <templates> klasörünü, onun da içine app imizin ismi olan <todo> kalsörünü "/templates/todo" şeklinde oluşturup, bu <todo> klasörünün içine de template lerimizi <home.html , ###.html> oluşturuyoruz. Şimdi <home.htlm> oluşturduk.)

<home.htlm> templateimiz ->

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo App</title>
</head>
<body>
    <h1>Welcome Todo App</h1>
</body>
</html>
```




bizim birçok app imiz ve her bir app imizin de birçok template i olabilir. Her seferinde bir değişikliği diğer template lerde de yapmak zorunda kalmamak için bir tane <base.html> diye bir iskelet template, yapı oluşturup diğer template leri buna extends edeceğiz, bağlayacağız. Bu yüzden biz app lerimizin içinde template klasörleri ve onların da içinde app lerimizin isimleriyle aynı isimde olan kalsörler oluşturup o klasörlerin içine app imizle ilgili template leri koyacağız. Base templet imizi ise genel proje klasörümüzün seviyesinde oluşturacağımız template klasörünün içinde tutacağız.

 Genel proje klasörümüz ile aynı seviyede oluşturduğumuz <templates> klasörümüzün içine <base.html> diye bir dosya oluşturup tag lerini yerleştiriyoruz. (body nin içine -> {% block content %}{% endblock content %} tagları yazıyoruz.)

<base.html> templateimiz ->

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo App</title>
</head>
<body>
    
    {% block content %}
        
    {% endblock content %}
        
</body>
</html>
```






Artık <base.html> imizi oluşturduğumuza göre diğer template lerimizi bundan extends ederek kullanabiliriz. Burada dikkat edilmesi gereken şey biz base template imizi proje klasörü seviyesinde oluşturduğumuz bir templates klasöründe oluşturduğumuz için daha önce yaptığımız gibi {% 'fscohort/base.html' %} şeklinde değil de {% extends 'base.html' %} şeklinde extends ediyoruz. ve {% block content %} {% endblock content %} taglarının arasına göstermek istediklerimizi yazıyoruz. 

Bunun için <settings.py> dosyasında "TEMPLATES" kısmının 'DIRS' satırında şöyle bir değişiklik yapıyoruz: << 'DIRS': [BASE_DIR, 'templates'], >> Böylelikle <settings.py> dosyamızın ilgili kısmı şöyle oluyor: ->

```python

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```


Bundan sonra <home.html> templatimizi şu şekilde değiştiriyoruz ->

```html
{% extends 'base.html' %}

{% block content %}

<h1>Welcome Clarusway Todo App</h1>

{% endblock content %}

```




Modelimizi oluşturarak başlayacağız.
Tittle field
boolean field
date field

<models.py> dosyamızda modelimizi oluşturuyoruz. ->

```python
from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    """ default u false veriyoruz çünkü bir todo oluşturduğumda tamamlanmış olmasın üstüne tıkladığımızda completed olsun"""

    created_date = models.DateTimeField(auto_now_add=True)
    """ auto_now_add=True kullanıyoruz : bu class tan oluşturduğumuz bir objenin ilk oluşturulduğu tarihi kadydediyor. Diğeri de auto_now=True idi bu da : her update edildiğindeki tarihi alıyor. """

    
    class Meta:
        ordering = ('-created_date',)
        """ oluşturma tarihine göre sırala; <-> ile en son oluşturduğumuzu en üste koy, <-> olmazsa en son oluşturduğumuz en altta kalacak. Yani created_date e göre tersten sırala"""
        verbose_name_plural = "Todo"
        """ çoğul olan model ismini tekil yapıyor. """

    def __str__(self):
        return self.title

```


Model oluşturduğumuzda hemen makemigrations ve migrate komutlarıyla djangoya db içi hazırlığını yap ve modelimi oluştur diyoruz.

go to terminal ->
```bash
$ py manage.py makemigrations
$ py manage.py migrate
```


Admin panelimizi ayağa kaldırarak modelimizi ekliyoruz ve de birkaç obje ekliyoruz.

Önce <admin.py> dosyamıza giderek modelimizi import edip admin panelimize register ediyoruz. -> 

```python
from django.contrib import admin
from .models import Todo

# Register your models here.

admin.site.register(Todo)
```


Admin panelimizi ayağa kaldırmak için superuser oluşturuyoruz. -> 

go to terminal ->
```bash
$ py manage.py createsuperuser
$ py manage.py runserver
```


#### CRUD 

##### Read ->
admin panelde todo lar oluşturduk. İlk olarak bu oluşturduğumuz todo ları ekranda listeleyelim.

<views.py> a gidip todo_list view ü oluşturuyoruz. db deki tüm todoları ORM komutuyla çağırıyoruz ve todos diye bir değişkene tanımlıyoruz. Tabi Todo modelimizi de import etmemiz gerekiyor....

```python
from django.shortcuts import render
from .models import Todo

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def todo_list(request):
    todos = Todo.objects.all()
    """ db de Todo modelindeki tüm verileri todos a tanımla. Şimdi bu todos u template gönderip orada render edeceğiz. """
    context = {
        'todos': todos
    }
    return render(request, 'todo/todo_list.html', context)
```



<views.py> da todo_list view ümüzü oluşturduk, şimdi template imizi oluşturuyoruz. app imizin içindeki template klasörünün içinde yine app imizle aynı adı taşıyan kalsörümüzün içine <todo_list.html> template imizi <base.html> den extends ederek oluşturuyoruz. todo larımızı unordered bir listenin elemanları şeklinde for döngüsüyle iterate ederek gösteriyoruz. ->

```python
{% extends 'base.html' %}

{% block content %}

<div>
    <ul>
        <h2>Todo List</h2>

{% for todo in todos %}

<li>{{todo}}</li>

{% endfor %}

    </ul>
</div>

{% endblock content %}

```



<todo_list.html> template imizi oluşturduk ve onu <urls.py> da adreslememiz gerekiyor. ->

```python
from django.urls import path
from .views import home, todo_list

urlpatterns = [
    path('', home, name='home'),
    path('todo_list/', todo_list, name='list'),
]

```





##### Cread ->

Şimdi create işlemi yapacağız. Yani yeni bir todo oluşturup ekleyeceğiz.

<views.py> a gidip todo_add view ü oluşturacağız. Kullanıcı bir obje oluşturacak ekranda. Bu objeyi oluşturması için kullanıcıya bir form veriyoruz ve o formu doldurarak bir obje oluşturmasını sağlıyoruz. Önce todo_add için bir form oluşturmalıyız. ->

```python
from django.shortcuts import render
from .models import Todo

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo/todo_list.html', context)

def todo_add(request):
    pass
```



app imizin içerisine <forms.py> dosyası oluşturuyoruz. djangodan forms ları import ediyoruz, bir de modelForm kullanacağımız için models.py dan da Todo modelimizi import ediyoruz. ->

```python
from django import forms
from .models import Todo

class TodoAddForm(forms.ModelForm):
    class Meta:
        model = Todo
        """ hangi modeli kullanacağımızı belirtiyoruz. """
        fields = ['title']
        """ hangi fieldları kullanacağımızı belirtiyoruz. """

        # fields = ['title', 'completed']

        # field = '__all__'
        """ bununla da tüm field ları seçebilirdik. """
```



Artık formumuzu oluşturduk, şimdi <views.py> da formumuzu import ederek todo_add views ümüzü oluşturmak için kullanıcıya doldurması için sunuyoruz. <views.py> ->

```python
from django.shortcuts import render
from .models import Todo
from .forms import TodoAddForm

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo/todo_list.html', context)

def todo_add(request):
    form = TodoAddForm()
    context = {
        'form': form
    }
    return render(request, 'todo/todo_add.html', context)
```




Şİmdi todo_add template ini oluşturmaya sıra geldi. App imizin içindeki templates/todo klasörlerinin içine <todo_add.html> templatimizi base.html i extends ederek oluşturuyoruz. burada bir tane formumuz olacak.  ->

```python
{% extends 'base.html' %}

{% block content %}

<form action="" method="post">

    {% csrf_token %} {{form}}
    """ formlarda güvenlikle ilgili bir konu, kullanmazsak hata veriyor, mutlaka kullanılmalı """

    # {% csrf_token %} {{form.as_p}}
    """ böyle de yazabiliriz, yani formu p tagı kullan! """

    <input type="submit" value="Add">

</form>

{% endblock content %}

```




<todo_add.html> template imizi oluşturduk ve onu <urls.py> da adreslememiz gerekiyor. ->

```python
from django.urls import path
from .views import home, todo_list, todo_add

urlpatterns = [
    path('', home, name='home'),
    path('list/', todo_list, name='list'),
    path('add/', todo_add, name='add'),
]

```



<todo_add.html> template imiz çalışıyor, kullanıcıya bir form sunuyor ve kullanıcı doldurup add, post yapıyor ama bizim todo listesine eklenmiyor çünkü <views.py> da kullanıcının doldurup da post yaparak gönderdiği veriye bir işlem yapmadık. Şimdi <views.py> da form ile gelen request.post u yakalayıp db ye kaydedeceğiz. ->

```python
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoAddForm

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo/todo_list.html', context)

def todo_add(request):
    form = TodoAddForm()
    """ kullanıcıya boş bir formu context ile template içinde gönderdik.Daha sonra kullanıcı bunu doldurdu ve post methoduyla submit etti, gönderdi  """
    if request.method == 'POST':
        # print(request.POST)
        """ request.POST ile terminalde bize hangi bilginin geldiğini gördük. """
    """ gelen request.post u burada yakalıyoruz. """
        form = TodoAddForm(request.POST)
        """ formumuzun içine request.post u koy. """
        if form.is_valid():
        """ form valid ise """
            form.save()
            """ formu kaydet. """
            return redirect('list')
            """ sonra da bizi listeye gönder. Yukarıda da redirect i import ediyoruz. """
    context = {
        'form': form
    }
    return render(request, 'todo/todo_add.html', context)
```






##### Update ->

<views.py> a gidip todo_update view ü oluşturacağız. Burada işin içerisine id giriyor. Update edeceğimiz todo nun specific bir field ı ki o da id oluyor, onunla db den update edeceğimiz todo yu çekmemiz gerekiyor. Yani db den bir todo yu çekmek için onun id sini kullanacağız. todo_update fonksiyonunda Parametre olarak request in yanına id yi de ekliyoruz.

todo = Todo.objects.get(id=id)
""" db den Todo modelinden single bir objeyi uniq bir field ile çekiyoruz. Bana request içerisinde gelen id si db de hangi id ye eşitse o todo yu al ve şuna yani todo ya ata."""



Yeni bir form daha oluşturuyoruz. Önceki formu da kullanabiliriz fakat biz completed field ını da burada istiyoruz. o yüzden <forms.py> da TodoUpdateForm diye yeni bir form daha oluşturuyoruz ve <views.py> da <forms.py> dan import ediyoruz.

form = TodoUpdateForm(instance=todo)
""" instance ı bir obje olarak düşünebilirsiniz. Hangi objeyi instance ın içine koyacağız? db den çağırdığımız objeyi. Koydum formun içerisine kullanıcıya gönderdik."""


Kullanıcıya gönderdik, kullanıcı bunu güncelledi ve post methoduyla bize geri gönderdi. -> 

if request.method == "POST":
    form = TodoUpdateForm(request.POST, instance=todo)
""" eğer request post ise; benim iki tane field ım var title ve completed , sadece title ı güncelledi, completed a dokunmadı, o zaman request.post un içinde sadece güncellediği field gelecek mesela title gelecek, title ı burada alacak, geri kalan ne varsa, todo nun içinde ne varsa instance=todo dan koy. yani formumu bu şekilde oluştur. Daha sonra valid se save et diyeceğiz. özetle kullanıcının update ettiği fieldları request.post tan al, dokunmadığı fieldları da instance=todo dan al. Burada model form kullanmak çok kolaylık sağlıyor bize. tek bir yapıyla bunu sağlıyoruz. ama formu biz oluştursaydık, fieldları tek tek bu şekilde işlem yapmamız gerekirdi. """

<views.py> ->

```python
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoAddForm, TodoUpdateForm

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo/todo_list.html', context)

def todo_add(request):
    form = TodoAddForm()
    if request.method == 'POST':
        # print(request.POST)
        form = TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form
    }
    return render(request, 'todo/todo_add.html', context)


def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoUpdateForm(instance=todo)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form
    }
    return render(request, 'todo/todo_update.html', context)
```




Şİmdi todo_update template ini oluşturmaya sıra geldi. App imizin içindeki templates/todo klasörlerinin içine <todo_update.html> templatimizi base.html i extends ederek oluşturuyoruz. Biz <todo_update.html> imize yani template imize view den ne gönderdik context içinde? bir tane form gönderdik. Bu formu burada yakalamamız lazım. ->

csfr :  Cross Site Request Forgery protection Formlarla ilgili bir mevzu.
        (Siteler Arası İstek Sahteciliği koruması )


```python
{% extends 'base.html' %}

{% block content %}

<form action="" method="post">
    {% csrf_token %}
    {{form}}
    """ form göndermiştik, formu burdan alıyoruz. """
    <input type="submit" value="Update">
    """ kullanıcı bu formun içerisinde update ini yaptıktan sonra submit etmesi lazım. """

</form>

{% endblock content %}  

```





<todo_update.html> template imizi oluşturduk ve onu <urls.py> da adreslememiz gerekiyor. ->

```python
from django.urls import path
from .views import home, todo_list, todo_add, todo_update

urlpatterns = [
    path('', home, name='home'),
    path('list/', todo_list, name='list'),
    path('add/', todo_add, name='add'),
    path('<int:id>/update', todo_update, name='update'),
    # path('update/<int:id>', todo_update, name='update'),
    """ url de id si bu olan todo yu update edeceğiz o yüzden url de id belirtmemiz lazım. """

]
```




404 hatası için ->

<views.py> da 

<from django.shortcuts import get_object_or_404>  import ediyoruz.
Bu ne işe yarıyor? object varsa çek yoksa 404 hatası object bulunamadı hatası ver.

<views.py>  ->

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoAddForm, TodoUpdateForm

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo/todo_list.html', context)

def todo_add(request):
    form = TodoAddForm()
    if request.method == 'POST':
        form = TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form
    }
    return render(request, 'todo/todo_add.html', context)


def todo_update(request, id):
    # todo = Todo.objects.get(id=id)
    todo = get_object_or_404(Todo, id=id)
    form = TodoUpdateForm(instance=todo)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form
    }
    return render(request, 'todo/todo_update.html', context)
    
```









##### Delete ->

<views.py> a gidip todo_delete view ü oluşturacağız.

<views.py> ->

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoAddForm, TodoUpdateForm

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo/todo_list.html', context)

def todo_add(request):
    form = TodoAddForm()
    if request.method == 'POST':
        # print(request.POST)
        form = TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form
    }
    return render(request, 'todo/todo_add.html', context)


def todo_update(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoUpdateForm(instance=todo)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form
    }
    return render(request, 'todo/todo_update.html', context)

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    """ todo yu id ile çek ve context yapısı içinde template e gönder, kullanıcıya form şeklinde göstereceğiz ve kullanıcı oradan bize request.post ile bize gönderecek """
    if request.method == "POST":
    """ request.post ise """
        todo.delete()
        """ todo delete et """
        return redirect('list')
        """ bizi listeye gönder """
    context = {
        'todo': todo
    }
    return render(request, 'todo/todo_delete.html', context)

```




Şİmdi todo_delete template ini oluşturmaya sıra geldi. App imizin içindeki templates/todo klasörlerinin içine <todo_delete.html> templatimizi base.html i extends ederek oluşturuyoruz.



```python
{% extends 'base.html' %}

{% block content %}

<form action="" method="post">

    {% csrf_token %}
    <p>Are you sure delete {{todo}} ?</p>
    <input type="submit" value="delete">

</form>

{% endblock content %}
    
```





<todo_delete.html> template imizi oluşturduk ve onu <urls.py> da adreslememiz gerekiyor. ->

```python
from django.urls import path
from .views import home, todo_list, todo_add, todo_update, todo_delete

urlpatterns = [
    path('', home, name='home'),
    path('list/', todo_list, name='list'),
    path('add/', todo_add, name='add'),
    path('<int:id>/update', todo_update, name='update'),
    path('<int:id>/delete', todo_delete, name='delete'),
]
```





Projenin logic kısmı bitti. Bundan sonra artık template ler arasında geçiş yapacağız, daha kullanışlı hale getireceğiz.


önce todolarımıza link ekleyeceğiz. Todolarımız list sayfasında. List sayfasına gidip <todo_list.html> ->

```python
{% extends 'base.html' %}

{% block content %}

<div>
    <ul>
        <h2>Todo List</h2>

{% for todo in todos %}

   <a href="{% url 'update' todo.id %}"> <li>{{todo}}</li> </a>
   """ link etıklanınca update sayfasına todo nun id si ile git. """

{% endfor %}

    </ul>
</div>

{% endblock content %}

```





todo completed True ise todo nun üzerini çizsin. Yine bunu da <todo_list.html> sayfasında if yapısıyla completed True ise şöyle yap, değilse böyle yap diyeceğiz. ->
<todo_list.html> ->

```python
{% extends 'base.html' %}

{% block content %}

<div>
    <ul>
        <h2>Todo List</h2>

{% for todo in todos %}

    {% if todo.completed %}
    """ eğer todo.completed true ise aşağıdaki gibi del ile yani üzeri çizili göster. """
        <a href="{% url 'update' todo.id %}"> <li> <del>{{todo}}</del> </li> </a>
    {% else %}
    """ değil ise aşağıdaki gibi yani olduğu gibi göster. """
        <a href="{% url 'update' todo.id %}"> <li>{{todo}}</li> </a> 
    {% endif %}
        
{% endfor %}

    </ul>
</div>

{% endblock content %}

```










update sayfasında delete butonu koyup bizi delete sayfasına göndermesini sağlayalım. ->
<todo_update.html> sayfasına gidiyoruz ->

```python
{% extends 'base.html' %}

{% block content %}

<form action="" method="post">
    {% csrf_token %}
    {{form}}
    <input type="submit" value="Update">

</form>

<a href="{% url 'delete' todo.id %}">
''' biz update sayfasına sadece form göndermiştik. Bu şekilde kalırsa hata alırız. Hata almamak için <views.py> a gidip update template ine context içerisinde form ile birlikte todo yu da göndermeliyiz ki gönderdiğimiz todo yu id si ile buradan çekip işlem yapabilelim.'''
    <button>Delete</button>
</a>

{% endblock content %}
    
```






<views.py> da update template ine context yapısı içerisinde form ile birlikte todo nun da id si ile işlem yapılabilmesi için gönderilmesi ->

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoAddForm, TodoUpdateForm

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo/todo_list.html', context)

def todo_add(request):
    form = TodoAddForm()
    if request.method == 'POST':
        # print(request.POST)
        form = TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form
    }
    return render(request, 'todo/todo_add.html', context)


def todo_update(request, id):
    # todo = Todo.objects.get(id=id)
    todo = get_object_or_404(Todo, id=id)
    form = TodoUpdateForm(instance=todo)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form,
        'todo': todo
    }
    return render(request, 'todo/todo_update.html', context)

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        todo.delete()
        return redirect('list')
    context = {
        'todo': todo
    }
    return render(request, 'todo/todo_delete.html', context)
```







todo larımızı list sayfasından ekleyelim. todo_add sayfamızdaki formu kopyalayıp todo_list sayfamızın üst kısmına yapıştırıyoruz.->

<todo_list.html>  ->

```python
{% extends 'base.html' %}

{% block content %}

<form action="" method="post">

    {% csrf_token %} {{form}}
    <input type="submit" value="Add">

</form>


<div>
    <ul style="border: 1px solid red; width: 20%;">
        <h2>Todo List</h2>

{% for todo in todos %}

    {% if todo.completed %}
        <a href="{% url 'update' todo.id %}"> <li style="border: 1px solid aqua; margin-bottom: 15px;"> <del>{{todo}}</del> </li> </a>
    {% else %}
        <a href="{% url 'update' todo.id %}"> <li style="border: 1px solid aqua; margin-bottom: 15px;">{{todo}}</li> </a> 
    {% endif %}
        
{% endfor %}

    </ul>
</div>

{% endblock content %}

```

formu kopyalayıp yapıştırdık, imput Add butonu geldi ama 
form u view den bu template e yani <todo_list.html> template ine göndermediğimiz için formun kutusu gelmedi. Bunun için views.py da form kodlarını da todo_list view ünün içine kopyalıyoruz. Ayrıca form u da context in içinde list templatine göndereceğiz. Böylelikle ->

<views.py> bu şekle geliyor ->

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoAddForm, TodoUpdateForm

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def todo_list(request):
    todos = Todo.objects.all()
    form = TodoAddForm()
    if request.method == 'POST':
        # print(request.POST)
        form = TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')

    context = {
        'todos': todos,
        'form': form
    }
    return render(request, 'todo/todo_list.html', context)

def todo_add(request):
    form = TodoAddForm()
    if request.method == 'POST':
        # print(request.POST)
        form = TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form
    }
    return render(request, 'todo/todo_add.html', context)


def todo_update(request, id):
    # todo = Todo.objects.get(id=id)
    todo = get_object_or_404(Todo, id=id)
    form = TodoUpdateForm(instance=todo)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form,
        'todo': todo
    }
    return render(request, 'todo/todo_update.html', context)

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        todo.delete()
        return redirect('list')
    context = {
        'todo': todo
    }
    return render(request, 'todo/todo_delete.html', context)

```

Artık biz <todo_list> template imizde hem todo larımızı listeliyoruz, hem de buraya bir tane boş form koyuyoruz. Eğer kullanıcı bu boş formu post ederse o todo yu da db ye kaydediyoruz (logic kodlarını todo_add view ünden kopyalayarak yazdık buraya), tıpkı todo_add template inde yaptığımız gibi.




Buradan sonra artık <urls.py> da "add" kısmını kapatabiliriz ->
<urls.py>  -> 

```python
from django.urls import path
from .views import home, todo_list, todo_update, todo_delete #todo_add,

urlpatterns = [
    path('', home, name='home'),
    path('list/', todo_list, name='list'),
    # path('add/', todo_add, name='add'),
    path('<int:id>/update', todo_update, name='update'),
    path('<int:id>/delete', todo_delete, name='delete'),
]

```



En son <todo_list.html> ve <todo_update.html> template lerinde inline style ile birşeyler yaptım. en son durumları -> 

<todo_list.html> ->

```python
{% extends 'base.html' %}

{% block content %}

<form action="" method="post">

    {% csrf_token %} {{form}}
    <input type="submit" value="Add">

</form>


<div>
    <ul style="border: 1px solid red; width: 20%;">
        <h2>Todo List</h2>

{% for todo in todos %}

    {% if todo.completed %}
        <a href="{% url 'update' todo.id %}"> <li style="border: 1px solid aqua; margin-bottom: 15px;"> <del>{{todo}}</del> </li> </a>
    {% else %}
        <a href="{% url 'update' todo.id %}"> <li style="border: 1px solid aqua; margin-bottom: 15px;">{{todo}}</li> </a> 
    {% endif %}
        
{% endfor %}

    </ul>
</div>

{% endblock content %}

```





<todo_update.html> ->

```python
{% extends 'base.html' %}

{% block content %}

<form action="" method="post">
    {% csrf_token %}
    {{form}}
    <input type="submit" value="Update">

</form>


<a href="{% url 'delete' todo.id %}"><button style="margin: 10px">Delete</button></a>

<a href="{% url 'list' %}"><button style="margin: 10px">List</button></a>

{% endblock content %}
    
```






### PostgreSQL bağlama

database ayarını settings den yapıyorduk. Default olarak sqlite3 geliyor.