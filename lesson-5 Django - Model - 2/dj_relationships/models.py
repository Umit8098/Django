from django.db import models

# Create your models here.

class Creator(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return (f'{self.first_name} {self.last_name}')


class Language(models.Model):
    name = models.CharField(max_length=50)
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE)
    
    def __str__(self):
        return (f'{self.name}')
    
class Framework(models.Model):
    name = models.CharField(max_length=40)
    dil = models.ForeignKey(Language, on_delete=models.CASCADE)
    # dil = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    # dil = models.ForeignKey(Language, on_delete=models.SET_DEFAULT, default="şunuyaz")
    # dil = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    # dil = models.ForeignKey(Language, on_delete=models.PROTECT)
    
    def __str__(self):
        return (f'{self.name}')


class Programmer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    framework = models.ManyToManyField(Framework)
    
    def __str__(self):
        return (f'{self.first_name}')