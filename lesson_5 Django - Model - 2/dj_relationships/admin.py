from django.contrib import admin
from .models import Creator, Language, Framework, Programmer

# Register your models here.

admin.site.register(Creator)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Programmer)
