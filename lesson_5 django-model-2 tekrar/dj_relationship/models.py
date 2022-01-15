from django.db import models

# Create your models here.

class Creator(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name
    
    
class Language(models.Model):
    name = models.CharField(max_length=50)
    # Founder = models.OneToOneField(Creator, on_delete=models.CASCADE)
    Founder = models.OneToOneField(Creator, on_delete=models.PROTECT)
    # Founder = models.OneToOneField(Creator, on_delete=models.SET_NULL, null=True)
    # Founder = models.OneToOneField(Creator, on_delete=models.SET_DEFAULT, default="njksd")
    # Founder = models.OneToOneField(Creator, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=40)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Programmer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    framework = models.ManyToManyField(Framework)
    
    def __str__(self):
        return self.first_name


