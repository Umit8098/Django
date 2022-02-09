### CRUD Normal Views
Create, Read, Update, Delete

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


- go to terminal, stop project (Ctrl + C), add app

(terminale gidip durduruyoruz ve bir app <fscohort> oluşturuyoruz.)

```bash
$ py manage.py startapp fscohort
```

- go to settings.py and add 'fscohort' app to installed apps and add below lines

(<settings.py> dosyasına gidip app kısmına ekliyoruz.)

```python
INSTALLED_APPS = [
    .....
    .....
    'django.contrib.staticfiles',
    # apps
    'fscohort',
]
```


##### media işlemleri için -> 

(Yine bugün biz media işlemleri yapacağımız için aşağıdaki code ları da <settings.py> dosyasının en altına (import olanı import bölümüne) ekliyoruz.)

```python
import os
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```


- create these folders at project level as /media/student

(Proje dosyasıyla aynı seviyede /media/student klasörlerini oluşturuyoruz.(media ları burada tutacağız.))


THEN->


- go to fscohort/models.py

(fscohort app inin altındaki <models.py> dosyasına gidip "Student" isminde bir model oluşturuyoruz, daha önce görmüştük. Bu modelde ImageField da kullandığımız için proje ve app klasörleriyle aynı seviyede media klasörü oluşturup içine de student klasörü oluşturuyoruz ki yüklenen medyalar düzenli olsun. media/student kalsörlerini iç içe oluşturup upload ı buraya verdik. Bir de option daha veriyoruz, eğer resim yüklenmezse default olarak bir avatar yüklensin, avatar resmini de media kalsörünün içine koyduk. (blanc=True dersek de resim yüklemeyi mecbur tutmayız. ) )

<fscohort/models.py> ->

```python
from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    """ blank=True (girilmesi zorunlu değil), null=True (null kaydedebilir.)"""
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    GENDER = {
        ('1', 'Female'),
        ('2', 'Male'),
        ('3', 'Other'),
        ('4', 'Prefer Not Say'),
    }
    gender = models.CharField(max_length=50, choices=GENDER)
    
    number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='student/', default='avatar.png' )

    def __str__(self):
        return f'{self.number} - {self.first_name}'
        # return self.number + ' ' + self.first_name


```



- go to terminal

(Bir model oluşturduğumuz için <makemigrations> (django, oluşturduğumuz modeli db de oluşturmak için hazırlık yapıyor.) ve <migrate> (migrations ile yaptığı hazırlıkları db de işliyor.) komutlarını kullanmalıyız. Bir model oluşturduğumuz ya da modelde değişiklik yaptığımız zaman ilk yapacağımız iş bu komutları kullanmak.)

```bash
$ py manage.py makemigrations
$ py manage.py migrate
```


- go to fscohort/admin.py and add to our model.

(fscohort/admin.py dosyasına gidip modelimizi import edip ekliyoruz.)

<fscohort/admin.py> ->

```python
from django.contrib import admin
from .models import Student

# Register your models here.

admin.site.register(Student)
```


- go to terminal and create superuser

(admin panalden modelimize ulaşmak için superuser oluşturuyoruz.)

```bash
$ py manage.py createsuperuser
```


- go to terminal and admin panel

```bash
$ py manage.py runserver
```

(admin panelde modelimize student ekliyoruz. resim ekleyerek save ediyoruz, eklemeden save ediyoruz. Farklarını görüyoruz.)


THEN ->


fscohort views.py ında home view ünü HttpResponse ile ekranda bir yazı çıkartmak istiyoruz.

proje <urls.py> ına gidip, fscohort app inin <urls.py> ını "include" ediyoruz, path ini ekliyoruz ve ayrıca <static> ve <settings> import edip, en sona static komutlarımızı yazıyoruz. Resim de eklediğimiz için.->

<main/views.py> ->

```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fscohort.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

*************************************************************************
!!!!!  settings dosyalarını karşılaştır. Biraz farklı ama çalıştı. !!!!!
*************************************************************************

fscohort app inde bir <urls.py> dosyası oluşturup ve içine app imizin <views.py> ında oluşturduğumuz home view ini import edip aşağıdaki kodları yazıyoruz.->

<fscoghort/urls.py> ->

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```


fscohort app inin <views.py> dosyasında django.http den HttpResponse u import et, ve home view ini oluştur.->

<fscohort/views.py> ->

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Welcome to Student Application</h1>')
```

THEN ->


(Artık templates lerimize geliyoruz...)

- create templates folder in our app as fscohort/templates/fscohort

(fscohort app klasörünün içine <templates> klasörünü, onun da içine app imizin ismi olan <fscohort> kalsörünü "/templates/fscohort" şeklinde oluşturup, bu <fscohort> klasörünün içine de template lerimizi <home.html , ###.html> oluşturuyoruz. Şimdi <home.htlm> oluşturduk.)

<home.htlm> templateimiz ->

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CW Student App</title>
</head>
<body>
    <h1>
        <center>
            Clarusway
        </center>
    </h1>
</body>
</html>
```


artık biz fscohort app imizin views.py ında HttpResponse değil de <home.htlm> template imiz dönsün istiyoruz. onun için fscohort app imizin views.py ına gidip aşağıdaki değişiklikleri yapıyoruz. ->

<fscohort/views.py> ->

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return render(request, template, context)
    return render(request, 'fscohort/home.html')
