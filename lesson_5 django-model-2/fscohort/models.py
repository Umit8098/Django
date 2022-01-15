from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()
    about_me = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    register_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (f"{self.number} - {self.first_name}")
    
    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Student_List"
        db_table = "Student_Table"