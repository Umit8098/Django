#### Model-View-Template

##### Model -> 
Backend demek yarısı db demek, verini saklanması, işlenmesi, ihtiyaç sahiplerine, talep edenlere gönderilmesi... bir db var ve onun içinde de tablolar var... öğrenci tablosu, öğretmen tablosu, okul tablosu... modeller o tablolara karşılık geliyor. Djangoya db işlemlerini ORM (Object Relational Mapping) sayesinde yaptırıyoruz. Arka planda hangi db çalışıyor bizi ilgilendirmiyor. Bizim yerimize ORM dönüşüm işlemlerini (bizim yazdığımız komutların db karşılıklarını) yapıyor. Biz sadece ORM komutlarını kullanarak db işlemlerinden kurtulmuş oluyoruz. Çünkü db işlemleri farklılık gösterebiliyor.

##### View -> 
Logic işlemlerini yapıldığı yerdir. Bize bir request geliyor, biz o requeste hangi görüntü ile cevap vereceksek onun için view kullanıyoruz.Mesela login page geldi, bizim sayfamız geldi /login koydu biz ona login ile ilgili view i gösteriyoruz. View' e biz bir request teslim ediyoruz, view bu request' i işliyor, gerekirse db işlemleri yaptırıyor sonra işlemi bittikten sonra bir response' la karşı tarafa geri dönüyor.

##### Template -> 
Render edilmek için kullanılan, karşı tarafa gönderilen/görünen görüntü. User a göstereceğimiz arayüzlerdir.)

### Forms
Bir kullanıcıdan veri almak için form kullanıyoruz. Formların djangoda özel bir yeri var.

- HTML Forms
- Django Forms

##### Form Class : 1.tip -> 
Modelde olduğu gibi Form tanımlıyoruz. Ama biraz zahmetli :
```python
from django import Forms

class StudentForm(forms.Form)
    first_name = forms.CharField(max_length=100, label="Your Name")
    last_name = forms.CharField(max_length=100, label="Your Surname")
    number = forms.IntegerField(required=False)
```


##### Model Forms : 2.tip -> 
Django diyor ki madem sen db kullanıyorsun, db de aslında bizim ihtiyaç duyduğumuz veriler zaten var, bu işi bana bırak senin yerine halledeyim işlerini kolaylaştırayım. O zaman şu modeli kullanman lazım : (önce Student modelini import ediyoruz, inner class olarak class Meta ile "sen formsun form olarak da bu Student modelindeki field ları kullan" diyoruz, bu fieldlardan da hangilerini kullanmak istediğimizi de seçebiliyoruz.)
```python
from django import Forms
from .models import Student

class StudentForm(forms.ModelForm)
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "number"]
```

)


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

(şimdi bakalım django muz kurulmuş mu, versionumuz neymiş)
$ django-admin --version


# create project
(şimdi proje oluşturuyoruz. boşluk nokta ile oluşturursak iç içe dosya oluşturmaz.)

$ django-admin startproject forms .
```


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

- go to terminal, stop project, add app

(terminale gidip durduruyoruz ve bi app <student> oluşturuyoruz.)

```bash
$ py manage.py startapp student
```

- go to settings.py and add 'student' app to installed apps and add below lines

(<settings.py> dosyasına gidip app kısmına ekliyoruz.)

(Yine bugün biz media işlemleri yapacağımız için aşağıdaki code ları da <settings.py> dosyasının en altına (import olanı import bölümüne) ekliyoruz.)

```python
import os
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

- create these folders at project level as /media/profile_pics

(Proje dosyasıyla aynı seviyede /media/profile_pics klasörlerini oluşturuyoruz.(media ları burada tutacağız.))


- go to student/models.py

(student app inin altındaki <models.py> dosyasına gidip aşağıdaki code ları yapıştırıyoruz. (Student isminde bir model oluşturuyoruz, daha önce görmüştük. Bu modelde ImageField da kullandığımız için media/profile_pics dosyasını oluşturup upload ı buraya verdik. blanc=True ile de resim yüklemeyi mecbur kılmadık. ) )

```python
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

```


- go to terminal