```


bizim birçok template imiz olabilir, her seferinde bir değişikliği diğer template lerde de yapmak zorunda kalmamak için bir tane <base.html> diye bir iskelet template, yapı oluşturup diğer template leri buna extends edeceğiz, bağlayacağız. app imizin içindeki template klasörümüzün içindeki app imizle aynı adı taşıyan klasöre <base.html> diye bir dosya oluşturup tag lerini yerleştiriyoruz. (body nin içine -> {% block content %}{% endblock content %} tagları yazıyoruz.)

<base.html> templateimiz ->

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CW Student App</title>
</head>
<body>
    <h1>
        <hr>
        <center>
            Clarusway
        </center>
        <hr>
    </h1>
    {% block content %}
        
    {% endblock content %}
</body>
</html>
```


Artık <base.html> imizi oluşturduğumuza göre diğer template lerimizi bundan extends ederek kullanabiliriz. {% extends 'fscohort/base.html' %} ve {% block content %} {% endblock content %} taglarını <base.html> i extends ediyoruz be block taglarinin arasına da göstermek istediklerimizi yazıyoruz. 

<home.html> templatimizi şu şekilde değiştiryoruz ->

```html
{% extends 'fscohort/base.html' %}

{% block content %}

<h2>
    <center>
        Welcome To Student App <br> (Backend Team)
    </center>
</h2>

{% endblock content %}

```

****************************************************
```bash
git add .
git commit -m 'feat: add template fscohort'
git push
```
*****************************************************


#### CRUD işlemleri :

app imizin <views.py> ına gidip oarada CRUD işlemlerine başlıyoruz. Kullanacağımız modeli import ediyoruz.

fscohort <views.py> -> 

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

def home(request):
    # return render(request, template, context)
    return render(request, 'fscohort/home.html')

def student_list(request):   <!-- db den veri çekme -->
    pass

def student_add(request):   <!-- db ye veri girme, store etme. -->
    pass


<!-- db den veri çekip işlem yapacağımız için verinin primary key ine ihtiyaç duyuyoruz. -->
def student_detail(request, pk):  <!-- db de olan veriyi çekme, db de olması lazım, db ye istek atarken request e primary key ekleyeceğiz. -->
    pass

def student_update(request, pk):  <!-- db de olan veriyi edit etme, db de olması lazım, db ye istek atarken request e primary key ekleyeceğiz. -->
    pass

def student_delete(request, pk):   <!-- db de olan veriyi delete etme, db de olması lazım, db ye istek atarken request e primary key ekleyeceğiz. -->
    pass
```




şimdi artık başlıyoruz. ORM kullanıyoruz.
<views.py> ->

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

def home(request):
    # return render(request, template, context)
    return render(request, 'fscohort/home.html')

def student_list(request):
    students = Student.objects.all() <!-- (SELECT * FROM) ile aynı db deki hepsini getir. models.py dan Student modelimizi import ediyoruz. -->
    context = {
        'students' : students
    }
    return render(request, 'fscohort/student_list.html', context) <!-- context ile içindeki bilgileri template imize gönderiyoruz. student_list.html template i oluştur, urls.py dan adresle -->

def student_add(request):  <!-- db ye veri ekliyeceğiz, Bunun için form kullanıyoruz, form oluşturacağız ve views.py a import edeceğiz aşağıya bak! -->
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)  <!-- resim dosyası için de request.FILES kullanıyoruz. -->
        if form.is_valid():
            form.save()
    
    context = {
        'form': form
    }
    return render(request, 'fscohort/student_add.html', context) <!-- student_add.html template i oluştur, urls.py dan adresle -->




def student_detail(request, id):
    student = Student.objects.get(id=id)
    context={
        'student': student
    }
    
    return render(request, 'fscohort/student_detail.html', context ) <!-- student_detail.html temp.i oluştur, urls.py dan adrsle -->
    <!-- student_detail.html de resimlerin görünmesi için projenin urls.py ında değişiklik yapılmalı "+ static kısımları", aşağıya bak! -->


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    """ form dan veri çekerken instance kısmı yazılıyor dikkat! """
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
            """ formu save ettikten sonra list e git """

    
    context = {
        'student': student,
        'form': form
    }
    return render(request, 'fscohort/student_update.html', context)


def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    
    context = {
        'student': student,
    }
    return render(request, 'fscohort/student_delete.html', context)

```


##### for <def student_list(request):> için ->

<student_list.html> template i oluştur -> 
```html
{% extends 'fscohort/base.html' %}
{% block content %}
<h2>Student List</h2>
<ul>
{% for student in students %}
<li> {{ student }} </li>
{% endfor %}
</ul>
{% endblock content %}
```

ve 

<student_list.html> template inin <urls.py> da adreslenmesi ->

```python
from django.urls import path
from .views import home, student_list

urlpatterns = [
    path('', home, name='home'),
    path('student_list/', student_list, name='list'),
]

```



##### for <def student_add(request):> için ->

db ye veri girişi için app imizin içinde <forms.py> dosyası ve içinde de "StudentForm" formumuzu modelimizden oluşturacağız. form, db ye yapılan post isteklerini sağlıyor. djangodan forms ları import ediyoruz <from django import forms> . Formlar iki çeşit; "forms.Form" dan yapılanlar ve "forms.ModelForm" dan yapılanlar. Biz çoğunlukla "Forms.ModelForm" kullanacağız  . O yüzden modelimizi import ediyoruz <from .models import Student> . Ayrıca "django.forms" dan "fields" ları da import ediyoruz <from django.forms import fields> . Bir de oluşturduğumuz formu fscohort app imizin <views.py> ına da import etmemiz gerekiyor <from .forms import StudentForm>. 

