Müşteri siz
Blog application yapın, kullanıcılar crud işlemleri yapsın, ana sayfada bunlar sergilensin, comments, likes, views eklensin.

CRUD işlemlerinin yapıldığı bir alan, bir app ve bir de user ların olduğu bir app lazım
Önce django setup ı yapılması lazım, venv, decouple, db, .env ilk aşama bu ve %50 si
main projesinin içinde 
user app, CRUD app
CRUD dan başlanmalı
user işlemleri yapılmalı
decorator larla bağlanacak.
list
create
detail
update
delete
user da creation form ile register olacak, login olacak.
main in url inde bu iki app birleştirilecek.

Blog larımız olacak,
picture upload edebileceğiz,
blog başlığı
blog body sinin bir kısmı
kaç mesaj gelmiş
kaç uniq görüntüleme olmuş 
kaç like almış
ne zaman yapıldığı

detaya
edit
delete


En başta bir virtual environment oluşturuyoruz, activate ediyoruz, django yu yüklüyoruz, upgrade ediyoruz, requirements.txt dosyamızı oluşturuyoruz. 

```bash
py -m venv benv
./benv/Scripts/activate
py -m pip install django   or  
pip install django
py -m pip install --upgrade pip
pip freeze
pip freeze > requirements.txt
```

- create .gitignore  (projenin içine .gitignore oluşturalım.)

- create project (projemizi oluşturalım.)

```bash
django-admin startproject cblog (iç içe iki klasör oluşturduk.)
(dıştaki cblog klasörünün ismini src olarak değiştirdik ve manage.py dosyası ile aynı seviyeye gelmek için src nin içine gireceğiz.)
ls
cd ./src/
ls   (manage.py ile aynı seviyeye geldik!)
```

- create application (application (blog) oluşturalım.)

```bash
py manage.py startapp blog
```

add settings.py into the INSTALLED_APPS

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'blog.apps.BlogConfig',
    # or
    # 'blog'
]
```

environment değişkenlerini korumak için .env dosyası oluşturuyoruz.
create .env file
first install python decouple

```bash
pip install python-decouple
or
py -m pip install python-decouple
```


add settings.py into 

```py
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```


add below line to .env file
<.env> ->

```py
SECRET_KEY = django-insecure-(pwhca6*426s5nqi14_)9m9a(sty&!zj$lhw)1xjinuv47xa3e
```

<settings.py> daki değişikliklerden sonra

```bash
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver

```

projenin urls.py ında application ın urls.py ' ını include ediyoruz, hemen ardından application ın urls.py ' ını oluşturuyoruz.

projenin <urls.py> ->

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

blog app in <urls.py> ına gidip view imizin yolunu yazmamız gerekiyor ama biz daha view yazmadığımız için hata vermemesi adına şimdilik yoruma alıyoruz.

<urls.py> ->

```py
from django.urls import path

# urlpatterns = [
#     path('', )
# ]
```


- Şimi önce modellememizi yapacağız, 
  modellerimizden bahsedelim, bir tane
  category modelimiz olacak onun altında bir tane post modelimiz olacak burda filtrele olacak???? ondan sonra home lines, post view ve like yani commet yorum tablomuz olacak, post view tablomuz olacak ve like tablomuz olacak.
- Öncelikle Post modelimizle başlayalım. Hangi 
  fieldlarımız olacak ondan bahsedelim, 
  başlığımız olacak title,
  içerik olacak content, 
  fotoğraf yükleyeceğiz image, 
  category si olacak category, post oluşturulduğu zaman otomatik olarak tarih verecek 
  publish_date, her update edildiği zaman otomatik olarak tarih verecek 
  last_updated, 
  olmazsa olmaz bir tane yazarımız olacak author, 
  bir tane status olacak ve ya draftı olacak isterse yazar bunu yayınlamayacak yada publish olacak ve ana sayfada gösterilecek ancak draft ta ise ana sayfada gösterilmeyecek kullanıcı isterse değişiklik yapıp publish eçekip ana sayfada post unu yayınlanmasını sağlayacak, 
  slug field ımız olacak genelde blog post ların.. şu şekilde url ler görünüyor  how-to-learn-django böyle aralarında tire tire oluyor url de. şimdi artık tek tek yazmaya başlıyoruz fieldlarımızı
- title = models.CharField
  (max_length=100)  max length zorunlu
- content = models.TextField() 
  max_length zorunlu değil vermiyoruz kullanıcının blog yazma kapasitesine bırakıyoruz
- image = models.ImageField() image 
  ları media 
  file larını db ye kaydetmiyoruz, ayrı bir yerde tutuyoruz, kendi 
  projemiz içerisinde de değil genelede bunlar 3rd party depolama alanlarında tutuluyor, en popüleri de AWS3 storege service. Buraya geri döneceğiz.
- category = models.ForeignKey
  (Category, 
  on_delete=models.PROTECT)  bir category tablosu oluşturacağuz, orayla 
  ForeingKey yapacağız, Category tablosuyla ForingKey i olacak ve on_delete=PROTECT olacak bu nedir yani bir postunuz varsa ve o posta ait bir category varsa category tablosundan bu postu silmesine izin vermiyor. CASCADE ise direkt siliyor yani category tablosundan category i silersek comple post u da siliyor, admin panelinde gösterilecek, burayı yoruma alıyoruz çünkü category tablosunu oluşturmadık.
  OneToOne, ManyToMany, OneToMany relationship var. ForingKey OneToMany relationship dir, yani bunun anlamı bir post un sadece bir tane category si olacak ama bir category e ait birçok post olabilir. Category parent, post lar child. Bir child ın bir tane parent ı olur ama bir parent ın birden çok child ı olabilir. 
- publish_date = models.DateTimeField
  (auto_now_add=True) post umuzu oluşturduğumuz zaman otomatik olarak tarih 
  saaat ekleniyor.
- last_updated = models.DateTimeField
  (auto_now=True) her update edildiğinde otomatik olarak tarih saaat 
  ekleniyor.
- author = models.ForeignKey Burada da user 
  model foringkey i göstereceğiz, bizim db de user tablomuz hazır 
  geliyordu yani user tablomuz var o tabloyu kullanacağız. User ilk başta migrate ettiğimizde bizim db imizde yani admin panelde de görünüyor hem bir grup tablomuz var hemde User tablomuz var işte o hazır verilen user tablomuzu kullanacağız. yine on_delete=models.CASCADE diyoruz yani user ı sildiğim zaman bu post da silinsin istiyorum. Çünkü bir anlamı yok yani user silinecekse postun kalmasının bir anlamı yok. author = models.ForeignKey(User, on_delete=models.CASCADE) Hata vermemesi için yoruma alıyoruz.
- status = models.CharField() şimdi 
  bunu drop down menü gibi yapacağız, onun için bir yöntem var ondan 
  bahsedeceğiz; choices yada options diyebilirsiniz; bir tane tupple içerisinde biri db de kayıtlı olacağı şekliyle (d) diğeri kullanıcı dropdown menüsünde ise Draft diye gözükecek.
  OPTIONS = (
      ('d', 'Draft'),
      ('p', 'Published'),
  )
  Bu kısmı üst tarafa yazacağız, ardından yine charfield olduğu için max_length vermek zorundayız, bizim buraya gelebilecek en uzun kelimemiz Published 9 karakter olduğu için bir de bizden olsun diyoruz ve 10 yazıyoruz. status = models.CharField(max_length=10, choices=OPTIONS, default='d') 
  Bir de bu drop down un dinamik olarak nasıl kullanılıyor onu da gösterecek.
- slug = models.SlugField(blank=True) 
  buna özel SlugField ı var, zorunlu olmadığını 
  blank=True ile belirtiyoruz, çünkü slug field ını zaten biz otomatik olarak generate edeceğiz, onu göstereceğiz nasıl generate edileceğini, dolayısıyla admin panelden doldurulmasına gerek kalmayacak. eğer doldurulması zorunlu olursa custom validationdan geçemeyecek hata verecek, bunun önüne geçmek için blank True diyoruz. Yine bunu uniq olmasını istiyoruz, çünkü bunu primary key yerine id yerine kullanacağız modelimizde o yüzden unique=True diyoruz. slug = models.SlugField(blank=True, unique=True)   id miz var ama genelde blog larda, e-ticaret sitelerinde de slug kullanılıyor, id kullanılmıyor genelde göstermiyorlar. 

<models.py> ->

```py

from django.db import models

class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)
    
```

- şimdi yoruma aldığımız iki 
  field vardı bunları yorumdan kurtaracağız, hayata geçireceğiz, önce author da kullandığımız otomatik olarak djangonun auth application ının altındaki model file ında oluşturmuş olduğu ve bize sunduğu User modelini django.contrib.auth.models den User ı import ederek kullanıyoruz. importumuzu yaptıktan sonra author u yorumdan kurtarıyoruz.

<models.py> ->

```py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)

```

- şimdi category field ımızda 
  kullandığımız Category modelimizi oluşturup yorumdan kurtaracağız. Category modelimizi Post modelimizin üstünde oluşturmamız lazım, çünkü Category modeli bizim parent modelimiz olacak, eğer altında tanımlarsak ForeignKey veremeyiz. Bunun sadece bir tane name field ı olacak ama bunu sonradan drop down olarak kullanacağız. Category ekleme işi de sadece admin panelinde olacak, sadece site yöneticisi Category ekleyebilecek, bunu form a koymayacağız ki her önüne gelen category eklemesin. Onun için bir tane default bir categoy ekliyeceğiz, eğer bir category bulamazsa "not categorized" diye default drop down seçenek koyacağız kullanıcı onu seçecek.
  name = models.CharField(max_length=100)

<models.py> ->

```py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    
class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)

```


Artık modelimizi admin panelde register edip kontrol edeceğiz,tabi önce migrations ve migrate etmemiz lazım.

```bash
py manage.py makemigrations
```
yaptık hata verdi, proje urls.py ında patern hatası verdi, include ettiğimiz paterni yoruma aldık.

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('blog.urls')),
]
```

şimdi de pillow u istedi, image field kullandığımız için, pillow yükledik, tabi requirements.txt ye eklememiz lazım, 

```bash
py -m pip install pillow
```

src nin içinden bir üst klasöre requirements.txt nin seviyesine çıkıyoruz;

```bash
cd ..
```

yüklediğimiz pillow kütüphanesini requirements.txt ye ekliyoruz.
```bash
pip freeze > requirements.txt
```

tekrar projemizin klasörüne yani src ye giriyoruz, manage.py ile aynı seviyeye
```bash
cd ./src/
```

artık mmigrations ve migrate yapabiliriz
```bash
py manage.py makemigrations
py manage.py migrate
```

Şimdi artık modelimizi admin panelde register edip kontrol edeceğiz, app imizin (blog) içindeki <admin.py> a gidip;

<admin.py> ->

```py
from django.contrib import admin
from .models import Category, Post

admin.site.register(Category)
admin.site.register(Post)
```

Admin panele gidiyoruz ve Category ve Post modelimiz görüyoruz.
```py
py manage.py runserver
```

Category nin sonuna gelen s takısı yani çoğul takısını class Meta ile düzelteceğiz. <models.py> a gidip Category modelimizin içine class Meta yazarak düzelttik, admin panelden de düzeldiğine baktık ;

<models.py> ->

```py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    
class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)
    
```


Admin panelde Protect ne işe yarıyordu onları gösterdi, Category oluşturuyoruz, Oject şeklinde görünen isimleri str metoduyla görüntüsünü düzeltik, Post class ında oluşturduğumuz instance ı nasıl gösterecek bana onu belirliyoruz,
<models.py> ->

```py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

    
class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.title
```


Admin panelde django ve react  diye iki tane category ekledik, 

image field ımız db ye kaydedilmiyor demiştik, onun için upload_to='' diye bir yol belirtmemiz gerekiyor. parantez içerisine hard coded birşey de oluşturabiliriz, blog/ yazarak blog 'un altına kaydet diye buşekilde yazabiliriz ama daha dinamik bir yol gösterdi. <settings.py> a gittik, en altta STATIC_URL var, bu aslında djangonun static file larını bulmak için kullandığı prefix. staticten sonra kullandığımız staticler nelerse onların dosya yolunu yazıyoruz.
mesela STATIC_URL = 'static/css/main.css'  diye url de gözükecek. Aynı bunu gibi bir tane de MEDIA_URL = ''  belirtmemiz gerekiyor, yoksa django sıkıntı çıkarıyor, ben bu media file ları nerede gösterceğim diye. Buna MEDIA_URL = '/media/' diyebilirsiniz, farklı birşey diyebilirsiniz ama best practice media deniyor.
Bundan sonrada MEDIA_ROOT='' diye bir yol tanıtmamızı istiyor django. Bunu yine BASE_DIR içerisindeki media_root diyoruz, MEDIA_ROOT = BASE_DIR/'media_root' 

ilk hali: <settings.py> ->
```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

```

değiştirdiğimiz kısım: <settings.py> ->
```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media_root' 

```

Bitti mi hayır bir ayar daha yapmamız gerekiyor, şimdi bu media root bizim media file larımızı koyacağımız directory olacak, yani ben ne dedim source un içerisinde ana base dır yolumun içerisinde bir tane media_root diye bir tane klasör açacak ve django kullanıcıların yüklediği media file larını bu klasörün altına yükleyecek.

Ana projedeki <urls.py> a gidiyoruz, burada şu importları yapıyoruz -> django.conf dan settings ve django.conf.urls.static den static (djangonun static function u)

Alt kısma if settings.DEBUG:  (settings deki DEBUG True idi yani diyor ki sen geliştirme aşamasındaysan production a geçmemişsen DEBUG ın True iken benim o belirttiğim media root vardı ya sen media file larını devolopment dayken bu belirttiğim media root file ından kullan, mediaları oradan çek şuanda ama ben daha sonra productiona geçtiğim zaman canlıya geçtiğim zaman ben bunarı başka yere yükleyeceğim, sana settings.py da farklı configurasyon ayarları vereceğim ama şuanda geliştirme yaparken benim media file larımı benim gösterdiğim klasör içerisinden kullan diyoruz.)
urlpatterns e += ile ekliyoruz urlpatterns listesine ekliyoruz, settings.MEDIA_URL i al ondan sonra document_root da yani senin kullanacağın documentlerin root u da 
benim belirttiğim settings.MEDIA_ROOT olacak diyoruz.
Aslında bu if bloğunun demek istediği geliştirme yaparken canlıya çıkmadan önce benim belirttiğim MEDIA_ROOT u ve  MEDIA_URL i kullan diyor, bukadar.
Normalde media file larını ve static file larını (çok değişmeyen css, javascript,web sayfasında kullandığımız statik, sabit resimler) en popüler depolama alanı olan AWS3 gibi 3rd party depolama araçlarında depolanıyor.
project <urls.py> ->
```py
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Şimdi media folder ımızı oluşturuyoruz. SRC nin içine, application klasörümüz ile, manage.py dosyası ile aynı seviyede. Folder klasörümüzün ismi settings.py da MEDIA_ROOT unuzda ne isim verdiyseniz o isim olmak zorunda (yani 'media_root')


Modelimize dönüyoruz;
    image = models.ImageField(upload='') bu şekilde upload diye şurda bir klasör oluştur onun altında da bir klasör oluştur oraya kaydet diyebiliriz, ama  media root umuzu yazmamıza gerek yok şimdi daha artistik birşey gösterecek, Category modelimizin de üstüne bir fonksiyon yazıyoruz,
    def user_directory_path(instance, filename)  bu function içerisine instance (Post tan oluşturduğumuz bir obje gibi düşünün instance o artık) ve filename diye iki parametre alıyor, sonra 
    return 'blog/{0}/{1}'.format(instance.author.id, filename)
    image field ımızın upload kısmına gidip fonksiyonumuzu kullan diyoruz, image yüklenmezse diye default olarak bir image belirtiyoruz.
    image = models.ImageField(upload=user_directory_path, default='django.jpg')
    Artık kullanıcı models de belirttiğimiz image field ına bir resim koyduğu zaman django otomatik olarak gidip media_root un altında blog diye bir klasör oluşturacak, onun altdında id diye bir klasör oluşturacak, onun altında da resmi koyacak.
    Admin panele gidip resim yüklüyoruz, draft seçiyoruz, 

<models.py> -> <

```py
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

    
class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, default='django.jpg')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.title

