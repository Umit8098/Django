from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.

# class User(AbstractUser):
#     portfolio = models.URLField(blank=True)
#     profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email field is mandatory')
            # eğer email yoksa hata mesajı döndür.
        email=self.normalize_email(email)
        # email formatına çeviriyor
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        # password ü kriptolaması için böyle yazdık
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff True')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser True')
        
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField('email address', unique=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    # ilk kayıt işleminin tarihini kaydet
    # auto_add=True güncelleme işleminin tarihini kaydet
    # superuser PermissionMixin içinden geliyor, o yüzden yeniden tanımlamıyoruz.
    # password, last_login  AbstractBaseUser içinden geliyor,
    # first_name, last_name bu projede koymayacağız istersek koyabiliriz.
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