(Burada dosya, upload işlemleri yapacağımız için terminale gidip pillow kütüphanesini kurmamız gerekiyor.(pillow: dosya yükleme işlemlerini yapabilmemizi sağlayan bir kütüphane.)
Alışkanlık edinmemiz gerekli -> Herhengi bir kütüphane indirdiğimiz zaman bunu requirements.txt'e eklememiz lazım. )

(Ardından bir model oluşturduğumuz için < makemigrations > (django, oluşturduğumuz modeli db de oluşturmak için hazırlık yapıyor.) ve < migrate > (migrations ile yaptığı hazırlıkları db de işliyor.) komutlarını kullanmalıyız. Bir model oluşturduğumuz ya da modelde değişiklik yaptığımız zaman ilk yapacağımız iş bu komutları kullanmak.)

```bash
$ pip install pillow
$ pip freeze > requirements.txt
$ py manage.py makemigrations
$ py manage.py migrate
```

(Artık templates lerimize geliyoruz...)

- create templates folder as student/templates/student
- create static folder as student/static/css

(student app klasörünün içine <templates> onun da içine app imizin ismi olan <student> kalsörlerini "/templates/student" oluşturup, bu <student> klasörünün içine de template lerimizi <base.html , ###.html, ###.html> oluşturuyoruz. Buradaki base html de ya shift+ünlem e basıp kendimiz şu code lara dikkat ederek -> html tag ının hemen üzerinde "{% load static %}" ve body nin içindeki "{% block container %}{% endblock container %}" code' larına dikkat ederek bir html oluşturabiliriz veya aşağıdaki kodları kullanabiliriz.
Her seferinde bir html template i yazmaktansa bir tane şablon base.html oluşturup diğer template lerde ilgili kısmı modifiye etme mantığı geliştirilmiş. )

(Tabi bir de app kalsörümüz olan <student> kalsörünün içine <static> klasörü tanımladık, onun içine <css> klasörü ve onun da altına <style.css> dosyası "/static/css/style.css" oluşturduk. Bunları kullanabilmek için de şablon template imiz olan base.html sayfasının en başına html tag ının da üzerine {% load static %} yazıyoruz. Ayrıca css için link verirken href attribute üne {% static 'css/style.css' %} kodunu yazıyoruz, dikkat! )


- base.html

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- <link rel="stylesheet" href="../static/css/style.css" /> -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}" />
  </head>
  <body>
    {% block container %}{% endblock container %}
  </body>
</html>
```

(templates' in altındaki student' ın altına <index.html> oluşturuyoruz. "{% extends "student/base.html" %} {% block container %}" ve  "{% endblock container %}" code' larına dikkat et. )


- index.html

```html
{% extends "student/base.html" %} {% block container %}
<h1>Home Page</h1>

<h3>Student App</h3>

{% endblock container %}
```

(templates' in altındaki student' ın altına <student.html> oluştur. "{% extends "student/base.html" %} {% block container %}" ve  "{% endblock container %}" code' larına dikkat et. (Burada bir form tanımlı.) )

- student.html

```html
{% extends "student/base.html" %} {% block container %}
<h2>Student Form</h2>
<form action="">
  <label for="">student name</label>
  <input type="text" />
  <input type="submit" value="OK" />
</form>
{% endblock container %}
```

(Şimdi template lerimiz hazır. Bunları gösterebilmek için nerede yazmamız lazım bunları render edecek birmekanizma kurmamız lazım? views da yapıyoruz bu logic işlemi.)

- go to student/views.py

(student app i nin içindeki views.py dosyasına gidip logic işlemlerini yapıyoruz. Diyoruz ki index view çağırıldığı zaman sen git <student/index.html> template ini render et. Yani bunu kullanıcının anlayabileceği hale getir. Yine student_page view i çağırıldığı zaman diyoruz ki sen git <student/student.html> templat ini render et.)

```python
from django.shortcuts import render

def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    return render(request,'student/student.html')