```
    
    slug field a geldik,

    django signals tan bahsedecek, postsave, presave, postdelete, predelete
    signals için modelimizin altında da belirtebiliriz ama best practice olarak app imizin (blog) içerisinde bir file oluşturuyoruz, <signals.py>.
    Eğer signals ı modelin altında oluştursaydık <apps.py> da yapmamız gereken bir değişikliği yapmak zorunda kalmayacaktık.
    Signals için ayrı bir file oluşturduğumuz için <apps.py> da bir değişiklik yapmamız gerekiyor. def ready(self) diye hazır bir function ı override ediyoruz. Yani diyoruz ki bu signals file ını import et ve bu signals file da işlem yap diyoruz.
    
<apps.py> ->

```py
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        import blog.signals
```

    Ama bu signals ı modelimizin içinde yazsaydık bu işleme gerek kalmayacaktı.Ekstradan signals.py oluşturduğumuz için apps.py da bu değişikliği yaptık.

    Şimdi <signals.py> a gelelim; nedir, yararları nelerdir? Kullanmak için;
    oluşturduğumuz post u kaydetmeden önce bir slug oluştursun istiyoruz onun için pre_save metodunu kullanacağız import ediyoruz,
    from django.db.models.signals import pre_save 
    bir de reiever var, post u save et dediğimiz zaman bu receiver yazdığımız kodu gerçekleşmesini sağlıyor, dispatcher birleştirici, yani tıkladığımız an şu işlemi yap kaydetme bekle ben bu işlemi yapıcam ondan sonra kayıt işlemini tamamla öyle düşünülebilir.
    from django.dispatch import receiver
    slug field larının arasında tire var bu işlemi yapan slugifly onu import edeceğiz. methodun içerisine koyduğumuz stringlerin arasında tire koyuyor.
    from django.template.defaultfilters import slugify
    ve de modelimizi (Post) import ediyoruz.
    from .models import Post
    receiver ımız bir decorator, içerisine parametre olarak  pre_save, senrder= signal ı kim gönderecek? Post modelimiz gönderecek ya onu alıyor.
    @receiver(pre_save, sender=Post)
    Daha sonra function ımızı yazıyoruz, istediğimiz ismi yazıyoruz, parametre olarak sender, instance (Post tan oluşturduğumuz obje düşünün), **kwargs (sayısını bilmediğimiz argumentler için (arguments ler için * koyuyoruz.)) koymak zorundayız.
    def pre_save_create_slug(sender, instance, **kwargs):
    Eğer benim oluşturduğum instance ın slug ı yoksa 
        if not instance.slug:
        instance.slug = slugify(instance.auther.username + ' ' + instance.title)
    
    bizim login olurken username kullandığımız için username imiz uniq olmak zorunda, bizim burada uniq bir değer girmek zorundayız onun için instance.auther.username kullanıyoruz (uniq bir değer diye)(bunu uuid ile de yapabiliriz), + ' ' + instance.title kullanıyoruz.

<signals.py> ->

```py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Post

@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + ' ' + instance.title)
        
```
Admin panele gidiyoruz, post oluşturuyoruz, slug ı boş bırakıyoruz otomatik oluştursun diye save ediyoruz, post a tıklıyoruz ve sluh kısmına bakıyoruz evet aralarına tire koyarak slug oluşturmuş.

Kullanıcımız silinebiliyor, kullanıcı silinince Post da siliniyor ama image lar db de kayıtlı olmadığı, file sisteminde kayıtlı olduğu için kullanıcını yüklediği  image lar silinmiyor. Bunun için yine burada işlem yapıyoruz. Post modelim silindiğinde image ı da silsin diye. Bunun için de kullanılıyor. Signals Bu yapılacak!!!!!!!!!
Bu yapılacak!!!!!!!!!
Bu yapılacak!!!!!!!!!
Bu yapılacak!!!!!!!!!
Bu yapılacak!!!!!!!!!
Bu yapılacak!!!!!!!!!
Bu yapılacak!!!!!!!!!
Bu yapılacak!!!!!!!!!


Diğer modellerimize geçiyoruz;  

Comment modelimizi basit tuttuk, bu çok daha karmaşık yapılabilir.Twitter daki gibi içi içe de parent-child commentler de olabilir ama burada kısa tutuldu.Sadece mesaj atınca ekranda görünmesi için basit tutuldu.
Bu comment e ait bir tane user ımız olması lazım. User modeli ile ForignKey ilişkisi olacak, on_delete=models.CASCADE olacak yani user silindiğinde commentimiz silinsin istiyoruz,
post ile bir ilişkisinin de olması lazım, post silindiği zaman altındaki yorumlarda silinmesi lazım, on_delete=models.CASCADE
commentin oluşturulduğu zaman olacak auto_now_add=True
content i olacak models.TextField()
str metodu belirliyoruz, def __str__(self): return self.user.username
<models.py> ->
```py
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, default='django.jpg')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username
    
```

Like modelimizi yazıyoruz, günümüzde postlarda ne var? like, comment, görüntülenme var.
Like a ait bir tane user ımız olması lazım. User modeli ile ForignKey ilişkisi olacak, on_delete=models.CASCADE olacak yani user silindiğinde like da silinsin istiyoruz,
post ile bir ilişkisinin de olması lazım, post silindiği zaman altındaki like ların da silinmesi lazım, on_delete=models.CASCADE
str metodu belirliyoruz, def __str__(self): return self.user.username
<models.py> ->
```py
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, default='django.jpg')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
```

PostView modelimizi yazıyoruz;
(kim görüntülemiş, hangi pstu görüntülemiş, saat kaçta görüntülemiş bu fieldları istiyoruz, tabi bunları çoğaltabiliriz de)
PostView için de bir tane user ımız olması lazım. User modeli ile ForignKey ilişkisi olacak, on_delete=models.CASCADE olacak yani user silindiğinde PostView de silinsin istiyoruz,
post ile bir ilişkisinin de olması lazım, post silindiği zaman altındaki View lerin de silinmesi lazım, on_delete=models.CASCADE
time_stamp veriyoruz;
str metodu belirliyoruz, def __str__(self): return self.user.username

<models.py> ->
```py
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, default='django.jpg')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
```

<admin.py> a gidip oluşturduğumuz modelleri import ediyoruz ki admin panelde görebilelim;
<admin.py> ->
```py
from django.contrib import admin
from .models import Category, Post, Comment, Like, PostView

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(PostView)
admin.site.register(Comment)
```

modelde değişiklik yaptığımız için makemigrations ve migrate yapıyoruz;
go to terminal
```bash
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```

şimdiye kadar yaptığımız değişiklikleri sadece admin panelde görebiliyoruz, çünkü template lerimizi henüz oluşturmadık.

Şu ana kadar db modellerini, tablolarını yazdık, şimdi formları yazacağız, kullanıcıdan form a koyduğumuz field ları doldurmasını isteyeceğiz, kullanıcı fieldları doldurunca biz onları frontend de template ler ile göstereceğiz. Şimdi formları yazacağız; app imizin içinde <forms.py> oluşturuyoruz, içinde postform ve commentform oluşturuyoruz, iki tane forma ihtiyacımız var, bir tanesi postform postu oluşturmak için hem postcreate de kullanacağız hem postu update ederken kullanacağız, diğer bir tanesi de comment için yani yorum için form oluşturacağız. Önce form oluşturmak için django dan forms import ediyoruz, sonra modelForm kullanacağımız için .models den Post ve Comment  modellerini import ediyoruz, PostForm mumuzu forms.ModelForm dan inherit ediyoruz class PostForm(forms.ModelForm):   ,   class Meta nın altına modelimizi ve bu modelin fieldlarını belirtiyoruz. (Kullanacaklarımızı yazmak yerine exclude da yapabilirdik.)
Bizim status ümüzü modelde drop down olarak kullanmıştık, bunu formda da kullanabiliriz, onu nasıl yapacağız? class metanın hemen üstüne override edeceğimiz field ı yazıyoruz, burada status ü override ediyoruz,  status = forms.ChoiceField(choices=Post.OPTIONS) yani choices içerisine Post.OPTIONS u al diyoruz.
category için de djangonun şöyle güzel bir yöntemi var ;  category db de kayıtlı, Options gibi static değil dinamik, yani biz admin panelden birşey eklediğimizde otomatik olarak drop down menüsüne onların da eklenmesini istiyoruz bunun için ModelsChoiceField var bunun içerisine bir tane queryset yazıyoruz, Category tablomdaki objects lerin hepsini al diyoruz, tabi Category modelimizi import etmemiz lazım, Şİmdi bana dinamik olarak ben category e admin panelden birşey eklediğim zaman form da o eklediğim şey dinamik olarak gözükecek, ayrıca birşey seçilmediğinde emty_label='Select' yazarak Select görünmesini sağlıyoruz.     category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select')
<forms.py> ->
```py
from django import forms
from .models import Post, Comment, Category

class PostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Post.OPTIONS)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select')
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'image',
            'category',
            'status',
        )
```

Şimdi CommentForm u oluşturacağız;
class CommentForm(forms.ModelForm):   forms.ModelForm dan inherit edecek,
class Meta:
model = Comment
fields = ('content',) user otomatik, post otomatik, time_stamp otomatik sadece content olacak, tupple olarak kullandığımız için virgül kullanıyoruz, list olarak da yazabiliriz fark etmez.

<forms.py> ->
```py
from django import forms
from .models import Post, Comment, Category

class PostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Post.OPTIONS)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select')
    class Meta:
        model = Post
        fields = (
            'title',
            'image',
            'content',
            'category',
            'status',
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    
```


Şuan modellerimiz tamam, formlarımız tamam, artık view lerimizi oluşturmaya başlayacağız;
<view.py> a gidiyoruz, (frontend de template oluştururken bir tane home page yapmadık, home page imizi blogların listelendiği template olarak düşündük biz extradan bir home page yapmadık.) def post_list(request):  postlarımızı sayfada listeleyeceğiz,  qs = Post.objects.all()    (qs-queryset genelde bu şekilde kullanılıyor, obj-objects için de böyle kullanılıyor genelde), Post u .models den import ediyoruz, 
context={
    'object_list':qs
}
return render(request, 'blog/post_list.html', context)
<views.py> ->
```py
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    context={
        'object_list':qs
    }
    return render(request, 'blog/post_list.html', context)
```

Şimdi ne yapıyorduk template ler kısmında bir tane base template oluşturup, onun haricinde application içerisinde oluşturduğumuz template lerimizi koyacaktık. 
base template i oluşturmak için <settings.py> a gidip TEMPLATES = listesinin içerisine   
<settings.py> -> 
```py
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

```

<settings.py> şunları yazıyoruz 'DIRS': [BASE_DIR, 'templates'];-> 
```py
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

Bundan sonra src nin içerisinde bir tane templates isimli new folder, yeni klasör açıp bunun içerisine de <base.html> oluşturuyoruz.
Şimdi bir tane normal html koyuyoruz ama daha sonra bootstrap in starter templae i var onu koyacağız, bootstrap le yapacağız ondan sonra.
title ı değiştiriyoruz Clarusway Blog yazıyoruz.
body nin içine block yapısı oluşturuyoruz.     
{% block content %}   {% endblock content %}
<base.html> ->
```py
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clarusway Blog</title>
</head>
<body>
    
    {% block content %}
        
    {% endblock content %}
        
</body>
</html>
```


## home/list page ->

blog içerisinde oluşturacağımız templates ler için application klaörümüz olan blog klasörünün içerisine templates isminde bir klasör oluşturup, içerisine yine application ımızın ismiyle bir klasör daha oluşturup içerisine de home page imiz olan <post_list.html> template imizi oluşturuyoruz. içerisine girip <base.html> dosyamızı extend ediyoruz. {% extends 'base.html' %} sonra block larımızı koyuyoruz, (birçok block oluşturup içerisine farklı kodlar konulabilir.)
{% block content %}
    
{% endblock content %}

<post_list.html> ->
```py
{% extends 'base.html' %} 
{% block content %}
    
{% endblock content %}
```

view.py gidiyoruz, post_list view ine bakıyoruz, şimdi listelerken nasıl yapıyorduk, all yaptığımız için queryset dönecek, onun için bizim <post_list.html> içerisinde blockların arasında for ile döngü oluşturmamız gerekiyor. object_list bizim views.py da oluşturduğumuz context içerisindeki key değerini aldık bunun içerisinde döngü oluşturuyoruz, bunun içerisindeki object in nelerini almak istiyoruz? {{object.title}} ,  resmi göstereceğiz, resmi gösterirken farklı birşey kullanıyoruz image tagı içerisinde src nin içerisinde gösteriyoruz<img src="{{ object.image.url }}" alt="">   ,  {{object.content}}

<post_list> ->
```py

{% extends 'base.html' %} 
{% block content %}

{% for object in object_list %}
{{object.title}}
<img src="{{ object.image.url }}" alt="">
{{object.content}}
{% endfor %}
    
{% endblock content %}

```

save edip app imizin <urls.py> imize gidip path imizi işliyoruz. .views imizden post_list view imizi import ediyoruz ve path imizi işliyoruz. 

<urls.py> ->
```py
from django.urls import path
from .views import post_list

urlpatterns = [
    path('', post_list, name='list')
]
```

Hata verdi! project urls.py daki comment yapılmış olan include path inin comment ini kaldırdık, post_list.html deki image tag ını comment e aldık, server ı yeniden çalıştırdık, çalıştı, 
h1 ve p tagları arasına aldık ve tekrar çalıştırdık, postları listeledik.
<post_list> ->

```py

{% extends 'base.html' %} 
{% block content %}

{% for object in object_list %}
<h1>{{object.title}}</h1>
<!-- <img src="{{ object.image.url }}" alt=""> -->
<p>{{object.content|truncatechars:20}}</p>
{% endfor %}
    
{% endblock content %}
```

object.content|truncatechars:20 ne işe yarıyor? ->

blurb_text = 'You are pretty smart!'
{{ blurb_text|truncatechars:15 }}
You are pretty…

blurb_text = 'You are pretty smart!'
{{ blurb_text|truncatewords:3 }}
You are pretty…

blurb = '<p>You are <em>pretty</em> smart!</p>'
{{ blurb|truncatewords_html:3 }}
<p>You are <em>pretty…</em></p>



Bundan sonraki kısmı frontend, tasarım.. daha sonra yapacağız, kaçmayacağız :))

image yorumda kaldı onu da açıyoruz. Açıp resmi de görüyoruz.

Bunu normal api ile yazarken de bunu api olarak döneceğiz, frontende göndermeyeceğiz, bunu jason response olarak döneceğiz, yine aynı şey, ondan sonra jason response daki api endpoint i alıp react ta axios ile alıp componentleri oluşturup, kullanacağız.


## create page ->

post_list view imiz bitti, create view i yapalım, arkasından update yapacağız.
Create biraz daha farklı bir önceki yaptığımıza göre bi tık farklı; <view.py> a gidip view imizi yazmaya başlıyoruz,
def post_create(request):
formumuzu oluşturmuştuk (PostForm) , onu kullanmak için import ediyoruz, from .forms import PostForm   ,  form = PostForm() önce PostForm umuzu boş bir şekilde ekrana getiriyoruz, bunun bir de kısa yöntemi var;
get ise boş bir form getir ondan sonra eğer request method post ise
formu bu sefer PostFormun içerisini request.Post ile doldur diyoruz ama biz media file da upload ettiğimiz için bir method daha eklememiz gerekiyor, request.FILES
if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)

