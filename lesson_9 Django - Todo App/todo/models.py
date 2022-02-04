from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_date',)
        verbose_name_plural = "Todo"
        
    def __str__(self):
        return self.title
    