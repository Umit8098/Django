from django.db import models

# Create your models here.

class Creator(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name

class Language(models.Model):
    name = models.CharField(max_length=50)
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE)
    # creator = models.OneToOneField(Creator, on_delete=models.PROTECT)
    # creator = models.OneToOneField(Creator, on_delete=models.SET_NULL, null=True)
    # creator = models.OneToOneField(Creator, on_delete=models.SET_DEFAULT, default="şunu yaz")
    # creator = models.OneToOneField(Creator, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=50)
    dil = models.ForeignKey(Language, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
   

class Programmer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    frameworks = models.ManyToManyField(Framework)
    
    def __str__(self):
        return self.first_name