<!-- form = PostForm()
if request.method == 'POST':
    form = PostForm(request.POST, request.FILES) -->
Bu yöntemi bazen şöyle görebilirsiniz arkadaşlar kısaca ondan bahsedeyim sonra devam ederiz ;
form = PostForm(requset.POST or None, request.FILES or None)
Bu ne anlama geliyor?  Post varsa post u al yoksa none olsun yani boş, files varsa files ı al yoksa none olsun yani boş. Yukarıdaki üç satır kod yerine tek satırda çözmüş. Hiç bir farkı yok iki de aynı kapıya çıkıyor.

Tamam devam ediyoruz bizim yöntemle, if form.is_valid(): formumuz valid ise,  şimdi burada bir işlem yapmamız gerekiyor bu formdan veriyi db ye gönderiyoruz ya db de author ın kim olduğunu bizim db ye söylememiz lazım. onun için ekstradan bir işlem yapacağız, bir farklılık da bu, eğer formumuz valid ise bir tane obje oluşturuyoruz post = form.save(commit=False) ne demek bu? bu datayı kaydet ama db ye işleme, önce ben birşey ekleyeceğim (bir user) bu post a. kaydettim bu postu, post.author = request.user postun içerisindeki author benim request objemin içerisindeki user a eşit olacak diyoruz yani bu postu yazan kişi şuan oturum açmış bulunan user, burada author kısmını doldurmuş oluyoruz. işlem bittikten sonra post.save()  diyoruz.
Burası önemli bu çok kullanılan bir yapı.

Postu oluşturduktan sonra redirect ediyoruz ama önce redirect i import ediyoruz,
return redirect('list')

Ha bu arada şöyle birşey daha var, mesela bizim birkaç tane daha app imiz var ve bu applerimizin de path name leri arasında da list olabilir, o zaman djangonun kafası karışıyor, bunu önlemek için   app urls.py da app_name = 'blog'  diye bir name space oluşturuyoruz ve blog diyoruz buna, nasıl kullanıyoruz bunu ;
return redirect('blog:list') blog application ın list ine gönder bunu!

app imizin <urls.py> ->
```py
from django.urls import path
from .views import post_list, post_create

app_name='blog'
urlpatterns = [
    path('', post_list, name='list'),
    path('create/', post_create, name='create'),
]
```

artık return redirect('blog:list')  blog app imizin list ine döndür diyerek view imizin context ini oluşturup template imize gönderiyoruz;
context = {
    'form':form
}
return render(request, 'blog/post_create.html', context)
<views.py> ->
```py
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    qs = Post.objects.all()
    context={
        'object_list':qs
    }
    return render(request, 'blog/post_list.html', context)

def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:list')
    context = {
        'form':form
    }
    return render(request, 'blog/post_create.html', context)
```

Şimdi bunun url ini oluşturalım, post_create view imizi import edip path imizi yazıyoruz.

<urls.py> ->
```py
from django.urls import path
from .views import post_list, post_create

app_name = 'blog'
urlpatterns = [
    path('', post_list, name='list'),
    path('create/', post_create, name='create')
]
```

Akabinde create template imizi oluşturuyoruz; base.html den extends edip, block larımızı yazıp arasına form oluşturuyoruz. form un action ı aynı sayfada olduğu için birşey yazmıyoruz, method='POST' olacak,
method post olduğu için csrf token tag ini {% csrf_token %} koyuyoruz, sonra bunun içerisie formumuzu paragraf tag i içerisinde gönderiyoruz, bir tane de button ekliyoruz type='submit' (POST diye) ,

<post_create.html> ->

```html
{% extends 'base.html' %}

{% block content %}

<form action="" method="POST">
    {% csrf_token %}
    {{form.as_p}}
    <button type="submit">POST</button>
</form>

{% endblock content %}
    
```

runserver yapıp create/ sayfasına gidiyoruz, formu görüyoruz, dolduryoruz, post diyoruz, yeni bir post oluşturduk.  
post.author=......   kısmını yoruma alarak ve de form.save() yaparak çalıştırdık, create etmeye çalıştık, Post has no author hatası aldık. Ben bunu db ye kaydedeceğim ama Post un içinde author a ait bir bilgi yok, author da doldurulması zorunlu bir alan, onun için hata veriyor.

slug da username ve title kullandık, ancak bir user aynı title da yani başlıkta bir post daha oluşturunca hata alıyoruz, şöyle bir mantık kurmuştuk eğer username unique ise bundan sonra title eklerse sıkıntı yaşamayız ama aynı user aynı title ile post oluşturunca hata almaya başladık.   
biz aynı kullanıcı ile post lar eklediğimiz için eğer aynı post u tekrar oluşturursak bize hata verebiliyor, o yüzden slug ımızı daha esnek yapmamız gerekiyor, bunu biraz değiştireceğiz,   
python uuid kütüphanesinin uuid4() modülü ile random sayı ürettirip onu ekleyeceğiz.

<signals.py> ->
```py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Post

@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + ' ' + instance.title)

```

blog app imizin içerisine kendi script imizi yazacağımız bir file oluşturuyoruz, ismine de best practice <utils.py> diyoruz. uuid4 u kullanacağız, document e gidip inceliyoruz, generate a random UUID yani bize random (universal unique id) uuid üretmesini istiyoruz. uuid import ediyoruz, bir tane function yazıyoruz, def get_random_code():    code = uuid.uuid4() bu bize integer olarak dönüyor ama bunu stringe çeviriyoruz, code = str(uuid.uuid4())   bakalım bize ne dönüyor  return code    print(get_random_code())   çalıştırdık ve terminalde uzun bir uniq kod döndü biz bu kadar uzun istemiyoruz 11 karakter istiyoruz, arada tire de olmasın istiyoruz, burada algoritma düşünüyoruz, nasıl bir algoritma kurabiliriz? 
    code = str(uuid.uuid4())[:11] başlangıçtan itibaren 11 karakter al diyoruz, replace('-','') metodumuzla tireyi şununla (space değil) değiştir diyoruz.  
çalıştırdık ve tireyi aradan çıkararak 10 karakterlik bir unique değer döndürdü.
```

<utils.py> ->

```py
import uuid

def get_random_code():
    # code = uuid.uuid4()
    code = str(uuid.uuid4())[:11].replace('-','')
    return code
```


Burası çalıştıktan sonra <signals.py> a gidip username kısmını değiştireceğiz, .utils den get_random_code u import ediyoruz,
slugify kısmına önce instance.title + ' ' + get_random_code()  yazıyoruz.

<signals.py> ->

```py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Post
from .utils import get_random_code

@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + ' ' + get_random_code())

```

runserver yapıp çalıştırıyoruz, yeni bir post oluşturuyoruz admin panelde ve slug da istediğimiz uniq değeri görüyoruz.

<views.py> a gidiyoruz, list view yapmıştık ama bir şeyi yanlış yapmışız, modelimizde bir published yani görünür, bir draft sadece user a görünür olsun dedik, ama bizim frontend imizde draft da olsa hepsi görünüyor, eksik yaptığımız birşey var, burada bizim db den status ü p (published) olanları (db de kayıtlı şekliyle p) getir bana dememiz lazım, bunun için filter kullanacağız,  qs = Post.objects.filter(status='p')  yani db ye git db de status ü p (Published) olanları getir, ben frontend e sadece p (Published) olanları göndereceğim diyoruz. (veya   qs = Post.objects.exclude(status='d') da yazılabilir.)

<views.py> ->

```py
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    qs = Post.objects.filter(status='p')
    context = {
        'object_list':qs
    }
    return render(request, 'blog/post_list.html', context)

def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:list')
    context = {
        'form':form
    }
    return render(request, 'blog/post_create.html', context)

```

runserver yaptık artık sadece published olanlar template e gönderiliyor. Sonra bu Post ların yazarlarının drafta veya published e çekebilmesini update etmelerini sağlayacağız.

create page ine gittik ve create formumuzun geldiğini gördük. Burada da bir eksiğimiz var; biz bir image file ekliyoruz ama bize yine de default image ı gösteriyor, onu düzelteceğiz, biz post_create.html template imizi yazarken form a ekstradan bir attribute yazmamız gerekiyor, bu django ile değil html ile alakalı bir durum picture, pdf, video  upload ederken formda enctype="multipart/form-data" attribute ünün eklenmesi gerekiyor.
<post_create.html> ->
```py
{% extends 'base.html' %}
{% block content %}

<form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{form.as_p}}
    <button type="submit">POST</button>
</form>

{% endblock content %}    
```

çalıştırdık, create ettik, image ı yüklediğini gördük.


## detail page ->

detail page i oluşturacağız; 
<view.py> a gidiyoruz ve post_detail view imizi yazıyoruz; 
def post_detail(request, slug)  request i alıyor, (burada biz specific yani özel bir obje ile işlem yapacağımız için o specific objeye ait uniq bir değere ihtiyacımız var), uniq bir değere  ve normalde buraya pk, id yazıyorduk ama bu projede uniq değer olaraak slug kullanmıştık onu yazıyoruz,
obj = get_object_or_404(Post, slug=slug) requst le beraber gelen slug ı slug a eşit olan Post taki objeyi alıp bunu frontend e gönderiyoruz (get_object_or_404 u da django.shortcuts dan import ediyoruz), bir de post_list te yani ana sayfadaki listede bir tane anchor tag belirleyip ona tıkladığımızda bizi pos_detail sayfasına yönlendirecek, burada hiçbir post işlemi yok direct sayfa render ediyoruz, bunları daha geliştireceğiz yavaş yavaş ana çatımızı şeklillendirelim, post_detail in içerisine CommentForm u göndereceğiz, daha güzelleştireceğiz. 
context = {
    'object': obj
}
return render (request, 'blog/post_detail.html', context)

<views.py> ->

```py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    qs = Post.objects.filter(status='p')
    context = {
        'object_list':qs
    }
    return render(request, 'blog/post_list.html', context)

def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:list')
    context = {
        'form':form
    }
    return render(request, 'blog/post_create.html', context)

def post_detail(request, slug):
    obj = get_object_or_404(Post, slug=slug) # slug=learn-drf-3c78be2186
    context = {
        'object': obj
    }
    return render(request, 'blog/post_detail.html', context)
```

blog/templates/blog klasörü içerisine <post_detail.html> template imizi oluşturuyoruz, <base.html> den extends i yapıyoruz, sonra object in neyini görmek istiyorsak belirtiyoruz.

<post_detail.html> ->

```html
{% extends 'base.html' %}
{% block content %}

<h1>{{ object.title }}</h1>
<img src="{{ object.image.url }}" alt="">
<p>{{ object.content }}</p>

{% endblock content %}
```

<urls.py> a gidip <post_detail.html> in path ini, yolunu tanımlıyoruz, daha önce path('<str:id>/', post_detail, name='detail') diye tanımlıyorduk, şimdi id değil de slug kullandığımız için path('<str:slug>/', post_detail, name='detail'), şeklinde tanımlıyoruz.

<urls.py> ->

```py
from django.urls import path
from .views import post_list, post_create, post_detail

app_name='blog'
urlpatterns = [
    path('', post_list, name='list'),
    path('create/', post_create, name='create'),
    path('<str:slug>/', post_detail, name='detail'),
]
```

ayrıca <post_list.html> template inden, sayfasından <post_detail.html> template ine, sayfasına yönlendirmek için <post_list.html> template inde bir tane anchor tagı oluşturuyoruz, anchor tag inin href ine detail page in url ini ve slug ı koyuyoruz {% url 'blog:detail' object.slug %} , yani url e blog:detail yaz arkasından slug ı koy diyoruz, içerisine de h1 tag ının içerisinde bulunan object.title ı koyuyoruz.

<post_list.html> ->

```html
{% extends 'base.html' %}
{% block content %}

{% for object in object_list %}
<a href="{% url 'blog:detail' object.slug %}">
    <h1>{{object.title}}</h1>
</a>
<img src="{{ object.image.url }}" alt="">
<p>{{object.content|truncatechars:20}}</p>
{% endfor %}

{% endblock content %}
```

detail page imizi de oluşturduk, bunları süsleyeceğiz..


## update page ->

sırada ne var, create ve detail yaptık şimdi update yapıcaz; <views.py> a gidip post_update view imizi yazıyoruz, def post_update(request, slug):    (burada biz specific yani özel bir obje ile işlem yapacağımız için o specific objeye ait uniq bir değere ihtiyacımız var, o da yine slug)
form = PostForm(request.POST or None, request.FILES or None, instance=obj) ayrıca form bize gelirken dolu gelmesi için instance attribute ünü kullanıyoruz, instance obj (db den get ettiğimiz specific objenin tüm verileriyle dolu olarak gelmesi) ye eşit olsun diyoruz,  
if form.is_valid():    eğer form valid ise
form.save()    form u save et
return redirect('blog:list')    list e redirect et (eğer burada redirect yapmazsak kullanıcı refresh veya geri tuşuna bastığında form birdaha gönderilir, onu engellemek için kullanıcıyı redirect ile post yapamayacağı bir sayfaya gönderilir. )
eğer method umuz get ise yani post yapılmamışsa template ne göndersin? ,
context={
    'object':obj,
    'form': form
}
return render(request, 'blog/post_update.html', context)

<views.py> ->

```py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    qs = Post.objects.filter(status='p')
    context = {
        'object_list':qs
    }
    return render(request, 'blog/post_list.html', context)

def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:list')
    context = {
        'form':form
    }
    return render(request, 'blog/post_create.html', context)

