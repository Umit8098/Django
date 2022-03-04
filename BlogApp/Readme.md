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


```bash
py -m venv benv
./benv/Scripts/activate
py -m pip install django   or  
pip install django
py -m pip install --upgrade pip
pip freeze
pip freeze > requirements.txt
```

- create .gitignore

- create project

```bash
django-admin startproject cblog (iç içe iki klasör oluşturduk.)
(dıştaki cblog klasörünün ismini src olarak değiştirdik ve manage.py dosyası ile aynı seviyeye gelmek için src nin içine gireceğiz.)
ls
cd ./src/
ls   (manage.py ile aynı seviyeye geldik!)
```

- create application

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
SECRET_KEY = django-insecure-(pwhca6*426s5nqi14_9m9a(sty&!zj$lhwpf1xjinuv47xa3e
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
  (max_length=10)
- content = models.TextField() 
  max_length 
  vermiyoruz kullanıcının blog yazma kapasitesine bırakıyoruz
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
- author = models.ForeignKey Burada 
  da 
  user 
  model foringkey i göstereceğiz, bizim db de user tablomuz hazır 
  geliyordu yani user tablomuz var o tabloy kullanacağız. User ilk başta migrate ettiğimizde bizim db imizde yani admin panelde de görünüyor hem bir grup tablomuz var hemde User tablomuz var işte o hazır verilen user tablomuzu kullanacağız. yine on_delete=models.CASCADE diyoruz yani user ı sildiğim zaman bu post da silinsin istiyorum. Çünkü bir anlamı yok yani user silinecekse postun kalmasının bir anlamı yok. author = models.ForeignKey(User, on_delete=models.CASCADE) Hata vermemesi için yoruma alıyoruz.
- status = models.CharField() şimdi 
  bunu drop 
  down menü gibi yapacağız, onun için bir yöntem var ondan 
  bahsedeceğiz; choices yada options diyebilirsiniz; bir tane tupple içerisinde biri db de kayıtlı olacağı şekliyle (d) diğeri kullanıcı dropdown menüsünde ise Draft diye gözükecek.
  OPTIONS = (
      ('d', 'Draft'),
      ('p', 'Published'),
  )
  Bu kısmı üst tarafa yazacağız, ardından yine cahrfield olduğu için max_length vermek zorundayız, bizim buraya gelebilecek en uzun kelimemiz Published 9 karakter olduğu için bir de bizden olsun diyoruz ve 10 yazıyoruz. status = models.CharField(max_length=10, choices=OPTIONS, default='d') 
  Bir de bu drop down un dinamik olarak nasıl kullanılıyor onu da gösterecek.
- slug = models.SlugField(blank=True) 
  buna özel SlugField ı var, zorunlu olmadığını 
  blank=True ile belirtiyoruz, çünkü slug field ını zaten biz otomatik olarak generate edeceğiz, onu göstereceğiz nasıl generate edileceğini, dolayısıyla admin panelden doldurmasına gerek kalmayacak. eğer doldurması zorunlu olursa custn validationdan geçemeyecek hata verecek, bunun önüne geçmek için blank True diyoruz. Yine bunu uniq olmasını istiyoruz o yüzden unique=True diyoruz. slug = models.SlugField(blank=True, unique=True)

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

şimdi de pillow u istedi, image field kullandığımız için, pillow yükledik, tabi requirements.txt ye eklemeiz lazım, 

```bash
py -m pip install pillow
```

src nin içinden bir üst klasöre requirements.txt nin seviyesine çıktık

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

Category nin sonuna gelen s takısı yani çoğul takısını class Meta ilşe düzelteceğiz. <models.py> a gidip Category modelimizin içine class Meta yazarak düzelttik, admin panelden de düzeldiğine baktık ;

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


Admin panelde Protect ne işe yarıyordu onları gösterdi, Category oluşturdu, Oject şeklinde görünen isimleri str metoduyla görüntüsünü düzelltik,
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

image field ımız db ye kaydedilmiyor demiştik, onun için upload_to='' diye bir parametre belirtmemiz gerekiyor. parantez içerisine blog/ yazarak blog 'un altına kaydet diye buşekilde yazabiliriz ama daha dinamik bir yol gösterdi. <settings.py> a gittik, en altta STATIC_URL var, bu aslında djangonun static file larını bulmak için kullandığı prefix. staticten sonra kullandığımız staticler nelerse olnların dosya yolunu yazıyoruz.
mesela STATIC_URL = 'static/css/main.css'  diye url de gözükecek. Aynı bunu gibi bir tane de MEDIA_URL = ''  belirtmemiz gerekiyor, yoksa django sıkıntı çıkarıyor, ben bu media file ları nerede gösterceğim diye. Buna MEDIA_URL = '/media/' diyebilirsiniz, farklı birşey diyebilirsiniz ama best practice media deniyor.
Bundan sonrada MEDIA_ROOT='' diye bir yol tanıtmamızı istiyor django. Bunu yine BASE_DIR içerisindeki media_root diyoruz, MEDIA_ROOT = BASE_DIR/'media_root' 
Bitti mi hayır bir ayar daha yapmamız gerekiyor, şimdi bu media root bizim media file larımızı koyacağımız directory olacak, yani ben ne dedim source un içerisinde ana base dır yolumun içerisinde bir tane media root diye bir tane klasör açacak ve django kullanıcıların yüklediği media file larını bu klasörün altına yükleyecek.


Ana projedeki <urls.py> a gidiyoruz, burada şu importları yapıyoruz -> django.conf dan settings ve django.conf.urls.static dan static (djangonu static function u)

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

Şimdi media folder ımızı oluşturuyoruz. SRC nin içine, application klasörümüz ile, manage.py dosyası ile aynı seviyede. Folder ımızın ismi settings.py da MEDIA_ROOT unuzda ne isim verdiyseniz o isim olmak zorunda (yani 'media_root')


Modelimize dönüyoruz;
    image = models.ImageField(upload='') bu şekilde upload diye şurda bir klasör oluştur onun altında da bir klasör oluştur oraya kaydet diyebiliriz, ama  media root umuzu yazmamıza gerek yok şimdi daha artistik birşey gösterecek, Category modelimizin de üstüne bir fonksiyon yazıyoruz,
    def user_directory_path(instance, filename)  bu function içerisine instance (Post tan oluşturduğumuz bir obje gibi düşünün instance o artık) ve filename diye iki parametre alıyor, sonra 
    return 'blog/{0}/{1}'.format(instance.author.id, filename)
    image field ımızın upload kısmına gidip fonksiyonumuzu kullan diyoruz, image yüklenmezse diye default olarak bir image belirtiyoruz.
    image = models.ImageField(upload=user_directory_path, default='django.jpg')
    Artık kullanıcı models de belirttiğimiz image field ına bir resim koyduğu zaman django otomatik olarak gidip media_root un altında blog diye bir klasör oluşturacak, onun altdında id diye bir klasör oluşturacak, onun altında da resmi koyacak.
    Admin panele gidip resim yüklüyoruz, draft seçiyoruz, slug field a geldik,

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

Kullanıcımız silinebiliyor, kullanıcı silinince Post da siliniyor ama image lar db de kayıtlı olmadığı, file sisteminde kayıtlı olduğu için kullanıcını yüklediği  image lar silinmiyor. Bunun için yine burada işlem yapıyoruz. Post modelim silindiğinde image ı da silsin diye. Bunun için de kullanılıyor.Bu yapılacak!!!!!!!!!
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
    content = models.TextField
    
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
    content = models.TextField
    
    def __str__(self):
        return self.user.username
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
```

PostView modelimizi yazıyoruz;
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
    content = models.TextField
    
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
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(PostView)
```

modelde değişiklik yaptığımız için makemigrations ve migrate yapıyoruz;
go to terminal
```bash
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```


Şu ana kadar db modellerini, tablolarını yazdık, şimdi formları yazacağız, kullanıcıdan form a koyduğumuz field ları doldurmasını isteyeceğiz, kullanıcı fieldları doldurunca biz onları frontend de template ler ile göstereceğiz. Şimdi formları yazacağız; app imizin içinde <forms.py> oluşturuyoruz, içinde postform ve commentform oluşturuyoruz, iki tane forma ihtiyacımız var, bir tanesi postform postu oluşturmak için hem postcreate de kullanacağız hem postu update ederken kullanacağız, diğer bir tanmesi de comment için yani yorum için form oluştuaracağız. Önce form oluşturmak için django dan forms import ediyoruz, sonra modelForm kullanacağımız için .models den Post ve Comment  modellerini import ediyoruz, PostForm mumuzu forms.ModelForm dan inherit ediyoruz class PostForm(forms.ModelForm):   ,   class Meta nın altına modelimizi ve bu modelin fieldlarını belirtiyoruz. (Kullanacaklarımızı yazmak yerine exclude da yapabilirdik.)
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
            'image',
            'content',
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
<view.py> a gidiyoruz, (frontend de template oluştururken birtane home page yapmadık, home page imizi blogların listelendiği template olarak düşündük biz extradan bir home page yapmadık.) def post_list(request):  postlarımızı sayfada listeleyeceğiz,  qs = Post.objects.all()    (qs-queryset genelde bu şekilde kullanılıyor, obj-objects için de böyle kullanılıyor genelde), Post u .models den import ediyoruz, 
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

Bundan sonraki kısmı frontend, tasarım..