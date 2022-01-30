
Repo
Crud
Postgr.
Decouple .env

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
(Burada dosya, upload işlemleri yapacağımız için terminale gidip pillow kütüphanesini kurmamız gerekiyor.(pillow: dosya yükleme işlemlerini yapabilmemizi sağlayan bir kütüphane.)

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

(fscohort app inin altındaki <models.py> dosyasına gidip "Student" isminde bir model oluşturuyoruz, daha önce görmüştük. Bu modelde ImageField da kullandığımız için proje ve app klasörleriyle aynı seviyede media klasörü oluşturup içine de student klaörü oluşturuyoruz ki yüklenen medyalar düzenli olsun. media/student kalsörlerini iç içe oluşturup upload ı buraya verdik. Bir de option daha veriyoruz, eğer resim yüklenmezse default olarak bir avatar yüklensin, avatar resmini de media kalsörünün içine koyduk. (blanc=True dersek de resim yüklemeyi mecbur tutmayız. ) )

```python
from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
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

(Bir model oluşturduğumuz için < makemigrations > (django, oluşturduğumuz modeli db de oluşturmak için hazırlık yapıyor.) ve < migrate > (migrations ile yaptığı hazırlıkları db de işliyor.) komutlarını kullanmalıyız. Bir model oluşturduğumuz ya da modelde değişiklik yaptığımız zaman ilk yapacağımız iş bu komutları kullanmak.)

```bash
$ py manage.py makemigrations
$ py manage.py migrate
```


- go to fscohort/admin.py and add to our model.

(fscohort/admin.py dosyasına gidip modelimizi import edip ekliyoruz.)

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

proje <urls.py> ına gidip, fscohort app inin <urls.py> ını "include" ediyoruz ->

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fscohort.urls')),
]

```


fscohort app inde bir <urls.py> dosyası oluşturup ve içine app imizin <views.py> ında oluşturduğumuz home view ini import edip aşağıdaki kodları yazıyoruz.->

fscoghort <urls.py> ->

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```


fscohort app inin <views.py> dosyasında django.http den HttpResponse u import et, ve home view ini oluştur.->

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
    students = Student.objects.all() <!-- (SELECT * FROM) ile aynı db deki hepsini getir. -->
    context = {
        'students' : students
    }
    return render(request, 'fscohort/student_list.html', context) <!-- student_list.html template i oluştur, urls.py dan adresle -->

def student_add(request):  <!-- db ye veri ekliyeceğiz,Bunun için form kullanıyoruz, form oluşturacağız, aşağıya bak! -->
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
    <!-- student_detail.html de resimlerin görünmesi için projenin urls.py ında değişiklik yapılmalı, aşağıya bak! -->


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


def student_delete(request, pk):
    pass
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
<student_add.html> template i oluştur ->

```python
{% extends 'fscohort/base.html' %}

{% block content %}

<h2>Student Add</h2>

<form action='' method='POST' enctype='multipart/form-data'>

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
<div> <img scr='{{student.image.url}}' alt=''> </div>
<div> {{ student.first_name}} </div>
<div> {{ student.last_name}} </div>
<div> {{ student.number}} </div>
<div> {{ student.email}} </div>
<div> {{ student.phone}} </div>
<div> {{ student.gender}} </div>

{% endblock content %}

```


<student_detail.html> template inin <urls.py> da adreslenmesi ->

```python
from django.urls import path
from .views import home, student_list, student_add, student_detail

urlpatterns = [
    path('', home, name='home'),
    path('student_list/', student_list, name='list'),
    path('student_add/', student_add, name='add'),
    path('detail/<int:id>/', student_detail, name='detail'),
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

{% csrf_token %} {{form.as_p}}

<input type='submit' value='Update'>

</form>

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
    path('detail/<int:id>/', student_detail, name='detail'),
    path('update/<int:id>/', student_update, name='update'),
]

```


<student_update.html> template ine gitmesi için <student_detail.html> template inden link veriyoruz ->

<student_detail.html> template i aşağıdaki gibi oluyor artık ->

```python
{% extends 'fscohort/base.html' %}

{% block content %}

<h2>Student Detail</h2>
<div> <img scr='{{student.image.url}}' alt=''> </div>
<div> {{ student.first_name}} </div>
<div> {{ student.last_name}} </div>
<div> {{ student.number}} </div>
<div> {{ student.email}} </div>
<div> {{ student.phone}} </div>
<div> {{ student.gender}} </div>
<div><a href="{% url 'update' student.id %}">Edit</a></div>

{% endblock content %}

```


