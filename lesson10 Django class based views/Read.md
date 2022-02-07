
8.lesson Django - CRUD  clone edilerek üzerine yapılan derstir.

- 8.lesson Django - CRUD clone edildi,
- virtual envirement oluşturuldu,
- requirement.txt dekiler kuruldu,
- pip upgrade edildi,
- settings.py daki SECRET_KEY .env dosyasında olduğu için repodan clone lama ile alınamadı, .env dosyasını local repositoryden copy-past ile .gitignore dosyası ile aynı seviyeye kaydettik,
- 

```bash
$ py -m venv env
$ .\env\Scripts\activate
$ pip install -r .\requirements.txt
$ py -m pip install --upgrade pip      (for pip upgrate)
().env dosyası local repo dan alınıp buray akopyalandı.)
$ py manage.py migrate     (settings.py için)
$ py manage.py runserver

```

- NOT:
Posgresql eklediğimiz zaman da hassas verileri mesela username, password onları settings.py dan alıp .env dosyasının içine yazıp, setting.py dosyasına da aynı secret_key de olduğu gibi config deyip .env yi işaret edebiliriz, etmeliyiz. 



Navigate to https://docs.djangoproject.com/en/3.2/topics/class-based-views/
Explain Documentation

## Class Based Views
(class ve model tanımlarken ilk harfleri büyük istiyor ama templat eiçin küçük harf istiyor.)

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

2. yöntem ->
   
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
from .views import home, student_list, student_add, student_detail, student_update, student_delete
from django.views.generic import TemplateView
from .views import HomeView

urlpatterns = [
    # path('', home, name='home'),
    # path('', TemplateView.as_view(template_name='fscohort/home.html'), name='home'),
    path('', HomeView.as_view(), name='home'),
    path('student_list/', student_list, name='list'),
    path('student_add/', student_add, name='add'),
    path('detail/<int:id>/', student_detail, name='detail'),
    path('update/<int:id>/', student_update, name='update'),
    path('delete/<int:id>/', student_delete, name='delete'),
] 
```

Haaa bunu neden kullanıyoruz. Tamamen hazırcılık için tasarlanmış. Mesela Create, Update, Delete işlemlerinin hepsinin ayrı ayrı template leri var. Bir kullanıcının yapabileceği tüm işlemler (List, Create, Update, Delete) için developera hazır template ler sunayım developer her sefereinde bunları baştan yazmasın şeklinde bir yaklaşımdır.





##### <ListView> 
(Display views lerimizden)

<views.py> a gidip list işlemine bakıyoruz; List i nerde yapıyorduk def student_list ile yapıyorduk. Hemen onun altına geliyoruz, tabi <ListView> ü import ediyoruz <django.views.generic> dan, tabi sonrasında <urls.py> da adresliyoruz, Şöyle yazıyoruz: 

(Ayrıca paginate_by = 5 ile kaç tane (burada 5) göstersin diyebiliyoruz. Bunu yazınca terminalde bir uyarı alıyoruz, neye göre 5 tane göstereceğim. Yani ban listeyi sıralamam için bir komut ver diyor. O komutu da modelimizde veriyoruz, yani her zaman en son eklediğimi en üstte göster. 
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




### <List.html> sonraki sayfaya geçme template pagination in django

List template i içinde sonraki sayfaya geçeme için yazılan kodlar. 

<student_list.html> ->
```python
{% extends 'fscohort/base.html' %}

{% block content %}

<h2>Student List</h2>

<ul>

{% for student in students %}

<a href="{% url 'detail' student.id %}">

<li>{{student}}</li>

</a>

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

2:25:00
