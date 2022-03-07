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


