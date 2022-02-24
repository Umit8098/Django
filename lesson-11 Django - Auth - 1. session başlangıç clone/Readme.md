- Project Clone

project name : authenticate
application name : user_example

<settings.py> contents : 
   loaded decouple
   SECRET_KEY is hidden
   INSTALLED_APPS in user_example.apps.UserExampleConfig (app in uzun şekilde yazılmış hali bu, sadece user_example da yeterli oluyor son versiyonlarında.)
   LOGIN_REDIRECT_URL = '/'  en alt satırda da bu kod var.Login olmuş bir kullanıcıyı nereye göndermek istediğimizi belirtiyoruz bu yolla.

<urls.py> contents : 
   include ile eklenen url ler iki tane. 
       path('', include("user_example.urls")),
       path('accounts/', include('django.contrib.auth.urls'))
       # djangonun kendi default authentication kütüphanesini include ediyor.


app imizin içindeki ->

<urls.py> ->
    path('special/', special, name='special'),
    path('register/', register, name='register'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"), name="password_change")


<views.py> ->
    ders  sırasında incelenecek.


### start

- Create virtual environment as a best practice:
  (environment oluşturuyoruz.)

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

authentication system in temeli kullanıcılardan oluşuyor.Kullanıcı oluşturulması, login, logout, credential ların kaydedilmesi, kullanıcıların yetkilendirilmesi, ana konularıdır.

Hangi kullanıcının, hangi seviyede bizim web sitemizde etkileşime gireceğini biz bu sistem sayesinde belirliyoruz.

The primary attributes of the default user are:
default user object in temel attributes leri 

- username
- password
- email
- first_name
- last_name

### Django Authentication System
3.parti kullanımlara da açık, mesela OAuth var, ilerleyen sessions larda görülecek.
Django içerisinde Authentication ile ilgili olan iki kısım var, INSTALLED_APPS ve MIDDLEWARE

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', # Burası temel authentication paketi
    'django.contrib.contenttypes',  # Burası modelle permissions ları yetkilendirmeyi ayarlamak
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

Yeni bir grup oluşturacağız. Groups un yanındaki +add e tıklayıp grup ismi verip yetkilendirmesini yapabiliyoruz. Clarusway diye bir grup oluşturduk. auth | group |Can add group permission yetkilendirmesini yaptık.

Şimdi bir de user oluşturuyoruz. Halihazırda admin olarak girdiğimiz bir user var. User oluşturduk.


### The Django Authentication Models

Django.contrib.auth.models has 
- User, 
- Permission,
- Group Models,

Below you can see the class diagrams for User as well as Permission and Group.
(Aşağıda Kullanıcı, İzin ve Grup için sınıf diyagramlarını görebilirsiniz.)

![](DjangoAuthModels.png)



# Add users programmatically

Programatik olarak kullanıcı oluşturma. Programatik demek clı (commend line interface) kullanmak demek. clı kullanarak çeşitli komutlarla bu işlemleri yapmak demek. Bu birçok açıdan çok daha hızlı işlem yapmanızı sağlıyor.

go to terminal

serverı durduruyoruz.


## powershell deki dosya yolumuz nasıl kısaltılır?

google: shorten powershell prompt
https://stackoverflow.com/questions/42862604/powershell-shortened-the-directory-prompt-but-how-to-save-the-change

```bash
function prompt {'Code: '}
```
artık terminalde sadece Code: yazacak




Başlamadan önce dokümantasyona gidelim, bakalım ne diyor?

https://docs.djangoproject.com/en/3.2/topics/auth/default/


- Creating users

create user için  create_user() helper function u var, bu fonksiyon sayesinde user oluşturmak mümkün. django.contrib.auth.models in User object ini import ediyor, ve aşağıda fonksiyonu kullanıyor

```bash

>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
>>> user.last_name = 'Lennon'
>>> user.save()

```


Önce shell imizi açıyoruz, komut neydi?: ->

go to terminal

```bash
python manage.py shell
or
py manage.py shell
```

shell imiz geldi, shell imize yazıyoruz artık, ilk yapmamız gereken kütüphanemizi çağırmak django.contrib.auth.models içinden User modelimizi import ediyoruz..->

```py
from django.contrib.auth.models import User
```
import ettik, sonra ilk kullanıcımızı oluşturacağız. Bir kullanıcıya eşitleyeceğiz, user eşittir ile başlıyoruz ve buna yeni bir kullanıcı oluşturuyoruz. Şimdi bu kullanıcı oluşturuyor ve database e doğrudan kaydediyor, yani bu komuttan create_user() fonksiyonundan sonra .save() kullanmaya gerek yok. Bunun dışında üç tane parametre istiyor default olarak, create_user(username, email=None, password=None, **extra_fields) extra field ları sona bırakacağız.



```bash
python manage.py shell

from django.contrib.auth.models import User

# Create user and save to the database
# create_user(username, email=None, password=None, **extra_fields)
# Creates, saves and returns a User.
user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')
# The username and password are set as given. 
# The domain portion of email is automatically converted to lowercase, and the returned User object will have is_active set to True.
# If no password is provided, set_unusable_password() will be called.
# The extra_fields keyword arguments are passed through to the User’s __init__ method to allow setting arbitrary fields on a custom user model.
# Extra fields:
User.objects.create_user('john', email='lennon@thebeatles.com', password='johnpassword', is_staff=True)
# Or
user.is_staff=True 
user.save()

# Update fields and then save again
user.first_name = 'John'
user.last_name = 'Citizen'
user.save()
```

yeni kullanıcı oluşturuyoruz; ->
```py
user = User.objects.create_user('backteam', 'myemail@crazymail.com', 'mypassword')
```
çalıştırdık,

Şimdi başka bir terminal açıp runserver yapıp admin page imize gidip oluşturduğumuz user ı görüyoruz.

user a first name , last name tanımlamamıştık, şimdi onları tanımlayacağız. Oluşturduğumuz kullanıcıyı user' a atamıştık..
```py
user.first_name = 'John'
```
admin page de bir değişiklik olmadı, bunun sebebi bu şekilde additional olan parametreleri belirledikten sonra user.save() demek zorundayız. 
```py
user.save()
```
şimdi bakıyoruz admin page e eveet first name John olarak kaydetmiş.

user a last name ve stuff tanımlayacağız.
```py
user.last_name = 'Citizen'
user.save()
```

```py
user.is_staff = True
user.save()
```

- Bir user ın first_name, last_name ini değiştirme: ->

önce user ı bir değişkene atıyoruz,
```py
>>> user1 = User.objects.get(username='john') 
>>> user1
```

dönüşü:
```py
<User: john>
```

arkasından:
```py
>>> user1.first_name = 'John' 
>>> user1.save()
```




- Changing passwords - Password değiştirme

```py
>>> from django.contrib.auth.models import User
>>> u = User.objects.get(username='john')
>>> u.set_password('new password')
>>> u.save()
```

Bizim oluşturduğumuz user ın password ünü değiştiriyoruz. ->
```py
>>> user = User.objects.get(username='john')
>>> user.set_password('new password')
>>> user.save()
```

kullanıcının password ünü değiştirdik, username ini de değiştirelim: 
backteam olan username i John olarak değiştirdik, sonra tekrar değiştirdik. ->
```py
>>> user = User.objects.get(username='backteam')
>>> user.username = 'John'
>>> user.save()
```





- Deleting user - user silme, programatik olarak.

1. yöntem
```bsh
User.objects.get(username='umit').delete()
```


2. yöntem (Aktif statüsünü False yapmak)
Nasıl yapıyoruz? kütüphanemizi zaten çağırdık, 
```bash
User.objects.get(first_name='John')
```

enter a bastık bize; ->
```bash
<User: backteam>
```
verdi, tamam yakalamışız böylece istediğimiz user ın Active statüsünü False yapabiliriz nasıl? ; -> 


```bash
user2=User.objects.get(first_name='John')
user2.is_active=false
user2.save()
```

sonra bu kullanıcı ile login olmaya çalışınca login olamıyor, admin page e gittiğimizde bu kullanıcının Permissions da Active statüsünün kalkmış olduğunu gördük. Bunu yaptığımızda kullanıcı login olamıyor ama ayarları hala duruyor belki ileride tekrar active etmeniz gerekirse, bazı ufak ayarlar ile user ı tekrar active edebiliriz.





# Add users with auth

Djangoda admin page de ve programatic olarak kullanıcı eklemeyi gördük, ama bunu yazdığımız views lar sayesinde kullanıcının login olmasını kendi hesabını oluşturmasını sağlayacağız ki bu en temel web sitesi ayarlarından bir tanesidir.

We want to allow adding regular users to our app.

path('accounts/', include('django.contrib.auth.urls'))

django.contrib.auth paketi var, bu paket default olarak login, logout, passwordchange gibi view ları içeriyor. Bunun url lerini çağırdığımızda accounts/ başında olacak.

Biz local hosttan :8000/accounts/ a gittiğimizde bize birçok yol veriyor, bunları django.contrib.auth kütüphanesinin kendi default url leri. mesela öncelikle login e bakalım. 8000/accounts/login/  bize bir default olarak bir login page veriyor, bu view ü biz yazmadık. Değişik değişik default olarak tanımlanmış sayfalar var.

- Go to authenticate/urls.py and add:
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    ### And using some urls which Django give us about authentication:
    path('accounts/', include('django.contrib.auth.urls'))
]
```

Bizim oluşturmadığımız bir view var o da accounts, nereden çağırıyoruz? default olarak django.contrib.auth kütüphanesinden çağırıyoruz.

home page e gidip oradan url' ye /accounts/login/ tıkladıktan sonra user1 ve password ü ile login olduk,

home Template ine gidip değişiklik yaptık.

user1 olarak login olunca artık admin page e giremiyoruz.
<home.html> ->
```py
<h1>This is the home page!</h1>

