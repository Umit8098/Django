python --version
pip --version
py -m venv env
.\env\Scripts\activate
(deactivate)
pip install django
python -m pip install --upgrade pip  # optional -- upgrade pip version     (veya  py -m pip install --upgrade pip)
pip freeze

/////////////////////
pip freeze > requirements.txt
(pip install -r .\requirements.txt)
////////////////////

/// proje oluşturma ///

django-admin startproject main .


/// app oluşturma ///

py manage.py startapp store

settings.py da INSTALLED_APPS e ekle, 
proje klasörünün urls.py ine dahil et

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]
```

store un urls.py ına git dedik. Ancak store un urls.py ı yok onun için biz oluşturuyoruz, ve içerisine aşağıdaki kodları yazıyoruz.

```
from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
]
```

store un urls.py ının işaret ettiği home views ünü oluşturmamız lazım. Hemen store un urls.py ın içerisinde şimdilik "Welcome to Backend" döndürecek bir fonksiyon şeklinde view tanımlıyoruz .

```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Welcome to Backend')
```


py manage.py runserver        (localhost ta server çalışıyor.)

yeni bir powershell terminali açıp venv active edip yapmak istediklerimizi burda yapıyoruz.

(Eğer şimdi admin dashboard oluşturmak istiyorsak, önce <py manage.py migrate> komutunu çalıştırmalıyız. Çünkü default olarak gelen settings dosyasında değişiklikler yaptık. Bu değişiklikleri db ye işlemesini <migrate> komutuyla söylüyoruz. Eğer bir model oluşturup ondan sonrasında admin dashboard oluşturacaksak zaten model oluşturduktan sonra <py manage.py makemigrations> ve <py manage.py migrate> komutlarını çalıştıracağımız için bir sorun olmuyor. Arkasından <admin.py> dosyasına <models.py> dosyasında oluşturduğumuz app imizin modelini tanıtıyoruz zaten.  Model oluşturmadan admin dashboard oluşturmak istiyorsak önce  <py manage.py migrate> komutunu çalıştırıp admin dashboard u oluşturup sonra <models.py> da modeli oluşturup sonra <models.py> dan modelimizi import ederek <admin.site.register(modelimizin ismi)> şeklinde <admin.py> dosyasına tanıtıyoruz.)


/// model oluşturduk ///
(save etmeyi unutma!!! yoksa çalışmaz.)

app imizin içerisindeki models.py dosyasının içerisine modelimizi oluşturuyoruz.

```
from django.db import models

# Create your models here.

class Product(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return (f"{self.first_name} - {self.last_name}")

```

Tablo oluşturma işi bittikten sonra;

```
py manage.py makemigrations          veya
python manage.py makemigrations
```
arkasından,

/// database' e syncronize etmek için ///
```
py manage.py migrate            veya
python manage.py migrate
```
komutlarını çalıştırıyoruz ve tablomuz oluşuyor.


/// admin dashboard oluşturmak için ///

py manage.py createsuperuser        veya 
python manage.py createsuperuser

app imizin models.py ında oluşturduğumuz tabloları admin panalede görebilmek için admin.py içerisine ilgili kodları yazmalıyız.

```
from django.contrib import admin
from .models import Product

# Register your models here.

admin.site.register(Product)
```


git'e push etmeden önce .gitignore dosyası oluştur. venv'ın ismini ekle (burada "env/" oluyor.) 
