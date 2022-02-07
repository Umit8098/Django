from django.db import models

# Create your models here.

class Stud(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()
    about_me = models.TextField(null=True, blank=True)
    # image = models.ImageField(null=True, blank=True)
    # image burada çalışmadı, ama fs_cohort app inde çalıştı
    register_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
    YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
    ]
    year_in_school = models.CharField(max_length=50, choices=YEAR_IN_SCHOOL_CHOICES, default='FR')
    
    def __str__(self):
        return (f'{self.number} - {self.first_name}')

    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Stud_List"
        db_table = "Stud_Table"