<forms.py> daki formumuz ->

```python
from django import forms
from django.forms import fields
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

```


<views.py> da business logic ini oluşturduktan sonra şimdi <student_add.html> template i oluştur ->

```python
{% extends 'fscohort/base.html' %}

{% block content %}

<h2>Student Add</h2>

<form action='' method='POST' enctype='multipart/form-data'>
""" image larla ilgili. enctype yazılması iyi olur. """

{% csrf_token %}{{form.as_p}}

<input type='submit' value='Add'>

</form>

{% endblock content %}

```


<student_add.html> template inin <urls.py> da adreslenmesi ->

```python
from django.urls import path
from .views import home, student_list, student_add

urlpatterns = [
    path('', home, name='home'),
    path('student_list/', student_list, name='list'),
    path('student_add/', student_add, name='add'),
]

```




##### for <def student_detail(request, id):> için ->

<views.py> da business logic ini oluşturduk şimdi <student_detail.html> template i oluştur ->

```python
{% extends 'fscohort/base.html' %}

{% block content %}

<h2>Student Detail</h2>
<div> <img src='{{student.image.url}}' alt=''> </div>
<div> {{ student.first_name}} </div>
<div> {{ student.last_name}} </div>
<div> {{ student.number}} </div>
<div> {{ student.email}} </div>
<div> {{ student.phone}} </div>
<div> {{ student.gender}} </div>

{% endblock content %}

```


<student_detail.html> template inin <urls.py> da adreslenmesi dikkat biraz farklı ->

```python
from django.urls import path
from .views import home, student_list, student_add, student_detail

urlpatterns = [
    path('', home, name='home'),
    path('student_list/', student_list, name='list'),
    path('student_add/', student_add, name='add'),
    path('<int:id>/', student_detail, name='detail'),
    """ 'detail/<int:id>/' da yazılabilir, kısmına dikkat! """
]

```


<student_detail.html> template ine gidilebilmesi için <student_list.html> template inden link veriyoruz ->

<student_list.html> template i aşağıdaki gibi oluyor artık ->

```python
{% extends 'fscohort/base.html' %}
{% block content %}

<h2>Student List</h2>

<ul>

{% for student in students %}

<a href="{% url 'detail' student.id %}">
""" bu bir linktir.bunu tıklayınca detail e id ile beraber git.  """

<li> {{ student }} </li>

</a>

{% endfor %}

</ul>

{% endblock content %}

```











##### for <def student_update(request, id):> için ->

<views.py> da business logic ini oluşturduk şimdi <student_update.html> template i oluştur ->

```python
{% extends 'fscohort/base.html' %}

{% block content %}

<h2>Student Update</h2>

<form action='' method='POST' enctype='multipart/form-data'>
""" enctype olsun! """

{% csrf_token %} {{form.as_p}}

<input type='submit' value='Update'>

</form>

{% endblock content %}
```




detail de ne yapmıştık list sayfasında link vermiştik, tıklayınca detail sayfasına gidiyordu. burada da benzer birşey yapacağız, bu sefer detail sayfasına bir link ekleyeceğiz ve update sayfasına yönlendireceğiz.

<student_update.html> template ine gitmesi için <student_detail.html> template inden link veriyoruz ->

<student_detail.html> template i aşağıdaki gibi oluyor artık ->

```python
{% extends 'fscohort/base.html' %}

{% block content %}

<h2>Student Detail</h2>
<div> <img src='{{student.image.url}}' alt=''> </div>
<div> {{ student.first_name}} </div>
<div> {{ student.last_name}} </div>
<div> {{ student.number}} </div>
<div> {{ student.email}} </div>
<div> {{ student.phone}} </div>
<div> {{ student.gender}} </div>
<div><a href="{% url 'update' student.id %}">Edit</a></div>
""" bu bir linktir, tıklayınca update e student.id ile git """

{% endblock content %}

```



<student_update.html> template inin <urls.py> da adreslenmesi ->

```python
from django.urls import path
from .views import home, student_list, student_add, student_detail, student_update

urlpatterns = [
    path('', home, name='home'),
    path('student_list/', student_list, name='list'),
    path('student_add/', student_add, name='add'),
    path('<int:id>/', student_detail, name='detail'),
    path('update/<int:id>/', student_update, name='update'),
    """ 'update/<int:id>/' kısmına dikkat! """
]

```







##### for <def student_delete(request, id):> için ->

<views.py> da business logic ini oluşturduk şimdi <student_delete.html> template i oluştur ->

```python
{% extends 'fscohort/base.html' %}

{% block content %}

<h3>Student Delete</h3>

<div>

<form action='' method='POST' enctype='multipart/form-data'>

{% csrf_token %} Are yoıu sure delete {{student}}?<br>

<input type='submit' value='Yes'>

</form>

<a href="{% url 'list' %}">
<button>No<button>
</a>

</div>

{% endblock content %}
```





<student_delete.html> template inin <urls.py> da adreslenmesi ->

```python
from django.urls import path
from .views import home, student_list, student_add, student_detail, student_update, student_delete

urlpatterns = [
    path('', home, name='home'),
    path('student_list/', student_list, name='list'),
    path('student_add/', student_add, name='add'),
    path('<int:id>/', student_detail, name='detail'),
    path('update/<int:id>/', student_update, name='update'),
    path('delete/<int:id>/', student_delete, name='delete'),
]

```


detail.html sayfasına delete sayfasına id ile gitmesi için link veriyoruz. ->