```

(View de işlemlerimizi yaptık. Şimdi biz ne demiştik ilk bana bir request geldiği zaman ilk olarak project in içindeki <urls.py> a bakıyor. Default olarak bize admin.site patterni geliyor. Biz buraya kendi yazdığımız view leri import edip ekliyoruz.)

(student ın altındaki views den index template ini import ediyoruz <from student.views import index> , bana url olarak hiçbirşey yazmadan gelirse git bu bu path i, index view i çalıştır <path('', index, name='index')> , sonra bana kolaylık olsun diye buna bir isim verebilirim <name='index'> diye.)

(Bir de diyorum ki <student> url  i ile gelenleri de, include komutu ile (tabi includ u import ederek) artık ben sana view göstermeyeceğim, sen git artık bu view leri app im olan student url i içerisinde ara <path('student/', include('student.urls'))> .  Bunu neden yapıyoruz, istersek burada hepsini index te olduğu gibi burda yazabilirdik, ama bizim app imiz büyük bir app olabilir, birkaç tane app olabilir bunların hepsini burada alt alta yazmak sıkıntı olabilir, karmaşaya sebep olabilir. Djando diyor ki az sayıda view ın varsa direkt buraya view in ismini yazıp kullanıcıya gösterebilirsin. Veya çok sayıda app imiz ve çok sayıda view imiz var o zamanda ben ilgili view leri, ilgili app lerin içlerindeki urls.py lara havale ederek sadeliği sağlıyoruz.)

- go to forms/urls.py

```python
from django.contrib import admin
from django.urls import path, include

from student.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('student/', include('student.urls')),
]
```

(Yukarıda include ile <student.urls> e atıf yaptığımız için student app in içerisinde <urls.py> dosyası oluşturuyoruz. Bunu neden yapıyoruz birçok app oluşturabiliriz, her app in içerisinde bir çok template olabilir, her template projenin altındaki urls den değil de ilgili app in altındaki urls den çağırılsın diye yapıyoruz.)

(student app' inin altına <urls.py> oluşturup project in altındaki urls den kopya çekerek içeriğini oluşturuyoruz. önce <from django.urls import path><from .views import student_page> ile importlarımızı yapıyoruz, sonra proje urls ine gelen <student> ile buraya yani app imizin içindeki urls e kadar gelen student in arkasından birşey gelmez ise <student_page> view ini çalıştır, bize kolaylık olsun diye de ismini student olarak değiştir diyoruz. )

- go to student/urls.py

```python
from django.urls import path

from .views import student_page

urlpatterns = [
    path('', student_page, name='student'),
]
```
- run server and see urls (boş url ve /student/ url ' lerini)

- then -> (sonra ->)

(Django bize ne diyordu formu ya sen kendin sıfırdan yap, yada bana bırak ben sana bir modeli aracı olarak kulanarak yardımcı olayım. Şuana kadar formu biz kendimiz yaptık. Nerede yapmıştık <student.html> içerisinde bir form oluşturduk. Şimdi django formlarda oluşturacağız. Bunun için student app inin içerisine <forms.py> diye bir dosya oluşturuyoruz. Bunun içerisine de aşağıdaki bazıları bilindik code ları yazıyoruz. django dan forms ları import ediyoruz <from django import forms> , <!-- <models.py> dan "Student" modelimizi import ediyoruz. --> "StudentForm" class ı oluşturuyoruz. )

- run server and explain urls and form.html

- go to students/forms.py

```python
from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    number = forms.IntegerField(required=False)
```


(views.py a gidip <forms.py> dan StudentForm u import ediyoruz <from .forms import StudentForm> , student_page view ini aşağıdaki code ile değiştiriyoruz , student_page view ini yeniliyoruz; bir context oluşturuyoruz; <forms.py> içerisinde tanımlamış olduğumuz StudentForm class ını <views.py> da import edip, student_page view inde "form" isminde bir instance oluşturduk. Bu yeni oluşturduğumuz boş instance ı , boş elemanı, boş formu context içerisinde <student.html> template ine gönderdik.  )

- go to student/views.py and amend student_page

```python
from .forms import StudentForm

def student_page(request):
    	form = StudentForm()
    	context = {
        	'form': form
    	}
    return render(request,'student/student.html', context)