{{ user.username }}
<br>
{{ user.first_name }}
```


Bu değişikliği yaptık ama first_name i olmayan userlar için bize hata verir, bu hatayı almamak için; if condition ile eğer user.first.name true ise {{user.first_name}} ver false ise yani yok ise else birşey verme! ile çözüyoruz.
<home.html> ->

```py

<h1>This is the home page!</h1>

{{ user.username }}
<br>

{% if user.first_name %}
    {{ user.first_name }}
{% endif %}
    
```




### Login template

templates klasörünün altında iki tane klasör var, biri registration, diğeri appimizin adinı taşıyan user_example. Application un kendi template lerini app in ismini taşıyan klasörün içine yazıyoruz (home.html special.html vb.). Ancak django diyor ki eğer siz kendiniz bir Login template oluşturacaksanız, registration diye bir klasör oluşturup onun içine koymanız gerekiyor (login.html , password_change.html , register.html vb.)  ki django bunu default olarak algılasın ve yerini göstersin.

Bu derste kullandığımız login page aşağıda. İçerisinde tek yaptığımız formu göstermek başka birşey yok.
<login.html> ->

```html

<form action="{% url 'login' %}" method="POST">

    {% csrf_token %}

    {{ form.as_p }}

    <input type="submit", value="Login">