```html
{% extends 'fscohort/base.html' %}

{% block content %}

<h2>Student Detail</h2>
<div><img src="{{student.image.url}}" alt=""></div>
<div>{{student.first_name}}</div>
<div>{{student.last_name}}</div>
<div>{{student.number}}</div>
<div>{{student.email}}</div>
<div>{{student.phone}}</div>
<div>{{student.gender}}</div>
<div>
    <a href="{% url 'update' student.id %}">Edit</a>
    <a href="{% url 'delete' student.id %}">Delete</a>
</div>

{% endblock content %}

```




detail.html sayfasına list sayfası için link veriyoruz ->

```html
{% extends 'fscohort/base.html' %}

{% block content %}

<h2>Student Detail</h2>
<div><img src="{{student.image.url}}" alt=""></div>
<div>{{student.first_name}}</div>
<div>{{student.last_name}}</div>
<div>{{student.number}}</div>
<div>{{student.email}}</div>
<div>{{student.phone}}</div>
<div>{{student.gender}}</div>
<div>
    <a href="{% url 'update' student.id %}">Edit</a>
    <a href="{% url 'delete' student.id %}">Delete</a>
    <a href="{% url 'list' %}">List</a>
</div>

{% endblock content %}

```




home.html sayfasına list ve add sayfaları için link veriyoruz ->

```html
{% extends 'fscohort/base.html' %}

{% block content %}

<h2>
    <center>
        Welcome To Student App <br> (Backend Team)
        <hr>
        <br>
        <a href="{% url 'list' %}">LIST</a>
        <a href="{% url 'add' %}">Add</a>
    </center>
</h2>
{% endblock content %}

```


<!-- Buraya kadar django 8.ders CRUD normal views-->
<!-- Buradan sonra django 10.ders class based views başlıyor -->

### CRUD Class Based Views


- NOT:
Posgresql eklediğimiz zaman da hassas verileri mesela username, password onları settings.py dan alıp .env dosyasının içine yazıp, setting.py dosyasına da aynı secret_key de olduğu gibi config deyip .env yi işaret edebiliriz, etmeliyiz. 



Navigate to https://docs.djangoproject.com/en/3.2/topics/class-based-views/
Explain Documentation

## Class Based Views
(class ve model tanımlarken ilk harfleri büyük istiyor ama template için küçük harf istiyor.)

- Bugünkü dersimizde tamamen hazırcılığı göreceğiz. Şimdiye kadar işlerimizi views.py da function yazarak hallettik. Bu işi nasıl daha kolay yapabiliriz den hareketle herşeyi basitleştiren, bir şablon halide döken bir sistem de var djangoda.
- View class diye birşey tanımlamışlar, çeşitli template ler türetmişler. 
- Bunlardan ilki TemplateView; Bir template i render etmek için TemplateView classını kullanabilirsin. Bunu direkt urls.py içerisinde bu işlemi yapabilirsiniz. Ekstradan views yazmaya gerek kalmıyor, ancak bunun için basit bir template olması gerekiyor. Karışık bir template varsa burda yapmak çok uygun değil.

```python
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="about.html")),
]
```


1. yöntem: ->

Mesela <views.py> da bizim oluşturduğumuz templatelerimize baktığımız zaman home page imiz var. home page imize herhangi bir context göndermiyoruz, sadece basit bir html file ını render ediyoruz.

<views.py> ->

```python
def home(request):
    return render(request, 'fscohort/home.html')
```

Şimdi biz bunun yerine bir TemplateView kullarak işimizi halletmeye çalışalım. <urls.py> a gidiyoruz. <django.views.generic> den <TemplateView> i import ediyoruz. Sonra template imizin ismini filan aşağıdaki gibi yazıyoruz.

<urls.py> ->

```python

from django.urls import path
from .views import home, student_list, student_add, student_detail, student_update, student_delete
from django.views.generic import TemplateView

urlpatterns = [
    # path('', home, name='home'),
    path('', TemplateView.as_view(template_name='fscohort/home.html'), name='home'),
    path('student_list/', student_list, name='list'),
    path('student_add/', student_add, name='add'),
    path('detail/<int:id>/', student_detail, name='detail'),
    path('update/<int:id>/', student_update, name='update'),
    path('delete/<int:id>/', student_delete, name='delete'),
] 

```

Ne yaptık burada home view ümüz vardı, onun yerine TemplateView.as_view dedik ve parantez içinde template sen bu template i render et dedik. Yine name ini de home dedik.

Buraya kadar ki 1. yöntem di.


2. yöntem: ->
   
Bu classları <urls.py> da değil de <views.py> içerisinde kullanmak. <views.py> a gidiyoruz, <TemplateView> ü import ediyoruz, home template inin view ünün yerine aşağıdaki kodları yazıyoruz. Arkasından tabiki bu view ü <urls.py> da import etmemiz lazım.

```python
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.views.generic import TemplateView

# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Welcome to Student Application</h1>')

def home(request):
    return render(request, 'fscohort/home.html')

class HomeView(TemplateView):
    template_name = 'fscohort/home.html'


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'fscohort/student_list.html', context)


def student_add(request):
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    context = {
        'form': form
    }
    return render(request, 'fscohort/student_add.html', context)


def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'fscohort/student_detail.html', context)


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context = {
        'student': student,
        'form': form
    }
    return render(request, 'fscohort/student_update.html', context)


def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    
    context = {
        'student': student,
    }
    return render(request, 'fscohort/student_delete.html', context)
```


