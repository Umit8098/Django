
project name : authenticate
application name : user_example

settings.py contents : 
   loaded decouple
   SECRET_KEY is hidden
   INSTALLED_APPS in user_example.apps.UserExampleConfig (app in uzun şekilde yazılmış hali bu, sadece user_example da yeterli oluyor son versiyonlarında.)
   LOGIN_REDIRECT_URL = '/'  en alt satırda da bu kod var.Login olmuş bir kullanıcıyı nereye göndermek istediğimizi belirtiyoruz bu yolla.

settings.py contents : 
   include ile eklenen url ler iki tane. 
       path('', include("user_example.urls")),
       path('accounts/', include('django.contrib.auth.urls'))


app imizin içindeki ->

urls.py ->
    path('special/', special, name='special'),
    path('register/', register, name='register'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"), name="password_change")


views.py ->
    ders  sırasında incelenecek.


### start
- Create virtual environment as a best practice:

```py
python -m venv env # for Windows
py -m venv env # for Windows
```
- Activate scripts:
```bash
.\env\Scripts\activate  # for Windows
```

- requirements.txt içeriğini yükleme:
```bash
pip install -r requirements.txt # requirements.txt içeriğini yükleme
py -m pip install --upgrade pip # upgrade to pip
```

settings.py da SECRET_KEY imiz olmadığı için proje çalışmaz. proje klasörünün seviyesinde .env file oluşturup, içerisine bir secret_key yazıyoruz. google dan secret key generator django diyoruz, https://djecrety.ir/ dan secter key generate edip .env içerisine SECRET_KEY=!!!l%42ic@nrya1j#g_7e%y$(b$yb78x^dey^a(omoqk!6g-&z  şeklinde tırnaksız olarak kaydediyoruz.

- go to terminal
```bash
py manage.py runserver
```

```bash
py manage.py migrate
```

```bash
py manage.py runserver
```

### Core

şimdiye kadar environment oluşturup active ettik, requirements.txt içeriğini kurduk, secret key oluşturduk ve .env içerisine kaydettik.

Hangi kullanıcının, hangi seviyede bizim web sitemizde etkileşime gireceğini biz bu sistem sayesinde belirliyoruz.

The primary attributes of the default user are:
default user object in temel attributes leri 

- username
- password
- email
- first_name
- last_name

### Django Authentication System

Django içerisinde Authentication ile ilgili olan iki kısım var, INSTALLED_APPS ve MIDDLEWARE

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', # Burası
    'django.contrib.contenttypes',  # Burası
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_example.apps.UserExampleConfig',
]
```

```py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # Burası kullanıcının aynı session da kalması, sayfayı kapatsa bile tekrar sayd-fayı açtığında yine login olduğu haliyle sayfaya girebilmesi
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Burası kullanıcıların requestlerini takip eden
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```


# Login Admin Site

Önce superuser oluşturuyoruz.

```py
python manage.py createsuperuser  # or with the parameters
python manage.py createsuperuser --username admin --email admin@mail.com
```


```py
py manage.py runserver
```

go to admin page

Yeni bir grup oluşturacağız. Groups un yanındaki +add e tıklayıp grup ismi verip yetkilendirmesini yapabiliyoruz. 









