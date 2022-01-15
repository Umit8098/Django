from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()
    about_student = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    register_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    YEAR_IN_SCHOOL_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    year_in_school = models.CharField(max_length=50, choices=YEAR_IN_SCHOOL_CHOICES, default='FR')
    
    def __str__(self):
        return (f"{self.number} - {self.first_name}")
    
    class Meta:
        ordering = ['number']
        verbose_name_plural = "Students_List"
        db_table = "Student_Table"