Arkasından tabiki bu view ü <urls.py> da import etmemiz lazım. Burada yaptığımız TemplateView u da yoruma alıyoruz,

<urls.py> ->

```python

from django.urls import path
from .views import student_list, student_add, student_detail, student_update, student_delete
from django.views.generic import TemplateView
from .views import HomeView

urlpatterns = [
    # path('', home, name='home'),
    # path('', TemplateView.as_view(template_name='fscohort/home.html'), name='home'),
    # # 1. yöntem urls.py da yapmak
    path('', HomeView.as_view(), name='home'),
    # 2. yöntem views.py da yapıp buraya import etmek
    path('student_list/', student_list, name='list'),
    path('student_add/', student_add, name='add'),
    # path('detail/<int:id>', student_detail, name='detail'),
    path('<int:id>/', student_detail, name='detail'),
    path('update/<int:id>/', student_update, name='update'),
    path('delete/<int:id>/', student_delete, name='delete'),
]

```

HomeViews.as_view kullanırken daha önce import ettiğimiz home view ünü silmemiz gerekir yoksa hata verir.



Haaa bunu neden kullanıyoruz. Tamamen hazırcılık için tasarlanmış. Mesela Create, Update, Delete işlemlerinin hepsinin ayrı ayrı template leri var. Bir kullanıcının yapabileceği tüm işlemler (List, Create, Update, Delete) için developera hazır template ler sunayım developer her seferinde bunları baştan yazmasın şeklinde bir yaklaşımdır.




##### <ListView> 
(Display views lerimizden)

<views.py> a gidip list işlemine bakıyoruz; List i nerde yapıyorduk def student_list ile yapıyorduk. Hemen onun altına geliyoruz, tabi <ListView> ü import ediyoruz <django.views.generic> dan, tabi sonrasında <urls.py> da adresliyoruz, Şöyle yazıyoruz: 

(Ayrıca paginate_by = 5 ile kaç tane (burada 5) göstersin diyebiliyoruz. Bunu yazınca terminalde bir uyarı alıyoruz, neye göre 5 tane göstereceğim. Yani bana listeyi sıralamam için bir komut ver diyor. O komutu da modelimizde veriyoruz, yani her zaman en son eklediğimi en üstte göster. 
<models.py>
```python
    class Meta:
        ordering = ['-id']
```
)

<views.py> ->

```Python
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.views.generic import TemplateView, ListView

# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Welcome to Student Application</h1>')

def home(request):
    return render(request, 'fscohort/home.html')

class HomeView(TemplateView):
    template_name = 'fscohort/home.html'


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'fscohort/student_list.html', context)

class StudentListView(ListView):
    model = Student
    # default name app/modelname_list.htm
    # template_name = 'fscohort/student_list.html'
    # default name object_list
    context_object_name = 'students'
    paginate_by = 5

def student_add(request):
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    context = {
        'form': form
    }
    return render(request, 'fscohort/student_add.html', context)


def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'fscohort/student_detail.html', context)


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context = {
        'student': student,
        'form': form
    }
    return render(request, 'fscohort/student_update.html', context)


def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    
    context = {
        'student': student,
    }
    return render(request, 'fscohort/student_delete.html', context)
```


<urls.py> ->

```python
from django.urls import path
from .views import home, student_list, student_add, student_detail, student_update, student_delete
from django.views.generic import TemplateView
from .views import HomeView, StudentListView

urlpatterns = [
    # path('', home, name='home'),
    # path('', TemplateView.as_view(template_name='fscohort/home.html'), name='home'),
    path('', HomeView.as_view(), name='home'),
    # path('student_list/', student_list, name='list'),
    path('student_list/', StudentListView.as_view(), name='list'),
    path('student_add/', student_add, name='add'),
    path('detail/<int:id>/', student_detail, name='detail'),
    path('update/<int:id>/', student_update, name='update'),
    path('delete/<int:id>/', student_delete, name='delete'),
] 
```


### <List.html> de sonraki sayfaya geçme template pagination in django

List template i içinde sonraki sayfaya geçeme için yazılan kodlar. Ayrıca <student_list.html> e bir de <student_add.html> e gidilebilsin diye bir de link veriyoruz. 

<student_list.html> ->
```python
{% extends 'fscohort/base.html' %}

{% block content %}

<h2>Student List</h2>

<ul>

{% for student in students %}

<a href="{% url 'detail' student.id%}" target="_blank"><li>{{student}}</li></a>

{% endfor %}

</ul>

<br><br><br>

<hr>
{% for student in page_obj %}
    {# Each "contact" is a Contact model object. #}
    {{ student.full_name|upper }}
{% endfor %}

<div class="pagination">
    <span class="step-links">
        {% if page_obj.has_previous %}
            <a href="?page=1">&laquo; first</a>
            <a href="?page={{ page_obj.previous_page_number }}">previous</a>
        {% endif %}

        <span class="current">
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
        </span>

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">next</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
    </span>
</div>
<hr>
    
{% endblock content %}

```





##### <DetailView> 
(Display views lerimizden)

<views.py> a gidip detail işlemine bakıyoruz; detail i nerde yapıyorduk def student_detail ile yapıyorduk. Hemen onun altına geliyoruz, tabi <DetailView> ü import ediyoruz <django.views.generic> dan, tabi sonrasında <urls.py> da adresliyoruz, Şöyle yazıyoruz: 

<views.py> ->