```


(Sonra student.html template inde de değişiklik yapmamız lazım. Template e diyoruz ki; Sen burada sana form diye gönderilen şeyi render et ( {{ form.as_p }} .as_p ile form elementlerinin arasına p elementi koyuyor. içeride sadece form yazarsak form içerisindeki elementeri yanyana yazar. ). Burada {% csrf_token %} kısmı önemli; eğer siz bir post işlemi yapıyorsanız bakın burada method a post dedik, csrf_token kullanmazsanız django size hata verir. Bu güvelikle ilgili bir işlem, hacklemeleri önlemek için kullanılıyor. ) (Birazdan file upload işlemi yapıcaz onun için form tag inin içerisine şunu <enctype="multipart/form-data"> yazmamız lazım.) 

- explain sending form
- 
(gönderme formunu açıkla)

- go to student/templates/student/student.html and amend below lines

```html
{% extends "student/base.html" %} {% block container %}

{% comment %}
<h2>Student Form</h2>
<form action="">
  <label for="">student name</label>
  <input type="text" />
  <input type="submit" value="OK" />
</form>
{% endcomment %}

<h2>Student Form</h2>

<form action="" method="post" enctype="multipart/form-data">
  {% csrf_token %} {{ form.as_p }}
  <input type="submit" value="OK" />
</form>

{% endblock container %}
```

- explain get, post, enctype and CSRF

(get, post, enctype ve csrf_token ' ı açıkla)


url e enter yapınca veya student sayfasına git diyince requestimiz GET olarak student/views.py'a gidiyor. Ancak arayüzde formun içini doldurup OK butonuna bastığımızda requestimiz <student/views.py> 'a post olarak gidecek. Ama biz burda GET POST ayrımı yapmıyorduk. Şimdi o işlemleri yapacağız.


**********************************************************************************************
ŞURAYA ATLA
**********************************************************************************************


Django bize iki tane opsiyon sunuyor ya sen herşeyi sıfırdan yazarsın ki biz şu ana kadar öyle yaptık, ya da bir modeli aracı olarak kulanırsın ben sana yardımcı olurum. Mesela bizim <models.py> ımız var, first_name, last_name, numbers ı tanımlamışız modelimizde. <forms.py> da birdaha tanımlamışız. django diyorki bu işi iki defa tekrar etme onun yerine ModelForm kullan. aşağıdaki code ları alıp <forms.py> dosyasına ekliyoruz, öncekileri comment yapıyoruz. Artık diyoruz ki daha önce StudentForm umuzu forms.Form dan türetmiştik, şimdi forms.ModelForm dan türetiyoruz. 

- go to student/forms.py and amend StudentForm and use forms.ModelForm class

```python
from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "number", "profile_pic"]
        # fields = "__all__"
        # exclude ... gelmesini istemediklerimiz
        labels = {"first_name": "Name"}
```

(diyoruz ki class Meta, model olarak student/models.py daki Student modelini kullan, Bu modelin içinden hangi fieldları kullanacaksak onları yazıyoruz, ya da fields = "__all__" ile hepsini kullanabiliyoruz. Hatta <<labels = {"first_name": "Name"}>> ile <<first_name>> i <<Name>> olarak kullan da diyebiliyoruz. save ettikten sonra artık biz form tanımlamadığımız halde modelimizi kullanarak bir form oluşturduk. Yani modelimiz bu kardeşim sen bize bu modelden bir form oluştur dedik sağolsun oluşturdu bize. Oldukça pratik bir yöntem baştan form dizayn etmiyoruz, fieldları söylüyoruz,)


##### Formdan gelen veriyi db e işlemek (formumuzu modelden türettiğimiz zaman kullanılacak kod)->

url e enter yapınca veya student sayfasına git diyince requestimiz GET olarak student/views.py'a gidiyor. Ancak arayüzde formun içini doldurup OK butonuna bastığımızda requestimiz <student/views.py> 'a post olarak gidecek. Ama biz burda GET POST ayrımı yapmıyorduk. Şimdi o işlemleri yapacağız.

Artık gelen verileri db ye yazmak için gerekli işlemleri yapıyoruz. Gelen veri önce <student.view.py> geliyor ya formdan gelen veriler POST olarak geliyor bize ve bizim be POST işlemini handle etmemiz lazım;
if condition method ile; eğer request method POST ise
boş bir formu, StudentForm içinde POST requstiyle gelen bilgilerle doldur.
Boş bir formun içini POST requstiyle gelen veri ile doldurduktan sonra ilk işlemimiz validasyon yapmak; 
  eğer form valid ise
    form.save()   ile formu save ederiz. Django direkt db ye save ediyor.
    (Alternatif save yöntemi de aşağıdaki gibi student_data= .. first_name.... cleaned_data önemli burada.....)

Biz burada bir de dosya (image.field) göndermiştik o dosya request.POST un içerisinde gelmiyor, request.FILES içerisinde geliyor onu da buraya ekliyoruz.

<!-- <student.models.py> dan <Student> modelimizi de import etmemiz lazım. -->

Form save işlemleri başarılı bir şekilde gerçekleşti, bizim artık bunu tekrar gets pozisyonuna sokmamız lazım. Bunun için <return.redirect('student')> yapmamız lazım (redirect i import etmemiz de lazım) çünkü POST tan kurtarıp GET e sokmamız lazım.

```python
from django.shortcuts import render, redirect
```

form = StudentForm() kısmını if in hemen üzerine alıyoruz ki GET işlemini karşılayabilelim.


- go to student/views.py and amend student_page


(form.save() yöntemi -> : Biz formu ModelForm dan türettik, modelden türettiğimiz için bu şekilde save yapabiliyoruz. )

navigate to admin panel and show student model there and display recorded students
(yönetici paneline gidin ve orada öğrenci modelini gösterin ve kayıtlı öğrencileri görüntüleyin)

- go to student/views.py and amend student_page

(Student/views.py'ye gidin ve Student_page'i değiştirin)


```python
def student_page(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student')
    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)