def post_detail(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    context = {
        'object': obj
    }
    return render(request, 'blog/post_detail.html', context)

def post_update(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('blog:list')
    context={
        'object':obj,
        'form':form
    }
    return render(request, 'blog/post_update.html', context)

```

blog/templates/blog klasörü içerisine <post_update.html> template imizi oluşturuyoruz, <base.html> den extends i yapıyoruz, form gösteriyoruz, action ımız bu view da olduğu için birşey yazmıyoruz, method='POST', img kullandığımız için ; enctype="multipart/form-data",   method='POST' kullandığımız için {% csrf_token %} {{ form.as_p }}
olmazsa olmaz submit button

<post_update.html> ->

```html
{% extends 'base.html' %}
{% block content %}

<h2>Update {{ object.title }}</h2>
<form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Update</button>
</form>

{% endblock content %}

```

<urls.py> a gidip <post_update.html> in path ini, yolunu tanımlıyoruz, daha önce path('<str:id>/', post_detail, name='detail') diye tanımlıyorduk, şimdi id değil de slug kullandığımız için path('<str:slug>/update/', post_update, name='update'), şeklinde tanımlıyoruz.

<urls.py> ->

```py
from django.urls import path
from .views import post_list, post_create, post_detail, post_update

app_name='blog'
urlpatterns = [
    path('', post_list, name='list'),
    path('create/', post_create, name='create'),
    path('<str:slug>/', post_detail, name='detail'),
    path('<str:slug>/update/', post_update, name='update'),
]
```


## delete page ->

Post delete i yapalım sonra frontend i güzelleştireceğiz, <view.py> a gidiyoruz, post delete view imizi yazıyoruz, def post_delete(request, slug):   specific bir objeyi belirtmek için yine uniq bir değer olan slug ı request ile birlikte kullanıyoruz, ve diğer kodlar...

<views.py> ->

```py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    qs = Post.objects.filter(status='p')
    context = {
        'object_list':qs
    }
    return render(request, 'blog/post_list.html', context)

def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:list')
    context = {
        'form':form
    }
    return render(request, 'blog/post_create.html', context)

def post_detail(request, slug):
    obj = get_object_or_404(Post, slug=slug)  # slug=learn-drf-3c78be2186
    context = {
        'object': obj
    }
    return render(request, 'blog/post_detail.html', context)

def post_update(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('blog:list')
    context={
        'object':obj,
        'form':form
    }
    return render(request, 'blog/post_update.html', context)
    
def post_delete(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('blog:list')
    context = {
        'object':obj
    }
    return render(request, 'blog/post_delete.html', context)
```



<urls.py> a gidip post_delete view ini import ediyoruz, <post_delete.html> in path ini, yolunu tanımlıyoruz, daha önce path('<str:id>/', post_detail, name='detail') diye tanımlıyorduk, şimdi id değil de slug kullandığımız için path('<str:slug>/delete/', post_delete, name='delete'), şeklinde tanımlıyoruz.

<urls.py> ->

```py
from django.urls import path
from .views import post_list, post_create, post_detail, post_update, post_delete

app_name='blog'
urlpatterns = [
    path('', post_list, name='list'),
    path('create/', post_create, name='create'),
    path('<str:slug>/', post_detail, name='detail'),
    path('<str:slug>/update/', post_update, name='update'),
    path('<str:slug>/delete/', post_delete, name='delete'),
]
```
url imizi de oluşturduk şuan ne yapacağız, template i oluşturacağız.
{{ object }} bize burada object ne dönüyor? title dönüyor. biraz önce onject.title yazdık ama gerek yok, ama kafalar karışmasın diye yine de yazıyoruz, <p>Are you sure delete {{ object.title }}</p>
form açıyoruz, method='POST'
{% csrf_token %}
yes (submit button ile form mu submit ediyoruz) ve cancel (anchor tag ı ile list page e yönlendiriyoruz) button u yapacağız,


<post_delete.html> ->

```html
{% extends 'base.html' %}
{% block content %}

<p>Are you sure delete {{ object.title }}</p>
<form action="" method="POST">
    {% csrf_token %}
    <a href="{% url 'blog:list' %}">Cancel</a>
    <button type="submit">Yes</button>

</form>

{% endblock content %}
```

çalıştırıyoruz, bir post ta tıklayıp detail sayfasına geliyoruz ve url e http://127.0.0.1:8000/learn-drf-30c99a262e/delete   delete yazınca bizi delete html template ine gönderiyor, cancel dersek anchor tag i bizi list e , Yes dersek de bu sefer view logic i post u silip bizi list e redirect ediyor.



Şimdi bunun frontend ini süsleyeceğiz, like kalp, göz ekleyeceğiz,

base.html e gidiyoruz, bootstrap ten starter template i var onu koyacağız, dha farklı hazır templateleri de var , onları indirip kullanabilirsiniz ama bu şimdilik yeterli bizim için,
bootstrap e gidiyoruz (https://getbootstrap.com/docs/4.5/getting-started/introduction/)  v4.5 versiyonundaki starter templat ini kopyalayıp, temizlediğimiz base.html imize yapıştırıyoruz. (Yoruma alınmış kısımları silebiliriz)
body nin içinde h1 tagını silip, önceki base.html imizde bulunan bloklarımızı yerleştiriyoruz. Blocklarımızı div in içerisine alıyoruz, class ına da bootstrap in container diyoruz
```html
    <div class="container">
        {% block content %}    
        {% endblock content %}
    </div>
```
değişikliği gördük, şimdi bunu card componentine koyup yavaş yavaş ilerleyeceğiz.
Navbar ekleyeceğiz, navbar eklemenin farklı yollarını göreceğiz, include tag i var exclude vardı ya inherit ediyorduk, bir de include edebiliyorsunuz yine onları,
navbar kodlarımız için bir template oluşturacağız, base.html in bulunduğu klasöre navbar.html dosyası oluşturuyoruz.Neden? base de fazla kodumuz olmasın, bizim navbar da değişiklik yaparsam eğer base html li fazla kurcalamayayım diye navbar için bir template oluşturuyoruz. (Ayrıca https://getbootstrap.com/docs/4.5/components/navbar/ dan da istediğiniz bir navbarı alıp aklayebilisiniz, sağ tarafta olan linkler için ise birkaç kod yazmanız gerekiyor.) Buradaki can alıcı nokta if bloklarının içindeki kullanıcı login ise şu linkleri göster, değilse bu linkleri göster kısmıdır. (template lerimiz daha hazır olmadığı için onların url kısımlarını körledik.)

<navbar.html> ->

```html
<header class="site-header">
    <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top ">
        <div class="container">
            <a class="navbar-brand mr-4" href="{% url 'blog:list' %}">Umit Blog</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar Toggle" 
            aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toogler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarToggle">
                <div class="navbar-nav mr-auto">
                    <a class="nav-item nav-link" href="{% url 'blog:list' %}">Home</a>
                    <a class="nav-item nav-link" href="#">About</a>
                </div>
                <!-- Navbar Right Side -->
                <div class="navbar-nav">
                    {% if user.is_authenticated %}
                    {% comment %} {% url 'logout' %} {% endcomment %}
                    <a class="nav-item nav-link" href="#">Logout</a>
                    {% comment %} {% url 'profile' %} {% endcomment %}
                    <a class="nav-item nav-link" href="#">Profile</a>
                    <a class="nav-item nav-link" href="{% url 'blog:create' %}">New Post</a>
                    {% else %}
                    {% comment %} {% url 'profile' %} {% endcomment %}
                    <a class="nav-item nav-link" href="#">Login</a>
                    {% comment %} {% url 'register' %} {% endcomment %}
                    <a class="nav-item nav-link" href="#">Register</a>
                    {% endif %}
                </div>
            </div>
        </div>
    </nav>
</header>
```

navbar template imizi oluşturduktan sonra base.html e gidip include ediyoruz, body nin içine block larımızın üstüne  {% include 'navbar' %}  ediyoruz. navbar diye yazınca hata verecek,


<base.html> ->

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

    <title>Blog App</title>
  </head>
  <body>
    {% include 'navbar.html' %}
    <div class="container">
        {% block content %}
    
        {% endblock content %}
    </div>
    
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

    <!-- Option 2: jQuery, Popper.js, and Bootstrap JS
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>
    -->
  </body>
</html>
```

kaydedip home page imiz olan list template imizin sayfasına baktığımız da navbar ın geldiğini gördük ama css eklememiz gerekiyor. base.html de bir link oluşturacağız, static file lardan bahsetmiştik css, javascript, image, code larını koyduğumuz dosya, şimdi hazırladığımız css file larını static klasörüne koyacağız. App imizin içine static isminde bir klasör oluşturuyoruz, isim önemli, içine de aynı templates klasöründe olduğu gibi app imizin ismiyle aynı isimde 'blog' bir klasör oluşturuyoruz , içine de main.css isminde kendi css lerimizi koyacağımız bir css dosyası oluşturuyoruz. Django da css, javascript, image kullanacağınız zaman yapıyı bu şekilde kuracaksınız. static diye bir klasör oluşturacaksınız, içerisine blog oluşturmak size kalmış oluşturmayabilirsiniz ama application ları name spacing yapmak önemli, içerisine de main.css dosyamızı oluşturup, css kodlarımızı yazıp,  base.html e gidip bootstrap css linkinin altına kendi css linkimizi ekleyeceğiz. 

blog/static/blog <main.css> ->

```css
body {
    background: #fafafa;
    color: #333333;
    margin-top: 5rem;
}

h1,
h2,
h3,
h4,
h5,
h6 {
    color: #444444;
}

ul {
    margin: 0;
}

.bg-steel {
    background-color: #5f788a;
}

.site-header .navbar-nav .nav-link {
    color: #cbd5db;
}

.site-header .navbar-nav .nav-link:hover {
    color: #ffffff;
}

.site-header .navbar-nav .nav-link.active {
    font-weight: 500;
}

.content-section {
    background: #ffffff;
    padding: 10px 20px;
    border: 1px solid #dddddd;
    border-radius: 3px;
    margin-bottom: 20px;
}

.account-img {
    height: 110px;
    width: 110px;
    margin-right: 20px;
    margin-bottom: 16px;
}

.account-heading {
    font-size: 2.5rem;
}
```


base.html e gidip css dosyamıza link ekleyeceğiz, Ancak djangoda static file ları kullanmak için base.html sayfamızın başına {% load ststic %} yazmamız gerekiyor. Link eklerken de href ine djangonun url belirtme yazım şekliyle url belirteceğiz, url de url yazıyorduk bunda ise static yazıyoruz, <link rel="stylesheet" href="{% static 'blog/main.css' %}">   ,

<base.html> ->

```html
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'blog/main.css' %}">

    <title>Blog App</title>
  </head>
  <body>
    {% include 'navbar.html' %}
    <div class="container">
        {% block content %}
    
        {% endblock content %}
    </div>
    
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

    <!-- Option 2: jQuery, Popper.js, and Bootstrap JS
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>
    -->
  </body>
</html>
```

django static klasörünü mutlaka istiyor, burda biz app içinde oluşturduk, bu static klasörünü app içerisinde değil de hani settings.py da TEMPLATES  de 'DIRS':[BASE_DIR, 'templates']  base dır a templates ekle demiştik ya, burada static file ımızı da o şekilde tanımlayabiliriz.

```
STATIC_URL = .......
MEDIA_URL = ......
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_RO.......
```

Base directory nin içerisinde bir tane static diye bir klasör oluşturuyoruz, bu şekilde yaparsak eğer ana projemizin içerisinde bir tane ststic klasörü oluşturup main.css imizi bunun içerisine de koyabiliriz. Django bundan ne anlıyor senin static file ların static diye bir klasörün altında ben o static in içerisine gidip oaradaki ststic file (css veya js) ını alacağım, sonra nerede load ettiysen base.html de mi? buradaki template e load edicem ama aload etmem için bana url ini vermen gerekiyor, link in href inde de satatic e özgü url ini {% static 'blog/main.css' %} veriyoruz.

Şimdi home page imize gidiyoruz, css lerimizin geldiğini ve çalıştıklarını görüyoruz, login olmadığımızda navbar da gelen  menüleri görüyoruz, kendi login sayfamızı/template imizi oluşturmadığımız için admin panelden login oluyoruz (djangoda session var, browserda bir sekmede login olunmuşsa diğer sekmelerde de login olarak tutuyor.) ve home page e döndüğümüzde if bloglarının çalıştığını ve login olmuş kullanıcı menülerini gösterdiğini görüyoruz. Ayrıca New Post menüsüne tıkladığımızda post oluşturmak için bizim daha önce hazırladığımız create template imize gönderiyor, Umit Blog a tıkladığımızda list template imize gönderiyor,  navbar ımız çalışıyor.
base.html imizi oluşturduk,  navbar ımızı oluşturduk, footer ekleyebilirsiniz, hangi sayfaya koymak istiyorsanız oradan include edebilirsiniz. 
Veya pageination codunuz varsa pagination.html diya ayrıyeten yazıp, onu include edebilirsiniz daha sonra, birçok şey yapabilirsiniz. 

Şimdi list.html imizi düzeltelim, yine bootstrap components cards (https://getbootstrap.com/docs/4.5/components/card/) ı biraz modifiye edip kullandık, 
önceki <post_list.html> ->
```html
{% extends 'base.html' %}
{% block content %}

{% for object in object_list %}
<a href="{% url 'blog:detail' object.slug %}">
    <h1>{{object.title}}</h1>
</a>
<img src="{{ object.image.url }}" alt="">
<p>{{object.content|truncatechars:20}}</p>
{% endfor %}

{% endblock content %}
```

Nasıl modifiye ettik? şimdi bizim bir tane post umuz yok, birçok post umuz var onun için bir for döngüsü kullanıyoruz, bir liste döneceğiz listemiz: object_list nereden alıyoruz bu object_list ' i? views.py da context in içine object_list olarak koymuşuz tüm published post larımızı , ve object_list imizi context içerisinde post_list template imize göndermişiz, işte o listenin elemanlarını card componentinin içerisinde göstereceğiz, card componenetimiz card class ı olan div ile başlıyor, yan yana görünmesi için row koyduk, o row u da column lara böldük, img source unu obj nin image ının url ini koyduk, card body de card title kısmına anchor tag ı ile detail page e link verdik, postun contentini koyuk, sonra asıl yapacağımız şeyler: mesaj sayısı, görüntüleme sayısı ve like sayısını koyacağız, ayrı bir p tag ı içerisinde font awesome dan class ları alıp span tagı içerisinde bunları yerleştirdik sonra {{ obj.comment_count }} bunları modelde bir method belirleyeceğiz bu methodlarla count sayılarını alacağız. Şimdilik onları yoruma aldık ki hata vermesin.
Sonraki p tag ının içerisinde de ne kadar zaman önce post edildiğinin gösterimi için bir tane template tag ı var, şimdi modelde publish date imiz vardı ya ne  yapıyordu? post objemiz oluştuğu zaman bir tarih zaman veriyor, timesince ise şu anki zaman ile post un oluşturulduğu zaman arasındaki farkı alıyor, şukadar gün şu kadar saaat önce diye aradaki farkı alabiliyoruz.
font awesome nereden bulduk; fontawesome artık register olmanızı istiyor, register olduktan sonra bir tane şey veriyor, start for free diyorsunuz, mail inizi girmenizi istiyor,   (https://fontawesome.com/start) sonra mailinize gelen link ile bize özel oluşturulmuş script codunun bulunduğu sayfaya yönlendiriyor, script codunu base.html de body nin en alt kısmına ekliyoruz. Önceden link veriyordu, şimdi script veriyor. Daha sonra yorum için comment, görüntüleme için göz, beğeni için kalp icon larını seçip span tag ının içinde <i class="far fa-comment-alt ml-2"></i> şeklinde yazıyoruz.


sonraki <post_list.html> ->
```html
{% extends 'base.html' %}
{% block content %}
<h1 style="text-align: center;">Umit Blog</h1>
<div class="row mt-5">
    {% for obj in object_list %}
    <div class="col-4">

        <div class="card shadow p-3 mb-5 bg-white rounded" style="width: 18rem; height: 25rem;">
            <img src="{{ obj.image.url }}" class="card-img-top" alt="post_image">
            <hr>
            <div class="card-body">
                <h5 class="card-title"><a href="{% url 'blog:detail' obj.slug %}">{{obj.title}}</a></h5>
                <p class="card-text">{{obj.content|truncatechars:20}}</p>
                <p> 
                    {% comment %} {{ obj.comment_count }} {% endcomment %}     
                    <span><i class="far fa-comment-alt ml-2"></i></span>
                    {% comment %} {{ obj.view_count }} {% endcomment %}     
                    <span><i class="fas fa-eye ml-2"></i></span>
                    {% comment %} {{ obj.like_count }} {% endcomment %}     
                    <span><i class="far fa-heart ml-2"></i></span>
                </p>
                <p class="card-text"><small>
                        Posted {{ obj.publish_date|timesince }} ago.
                    </small>
                </p>

                </p>
            </div>
        </div>
    </div>

    {% endfor %}
</div>
{% endblock content %}

```


font awesome nereden bulduk; fontawesome artık register olmanızı istiyor, register olduktan sonra bir tane şey veriyor, start for free diyorsunuz, mail inizi girmenizi istiyor,   (https://fontawesome.com/start) sonra mailinize gelen link ile bize özel oluşturulmuş script codunun bulunduğu sayfaya yönlendiriyor, script codunu base.html de body nin en alt kısmına ekliyoruz. Önceden link veriyordu, şimdi script veriyor.

<base.html> ->

```html
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'blog/main.css' %}">

    <title>Blog App</title>
  </head>
  <body>
    {% include 'navbar.html' %}
    <div class="container">
        {% block content %}
    
        {% endblock content %}
    </div>
    
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

    <!-- Option 2: jQuery, Popper.js, and Bootstrap JS
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>
    -->

    <script src="https://kit.fontawesome.com/f3876d5d9f.js" crossorigin="anonymous"></script>

  </body>
</html>
```


home/list page de card ların içerisindeki postların yorum için comment, görüntüleme için göz, beğeni için kalp icon larının yanında counter sayılarını koyacağız, bu sayıları biz post modeli üzerinden alabiliriz, çünkü post list te biz post objesi üzerinde dönüyoruz, view imiz de Post objects inden filter ettiğimiz için Post modülünden bu methodları yazdık. <models.py> a gidip oluşturduğumuz Post modelinin altına str metodunun da altına  def comment_count(self): methodumuzu yazıyoruz, içerisine self alacak çünkü bu bizim Post class ımızın methodunu yazıyoruz, 
(bir post un birden çok comment i olabilir ama bir comment in bir post u olabilir.) bize bu method return self.comment_set.all().count()   bütün commentlerimizin sayısını veriyor.  (Comment class ımızdaki post, comment küçük harf ile yazılacak, djangonun özelliği,  comment_set ile bizi post modelimize ulaştırıyor, post modelimizden de bütün commentlerin sayısını al (djangonun orm yapısından dolayı biraz karışıkmış gibi görünüyor.))

view count için de yine view imizi küçük harfle kullanıyoruz     
def view_count(self):     return self.postview_set.all().count()

like count için de         def like_count(self):    return self.like_set.all().count()

child dan parentta ulaşmak için bu method u kullanmak gerekiyor, child daki forignkey den parenta ulaşmak için bu methodu kullanmak gerekiyor. 

<models.py> ->

```py
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, default='django.jpg')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True) # how-to-learn-django
    
    def __str__(self):
        return self.title
    
    def comment_count(self):
        return self.comment_set.all().count()
    
    def view_count(self):
        return self.postview_set.all().count()
    
    def like_count(self):
        return self.like_set.all().count()
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

```


<post_list.html> e gidip oluşturduğumuz count method lara ulaşacağız, yoruma aldığımız yerleri yorumdan kurtarıyoruz, buradan methodlara ulaşabiliyoruz, object oriented da cross oluşturduğumuzda method a. yazıp ulaşabiliyorduk ya, ama method da sonuna parantez koyuyorduk method un, burada template teyken method a ulaşırken sonuna parantez koymuyoruz. methodları span tag leri arasına icondan hemen sonra koyuyoruz.

algoritmayı view de değil de model de yazdık, modelde de class lardan yararlandık, class lara method yazabiliyoruz, methodlarla bu sayılara ulaşabiliyoruz, bunu view de yazıp viewe context in içerisinde koyup da yapabilirdik ama bu method daha kolay, yani bütün logic inizi view e koymanıza gerek yok, modele de koyabilirsiniz, template e de koyabilirsiniz, üçüne de koyabilirsiniz, ama ana logic view de olur.

<post_list.html> ->

```py
{% extends 'base.html' %}
{% block content %}
<h1 style="text-align: center;">Umit Blog</h1>
<div class="row mt-5">
    {% for obj in object_list %}
    <div class="col-4">

        <div class="card shadow p-3 mb-5 bg-white rounded" style="width: 18rem; height: 25rem;">
            <img src="{{ obj.image.url }}" class="card-img-top" alt="post_image">
            <hr>
            <div class="card-body">
                <h5 class="card-title"><a href="{% url 'blog:detail' obj.slug %}">{{obj.title}}</a></h5>
                <p class="card-text">{{obj.content|truncatechars:20}}</p>
                <p> 
                    {% comment %} {{ obj.comment_count }} {% endcomment %}     
                    <span><i class="far fa-comment-alt ml-2"></i>{{ obj.comment_count }}</span>
                    {% comment %} {{ obj.view_count }} {% endcomment %}     
                    <span><i class="fas fa-eye ml-2"></i>{{ obj.view_count }}</span>
                    {% comment %} {{ obj.like_count }} {% endcomment %}     
                    <span><i class="far fa-heart ml-2"></i>{{ obj.like_count }}</span>
                </p>
                <p class="card-text"><small>
                        Posted {{ obj.publish_date|timesince }} ago.
                    </small>
                </p>

                </p>
            </div>
        </div>
    </div>

    {% endfor %}
</div>
{% endblock content %}

```


çalıştırdık (runserver) sayıları gördük. admin panelden publish postlardan bir tanesine like, post view, comment ekledik ve home/list page de count ettiğini, logic in çalıştığını gördük.

blog application ı bitireceğiz, daha sonra user application ını kuracağız , orada authenticon kısmını kuracağız, profile page ini oluşturacağız, genel çatıyı kurduk, biraz daha süsleyeceğiz, birkaç tane daha form (comment form) ekleyeceğiz,

şimdi detail view imizi şekillendireceğiz, <views.py> a gidiyoruz, list view de olduğu gibi like message ve gösterme sayısını yerleştireceğiz, alta bir de comment formu koyacağız, kullanıcıdan comment almak için bir form oluşturmamız gerekiyor, zaten comment modelimiz var, bu modelden modelForm ile bir tane form oluşturacağız, bu formu da detail template imize göndereceğiz, aaa zaten modelForm u oluşturmuşuz <forms.py> da, ModelForm dan inherit ediyoruz, model olarak Comment modelini kullanıyoruz, içeirsine sadece content koyuyoruz, neden sadece conten koyuyoruz?, zaten kullandığımız Comment modelinde user forignKey, post da forignKey, time_stamp i kendisi veriyordu, kullanıcıdan tek istediğimiz form a comment ini yazması, daha sonra bunu view de göstereceğiz, view de nerde? post detail e gidince kullanıcı, post_detail in içerisinde, sayfasında render edeceğiz bu formu,
formu nasıl render ediyorduk? get olduğu zaman formumuzu render edecek  form= CommentForm()  (CommentForm u forms.py dan impor ediyoruz)  , zaten object imizi almışız, arkasından kullanıcı bir post işlemi yapacak, commenti POST edecek  ve  if request.method == 'POST':     eğer request method post ise, formu dolduruyoruz,   form = CommentForm(request.POST)   formu POST methoduyla request edilen veilerle doldur,  sonra formun valid olup olmadığının kontrolü    if form.is_valid():     ,   ardından Post ta yaptığımız gibi; önce bir obje oluşturacağız, formu save edeceğiz ama db ye kaydetmeyeceğiz neden? bizim form un içerisine (bakın modelde db e kaydetmemiz gereken ne var post ve user)  post ve user ı formun içerisine koymamız gerekiyor, time_stamp i zaten create ettiği zaman db kendisi koyuyor, contenti zaten kullanıcıdan alıp gönderiyoruz, bizim user ve post u form ile birlikte db ye göndermemiz gerekiyor, yani post create de yaptığımızı burada tekrar edeceğiz, comment diye bir değişken oluşturuyoruz, sonra comment = form.save(commite=False)    formu save et comment e tanımla commite false diyerek commite etmedik yani db ye göndermedik, bunun default u True dur,  (db ye göndermedik henüz) ,   şimdi artık biz bu comment objesine user ı koymamız lazım db ye göndermeden önce comment.user = request.user    request objesinin içerisindeki user ı al yani login olmuş user ı al comment objesine koy, sonra bu comment objesinin bir de post unu göndermemiz lazım, zaten yukarıda obj değişkeniyle slug=slug olan Post u almıştık,   comment.post = obj      obj değişkenimiz yani post umuzu da comment e koyuyoruz  ve formumuzu doldurmuş oluyoruz,   ondan sonra comment.save() ile  db ye bunu kaydetmişolacağız,  tabi her post işleminden sonra return redirect() yapıcaz ama tabi şöyle olacak, comment formum  detail page in altında olacağı için post ettiğimiz zaman bizim yine bu sayfada kalmamız gerekecek, aynı sayfayı render etmemiz gerekecek, onun için return redirect('blog:detail', slug=slug)    yani aynı sayfada renden etmesi için uniq değer olan slug ı da eklemeiz gerekiyor ki hangi detail sayfası olduğunu bu uniq değer ile belirtiyoruz,  Bunu farklı şekillerde de yapabilirisiniz mesela  return redirect(request.path)     bu da aynı bulunduğu sayfaya redirect eder, ancak ilk kullanım daha iyi bir kullanım.
daha sonra da formu muzu context içerisinde template imize göndereceğiz, 
context= {
    'object': obj,
    'form': form
}

<views.py> ->

```py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, CommentForm

def post_list(request):
    qs = Post.objects.filter(status='p')
    context = {
        'object_list':qs
    }
    return render(request, 'blog/post_list.html', context)

def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:list')
    context = {
        'form':form
    }
    return render(request, 'blog/post_create.html', context)

def post_detail(request, slug):
    # print(request.user)
    form = CommentForm()
    obj = get_object_or_404(Post, slug=slug)  # slug=learn-drf-3c78be2186
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commite=False)
            comment.user = request.user
            comment.post = obj
            comment.save()
            return redirect('blog:detail', slug=slug)
    context = {
        'object': obj,
        'form': form
    }
    return render(request, 'blog/post_detail.html', context)

def post_update(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('blog:list')
    context={
        'object':obj,
        'form':form
    }
    return render(request, 'blog/post_update.html', context)
    
def post_delete(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('blog:list')
    context = {
        'object':obj
    }
    return render(request, 'blog/post_delete.html', context)
```


view imizi yazdık ve formumuzu context içerisinde detail template imize gönderdik, şimdi bu view i detail template imizde, page imizde render edeceğiz, <post_detail.html> e gidiyoruz, formumuzu yerleştiriyoruz, yine aynı sayfaya gönderdiğimiz için action ımızı yine boş bırakıyoruz , methodumuz post olacak, method post olduğu için csrf imizi koyuyoruz, sonra formumuzu render ediyoruz bir tane de submit button u koyuyoruz, save edip page imize gidiyoruz, tabi şuan sadece comment i oluşturacak, çalıştığını kontrol edelim, admin panelinden de comments başlığı altından da commentimizi görüyoruz.

<post_detail.html> ->

```py
{% extends 'base.html' %}
{% block content %}

<h1>{{ object.title }}</h1>
<img src="{{ object.image.url }}" alt="">
<p>{{ object.content }}</p>
<form action="" method="POST">
    {% csrf_token %}
    {{ form }}
    <button type="submit">Comment</button>
</form>

{% endblock content %}
```

şimdi biz bu commentin içerisindeki verileri, kim yapmış, ne zaman yapmış, içeriği ne, commentin hemen altında göstereceğiz; Post modelimizden çektiğimiz, post_detail view imizden template imize context te gönderdiğimiz object in içerisinde neler var bir bakalım? <models.py> daki modelimizi açalım, bir method oluşturacağız, object imiz içinde bizim comment imizin olması gerekiyor, bizim bu comment e ulaşmamız gerekiyor, bunu nasıl yazacağız? yukarıda methodlar yazmıştık ya, yine bir method la bunun altına tanımlayacağız, diyeceğiz ki bu objeye ait olan commentleri göster, zaten bundan tekrar bahsedecektik, <models.py>  de methodlarımızın altından devam ediyoruz, 
def comments(self):           
return self.comment_set.all()  (Normalde Comment ama burada comments küçük harfle kullanıyoruz.)  bu post classından oluşmuş bir objenin yani benim blog umun altına yapılmış bütün comments leri bu method la ulaşabileceğiz


<models.py> ->

```py
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, default='django.jpg')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True) # how-to-learn-django
    
    def __str__(self):
        return self.title
    
    def comment_count(self):
        return self.comment_set.all().count()
    
    def view_count(self):
        return self.postview_set.all().count()
    
    def like_count(self):
        return self.like_set.all().count()
    
    def comments(self):
        return self.comment_set.all()
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
```


daha sonra detail <post_detail.html> e gidip, şeyi render etmek için for döngüsü yapacağız, for comment in object.comments  (view imizde objemiz neydi object ti, modelimizde methodumuza ne isim vermiştik comments), yukarıdaki method larla sayılarına ulaşmıştık, buradaki method da sadece commentleri alacağız sayısını değil, 
{{ comment.content }}
{% endfor %}
çalıştığını gördük,  kim tarafından yazıldığını p tagı içerisinde 
<p>comment by {{ user }}</p>

<post_detail.html> ->

```py
{% extends 'base.html' %}
{% block content %}

<h1>{{ object.title }}</h1>
<img src="{{ object.image.url }}" alt="">
<p>{{ object.content }}</p>
<form action="" method="POST">
    {% csrf_token %}
    {{ form }}
    <button type="submit">Comment</button>
</form>
<br>
{% for comment in object.comments %}
<p>comment by {{ user }}</p>
{{ comment.content }}
<hr>
{% endfor %}

{% endblock content %}
```


şimdi like oluşturacağız, onun için <views.py> da bir fonksiyon yazacağız, like tıklayınca db deki like sayısını arttıracak, aynı kullanıcı tekrar tıklarsa like lamışsa geri alacak, bunun algoritmasını kuruyoruz, en alt satıra gelip ;  biz burada yine db de bir işlem yapacağımız için yani db de bizim like modelimiz var like modelimize bir tane veri ekleyeceğiz, tekrar tıklanırsa silinmesi gerekiyor, bizim bu işlemi post ile yapmamız gerekiyor, 
def like(request, slug):
    if request.method == 'POST':
     şimdi burada bir algoritama kurmamız gerekiyor, ilk önce bizim hangi post u like layacağımızı almamız gerekiyor, bizim yine like ın içerisine bir slug göndermemiz gerekiyor, slug la bizim hangi post a işlem yapacağımızı bilmemiz gerekiyor, neden bilmemiz gerekiyor?, model de like a gelirsek içinde bir post değişkenimizin olduğunu görüyoruz, hangi post a like yapacağımızı bilmemiz gerekiyor, bunun için request le birlikte slug da gönderiyoruz,
     obj = get_object_or_404(Post, slug=slug)    artık bununla hangi post a like yapacağımızı biliyoruz,
     burada 
     like_qs = Like.objects.filter(user=request.user, post=obj)  like queryset diye bir değişken oluşturuyoruz, (modelden Like modelimizi import ediyoruz) bunda da db de yaptığımız bir like var mı onu filtre edeceğiz, kontrol edeceğiz, filter içinde; user ımız şuandaki request.user ımıza eşit olacak, post da hangi post da şuanki işlem yaptığımız post a eşit olması lazım yani obj ye eşit olması lazım. Şimde eğer bundan bir değer dönüyorsa demekki biz bu postu like lamışız o zaman tıkladığımız zaman sayıyı bir düşürecek, eğer like ımız yoksa sayıyı bir arttıracak ; 
     <!-- if like_qs.exists():      -->
     <!-- exists() diye bir method var, genelde query set lerde exists() kullanılıyor, yani bu like_qs ten elde ettiğimiz birşey varsa; -->
     <!-- (exists() olmadan da oluyor.) -->
     if like_qs:     
     like_qs[0].delete()   o var olanı sil,
     else:        yok eğer dolu değilse de 
     Like.objects.create(user=request.user, post=obj)     şuanki user ımızı ve şuanki post umuzu al oluştur.
     bunları yaptıktan sonra redirect ile yine detail page de kalmasını söylüyoruz,  return redirect('blog:detail', slug=slug)

<views.py> ->

```py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like
from .forms import PostForm, CommentForm

def post_list(request):
    qs = Post.objects.filter(status='p')
    context = {
        'object_list':qs
    }
    return render(request, 'blog/post_list.html', context)

def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:list')
    context = {
        'form':form
    }
    return render(request, 'blog/post_create.html', context)

def post_detail(request, slug):
    # print(request.user)
    form = CommentForm()
    obj = get_object_or_404(Post, slug=slug)  # slug=learn-drf-3c78be2186
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = obj
            comment.save()
            return redirect('blog:detail', slug=slug)
    context = {
        'object': obj,
        'form': form
    }
    return render(request, 'blog/post_detail.html', context)

def post_update(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('blog:list')
    context={
        'object':obj,
        'form':form
    }
    return render(request, 'blog/post_update.html', context)
    
def post_delete(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('blog:list')
    context = {
        'object':obj
    }
    return render(request, 'blog/post_delete.html', context)

def like(request, slug):
    if request.method == 'POST':
        obj = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=obj)
        if like_qs:
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=obj)
        return redirect('blog:detail', slug=slug)
```

views.py da view imizi yazdık, şimdi buna bir url tanımlayalım, app imizin <urls.py> ına gidip

<urls.py> ->

```py
from django.urls import path
from .views import post_list, post_create, post_detail, post_update, post_delete, like

app_name='blog'
urlpatterns = [
    path('', post_list, name='list'),
    path('create/', post_create, name='create'),
    path('<str:slug>/', post_detail, name='detail'),
    path('<str:slug>/update/', post_update, name='update'),
    path('<str:slug>/delete/', post_delete, name='delete'),
    path('<str:slug>/like/', like, name='like'),
]

```

oluşturduğumuz bu like viewi detail page imize koyacağız, tabi şuan sadece html yazarak koyuyoruz daha sonra stillendireceğiz, en alta gelip;
kullanıcıdan like bilgisi almak için form kullanıyoruz, bunun için forms.py da form oluşturmadık, kendimiz de html de form oluşturabiliriz, burası önemli bu formda ki action ımıza nereye gitmesini istiyorsak orasının url ini dinamik olarak tanımlıyoruz, burada blog app imizin like url ine gitmesini ve de giderken objectin slug ını almasını istiyoruz, 
(action kısmında blog app in like url ine object in slug ıyla gönderme sebebimiz; bu formdaki verilerle views.py daki like view inde işlem yapmamızı sağlamak için ve de like view ine de urls.py da tanımladığımız like url i vasıtasıyla ulaşabildiğimiz için form un action kısmına blog app inin like url ini vermemiz gerekiyor, arkasından da objenin slug verisiyle hangi post olduğunu belirtmemiz gerekiyor. )
methodumuz da post olacak.
method post olduğu için csrf token ımızı koyuyoruz,
form için iki tane input oluşturacağız ama inputlarımızı göstermeyeceğiz, neden input oluşturuyoruz? model.py a bakarsak Like modelimizde bir user bir de post bilgisinin girilmesi gerekiyor ama biz bunları otomatik olarak zaten view imizde def like içerisinde Like_objects.create içerisine (user=request.user, post=obj)  ile create ederken koyuyoruz. Dolayısıyla input type text değil de hidden yapıyoruz ki kullanıcı bunu görmesin, name i busefer manuel vermek zorundayız çünkü bunu kendimiz hazırlıyoruz, django name i default olarak şu şekilde veriyor; field ın adı ne ise post diyeceğiz.
diğer input u da aynı şekilde busefer name i ne olacak db de ismi ne ise onu vereceğiz yani user diyeceğiz.
bir tane de submit button oluşturuyoruz, şimdilik Like diyoruz daha sonra fontawesome dan alacağımız icon ile değiştireceğiz.
hemen ardına da post_list.html de olduğu gibi like sayısını  {{ object.like_count }}  ile göstersin istiyoruz. 

<post_detail.html> ->

```py
{% extends 'base.html' %}
{% block content %}

<h1>{{ object.title }}</h1>
<img src="{{ object.image.url }}" alt="">
<p>{{ object.content }}</p>
<form action="" method="POST">
    {% csrf_token %}
    {{ form }}
    <button type="submit">Comment</button>
</form>
<br>
{% for comment in object.comments %}
<p>comment by {{ user }}</p>
{{ comment.content }}
<hr>
{% endfor %}

<form action="{% url 'blog:like' object.slug %}" method="POST">
    {% csrf_token %}
    <input type="hidden", name="post">
    <input type="hidden", name="user">
    <button type="submit">Like</button>{{ object.like_count }}
</form>

{% endblock content %}
```

çalıştırıyoruz, new post oluşturuyoruz, title ına tıklayıp detail page ine gidiyoruz, like buttonuna tıklıyoruz bir artıyor, bir daha tıklıyoruz bir azalıyor, yani çalışıyor, exists() demeye gerek yokmuş, başka bir kullanıcıyla deneyelim, admin panelden başka bir kullanıcı oluşturuyoruz, staff ve superuser yetkisi de veriyoruz (çünkü sadece admin panalden login olunabiliyor şuanda onun için yeni kullanıcı da ancak admin panelden login olabileceği için superuser yetkisini veriyoruz ki login olsun ve post detail paginden like yapabilsin)  login oluyor, deniyoruz, çalışıyor.  


user ın authenticate ise varsa update ve delete buttonları görünecek, değilse user a update ve delete buttonlarını göstermeyeceğiz, şuanda url imizi korumuyoruz daha, yani user detail page imizin url kısmına update veya delete yazdığı zaman bu sayfalara ulaşamaması lazım, onlara geleceğiz.
şimdi o işlemi de halledelim, <detail.html> e gidiyoruz, 
bizim kullanıcının kendi post larını update ve delete yapabilmesi için sadece kendi post larının detail page inde update ve delete  i gösterecek ancak kendine ait olmayan post ların detail page inde bunları göstermeyecek şekilde bir logic kurmamız gerekiyor, yani bu post bu user a mı ait? ;
bir tane if statement kuruyoruz, 
{% if user.id == object.author.id %}   user olmuş kişi ile post un author unun id si eşit eşit ise yani login olmuş kişi ile postun sahibi aynı kişi ise;
<a href="{% url 'blog:update' object.slug %}">Update</a>   Update e slug sayesinde spesific obje ile  git   
<a href="{% url 'blog:delete' object.slug %}">Delete</a>   Delete e slug sayesinde spesific obje ile git

<detail.html> ->

```py
{% extends 'base.html' %}
{% block content %}

<h1>{{ object.title }}</h1>
<img src="{{ object.image.url }}" alt="">
<p>{{ object.content }}</p>
<form action="" method="POST">
    {% csrf_token %}
    {{ form }}
    <button type="submit">Comment</button>
</form>
<br>
{% for comment in object.comments %}
<p>comment by {{ user }}</p>
{{ comment.content }}
<hr>
{% endfor %}

<form action="{% url 'blog:like' object.slug %}" method="POST">
    {% csrf_token %}
    <input type="hidden", name="post">
    <input type="hidden", name="user">
    <button type="submit">Like</button>{{ object.like_count }}
</form>
<br>

{% if user.id == object.author.id %}
<a href="{% url 'blog:update' object.slug %}">Update</a>
<a href="{% url 'blog:delete' object.slug %}">Delete</a>
{% endif %}
    
{% endblock content %}
```

Ama bizim bir güvenlik açığımız var burada, ne o? user ın sahibi olmadığı postlar ile ilgili update, delete buttonları görünmüyor ama detail page inde iken url e update veya delete yazarsa o sayfalara girebiliyor, yani kendine ait olmayan postları update/delete edebiliyor, bu bir güvenlik açığı.
url imizi view imizde koruyabiliriz. <views.py> a gidiyoruz; 
post_delete view imizde obj tanımladıktan sonra hemen altına 
if request.user.id != obj.author.id:  (burda id leri yazmasanız da olur ama garanti olsun diye yazıyoruz.)
<!-- return HttpResponse('You are not authorized!' )      tabi HttpResponse u da import etmeliyiz. -->
return redirect('blog:list' )    list sayfasına da redirect edebiliriz.
çalıştırıyoruz, artık user, sahibi olmadığı post ların detail page inde iken url e delete yazıp delete page ine gitmeye çalışırsa list page ine redirect ediliyor.
<!-- veya message vereceğiz, message a daha gelmedik. -->
post_update view imiz de de aynı codu yazıyoruz..
çalıştırıyoruz, artık user, sahibi olmadığı post ların detail page inde iken url e update yazıp update page ine gitmeye çalışırsa list page ine redirect ediliyor.

<views.py> ->

```py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like
from .forms import PostForm, CommentForm
from django.http import HttpResponse

def post_list(request):
    qs = Post.objects.filter(status='p')
    context = {
        'object_list':qs
    }
    return render(request, 'blog/post_list.html', context)

def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:list')
    context = {
        'form':form
    }
    return render(request, 'blog/post_create.html', context)

def post_detail(request, slug):
    # print(request.user)
    form = CommentForm()
    obj = get_object_or_404(Post, slug=slug)  # slug=learn-drf-3c78be2186
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = obj
            comment.save()
            return redirect('blog:detail', slug=slug)
    context = {
        'object': obj,
        'form': form
    }
    return render(request, 'blog/post_detail.html', context)

def post_update(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if request.user.id != obj.author.id:
        # return HttpResponse('You are not authorized!')
        return redirect('blog:list')
    if form.is_valid():
        form.save()
        return redirect('blog:list')
    context={
        'object':obj,
        'form':form
    }
    return render(request, 'blog/post_update.html', context)
    
def post_delete(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    if request.user.id != obj.author.id:
        # return HttpResponse('You are not authorized!')
        return redirect('blog:list')
    if request.method == 'POST':
        obj.delete()
        return redirect('blog:list')
    context = {
        'object':obj
    }
    return render(request, 'blog/post_delete.html', context)

def like(request, slug):
    if request.method == 'POST':
        obj = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=obj)
        if like_qs:
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=obj)
        return redirect('blog:detail', slug=slug)

```

Şu ana url imizi de güvenlikli hale getirdik. Daha sonra authentication koyunca da login require koyacağız, yani login olmayan bazı işlemleri yapamayacak. Mesela comment koyamayacak, like için login olmasını isteyeceğiz.





Şimdi <post_detail.html> template inin html-css kısmını değiştiriyoruz; üzerinden bir daha geçiyoruz. djangonun crispy forms paketi ile formlarımızı güzelleştirdik, (aşağıda kurulumunu izah ediyoruz.)
card objesi içerisine image ı koyduk, sonra title ı koyduk, 

<post_detail.html> ->

```html
{% extends 'base.html' %}
{% load crispy_forms_tags %}
{% block content %}

<div class="card mb-3">
    <img src="{{ object.image.url }}" class="card-img-top" alt="post_image">
    <div class="card-body">
        <h2 class="card-title">{{ object.title }}</h2>
        <hr>
        <div>
            <span><i class="far fa-comment-alt ml-2"></i>{{ object.comment_count }}</span>
            <span><i class="fas fa-eye ml-2"></i>{{ object.view_count }}</span>
            <span><i class="far fa-heart ml-2"></i>{{ object.like_count }}</span>
            <span class="float-right"><small>Posted {{ object.publish_date|timesince }} ago.</small></span>
        </div>
        <hr>
        <p class="card-text">{{ object.content }}</p>
        <hr>
        <div>
            <h4>Enjoy this post? Give it a LIKE!</h4>
        </div>
        <div>
            <form action="{% url 'blog:like' object.slug %}" method="POST">
                {% csrf_token %}
                <input type="hidden" name="post">
                <input type="hidden" name="user">
                <button type="submit"><i class="far fa-heart fa-lg"></i></button>
                {{ object.like_count }}
            </form>
            <hr>
            <!-- {% if user.is_authenticated %} -->
                <h4>Leave a comment below</h4>
                <form action="" method="POST">
                    {% csrf_token %}
                    {{ form | crispy}}
                    <button class="btn btn-secondary btn-sm mt-1 mb-1">SEND</button>
                </form>
                <hr>
                <h4>Comments</h4>
                {% for comment in object.comments %}
                <div>
                    <p>
                        <small><b>Comment by {{ user.username}}</b></small> - <small>{{ comment.time_stamp|timesince }} ago.</small>
                    </p>
                    <p>
                        {{ comment.content }}
                    </p>
                </div>
                {% endfor %}
                <hr>
                <!-- {% else %} -->
                        {% comment %} {% url 'login' %} {% endcomment %}
                <!-- <a href="#" class="btn btn-primary btn-block">Login to comment</a> -->
            <!-- {% endif %}        -->
        </div>
    </div>
    <div class="m-3">
        
        {% if user.id == object.author.id %}
        <a href="{% url 'blog:update' object.slug %}" class="btn btn-info">Edit</a>
        <a href="{% url 'blog:delete' object.slug %}" class="btn btn-danger">Delete</a>
        {% endif %}
    </div>
</div>

{% endblock content %}
```




- Formlarımız çirkin görünüyor, djangonun form düzenleme paketi olan crispy form kullanacağız. Önce install edeceğiz, arkasından <settings.py> da INSTALLED_APPS e ekleyeceğiz. default olarak uni-form ile geliyor ama biz bootstrap4 e çevireceğiz,

```
INSTALLED_APPS = (
    ...
    'crispy_forms',
)
```


```
{% load crispy_forms_tags %}

<form method="post" class="uniForm">
    {{ my_formset|crispy }}
</form>
```

şeklinde kullanılıyor..

install etmek için environment klasörümüzün seviyesine geliyoruz (hali hazırda env klasörü ile aynı seviyede bulunan src klasörünün içerisindeyiz. Yani bir üst seviyeye çıkmamız gerek.)

benv klasörümüze çıkıyoruz; 

<terminal> ->

```bash
.....BlogApp1\src>cd ..
```


```bash
.....BlogApp1>pip install django-crispy-forms
.....BlogApp1>pip freeze > requirements.txt
```

```bash
py -m pip install --upgrade pip
```


crispy forms u <settings.py> da INSTALLED_APPS e ekliyoruz, default olarak uni-form ile gelen bootstrap i bootstrap4 e çeviriyoruz;

<settings.py> ->

```py
INSTALLED_APPS = (
    ...  ,
    # 3rd party packages
    'crispy_forms',
)

en alt kısma gelip
CRISPY_TEMPLATE_PACK = 'bootstrap4'
```


Tamam artık tüm template lerdeki (post_create.html, post_update.html) formlarımızı crispy ile güzelleştiriyoruz. 
(    {% load crispy_forms_tags %}     ve     {{form|crispy}}    ile)

önceki <post_create.html> ->

```html
{% extends 'base.html' %}
{% block content %}

<form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{form.as_p}}
    <button type="submit">POST</button>
</form>

{% endblock content %}    
```



sonraki <post_create.html> ->

```html
{% extends 'base.html' %}
{% load crispy_forms_tags %}
{% block content %}

<form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{form|crispy}}
    <button type="submit">POST</button>
</form>

{% endblock content %}    
```


tabi crispy i install ederken server ı durdurmuştuk, tekrar environment imizi activate edip src klasörümüzün içine yani manage.py dosyamızla aynı seviyeye gelip runserver yapıyoruz, create page imize geliyoruz ve çalıştığını görüyoruz.



önceki <post_update.html> ->

```html
{% extends 'base.html' %}
{% block content %}

<h2>Update {{ object.title }}</h2>
<form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Update</button>
</form>

{% endblock content %}
    
```


sonraki <post_update.html> ->

```html
{% extends 'base.html' %}
{% load crispy_forms_tags %}
{% block content %}

<h2>Update {{ object.title }}</h2>
<form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form|crispy }}
    <button type="submit">Update</button>
</form>

{% endblock content %}
    
```

çalıştırdık, login olduğum user ile yapılmış bir post u update etmeye çalıştığımda karşımıza gelen sayfa crispy ile düzeltilmiş sayfa olduğunu gördük, çalışıyor..


soru: crispy e ayar yapma? sayfayı tam olarak kaplamasın. div e vereceğimiz class ile mi yapılacak?
div e class vererek de olur, forms da vidget ile oluşturduğunuz field lara class verebiliyorsunuz, classda bootstrap class ını seçip daha küçük form olarak o class ı değiştirebilirsiniz, inputlara class vermek istiyorsanız vidget attribute ü ile class verebilirsiniz. veya bir div içeririsine alıp divin boyutunu değiştirebilirsiniz.


Birkaç şey eksik kaldı, view count u koyacağız, 

Şimdi <post_create.html> template inin html-css kısmını değiştiriyoruz, birkaç tane class verdik bootstrap ile ; djangonun crispy forms paketi ile de formumuzu güzelleştirdik,

önceki <post_create.html> ->

```html
{% extends 'base.html' %}
{% load crispy_forms_tags %}
{% block content %}

<form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{form|crispy}}
    <button type="submit">POST</button>
</form>

{% endblock content %}    
```


sonraki <post_create.html> ->

```html
{% extends 'base.html' %}
{% load crispy_forms_tags %}
{% block content %}
<div class="row">
    <div class="col-md-6 offset-md-3">
        <h3>Blog Post</h3>
        <hr>
        <form action="" method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            {{form|crispy}}
            <button type="submit" class="btn btn-outline-info">POST</button>
        </form>
    </div>
</div>
{% endblock content %}    
```


Şimdi <post_delete.html> template inin html-css kısmını değiştiriyoruz, birkaç tane class verdik bootstrap ile ; djangonun crispy forms paketi ile de formumuzu güzelleştirdik, Burada load static de denmiş ama yazılmasa da olur.

önceki <post_delete.html> ->

```html
{% extends 'base.html' %}
{% block content %}

<p>Are you sure delete {{ object.title }}</p>
<form action="" method="POST">
    {% csrf_token %}
    <a href="{% url 'blog:list' %}">Cancel</a>
    <button type="submit">Yes</button>
</form>

{% endblock content %}
```



sonraki <post_delete.html> ->

```html
{% extends 'base.html' %}
<!-- {% load static %} -->
{% block content %}

<div class="row mt-5">
    <div class="col-md-6">
        <div class="card card-body">
            <p>Are you sure delete "{{ object }}"?</p>
            <form action="" method="POST">
                {% csrf_token %}
                <a href="{% url 'blog:list' %}" class="btn btn-warning">Cancel</a>
                <input type="submit" class="btn btn-danger" name="Confirm" />
                <!-- <button type="submit" class="btn btn-danger">Yes</button> -->
            </form>
        </div>
    </div>
</div>

{% endblock content %}
```




Şimdi <post_update.html> template inin html-css kısmını değiştiriyoruz, birkaç tane class verdik bootstrap ile ; djangonun crispy forms paketi ile de formumuzu güzelleştirdik, Burada load static de denmiş ama yazılmasa da olur.

önceki <post_update.html> ->

```html
{% extends 'base.html' %}
{% load crispy_forms_tags %}
{% block content %}

<h2>Update {{ object.title }}</h2>
<form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form|crispy }}
    <button type="submit">Update</button>
</form>

{% endblock content %}
    
```



sonraki <post_update.html> ->

```html
{% extends 'base.html' %}
{% load crispy_forms_tags %}
{% block content %}

<div class="container card mb-3 pb-3">
    <div class="row">
        <div class="col-md-6 offset-md-3">
            <h3>Update Post</h3>
            <hr>
            <form action="" method="POST" enctype="multipart/form-data">
                {% csrf_token %}
                {{ form|crispy }}
                <button type="submit" class="btn btn-outline-info">Update</button>
            </form>
        </div>
    </div>
</div>

{% endblock content %}
```

çalıştırdık, fonksiyonlarımızı kontrol ediyoruz, detail e gidiyoruz, comment ekliyoruz, sayısının arttığını, like ladığımız zaman sayının artıp azaldığını gördük, 
Login fonksiyonu ekleyeceğiz, login olmazsa comment kısmını göstermeyecek, login to comment diyeceğiz, tıklayınca login e gidecek.

 Blog application tarafı tamam gibi user application a geçeceğiz, bir tane Profile page oluşturacağız, profile a gideceğiz, edit yapabilecğiz, login logout ekleyeceğiz, register ekleyeceğiz, tamamen normal bir siteye gittiğinizde nasıl görünüyorsa, login logout nasıl oluyorsa aynı şekilde yapacağız.

Şimdi yeni bir application (user) başlatalım, src klasörümüzün içinde, blog app imizle aynı seviyede (manage.py file ile aynı seviyede) terminale gidiyoruz ;

<terminal> ->

```bash
py manage.py startapp users
```
users app imiz geldi, settings.py a gidip app imiz ekleyelim,

<settings.py> ->

```py
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    # my_apps
    'blog.apps.BlogConfig',
    'users',
    # or
    # 'blog'
    # 3rd party packages
    'crispy_forms',
]
```

(settings.py da app imizin ismi ile kaydettik INSTALLED_APPS e ama bizim application umuzun ismi users olduğu için djangoda default olarak bu ismi kullandığı için, farklı yerlerde veya signals kullanırken sıkıntı çıkartıyor, farklı bir yere yazmanız gerekiyor. O yüzden app imizi settings.py a kaydederken uzun haliyle kaydediyoruz ki sıkıntı çıkarmasın bize signals kullanırken. Ayrıca alışkanlık edinin app inizi uzun haliyle kaydedin INSTALLED_APP e . )

<settings.py> ->

```py
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    # my_apps
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    # or
    # 'blog'
    # 3rd party packages
    'crispy_forms',
]
```

Şimdi users da profile sayfamız için model oluşturacağız, kendimize göre field lar belirledik (kullanıcı ile ilgili bilgi almak için), user ımız profile ile ilişkili olması lazım, bir user ın bir profile ı olması lazım, bir user ın birden fazla profile ı olamaz, yani onetoone relation olması lazım,
user = model.OneToOneField(User,)  User modelimiz vardı ya onunla bire bir ilişki kuruyoruz, tabi User modelimizi de import ediyoruz (blog app imizde User modelini djangonun default User modelinden almıştık, burada da yine aynı yerden import ediyoruz, django.contrib.auth.models den djangonun default User modelini import ediyoruz), on_delete=models.CASCADE   (user silindiğinde profile da silinsin istiyoruz)
image = models.ImageField(upload_to=  , default=  )   Bir tane profile image ı olsun, iki parametre veriyorduk, biri upload yani nereye yüklesin? ,  diğeri kullanıcı register ile user oluşturduğu zaman otomatik olarak bir profile page i oluşacak bu profile page inin de default bir resmi olacak bu kullanıcının,
şimdi diğer modelde bu upload değişkenine dinamik birşey yazmıştık media_root klasörünün  içerisinde dinamik olarak bir klasör oluşturmuştuk o klasörün içerisine otomatik olarak kendisi kaydediyordu.Nasıl yapmıştık? bir tane fonksiyon/method yazmıştık (path/klaör oluşturmak için) modelimizin üzerinde; Burada da aynısını yapıyoruz;
def user_profile_path(instance, filename) iki parametre alıyordu, biri instance (instance dan kasıt profile dan üreteceğimiz obje), diğeri filename
return 'user/{0}/{1}'.format(instance.user.id, filename) settings.py da belirttiğimiz media_root klasörünün altına user klasörü, onun da altına, {0} olan kısma instance ın user id sini isim olarak alan bir klasör koyacak, {1} olan kısma da filename i isimli dosyayı koyacak ve user kalsörünün altına tıpkı media_root kalsörünün altına olduğu gibi dinamik olarak iç içe klasör oluşturacak.
def user_profile_path(instance, filename):
    return 'users/{0}/{1}'.format(instance.user.id, filename)
image field ının upload_to parametresine de user_profile_path i yazacağız, 
Kullanıcıdan aldığımız tüm video ve resimler bu settings.py da tanımlamış olduğumuz media_root un altına otomatik olarak gidecek, ama bu media_root un altında toplanan resimler karman çorman olmasın, hangi app e ait olduğu anlaşılsın diye bir dizin yapısında olması için blog app den gelenleri blog klasörünün altına , users app den gelenleri user kalsörünün altına kaydet.
default olarak da daha önceden media_root klasörüne yüklediğimiz avatar.png resmini koy diyoruz.

bio = models.TextField(blank=True) bir de bio ekliyoruz, (daha farklı fieldlar da eklenebilir.)
str methodu tanımlıyoruz (db de bize user olarak göstersin.)

users app in  <models.py> dosyasına gidip ;

<models.py> ->

```py
from django.db import models
from django.contrib.auth.models import User

def user_profile_path(instance, filename):
    return 'users/{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_profile_path, default='avatar.png')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user
```


terminale gidip, yeni bir model oluşturduğumuz için migrations ve migrate yapıyoruz, (tabi manage.py dosyası ile aynı sevide olduğumuza dikkat ederek, burada src klasörünün içerisinde bulunuyor manage.py)

<terminal> ->

```bash
py manage.py makemigrations
py manage.py migrate
```


users app in <admin.py> ına gidip, users app inin models.py ından Profile modelimizi import edip, admin site a register ediyoruz.

users <admin.py> ->

```py
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
```

admin page imize gidip bakıyoruz, evet users application ımız ve içerisinde profile modelimizi görüyoruz.
Mesela profiles modelimize first name last name de ekleyebilirsiniz, str methodunu şekillendirebilirsiniz, 
Yeni bir profil oluşturduk, umit Profile diye gösteriyor bize, default olarak da avatar resmini otomatik koydu.

users <models.py> ->

```py
from django.db import models
from django.contrib.auth.models import User

def user_profile_path(instance, filename):
    return 'users/{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_profile_path, default='avatar.png')
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return "{} {}".format(self.user, 'Profile')
```

Şimdi arkadaşlar biz bu profile ı manuel olarak oluşturduk. Biz yeni bir user oluşturduğumuzda yada bir user register olduğu zaman, o user ın profile ının da otomatik olarak oluşmasını istiyoruz.

(Her user oluşturulduğunda, otomatik olarak bunun bir de profile ı oluşturulsun!
Bunun için <signals.py> oluşturuldu,
Bunda mantık şu bir tane model olacak, bu model signal gönderecek, bir receiver  olacak o receiver ın altına fonksiyon yazıp, o fonksiyonla ne işlem yapacağımızı yazacağız, Burada bizim sender ımız User, User modelimizden bir User oluşturulduğu zaman ama ne zaman bu User oluşturulduktan sonra yani save ettikten sonra bu işlemi gerçekleştir yani post_save , sonra create_profile diye bir fonksiyon yazıyoruz, bu sender ı alacak, instance ı alacak, created ı alacak neden? post_save de create edildikten sonra olduğu için if created codition ını kullanabilmek için,  **kwargs alacak, sonra eğer bu User dan bir tane instance oluşturulmuşsa, git Profile dan Profile instance ı oluştur. 
Bunu yapmak için apps.py a gidip ready methodunu yazmamız gerekiyor.)

Geçtiğimiz bölümde signals lardan bahsedilmişti, postsave, presave, postdelete, predelete...
yani bir save işlemi yaptıktan sonra, yapmadan önce bir sinyal gönder, o sinyale istinaden farklı bir işlem yapılsın..
şimdi burada da diyoruz ki bir user oluşturulduğunda, Profile objesi/instance ını otomatik olarak oluştur diyeceğiz.
blog app imizde ne yapmıştık <signals.py>  diye bir dosya oluşturmuştuk, burada da (users app imizin içinde) bir tane oluşturuyoruz,
Şuna karar vermemiz gerekiyor, postsave olduktan sonra veya presave (kaydettikten sonra mı? kaydetmeden önce mi?) burada kaydettikten sonra, yani user ı oluşturduktan sonra bana bir tane profile create etmesini istiyoruz.
signals larımızı import ediyoruz, (bunları ezberlemek zorunda değilsiniz, document den bakarsınız)
from django.db.models.signals import post_save
şimdi burada ne kullanacağız? default olarak gelen bir tane user modelimiz vardı ya hani biz user ı orada oluşturuyoruz, onun için, signals bana user gönderecek , user ı burada import etmemiz gerekiyor, (signal i gönderecek olan şey bu. yani user oluşturulduğunda bir sinyal gönderecek 'yeni bir user oluşturuldu, sen de şunu yap!')
from django.contrib.auth.models import User
daha sonra bir tane de reciver yani bu signal i alan receiver import etmemiz gerekiyor,
from django.dispatch import receiver
bir de neyi import edeceğiz? biz user create edildiğinde profile oluşmasını istiyoruz ya işte o Profile modelini import etmemiz gerekiyor,
from .models import Profile
Bu receiver bir decorator dü @receiver, içerisine iki tane parametre alıyor, biri ne kullanacak (burada post_save), diğeri de sender kim olacak? (burada User modelimiz olacak sender=User)
@receiver(post_save, sender=User):
create profile oluştur, birkaç tane parametre alıyor, sender (kim gönderdi bunu bana), instance (User dan oluşan obje) , post_save ekstaradan created diye birşey alıyor (neden? eğer user modeli created edildiyse şartını koyacağız onun için, ve **kwargs bunu yazmak zorunluluğu (django bazı kw arguments ları kendisi koyuyor, onları karşılamak için bu **kwargs kullanıyoruz.) var.)
def create_profile(sender, instance, created, **kwargs):
eğer instance dan gelen User modeli create edildiyse:
if created:
Profile objesi create et, image ve bio otomatik oluşturulduğu için signals a sadece user ı gönderiyoruz, user da burada instance dan gelen class (Biz mesela yeni bir user oluşturuyoruz ya manuel olarak, aslında bu bizim user clasından oluşturduğumuz bir instance oluyor. python mantığında bir class dan üretilen herşey o class ın bir instance ı oluyor.)
Eğer bir user create edilmişse onun instance ı user a eşitle 
Pofile.objects.create(user=instance)

users <signals.py> ->

```py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

oluşturduğumuz bu <signals.py> ı, users app inin <apps.py> ında UsersConfig class ında ready methoduna import etmemiz gerekiyor. 
def ready(self):
    import users.signals

users <apps.py> ->

```py
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
```


login logout ayrı bir app içerisinde tanımlarız,

- ARAŞTIR !
Bizim yazdığımız like çok düzgün değil, like yaptığımız zaman sayfa komple render oluyor, bulunduğu kısım yani sadece like yenilenmiyor, bunlar genelde AJAX (Asyncron Javascript Xml) ile yazılıyor. AJAX backende sayfayı refresh etmeden veri göndermek için kullanılıyor. Html sayfasında AJAX kodu yazıyoruz Javascript ile,  bu sefer Http response gönderiyoruz databse e Javascript koduyla , GET POST methodu yapabiliyoruz. O zaman like yapınca tüm sayfanın yenilenmesinden kurtuluyoruz.

Flusk daha basit ama djangonun builtin sağladığı security özellikleri yok, orm yapısı yok, flusk node js ile muadil bir framework


şuan autentication login logout larına nereden ulaşacağız? onları göreceğiz, 

login logout nasıl olacağız? login için form oluşturup kendimiz yapabiliriz, logout için gerek yok.

login için djangonun otomatik olarak oluşturduğu bir form var, ayrıca şöyle bir builtin yapısı da var; login button ının yanında forgot Password? diy ebir link var, buna tıklayınca sisteme kayıtlı olan email adresinizi istiyor, mail inizi girip request reset yani reset talebi ne basınca emailinize otomatik bir mail gönderiyor, email e gelen mail de istenen linke tıklayınca da yeni bir reset password oluşturma ekranı geliyor.

register için otomatik olarak oluşturulmuş bir bir form yok, bunu kendimiz yazdık,

bizim users app imizde bir <urls.py> oluşturup projenin <urls.py>  ına dahil etmemiz lazım,
project/cblog <urls.py> a ekledik users app imizin urls ini

project/cblog <urls.py> ->

```py
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```


django.contrib.auth  dan   views as auth_views   i import ediyoruz  (views i import ediyoruz ama genelde best practice djangonun authentication view lerini import ettiğimiz zaman yeniden isimlendiriliyor. burada as auth_views diye yeniden isimlendirdik.) bu views de neler var? Bu normal her app de yazdığımız gibi view ler bunlar. Class base view ler. Burada bize ne vermişler? LoginView vermiş, LogoutView vermiş, PasswordResetView, PasswordResetDoneView, yani biz burada kendimiz view yazmak yerine buradaki viewleri import edip (normalde kendimiz ne yapıyorduk? from .views import viewimiz yazdığımız view i import ediyorduk.) ama burada komple views i import edip bunun içerisinde işimize yarayacak view leri kullanacağız.

path imizi yazıyoruz,
bunları daha sonra düzenleyeceğiz,
burada diyoruz ki url de users dan sonra login gelirse yani users/login/ şu view e git diyoruz ama view i biz yazmadık, auth_views deki default viewlerden aldık.
path("login/", auth_views.LoginView.as_view(), name='login')     (auth_views in içindeki LoginView i al, as_view() ekliyoruz içine parametreler de alabiliyor, bahsedecek, name='login' yazmak zorundayız,neden? documandan baktık, hangi view e hangi isim vermemiz gerektiği yazıyor orada)
django.contrib.auth un içindeki view.py ın içine girerek LoginView i inceliyoruz, mesela template name i değiştireceğiz, bizim yazacağımızdan daha güzel bir view yazmış, siz yazmaya kalksanız bukadar iyi yazamazsınız. default değerler üzerinde değişiklik yapmak istiyorsanız burayı inceleyip, bununla uğraşmanız gerekiyor djnagonun handikapı da bu.
bunun aynısını logout için de yapacağız.
registration sağlamıyor django, registration için form oluşturacağız, o formu frontend e göndereceğiz, default olarak verdiği birşey yok, view ini de biz yazacağız,

users <urls.py> ->

```py
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login' ),
]
```


şimdi registration formunu yazop, registration view ini yazalım, users app imizin içinde <forms.py> dosyası oluşturuyoruz, içine registration form oluşturacağız, formu da django nun UserCreationForm undan inherit ederek oluşturacağız.
UserCreationForm u inceliyoruz, bu form bize password1 ve password2 yi veriyor, class meta ile de User modelinden de ekstra olarak username i alıyor. password1 ve password2 yi kendisi ekliyor, class meta ile de ekstra olarak User modelinden de username i ekliyor, bize default olarak bir UserCreationForm vermiş ancak biz buna ekstradan bir de email field ı eklemek istiyoruz, ekstradan email field ı koyacağız.
djangodan forms ları import ediyoruz,
django.contrib.auth.models den default olarak bulunan User modelimizi import ediyoruz (username için),
django.contrib.auth.forms dan UserCreationForm u import ediyoruz
class RegisterationForm(UserCreationForm):  (UserCreationForm dan inherit ediyoruz, UserCreationForm da forms.ModelForm dan tüm özellikleri inherit ettiği için bizim tekrardan forms.ModelForm dan import etmemize gerek yok. Yani biz UserCreationForm dan import ettiğim zaman artık RegistrationForm da  forms.ModelForm dan inherit etmiş olacağız, bundan dolayı şunu yapabiliriz; Class Meta: Normalde bunu modelForm da kullanabiliyorduk ya yukarıda modelForm belirtmedik ama zaten UserCreationForm form.ModelForm dan inherit etmişti. Bu özelliğe artık RegistrationForm umuz da sahip.)
model = User
fields = ('username', 'email') burada User modelimizden username ve email field larını da ekliyoruz.User modelindeki tüm fieldları ekleyebiliriz. 


users <forms.py> ->

```py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
```

şuan user create ederken sadece username istiyor, çünkü username zorunlu alanımız, email zorunlu alan değil, ama biz kullanıcıdan zorunlu olarak email adresi almak istiyoruz, eğer password ünü unutmuşsa email ine mesaj gitsin, oradan reset yapsın. Eğer email ini unique olarak istemezsek sıkıntı olur. emeil e de custom validation yazacağız. bunun için bir method tanımlıyoruz.
eğer djangoda biz bir field için validation yazacaksak clean_fieldname ismini vermemiz gerekiyor, burada email için validation yazacağımız için clean_email diye isimlendiriyoruz.
def clean_email(self):
email = self.cleaned_data['email']  (formun içerisindeki kullanıcının doldurduğu email i al (formun içerisinden bir veri alınırken best practice cleaned_data ile alınır))
if User.objects.filter(email=email).exists()    (email field ı User modelimizde kayıtlı olduğundan kontrol ediyoruz; yukarıda tanımladığımız email i olan Userları bana filter et! bu şey exists ise yani kullanıcının gidiği emailin aynısından varsa:)
raise forms.ValidationError('Please use another Email, that one already taken')  (ValidationError forms un içinde,  validation error yükselt)
eğer yoksa hiçbir işlem yapmayıp,
return email     (kullanıcının girdiği email i return et diyoruz.)
ve email custom validation kısmı da tamam, validation methodumuzu yazdık.

users <forms.py> ->

```py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Please use another Email, that one already taken')
        return email

```

/*******************/

custom validation örneği:
first name ekledik ve bir validation yazdık içeriğinde a varsa hata döndür.
users <forms.py> ->
```py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Please use another Email, that one already taken')
        return email

    def clean_first_name(self):
        name = self.cleaned_data['first_name']
        if "a" in name:
            raise forms.ValidationError('Your name include "a"')
        return name
    
```


/*******************/


Registration formumuz tamam, artık view ile url vasıtasıyla template imize koyacağız.
users <views.py> a gidip view imizi yazalım, önce users <forms.py> dan RegistrationForm umuzu import ediyoruz, ardından;
def register(request):     
form = RegisterationForm(request.POST or None) (request post ise post ile doldur değilse None Boş render et!)
if form.is_valid():  eğer form valid ise 
form.save()    formu kaydet

users <views.py> ->

```py
from django.shortcuts import render
from .forms import RegisterationForm

def register(request):
    form = RegisterationForm(request.POST or None)
    if form.is_valid():
        form.save()
```

şimdi bir html üretip orada render edelim, onun için ne yapmamız gerekiyor ?
context oluşturup formu içerisine koyup return render ile template e göndereceğiz, nereye? users ın içerisinde templates klasörü oluşturup içine app imizin ismi ile bir klasör daha oluşturup onun da içine register.html template imizi oluşturuyoruz, işte buraya 

users <views.py> ->

```py
from django.shortcuts import render
from .forms import RegisterationForm

def register(request):
    form = RegisterationForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return redirect('login')  login page imiz henüz yok.
    
    context = {
        'form': form,
    }
    
    return render(request, 'users/register.html', context )

```

users <urls.py> a gidip path tanımlayalım; (login path ini şimdilik silelim)

users <urls.py> ->

```py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    path('register/', register , name='register' ),
]

```


users templates users <register.html> ->

```html
{% extends 'base.html' %}
<!-- {% block title %}Register{% endblock %} -->
{% load crispy_forms_tags %}   
{% block content %}
<div class="content-section">
    <form action="" method="post">
        {% csrf_token %}
        <fieldset class="form-group">
            <legend class="border-bottom mb-4">Join Today</legend>
            {{ form|crispy }}
        </fieldset>
        <div class="form-group">
            <button class="btn btn-outline-info" type="submit">Sign Up</button>
        </div>
    </form>
    <div class="border-top pt-3">
        <small class="text-muted">
            {% comment %}{% url 'login' %}{% endcomment %}
            Already have an account?<a class="ml-2" href="#">Sign In</a>
        </small>
    </div>
</div>
{% endblock content %}
     
```


normalde register ımıza normalde nereden ulaşıyorduk? eğer login değilsek navbarda sağ üst köşede login ve register linkleri var oradan ulaşıyorduk. Eğer register linkini göremiyorsak demekki login olmuşuz, Adminden logout ile çıkış yapıyoruz ve tekrar navbar ımıza bakıyoruz evet register geldi. Şimdi navbar template ine gidip bu register url ini ekleyelim, 

src templates <navbar.html> ->

```html
<header class="site-header">
    <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top ">
        <div class="container">
            <a class="navbar-brand mr-4" href="{% url 'blog:list' %}">Umit Blog</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar Toggle" 
            aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toogler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarToggle">
                <div class="navbar-nav mr-auto">
                    <a class="nav-item nav-link" href="{% url 'blog:list' %}">Home</a>
                    <a class="nav-item nav-link" href="#">About</a>
                </div>
                <!-- Navbar Right Side -->
                <div class="navbar-nav">
                    {% if user.is_authenticated %}
                    {% comment %} {% url 'logout' %} {% endcomment %}
                    <a class="nav-item nav-link" href="#">Logout</a>
                    {% comment %} {% url 'profile' %} {% endcomment %}
                    <a class="nav-item nav-link" href="#">Profile</a>
                    <a class="nav-item nav-link" href="{% url 'blog:create' %}">New Post</a>
                    {% else %}
                    {% comment %} {% url 'profile' %} {% endcomment %}
                    <a class="nav-item nav-link" href="#">Login</a>
                    {% comment %} {% url 'register' %} {% endcomment %}
                    <a class="nav-item nav-link" href="{% url 'register' %}">Register</a>
                    {% endif %}
                </div>
            </div>
        </div>
    </nav>
</header>
```


evet registration page imiz çalıştı, register da oluyoruz, register olduğumuzda da aynı sayfada kalıyoruz çünkü redirect etmedik login page imiz henüz hazır değil diye, ancak register olabiliyor, admin panelden gördük register olunduğunu.  
email field ımız da geldi, ancak email field ımız şu anda doldurulması zorunlu alan değil, onu zorunlu alan yapacağız.
Email default olarak (blank=True) zorunlu alan olarak gelmiyor, ama override edebiliyoruz, 
<forms.py> da oluşturduğumuz RegistrationForm un bir field ı olan email field ını yine orada override edebiliriz (yani bazı özelliklerini geçersiz kılabiliriz),
içerisinde fieldlarımızı belirlediğimiz class Meta nın hemen üzerinde yapıyoruz bu override işlemini, şöyle yapıyoruz;
email = forms.EmailField()   (Bu şekilde içerisine hiçbirşey yazmazsak, boş bırakırsak zorunlu alan haline gelir. required=True haline gelir, default hali blank=True dur. (buradaki blank formdaki required a denk geliyor yani))

users <forms.py> ->

```py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email')
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Please use another Email, that one already taken')
        return email
    
```

çalıştırdık, register a gittiğimizde email in yanında yıldızı gördük, yani zorunlu alan olmuş (tabi bu yıldızı crispy yapıyor.), kullanıcı oluşturduk, oluştuğunu da admin page de gördük, aynı zamanda signals ile de profile ınıda oluşturdu, oluştururken email i zorunlu alan olduğu için istedi, sign up yaptık yine bizi aynı sayfada tuttu çünkü redirect etmemiştik.

NOT: Eğer burada fields kısmında sadece ('email',)  diye yazarsak sadece email ve passwordleri isteyecek, ancak dikkat tupple olduğu için ve tek item olduğu için email item ının sonuna virgül istiyor.

Şimdi login logout a gelmeden şu profile page imizi render temek istiyoruz;
Bunun için bizim bir form a ihtiyacımız var, (Şuan için aslında halihazırda bizim profile modelimiz var ve dolu nasıl dolu? user create ederken signals ile bir de Profile modeli oluşturmuştuk ya model.py da (user,image, bio field ları olan))
aslında bizim bir update form gibi olacak, yani profile page i update form gibi render edeceğiz db den, getirirken içerisini dolu getireceğiz, formları da buna göre isimlendireceğiz update_form diye isimlendireceğiz.
users <forms.py> a geliyoruz, Bizim normalde Profile modelimizde user, image ve bio fieldlarımız var, ama biz profile page inde ekstradan username ve email field larının da olmasını istiyoruz. Bunun için iki form yapacağız, username ve email i (User modelinden aldığımız fieldlar) bir form da, diğer form da da image, bio kısmını koyacağız ve iki formu tek bir sayfada birleştireceğiz. Bunu da özellikle iki form tek sayfada nasıl birleştirilir görmek için, 
class PorfileUpdateForm(forms.ModelForm):   (forms.ModelForm dan inherit ediyoruz)
class Meta:
model = Profile            (Modelimiz Profile olacak, Ayrıca Profile ı from .models import Profile ile import ediyoruz.)
fields = ("image","bio")    (user field ını almıyorum, zaten bu aslında Primary Key şeklinde, OneToOne, buradan sadece iki tane field ı image ve bio yu alacağız.)

class UserUpdateForm(forms.ModelForm):
class Meta:
model = User   (Modelimiz User olacak (User zaten import edilmiş))
fields = ("username","email")

users <forms.py> ->

```py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email')
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Please use another Email, that one already taken')
        return email

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("image","bio")

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","email")

```

Evet iki formumuz da hazır şuan, user <views.py> ımıza geliyoruz, profile page imiz için bir view yazacağız, 
def profile(request):
iki formumuz vardı onları alacağız birine u_form (UserUpdateForm), diğerine de p_form (ProfileUpdateForm) diyoruz,
u_form = UserUpdateForm(request.POST or None, instance=request.user) (Biz ayrıca form bize db deki bilgilerle dolu gelsin istiyoruz, bunun için specific birn instance belirtiyoruz, instance için hangi user olduğunu belirtmemiz lazım, django da zaten request.user ile bize hangi user ile login olunduğunu verdiği için bu şekilde yazıyoruz.)
Aynısını diğeri için de yapıyoruz.
p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user) (Burada bir de image file olduğu için şunu ekliyoruz; requst.FILES or None, yine formu dolu istiyoruz (yani şuanda login olmuş user ın profile ına ulaşıp onu instance ile p_form a yüklüyoruz) bunun için bir specific bir instance belirtiyoruz, instance=request.user.profile)   
bunlara ulaştıktan sonra formu validation etmemiz gerekiyor, ama burada iki tane formumuz var bunun için;
if u_form.is_valid() and p_form.is_valid():  (bu iki form da valid ise and ile sağladık or olsa birisi valid olsa geçer)
u_form.save()
p_form.save()
formları kaydettikten sonra aynı sayfaya kalınmasını istiyoruz,
return redirect(request.path)   (aynı sayfaya return et,  redirect i import et.)
formlarımızı kaydettik, şimdi bunları template imize göndereceğiz,
context={
    "u_form":u_form
    "p_form":p_form
}
return render(request, "users/profile.html", context )

user <views.py> ->
```py
from django.shortcuts import render, redirect
from .forms import RegisterationForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    form = RegisterationForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return redirect('login')  login page imiz henüz yok.
    
    context = {
        'form': form,
    }
    
    return render(request, 'users/register.html', context )

def profile(request):
    u_form = UserUpdateForm(request.POST or None, instance=request.user)
    p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        return redirect(request.path)
    
    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    
    return render(request, "users/profile.html", context)
```


users app imizin içerisindeki templates klasörünün içerisindeki app imizin ismini taşıyan klasörümüzün içerisinde <profile.html> template imizi oluşturuyoruz, 

users templates users <profile.html> ->

```html
{% extends 'base.html' %}
{% load crispy_forms_tags %}
{% block content %}
<div class="content-section">
    <div class="media">
        <img class="rounded-circle account-img" src="{{ user.profile.image.url }}">
        <div class="media-body">
            <h2 class="account-heading">{{ user.username }}</h2>
            <p class="text-secondary">{{ user.email }}</p>
        </div>
    </div>
    <form action="" method="post" enctype="multipart/form-data">
        {% csrf_token %}
        <fieldset class="form-group">
            <legend class="border-bottom mb-4">Profile</legend>
            {{ u_form| crispy }}
            {{ p_form| crispy }}
        </fieldset>
        <div>
            <button class="btn btn-outline-info" type="submit">Update</button>
        </div>
    </form>
</div>
{% endblock content %}
    
```

url ini oluşturup navbar daki linklerini aktif edeceğiz.