```python

from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Welcome to Student Application</h1>')

def home(request):
    return render(request, 'fscohort/home.html')

class HomeView(TemplateView):
    template_name = 'fscohort/home.html'


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'fscohort/student_list.html', context)

class StudentListView(ListView):
    model = Student
    # default name app/modelname_list.htm
    # template_name = 'fscohort/student_list.html'
    # default name object_list
    context_object_name = 'students'

def student_add(request):
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    context = {
        'form': form
    }
    return render(request, 'fscohort/student_add.html', context)


def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'fscohort/student_detail.html', context)

class StudentDetailView(DetailView):
    model = Student
    

def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context = {
        'student': student,
        'form': form
    }
    return render(request, 'fscohort/student_update.html', context)


def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    
    context = {
        'student': student,
    }
    return render(request, 'fscohort/student_delete.html', context)

```



<urls.py> Burada biz id ile işlem yapıyorduk. Ama burada pk kullanmamız gerekiyor. Çünkü modelde field pk diye geçiyor, id diye geçmiyor. ->

```python

from django.urls import path
from .views import student_add, student_detail, student_update, student_delete, home, student_list
from django.views.generic import TemplateView
from .views import HomeView, StudentListView, StudentDetailView

urlpatterns = [
    # path('', home, name='home'),
    # path('', TemplateView.as_view(template_name='fscohort/home.html'), name='home'),
    path('', HomeView.as_view(), name='home'),
    # path('student_list/', student_list, name='list'),
    path('student_list/', StudentListView.as_view(), name='list'),
    path('student_add/', student_add, name='add'),
    # path('detail/<int:id>/', student_detail, name='detail'),
    path('detail/<int:pk>/', StudentDetailView.as_view(), name='detail'),
    path('update/<int:id>/', student_update, name='update'),
    path('delete/<int:id>/', student_delete, name='delete'),
] 

```

illa id kullanacağım diyorsan eğer şöyle => 

<views.py> da pk_url_kwarg = 'id' bu kodu ekliyorsun, ayrıca urls de de ;->

```python

from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Welcome to Student Application</h1>')

def home(request):
    return render(request, 'fscohort/home.html')

class HomeView(TemplateView):
    template_name = 'fscohort/home.html'


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'fscohort/student_list.html', context)

class StudentListView(ListView):
    model = Student
    # default name app/modelname_list.htm
    # template_name = 'fscohort/student_list.html'
    # default name object_list
    context_object_name = 'students'

def student_add(request):
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    context = {
        'form': form
    }
    return render(request, 'fscohort/student_add.html', context)


def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'fscohort/student_detail.html', context)

class StudentDetailView(DetailView):
    model = Student
    pk_url_kwarg = 'id'

def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context = {
        'student': student,
        'form': form
    }
    return render(request, 'fscohort/student_update.html', context)


def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    
    context = {
        'student': student,
    }
    return render(request, 'fscohort/student_delete.html', context)

```



<urls.py> burada da id ile kullanabilirsin. ->

```python

from django.urls import path
from .views import student_add, student_detail, student_update, student_delete, home, student_list
from django.views.generic import TemplateView
from .views import HomeView, StudentListView, StudentDetailView

urlpatterns = [
    # path('', home, name='home'),
    # path('', TemplateView.as_view(template_name='fscohort/home.html'), name='home'),
    path('', HomeView.as_view(), name='home'),
    # path('student_list/', student_list, name='list'),
    path('student_list/', StudentListView.as_view(), name='list'),
    path('student_add/', student_add, name='add'),
    # path('detail/<int:id>/', student_detail, name='detail'),
    path('detail/<int:id>/', StudentDetailView.as_view(), name='detail'),
    # path('detail/<int:pk>/', StudentDetailView.as_view(), name='detail'),
    path('update/<int:id>/', student_update, name='update'),
    path('delete/<int:id>/', student_delete, name='delete'),
] 

```



##### <CreateView> 
(Editing views lerimizden)

<views.py> da CreateView i import ediyoruz, redirect için ise önce django.urls den reverse_lazy i import ediyoruz, sonra aşağıya ise success_url = reverse_lazy('list') yazıyoruz.  

<views.py> ->

```python

from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Welcome to Student Application</h1>')

def home(request):
    return render(request, 'fscohort/home.html')

class HomeView(TemplateView):
    template_name = 'fscohort/home.html'


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'fscohort/student_list.html', context)

class StudentListView(ListView):
    model = Student
    # default name app/modelname_list.htm
    # template_name = 'fscohort/student_list.html'
    # default name object_list
    context_object_name = 'students'

def student_add(request):
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context = {
        'form': form
    }
    return render(request, 'fscohort/student_add.html', context)

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'fscohort/student_add.html' # default name app/modelname_form.html
    success_url = reverse_lazy('list')
    # success_url = '/student_list/'  # Bu şekilde de olabilir.



def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'fscohort/student_detail.html', context)

class StudentDetailView(DetailView):
    model = Student
    # pk_url_kwarg = 'id'

def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context = {
        'student': student,
        'form': form
    }
    return render(request, 'fscohort/student_update.html', context)


def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    
    context = {
        'student': student,
    }
    return render(request, 'fscohort/student_delete.html', context)

```


<urls.py> -> 