</form>

```



Django_Autentication.md içerisinde login page için aşağıdakileri yazmış ama biz yukarıdaki login page code larını kullandık.

<login.html> ->

```html

{# Optional #}
<h1>Hello this is login page!</h1>

{# Optional #}
{# If the user enters wrong password, an error message will be shown #}
{% if form.errors %}
    <p>Your username and password didn't match. Please try again.</p>
{% endif %}

{# Optional #}
{% if next %}
    {% if user.is_authenticated %}
        <p>Your account doesn't have access to this page. To proceed,
        please login with an account that has access.</p>
    {% else %}
        <p>Please login to see this page.</p>
    {% endif %}
{% endif %}
    

<form action="{% url 'login' %}" method="post">

    {% csrf_token %}

    <p>Username: {{ form.username }}</p>
    <p>Password: {{ form.password }}</p>

    <input type="submit" value="login">
    
    <input type="hidden" value="{{ next }}" name="next">

</form>

{# Optional #}
{# Assumes you setup the password_reset view in your URLconf #}
  <p><a href="{% url 'password_reset' %}">Lost password?</a></p>

```





### Logout

logout dediğimizde kullanıcının logout olduğunda görüntülenen sayfa djangonun kendi sayfası, bu view ü biz oluşturmadık. Bu sayfada Log in again linki ile bizi default olarak admin giriş sayfasına yönlendiriyor. Bu istenen bir durum değildir.
Bu durumu düzeltmek için registration klasörünün altına login.html template i tanımlandığı gibi custom olarak logout page de tanımlanabilir. Ancak biz bu sorunu <settings.py> da yazacağımız   LOGOUT_REDIRECT_URL = '/'    komutu ile aşıyoruz. Artık kullanıcıyı logout olunca home page e yönlendiriyor. 

Want to redirect to home page when logout
Logout yaparken ana sayfaya yönlendirmek istiyorum.

settings.py a gidip en alta    LOGOUT_REDIRECT_URL = '/'    yazıyoruz. 


Add settings.py ->

```py

LOGOUT_REDIRECT_URL = '/'

```





### Enable views to add new users
(Yeni kullanıcılar eklemek için görünümleri etkinleştirin)

- Add a new view to add registration.
  Kayıt eklemek için yeni bir görünüm ekleyin.

- Go to views.py, create new view:
  views.py'ye gidin, yeni görünüm oluşturun

Bunun için, django.contrib.auth.forms dan import ederek UserCreationForm kullanıyoruz. UserCreationForm djangonun kendi otomatik formudur. Bize sağladığı şey username istiyor, password istiyor ve password u doğrulamanızı istiyor. Ancak genel olarak kullanıcıların email ile login olmaları isteniyor. Bunun için customisation yapılacak. Bu djangonun kendi default ayarlarıdır, defaultta username ve password istiyor.
register (kayıt ol) view ünü tanımlarken önce UserCreationForm() u alıp form değişkenine tanımlamış. form u da context içerisinde   request objesiyle birlikte  registration/register.html  e  göndermiş.

<views.py> ->

```py
# First import UserCreationForm
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, "registration/register.html", context)
```


Ancak bizim <views.py> ımız da yukarıdaki code lara ek olarak sadece bir if bloğu var. Bu if bloğu bize neyi sağlıyor? ; Eğer request.method == 'POST' ise UserCreationForm(request.POST) u form değişkenine tanımla,  eğer form valid ise form.save()   et,    formdan alınan username i username değişkenine tanımla  ,  formdan alınan password1 i password değişkenine tanımla (neden password1 çünkü confirmation olarak girilen password ü iki defa soruyor password1 ve password2 birbirini tutuyorsa kabul ediyor. O yüzden biz password1 diyoruz.) ,  programatic olarak nasıl oluşturuyorduk onu hatırlayalım; python shell de aynı oluşturduğumuz gibi bir authenticate fonksiyonumuz var bu username i username e, password u password e eşitliyor v e bunu user değişkenine tanımlıyor. login fonksiyonu da request ve user objelerini parametre olarak alıp login yapıyor. Ardından login olduktan sonra redirect olarak home a gönderiyor. if bloğundaki else de yukarıdakiler gerçekleşmezse UserCreationForm() u form değişkenine tanımla ve context içerisinde requestle birlikte template e gönder.

<views.py> ->

```py

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home_view(request):
    return render(request, 'user_example/home.html')

@login_required
def special(request):
    return render(request, 'user_example/special.html')


def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(username=username, password=password)
            
            login(request, user)
            
            return redirect('home')
        
    
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    
    return render(request, "registration/register.html", context)


def password_change(request):
    
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = UserChangeForm()
    context = {
        'form': form
    }
    return render(request, "registration/password_change.html", context)

```









- Before creating register page, lets add it to the url list of our app;
  Kayıt sayfası oluşturmadan önce, uygulamamızın url listesine ekleyelim.

app imizin urls.py ına gidip path ini ekliyoruz.

<urls.py> ->

```py
from django.urls import path
from .views import home_view, register

urlpatterns = [
    path('', home_view, name="home"),
    path('register', register, name='register')
]

```





- Create register.html under templates/registration folder.
  templates/register klasörü altında register.html oluşturun.

Basitçe form post metodu alıyor, dolayısıyla csrf_token alıyor, sadece formu alıyor, input type submit ve value su Register. Template inde hazır olan bir form kullanıyoruz. Nereden inherit ettik? django.contrib.auth paketinin içerisindeki forms lardan UserCreationForm . Bununla bir view tanımladık.

<register.html> ->

```html
<h1>Registration page</h1>

<form action="{% url 'register' %}" method="post">

    {% csrf_token %}
    
    {% if form.errors %}
        <p>There is something wrong what you entered!</p>
    {% endif %}

    {{ form.as_p }}
    {# as_p orders the scene #}

    <input type="submit" value="Register">

</form>
```





- Try to create new user
  Yeni kullanıcı oluşturmayı deneyin

- It will send user info to register app, go to the admin page and check it!
  Uygulamayı kaydetmek için kullanıcı bilgilerini gönderecek, yönetici sayfasına gidin ve kontrol edin!

- Cant see the new user, so we need to save new user to our users list using view
  Yeni kullanıcıyı göremiyoruz, bu yüzden görünümü kullanarak yeni kullanıcıyı kullanıcı listemize kaydetmemiz gerekiyor

- If its a get request or post? For get requests, only showing the form is enough.  But for post request need to add someting.
  Bu bir istek mi yoksa gönderi mi? Alma istekleri için sadece formun gösterilmesi yeterlidir. Ancak gönderi isteği için bir şeyler eklemeniz gerekir.

- If post and creates a user, need to save it. Use if block:
  Bir kullanıcı gönderir ve oluşturursa, kaydetmeniz gerekir. if bloğunu kullanın:



```py
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

# add authenticate and login 
from django.contrib.auth import authenticate, login

def home_view(request):    
    return render(request, "user_example/home.html")

def register(request):
    
    if request.method == 'POST':
        # pass in post data when instantiate the form.
        form = UserCreationForm(request.POST)
        # if the form is ok with the info filled:
        if form.is_valid():
            form.save()
            # that creates a new user
            # after creation of the user, want to authenticate it
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # inspect the page and see the first password is password1, import authenticate
            user = authenticate(username=username, password=password)
            
            # want user to login right after registered, import login
            login(request, user)
            # want to redirect to home page, import redirect
            return redirect('home')
            
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    
    return render(request, "registration/register.html", context)
```




Bir de site kullanıcının register olmadan da ziyaret edebileceği bir site olabilir, ama login olduğunda farklı bir kullanıcı arayüzü görüntilüyor olabilir. Örneğin bir alışveriş sitesine register olmadan girebilir, hatta alışveriş bile yapabilirsiniz. Ama opsiyonel olarak register olarak giriş yapıldığında seçimleriniz, kredi kartı bilgileriniz, tekrar görüntülenebilecek filan..
Bunun için if bloklarında şunları kullanabilirsiniz. ->


- Lets try to create a new user again
  Tekrar yeni bir kullanıcı oluşturmayı deneyelim

- It must redirect to homepage
  Ana sayfaya yönlendirmesi gerekiyor

- See the user on admin page, there are lots of options to modify user via admin page
  Kullanıcıyı yönetici sayfasında görün, kullanıcıyı yönetici sayfası aracılığıyla değiştirmek için birçok seçenek vardır.

- Lets show something to the user on homepage about registration process
  Kullanıcıya ana sayfada kayıt işlemi hakkında bir şeyler gösterelim

- Go to home.html

<home.html> ->

```html

<h1>This is the home page!</h1>


{% if user.is_authenticated %}
    <h2>Your name is:{{ user.username }}</h2>
{% else %}
    <h2>You are not logged in!</h2>
{% endif %}

```

or / veya ;

```py
<h1>This is the home page!</h1>

{{ user.username }}
<br>

{% if user.first_name %}
    {{ user.first_name }}
{% endif %}

```

- Refresh home page and see the result.
  Ana sayfayı yenileyin ve sonucu görün.




### Password Change

The default password reset system uses email to send the user a reset link. You need to create forms to get the user's email address, send the email, allow them to enter a new password, and to note when the whole process is complete.

Django default olarak password reset sistemini kullanıcı emailine bir reset linki göndererek kullanır. 

View üne bakalım; password_change(request) view ü , burada method yine POST  ise , UserChangeForm(request.POST) kullanıyor. Daha önce UserCreateForm kullanmıştık. django.contrib.auth.forms  dan  UserChangeForm u import ediyoruz. form a tanımlıyoruz , validation yapıyoruz , kaydediyoruz  ,  home page e redirect ediyor  ,  else UserChangeForm  u gösteriyor ,  password_change template ini render ediyor.

- Add view

```py

def password_change(request):
    if request.method == 'POST':
        # We will use user change form this time
        # Import it
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = UserChangeForm()
    
    context = {
        'form': form
    }
    
    return render(request, "registration/password_change.html", context)

```




<views.py> ->

```py

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home_view(request):
    return render(request, 'user_example/home.html')

@login_required
def special(request):
    return render(request, 'user_example/special.html')


def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(username=username, password=password)
            
            login(request, user)
            
            return redirect('home')
        
    
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    
    return render(request, "registration/register.html", context)


def password_change(request):
    
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = UserChangeForm()
    context = {
        'form': form
    }
    return render(request, "registration/password_change.html", context)

```



password_change template imiz bu proje için gösterdiği tek şey formu göstermek, başka hiçbirşey yok. change button u ile  password u change etmek. Yine burada da customization yapılabilir.


- Add registration/password_change.html
  registration/password_change.html oluşturup ekleyin


<password_change.html> ->

```py

<h1>Password Change page</h1>

<form action="{% url 'password_change' %}" method="POST">

    {% csrf_token %}

    {{ form.as_p }}

    <input type="submit", value="Change">

</form>

```




app imizin urls.py ına gidip path ini ekliyoruz.

Dikkatimizi çeken başka bir şey password_change için özel bir yol tanımladık. Bu yola bakabilirsiniz pasword_change.html i göstermek için.  

- Add url

<urls.py> ->

```py
from django.urls import path
from .views import home_view, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name="home"),
    path('register', register, name='register'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"), name="password_change")
]
```


Burada değişik birşey gördük, default olarak bizi yine djangonun default password_change sayfasna yönlendirdi.

Password change succesfull dan sonra home page e nasıl dönecek????



### Links to official documentation

https://docs.djangoproject.com/en/3.2/topics/auth/default/

https://docs.djangoproject.com/en/3.2/ref/settings/

https://django-allauth.readthedocs.io/en/latest/overview.html

https://docs.djangoproject.com/en/3.2/topics/auth/customizing/
