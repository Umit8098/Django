from django.contrib import admin
from .models import Creator, Language, Framework

# Register your models here.

admin.site.register(Creator)
admin.site.register(Language)
admin.site.register(Framework)