```python

from django.urls import path
from .views import student_add, student_detail, student_update, student_delete, home, student_list
from django.views.generic import TemplateView
from .views import HomeView, StudentListView, StudentDetailView, StudentCreateView

urlpatterns = [
    # path('', home, name='home'),
    # path('', TemplateView.as_view(template_name='fscohort/home.html'), name='home'),
    path('', HomeView.as_view(), name='home'),
    # path('student_list/', student_list, name='list'),
    path('student_list/', StudentListView.as_view(), name='list'),
    # path('student_add/', student_add, name='add'),
    path('student_add/', StudentCreateView.as_view(), name='add'),
    # path('detail/<int:id>/', student_detail, name='detail'),
    # path('detail/<int:id>/', StudentDetailView.as_view(), name='detail'),
    path('detail/<int:pk>/', StudentDetailView.as_view(), name='detail'),
    path('update/<int:id>/', student_update, name='update'),
    path('delete/<int:id>/', student_delete, name='delete'),
] 

```



##### <UpdateView> 
(Editing views lerimizden)
(Her bir durum için ayrı bir view yazmışlar arkadaşlar.)

<views.py> da yine en başta <UpdateView> i import ediyoruz, class Update views ümüzü yazıyoruz, id ve pk farkına dikkat ediyoruz, reverse_lazy ye dikkat ediyoruz... 

<views.py> ->

```python
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Welcome to Student Application</h1>')

def home(request):
    return render(request, 'fscohort/home.html')

class HomeView(TemplateView):
    template_name = 'fscohort/home.html'


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'fscohort/student_list.html', context)

class StudentListView(ListView):
    model = Student
    # default name app/modelname_list.htm
    # template_name = 'fscohort/student_list.html'
    # default name object_list
    context_object_name = 'students'

def student_add(request):
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context = {
        'form': form
    }
    return render(request, 'fscohort/student_add.html', context)

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'fscohort/student_add.html' # default name app/modelname_form.html
    success_url = reverse_lazy('list')
    # success_url = '/student_list/'  # Bu şekilde de olabilir.


def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'fscohort/student_detail.html', context)

class StudentDetailView(DetailView):
    model = Student
    # pk_url_kwarg = 'id'

def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context = {
        'student': student,
        'form': form
    }
    return render(request, 'fscohort/student_update.html', context)

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'fscohort/student_update.html'
    #default name app/modelname_form.html
    success_url = reverse_lazy('list')

def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    
    context = {
        'student': student,
    }
    return render(request, 'fscohort/student_delete.html', context)

```



<urls.py> -> 

```python

from django.urls import path
from .views import student_add, student_detail, student_update, student_delete, home, student_list
from django.views.generic import TemplateView
from .views import HomeView, StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView

urlpatterns = [
    # path('', home, name='home'),
    # path('', TemplateView.as_view(template_name='fscohort/home.html'), name='home'),
    path('', HomeView.as_view(), name='home'),
    # path('student_list/', student_list, name='list'),
    path('student_list/', StudentListView.as_view(), name='list'),
    # path('student_add/', student_add, name='add'),
    path('student_add/', StudentCreateView.as_view(), name='add'),
    # path('detail/<int:id>/', student_detail, name='detail'),
    # path('detail/<int:id>/', StudentDetailView.as_view(), name='detail'),
    path('detail/<int:pk>/', StudentDetailView.as_view(), name='detail'),
    # path('update/<int:id>/', student_update, name='update'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', student_delete, name='delete'),
] 

```



##### <DeleteView> 
(Editing views lerimizden)

<views.py> ->

```python

from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Welcome to Student Application</h1>')

def home(request):
    return render(request, 'fscohort/home.html')

class HomeView(TemplateView):
    template_name = 'fscohort/home.html'


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'fscohort/student_list.html', context)

class StudentListView(ListView):
    model = Student
    # default name app/modelname_list.htm
    # template_name = 'fscohort/student_list.html'
    # default name object_list
    context_object_name = 'students'
    paginate_by = 5

def student_add(request):
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context = {
        'form': form
    }
    return render(request, 'fscohort/student_add.html', context)

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'fscohort/student_add.html' # default name app/modelname_form.html
    success_url = reverse_lazy('list')
    # success_url = '/student_list/'  # Bu şekilde de olabilir.


def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'fscohort/student_detail.html', context)

class StudentDetailView(DetailView):
    model = Student
    # pk_url_kwarg = 'id'

def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context = {
        'student': student,
        'form': form
    }
    return render(request, 'fscohort/student_update.html', context)

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'fscohort/student_update.html'
    #default name app/modelname_form.html
    success_url = reverse_lazy('list')

def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    
    context = {
        'student': student,
    }
    return render(request, 'fscohort/student_delete.html', context)

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'fscohort/student_delete.html'
    # default name app/modelname_confirm_delete.html
    success_url = reverse_lazy('list')

```


<urls.py> ->

```python
from django.urls import path
from .views import student_add, student_detail, student_update, student_delete, home, student_list
from django.views.generic import TemplateView
from .views import HomeView, StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    # path('', home, name='home'),
    # path('', TemplateView.as_view(template_name='fscohort/home.html'), name='home'),
    path('', HomeView.as_view(), name='home'),
    # path('student_list/', student_list, name='list'),
    path('student_list/', StudentListView.as_view(), name='list'),
    # path('student_add/', student_add, name='add'),
    path('student_add/', StudentCreateView.as_view(), name='add'),
    # path('detail/<int:id>/', student_detail, name='detail'),
    # path('detail/<int:id>/', StudentDetailView.as_view(), name='detail'),
    path('detail/<int:pk>/', StudentDetailView.as_view(), name='detail'),
    # path('update/<int:id>/', student_update, name='update'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    # path('delete/<int:id>/', student_delete, name='delete'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),
] 

```







### <List.html> de sonraki sayfaya geçme template pagination in django

List template i içinde sonraki sayfaya geçeme için yazılan kodlar. 

