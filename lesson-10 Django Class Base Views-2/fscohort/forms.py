from django import forms
from django.forms import fields
from .models import Student
from django.core.exceptions import ValidationError

class StudentForm(forms.ModelForm):
    
    def clean_number(self):
        number = self.cleaned_data['number']
        if not(1000 < number < 10000):
            raise ValidationError('Student number should be in between 1000 and 10000')
        return number
    class Meta:
        model = Student
        fields = '__all__'