```



*********************************************************************************
BURAYA ATLA
*********************************************************************************


##### Formdan gelen veriyi db ya işlemek (formumuzu modelden türetmediğimiz zaman kullanılacak kod) ->

<student.views.py> dosyasına gidip <student_page> view inde aşağıdaki değişiklileri yapmalıyız.

<student.models.py> dan <Student> modelimizi de import etmemiz lazım.

```
from .models import Student
```

(Alternatif save yöntemi -> : formumuzu modelden türetmediğimiz zaman kendimiz oluşturduğumuzda bu şekilde save edebiliriz. )

Form save işlemleri başarılı bir şekilde gerçekleşti, bizim artık bunu tekrar gets pozisyonuna sokmamız lazım. Bunun için <return.redirect('student')> yapmamız lazım (redirect i import etmemiz de lazım) çünkü POST tan kurtarıp GET e sokmamız lazım.

```python
from django.shortcuts import render, redirect
```


```python
def student_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student_data = {
                "first_name": form.cleaned_data.get('first_name'),
                "last_name": form.cleaned_data.get('last_name'),
                "number": form.cleaned_data.get('number'),
                # "profile_pic": form.cleaned_data.get('profile_pic'),
            }
            # database save process
            # student = Student(first_name=student_name, last_name=student_surname, number=student_number, mentor=student_mentor)
            student = Student(**student_data)
            if 'profile_pic' in request.FILES:
                student.profile_pic = request.FILES['profile_pic']
            student.save()
            return redirect('student')

    form = StudentForm()
    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)
```


explain POST, and how to save student

- go to terminal

(Terminale git, superuser oluştur ->)

```bash
py manage.py createsuperuser
```

navigate to admin panel and show that student model does not exist

- go to student/admin.py

(admin dashboard a Student modelimizi ekleyelim.)

```python
from django.contrib import admin