<student_list.html> ->
```python
{% extends 'fscohort/base.html' %}

{% block content %}

<h2>Student List</h2>

<ul>

{% for student in students %}

<a href="{% url 'detail' student.id%}" target="_blank"><li>{{student}}</li></a>

{% endfor %}

</ul>

<a href="{% url 'add'%}">ADD</a>

<br><br><br>

<hr>
{% for student in page_obj %}
    {# Each "contact" is a Contact model object. #}
    {{ student.full_name|upper }}
{% endfor %}

<div class="pagination">
    <span class="step-links">
        {% if page_obj.has_previous %}
            <a href="?page=1">&laquo; first</a>
            <a href="?page={{ page_obj.previous_page_number }}">previous</a>
        {% endif %}

        <span class="current">
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
        </span>

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">next</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
    </span>
</div>
<hr>
    
{% endblock content %}

```









### Postgresql bağlama

settings.py da default olarak db sqlite3 kullanıyoruz.


Önce pgadmin açıyoruz.

PostgreSQL14 -> Database sağ tık -> Create -> Database tık -> Database e todo yazıyoruz, Owner postgres olarak bırakıyoruz, save ediyoruz burada.

Sonra VSCode server ı durdurup <psycopg2> paketimizi kuracağız.

<terminal>
```bash
$ py -m pip install psycopg2
```

<settigs.py> da INSTALLED_APPS e ekliyoruz, db kısmında değişiklik yapıyoruz. ->

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'fscohort',
    # 3rd party apps
    'psycopg2',
]

```



DATABASES i yoruma alıyoruz ve yerine şunu yazıyoruz; ->



```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todo', #db properties den
        'USER': 'postgres', #db properties den
        'PASSWORD': 'umitumit', # postgresql password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```


save edip server ı tekrar ayağa kaldırıyoruz.

<terminal>
```bash
$ py manage.py runserver
```


server ı durduruyoruz, terminalde  <Ctrl + C> ile, ardından settings de değişiklik yaptığımız için migrate yapıyor ve server ı çalıştırıyoruz.



<terminal> ->

```bash
$ py manage.py migrate
$ py manage.py runserver
```



Artık db yi değiştirdik. Bizim listemiz artık boş, çünkü liste öteki db de kaldı. Ama ekleyebiliyoruz. Ekledik ve pgadmine gidip bakıyoruz. todo db sinin altında Schemas ın altında Tables ın içinde fscohort_student ın altında (fscohort_student ın üzerine sağ tıklayıp View/Edit Data -> All Rows diyoruz ->) Tablomuzu görüyoruz.



### Custom Validation

<forms.py> a gidiyoruz. 

Modelimizde number = ... IntegerField ımız vardı. (Aslında yok o yüzden önce modelimizdeki number field ını integer a çaviriyoruz.)

<models.py> ->

```python

from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    GENDER = {
        ('1', 'Female'),
        ('2', 'Male'),
        ('3', 'Other'),
        ('4', 'Prefer Not Say'),
    }
    gender = models.CharField(max_length=50, choices=GENDER)
    """ gender için dropdown menü yapıyoruz. """
    # number = models.CharField(max_length=50)
    number = models.IntegerField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='student/', default='avatar.png')
    
    def __str__(self):
        return f'{self.number} - {self.first_name}'
    
    class Meta:
        ordering = ['-id']

```



 Ve biz bu öğrenci numaralarına belirli bir limit koymak istiyoruz; 1000 ile 10000 arasında olsun gibi. Bunu için custom validation yazmamız lazım. Bu formlarda yapılan bir işlem. views.py da form.is_valid dediğimiz zaman formlarda yazdıklarımızı karşılıyor mu karşılamıyor mu ona bakıyor. Biz custom bir validation yazabiliriz; diyebiliriz ki student in numarası 1000-10000 arasında olsun. Onu nerede yapabiliriz? form.is_valid dediğimiz için <forms.py> da yapıyoruz. 
Şöyle; StudentForm class ımın içinde, fonksiyonumuz clean ile başlıyor <def clean_number():> sonra hangi attribute u kontrol yapacaksam onu yazıyoruz. ->

<forms.py> ->

```python

from django import forms
from .models import Student
from django.forms import fields
from django.core.exceptions import ValidationError

class StudentForm(forms.ModelForm):
    def clean_number(self):
        number = self.cleaned_data['number']
        if not(1000 < number < 10000):
            raise ValidationError('Student number should be in between 1000 and 10000')
        return number
        
    class Meta:
        model = Student
        fields = '__all__'


```
Bir formun içerisinden specific bir veriyi çekerken <self.cleaned_data['number']> şeklinde kullanmamız lazım. cleaned_data içerisinden number ı aldık.
if not(1000 < number < 10000): ise hata ver diycez onun için bir kütüphane import etmemiz lazım -> <from django.core.exceptions import ValidationError> hatayı bununla vereceğiz, ValidationError hatası göndereceğiz.








### Data Base şifresi gizleme (add to .env file)

<.env> ->

```python

SECRET_KEY = django-insecure-c=^dr@v1()kprvr1j9_)msgdea7#$nc03i2xmt*x5l^!3*a&c7
DB_PASSWORD = umitumit

```


<setting.py> ->

```python

"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'fscohort',
    # 3rd party apps
    'psycopg2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todo', #db properties den
        'USER': 'postgres', #db properties den
        # 'PASSWORD': 'umitumit', # postgresql password
        'PASSWORD': config('DB_PASSWORD'), # postgresql password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


```