from .models import Student
# Register your models here.
admin.site.register(Student)
```



### BOOTSTRAP

go to student/templates/student/base.html and add bootstrap
(base.html e gidip bootstrap eklemek ->)

Bootstrap sitesinden aldığımız Bootstrap css linkini ve body nin bitiminden hemen önce de JavaScript src kodlarını ekliyoruz. ekliyoruz


```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- <link rel="stylesheet" href="../static/css/style.css" /> -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}" />
    <!-- CSS only Bootstrap-->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
      crossorigin="anonymous"
    />
  </head>

  <body>
    <div style="margin-top: 100px; margin-bottom: 100px" class="container">
      {% block container %}{% endblock container %}
    </div>
    <!-- JavaScript Bundle with Popper for bootstrap -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```
.
.
- uygulandığını görüyoruz. (index.html yani '' sayfasında ve student.html yani '/student/' sayfasında)


### CRISPY FORMS

(djangoya has templatelerimizi güzelleştiren bir yapı, application. Burada formları düzenleme için kullanılıyoruz. Bu paketi yüklüyoruz.)

- go to terminal
(terminale gidip, çalışan terminali durdurup crispy app ini yüklüyoruz.)

```bash
pip install django-crispy-forms
pip freeze > requirements.txt
```

- go to settings.py

(yeni bir app kurunca yaptığımızı tekrar ediyoruz, settings e gidip app imizi ekliyoruz, ayrıca settings in sonuna da şu kodu eklememiz gerekiyor. )

```python
INSTALLED_APPS = (
    ...
    # 3rd party packages
    'crispy_forms',
)

CRISPY_TEMPLATE_PACK = 'bootstrap4'  (settings' in en sonuna)
```


- go to student/templates/student/student.html and crispy tags

<student.html> gidip form tagından önce bu kodu -> 
{% load crispy_forms_tags %} 

arkasından  daha önce form.as_p diye kullandığımız kısmı silip ya da yoruma alıp  {# ..yorum..  #} ->
{{ form | crispy}} 
yapıyoruz,


```django
({% load crispy_forms_tags %}
{{ form | crispy}})
```


Formumuzu aşağıda olduğu gibi div içine alıp <style="margin-left: 20px; width: 30%;">  ve de input tag ına da <style="margin-top: 10px;">  verebiliyoruz. 

```html
{% extends "student/base.html" %} {% block container %}

<h2>Student Form</h2>

{% comment %}
<form action="">
  <label for="">student name</label>
  <input type="text" />
  <input type="submit" value="OK" />
</form>
{% endcomment %}

<div style="margin-left: 20px; width: 30%;">
<h2>Student Form</h2>
{% load crispy_forms_tags %}
<form action="" method="post" enctype="multipart/form-data">
  {% csrf_token %} {% comment %} {{ form.as_p }} {% endcomment %} {{ form | crispy}}
  <input style="margin-top: 10px;" type="submit" value="OK" />
</form>
</div>
{% endblock container %}
```



### Messages

(Save işlemlerimizi yaptığımız zaman ekrana birtakım mesajlar çıkmasını istiyorsak, o zaman djangonun messages paketini kullanmamız lazım. Mesela "save successfully" gibi messages lar çıkarmak istiyoruz.)

- go to student/views.py and import messages end send success message

(<student/views.py> a gidiyoruz, önce messages' ı import ediyoruz <from django.contrib import messages>. Sonra success mesajı gönderiyoruz, ilgili yere yani save komutunun hemen altına <messages.success(request, 'Student added successfully')> yazıyoruz. Bunu nereye gönderiyoruz templates e (base.html) gönderiyoruz arka planda ve templates de işlem yapmamız gerekiyor.)

```python
from django.contrib import messages

def student_form(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully")
            return redirect('/student/')
    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)
```


- go to student/templates/student/base.html and add messages codes

( base html e gidiyoruz,  body kısmına block tan önce if endif codelarını yazıyoruz. bootstrap ta error diye bir mesaj yok, bu yüzden onu danger olarak yazıyoruz, diğerlerini tag ı neyse onu yazıyoruz, burada success diye bir mesaj olduğu için alert alert-{{ message.tags }} diye gönderebiliyoruz.)

(dikkat burada da div içine alıp style vermişiz, bunlarla da değişiklikler yapabiliriz.)

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- <link rel="stylesheet" href="../static/css/style.css" /> -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}" />
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>

<body>
    <div style="margin-top: 10px; margin-bottom: 10px" class="container">
        {% if messages %}
        {% for message in messages %}
        {% if message.tags == "error" %}
        <div class="alert alert-danger">{{ message }}</div>
        {% else %}
        <div class="alert alert-{{ message.tags }}">{{ message }}</div>
        {% endif %}
        {% endfor %}
        {% endif %}
        {% block container %}{% endblock container %}
    </div>
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous">
    </script>
    <script src="{% static 'student/js/timeout.js' %}"></script>
</body>

</html>
```
